# Pixie — Technical Architecture + Stack

## Architecture Overview

Pixie is a two-sided marketplace with three distinct technical systems:

1. **Agent Mobile App** — capture, redaction, submission
2. **AI Pipeline** — validation, extraction, proof chain
3. **Customer Platform** — dashboard, API, analytics

All three must work together within a 2–4 hour task fulfillment SLA for standard tasks.

---

## Mobile App — Agent Side

### Platform Choice: Flutter

**Selected over React Native. Rationale:**
- Flutter compiles to native ARM code — no JavaScript bridge overhead
- 60/120fps camera preview required for real-time face redaction overlay
- Custom rendering engine gives precise control over camera preview canvas
- Single codebase for iOS + Android (critical for small team)
- Dart's strong typing reduces runtime errors in mission-critical capture flow
- GitHub: 170K stars, Stack Overflow #1 cross-platform framework 2024 (46% adoption)

React Native was considered but rejected: JS bridge latency is unacceptable for real-time MediaPipe integration; camera API control is more limited.

### Key App Screens

1. **Task Discovery Map**: Geo-fenced task pins on map. Colored by type (blue=shelf, green=outdoor, orange=video, red=urgent). Task count badge by zone. Filter by: pay rate, task type, distance.

2. **Task Detail + Accept**: Task description, photos of target location (if available), estimated earnings (base + potential surge), estimated time, map view, one-tap accept.

3. **Capture Interface**: The core UX.
   - Camera preview with real-time redaction overlay (blurred face boxes shown in real-time — agent sees blur effect happening)
   - AR guide overlay: shows required coverage (e.g., "pan shelf left to right — 3 of 5 sections captured")
   - Live AI validation indicators: "shelf detected ✓", "product labels visible ✓", "faces — blurring ✓"
   - Progress bar: % of required coverage completed
   - Shot counter: "4 of 8 required photos captured"

4. **Submission + Progress**: Upload progress, real-time AI validation status, earnings locked when accepted.

5. **Earnings Dashboard**: Total earned, this week, pending, all-time. Task history with accepted/rejected breakdown. Level progress bar. Referral code + share button.

### Technical Requirements

| Requirement | Target | Notes |
|---|---|---|
| Camera preview frame rate | 30fps min, 60fps target | MediaPipe runs in preview thread |
| Face redaction latency | <15ms | MediaPipe achieves 5–10ms on mid-range devices |
| App size | <50MB | Critical for adoption in emerging markets |
| Offline mode | Yes | Task queue, local capture → upload when connected |
| Background location | Event-only | Only at task accept + task completion — not continuous |
| Min Android version | Android 7.0 (API 24) | MediaPipe requirement |
| Min iOS version | iOS 12 | MediaPipe requirement |
| Target devices | Mid-range 2020+ | Tested on Pixel 4a, iPhone SE 2nd gen |

### Privacy Architecture (Mobile)

- GPS: Recorded only at task acceptance and task completion timestamps. Never background-tracked.
- Camera: On-device face redaction before any frame is encoded for upload. No unredacted frames leave device.
- Device ID: Pseudonymous device hash (SHA-256 of device fingerprint). Not stored with agent PII.
- Secure Enclave: Ed25519 private key stored in Android Keystore / iOS Secure Enclave. Never leaves device.

---

## Backend Architecture

### Core Services (Microservices on Kubernetes)

**Task Service**
- Task creation, validation, geo-distribution
- Assignment logic (nearest agent with highest reputation gets priority)
- Task state machine: POSTED → ASSIGNED → LOCKED → SUBMITTED → VALIDATED → DELIVERED

**Capture Ingest Service**
- Receives encrypted submissions from agents
- Validates cryptographic signature (Ed25519)
- Checks GPS/timestamp consistency
- Queues for AI processing (Kafka topic)

**AI Processing Service**
- Orchestrates validation pipeline + extraction pipeline
- Manages ML model versions (MLflow)
- Routes edge cases to human review queue

**Agent Service**
- Profile management, reputation scoring, earnings calculation
- Payout initiation (Hyperwallet API)
- Notification dispatch (Firebase FCM for push)

**Customer Service**
- Dashboard data serving
- API gateway (REST + webhooks)
- Billing management (Stripe)
- Report generation

**Admin Service**
- Human review queue
- Platform health monitoring
- Agent management (suspension, verification)

### Infrastructure

| Component | Technology | Rationale |
|---|---|---|
| Container orchestration | Kubernetes (AWS EKS) | Scalability, industry standard |
| Message queue | Apache Kafka | Burst traffic handling (City Siege events, CAT events) |
| Primary database | PostgreSQL (via Supabase) | Relational, Row Level Security, real-time subscriptions |
| Cache | Redis | Task assignment (lock management), session cache |
| File storage | AWS S3 (encrypted at rest) | Raw images, 30-day retention policy |
| CDN | CloudFront + Cloudflare | Image delivery, DDoS protection |
| Cloud | AWS primary (EKS, SageMaker, S3, CloudFront) | ML ecosystem, global presence |

### Key Architecture Decisions

**Kafka for ingest**: When a City Siege event fires, thousands of agents complete tasks simultaneously. Without Kafka buffering, this spike would overwhelm the AI pipeline. Kafka absorbs the burst and the pipeline processes at its own rate.

**Supabase for database**: Real-time subscriptions enable the customer dashboard to update live as task completions come in — no polling. Row Level Security ensures customers only see their own data at the database layer, not just at the API layer.

---

## Cryptographic Proof System

### The Goal
Every submission must be provably authentic: captured at the claimed location, at the claimed time, by a real unmodified device, without tampering post-capture.

### Architecture

**Step 1 — Device Identity**
At first app launch, device generates an Ed25519 keypair. Private key stored in Android Keystore / iOS Secure Enclave (hardware-backed, cannot be extracted). Public key registered with Pixie server. Optional hardware attestation: Android SafetyNet / Apple DeviceCheck (proves the device is not rooted/jailbroken).

**Step 2 — Task Token**
Server issues a signed task token when agent accepts a task:
```
task_token = {
  task_id, agent_id_hash, issued_at, expires_at (+30 min), server_nonce
}
signed with Pixie server private key
```

**Step 3 — Capture Signature**
At moment of capture (shutter press):
```
capture_payload = SHA-256({
  raw_frame_hash,
  gps_coordinates,
  timestamp_ms (device clock + server-synced),
  accelerometer_snapshot,
  task_token
})
capture_signature = Ed25519.sign(capture_payload, device_private_key)
```

**Step 4 — C2PA Manifest**
Submission wrapped in C2PA-compatible structure with Pixie's Certificate Authority signature. C2PA is backed by Adobe, Microsoft, Google — becoming the industry standard for "content credentials."

**Step 5 — Immutable Record**
Hash stored in append-only PostgreSQL log + OriginStamp blockchain timestamp (external, immutable proof of existence at time T).

### Anti-Gaming Mitigations

| Attack Vector | Mitigation |
|---|---|
| GPS spoofing | SafetyNet/DeviceCheck hardware attestation + accelerometer walking pattern consistency |
| Photo replay (old photos) | Task token expires 30 minutes after issuance — photos without valid token rejected |
| AI-generated fake images | C2PA manifest traces to real device; GAN detector in validation pipeline |
| Coordinated fraud (same photo, multiple agents) | Perceptual hash deduplication across task submissions |
| Identity fraud | Phone + government ID verification for agents earning >$600/year (IRS threshold) |

---

## AI Pipeline Architecture

### Processing Flow (2–4 hour standard SLA)

```
INGEST → VALIDATE → EXTRACT → DELIVER
  ↓          ↓          ↓         ↓
Kafka    Security   ML Models   Customer
Queue    Checks     Pipeline    Dashboard
         (<30s)     (<3 min)    + API
```

**Validation stage** (server-side, <30 seconds):
1. Signature verification (Ed25519)
2. GPS/timestamp consistency check
3. Task token validity
4. Device attestation check
5. Face detection secondary validation (confirm no detectable faces survived on-device redaction)
6. Content presence check ("does this contain the requested content type?")
7. Quality check (blur score, exposure, resolution)

Outputs: ACCEPT / REJECT_WITH_FEEDBACK / ESCALATE_TO_HUMAN

**Extraction stage** (server-side, <3 minutes):
1. Product/SKU detection (YOLO-based, retail fine-tuned)
2. Price tag OCR (custom transformer)
3. Brand/logo recognition (ResNet-based)
4. Shelf analysis (share of shelf, facing count, planogram compliance)
5. Use-case-specific models (traffic counting, damage assessment, occupancy)

### ML Stack

| Component | Technology | Notes |
|---|---|---|
| On-device inference | TensorFlow Lite + MediaPipe | Mobile-optimized models |
| Server-side inference | PyTorch + SageMaker endpoints | Auto-scaling, A/B model testing |
| Model registry | MLflow | Version tracking, experiment management |
| Training pipeline | Apache Airflow | Weekly fine-tuning orchestration |
| Feature store | Feast (open source) | Agent reputation features, image quality features |
| Drift monitoring | Evidently AI | Alerts on accuracy drop in new regions/store formats |
| Labeling | Internal → Scale AI API (edge cases) | Scale AI for high-uncertainty samples |
| Training data | Pixie production data + SKU-110K dataset (foundation) | Proprietary data accumulates from Month 1 |

---

## Customer Platform

### Dashboard Modules
1. **Task Management**: Create tasks, define scope/location/budget, monitor fulfillment status live
2. **Live Map**: Real-time task completion pins, click to view submission
3. **Analytics**: AI-extracted data visualized — shelf share trends, price tracking, occupancy heatmaps
4. **Submission Viewer**: Individual submissions with AI annotation overlays, download options
5. **Reports**: Scheduled reports, custom date ranges, export to CSV/JSON

### API Design (REST)
```
POST   /v1/tasks                    # Create task
GET    /v1/tasks/{id}               # Task status
GET    /v1/tasks/{id}/results       # Extraction results (JSON)
GET    /v1/tasks/{id}/media         # Photos/video (signed URL)
POST   /v1/webhooks                 # Register webhook for events
GET    /v1/analytics/shelf-share    # Aggregated shelf analytics
GET    /v1/analytics/price-trends   # Price trend data
```

### Data Export
- JSON (standard)
- CSV (tabular extraction output)
- Snowflake native connector (Enterprise tier)
- BigQuery native connector (Enterprise tier)
- Tableau certified connector (Year 2)

---

## Integrations Roadmap

### Year 1 (MVP + V1)
- **Salesforce**: Task results → CRM records for field sales teams. Native app in Salesforce AppExchange.
- **Slack/Teams**: Webhook notifications for task completion + alerts
- **Snowflake**: Direct data warehouse export
- **REST API + webhooks**: For custom integrations

### Year 2
- **Guidewire** (insurance claims platform)
- **SAP/Oracle** (planogram compliance data)
- **Power BI** certified connector
- **Procore** (construction management — for construction progress use case)

---

## Authentication + Security

| System | Technology | Notes |
|---|---|---|
| Agent app auth | Clerk | Phone + ID verification flow |
| Customer dashboard | Auth0 | SSO (SAML 2.0 / OIDC), MFA |
| API auth | JWT + API keys | Rotating keys, scoped permissions |
| Encryption in transit | TLS 1.3 | All endpoints |
| Encryption at rest | AES-256 | S3, RDS |
| Secrets management | AWS Secrets Manager | No hardcoded credentials |
| Vulnerability mgmt | Quarterly pen test | External firm |

---

## Payment Infrastructure

| Function | Technology | Rationale |
|---|---|---|
| Customer billing | Stripe | Industry standard, subscription management |
| Agent payouts | Hyperwallet (PayPal subsidiary) | 200+ countries, local payout methods (mobile money, bank, PayPal), 1099 automation |
| Tax compliance | Hyperwallet + TaxJar | Automatic 1099-NEC for US agents >$600/year |
| Currency | Multi-currency via Hyperwallet | Critical for international agent expansion |

---

## Monitoring + Observability

| Component | Technology |
|---|---|
| APM + logging | Datadog |
| Error tracking | Sentry (mobile + backend) |
| ML model monitoring | Evidently AI |
| Uptime monitoring | Datadog Synthetics |
| Business metrics | Amplitude (agent app), Mixpanel (customer dashboard) |

---

## Performance Targets

| Metric | Target |
|---|---|
| Task assignment latency | <200ms from accept to lock confirmation |
| Upload speed (10 images) | <30 seconds on LTE |
| AI validation SLA | <30 seconds |
| AI extraction SLA | <3 minutes |
| Customer delivery SLA | <4 hours (standard), <30 min (priority) |
| Dashboard load time | <2 seconds |
| API response time (p99) | <500ms |
| Uptime | 99.9% (SLA to enterprise customers) |

---

## Scalability Notes

**Kafka is the critical scaling component**: A City Siege event can generate 10,000 simultaneous submissions. Without a message queue, this burst would cascade into AI pipeline failure. Kafka absorbs the burst; the AI pipeline processes at sustainable throughput.

**SageMaker auto-scaling**: ML inference endpoints scale automatically with load. Spot instances for batch training reduce GPU cost by 60–80%.

**S3 for raw images**: Each submission is ~50MB (10 images × 5MB). At 100K tasks/day = 5TB/day. S3 with 30-day lifecycle policy (delete raw images, retain structured data). Monthly storage cost at 100K tasks/day: ~$50K/month. Structured data retained indefinitely (tiny by comparison).
