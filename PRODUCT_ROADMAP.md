# Pixie — Product Roadmap

## Philosophy

Build the minimum that proves the model. Don't build features — build proof. Each stage delivers a complete, usable product, not a half-done platform.

---

## MVP (Month 0 — Launch Day)

**Goal**: One agent can complete a real task for one paying customer and get paid. Everything else is future work.

### Agent App (iOS + Android)
- Task discovery map (geo-fenced task pins)
- Task detail screen + accept flow
- Camera capture with real-time face redaction (MediaPipe on-device)
- Guided capture overlay (basic: shot counter + progress indicator)
- Submission upload (images + metadata)
- Basic earnings dashboard (tasks completed, pending payment, total earned)
- PayPal/bank payout request

### AI Pipeline
- Face detection validation (server-side, secondary check)
- GPS/timestamp verification
- Basic content presence check ("does this contain a shelf?")
- Photo quality check (blur, exposure, resolution)
- ACCEPT / REJECT / ESCALATE decision

### Customer Web Portal
- Task creation wizard (location, task type, instructions, budget)
- Map view: task status pins (posted → accepted → submitted → delivered)
- Image gallery: view submitted photos
- Basic CSV export (task_id, location, timestamp, image_urls)
- Stripe billing (credit pre-purchase)

### Admin Dashboard
- Task management (create, pause, cancel)
- Agent list (status, earnings, rejection rate)
- Manual QA review queue
- Payout processing (Hyperwallet)
- Platform health metrics (fulfillment rate, validation pass rate)

### What's NOT in MVP
- AI extraction (structured data from images — added in V1)
- API access
- C2PA proof chain (added in V1)
- Live streaming
- Advanced analytics
- Subscription plans (only pay-per-task at launch)
- Salesforce/Snowflake integrations
- Custom AI models

**MVP success criteria**: 3 customers complete at least 20 tasks each, 80%+ fulfillment rate, 0 privacy incidents.

---

## V1 (Month 3–6)

**Goal**: Enterprise customers get AI-extracted structured data, not just photos. This is when Pixie becomes a "data company" not just a "photo company."

### AI Extraction (the big unlock)
- **Product/SKU detection**: YOLO-based model, SKU-110K trained. Output: brand, product name, facing count, position.
- **Price tag OCR**: Custom model for printed shelf labels. Output: price value, currency, promotional price.
- **Brand/logo recognition**: ResNet-based. Output: brand confidence scores.
- **Basic shelf metrics**: Share of shelf %, out-of-stock flags.
- **Accuracy target**: 80%+ on standard US retail shelf conditions.

### API Access
- REST API with authentication (API keys)
- `POST /tasks` — create task programmatically
- `GET /tasks/{id}/results` — get structured extraction JSON
- Webhooks for task completion events
- API documentation (Swagger/OpenAPI spec)

### C2PA Proof Chain
- Ed25519 device keypair at first app launch
- Task token issuance at task accept
- Capture signature at photo moment
- C2PA manifest wrapping
- OriginStamp blockchain timestamp
- Proof verification endpoint for customers

### Enhanced Dashboard
- Shelf share trend chart (over time, by location)
- Price tracking line chart (competitor prices per store over time)
- Out-of-stock alert system (flag when same location shows OOS two visits in a row)
- Side-by-side store comparison view
- Task performance stats (fulfillment rate, avg completion time)

### Agent App Enhancements
- Rejection feedback messages (specific, actionable — not "quality issue")
- Level system visible (Rookie → Scout → Expert → Elite progress bar)
- Referral code + share mechanic
- Task history with accepted/rejected breakdown
- Streak bonuses active

### Subscription Plans
- Growth plan ($2,500–$5,000/month) launched
- Annual prepay option (15% discount)
- Starter Pack ($500 prepaid credit) as low-friction trial

### Salesforce Integration (V1.5)
- Native Salesforce app: task results surface in CRM records
- Field sales team sees shelf data alongside account records
- Build for AppExchange certification

---

## V2 / Series A Product (Month 12–18)

**Goal**: The product that proves Pixie can serve large enterprise accounts and expand internationally.

### Live Streaming
- Agent initiates live stream for customer dashboard
- Real-time AI annotation overlay (object detection, occupancy count)
- Customer can direct agent ("move left, zoom in on bottom shelf")
- Pricing: $5–$15/minute standard, $10–$20/minute AI-annotated
- Enterprise subscription: unlimited streams at flat monthly rate

### Custom AI Models
- Enterprise customers can bring their product catalog (SKU list, brand guidelines)
- Pixie trains custom model for their specific SKUs (higher accuracy than generic model)
- Exclusive custom model = customer IP, not shared with competitors
- Pricing: $10K–$50K one-time setup + monthly maintenance

### Advanced Analytics
- Trend analysis with YoY comparison (requires 12+ months of data)
- Anomaly detection (automatic alert when metric deviates from baseline)
- Competitor price tracking dashboard (all competitor SKUs, all tracked stores)
- Custom report templates (drag-and-drop report builder)

### Data Exports
- Snowflake native connector (no ETL required)
- BigQuery native connector
- Automated report emails (PDF/Excel) on schedule

### International (UK launch)
- UK agent app: localized (£ payouts, UK phone verification)
- UK GDPR compliance (DPA template, GDPR disclosures)
- UK launch: London + Manchester + Birmingham
- Customer base: UK CPG brands (Unilever, Diageo, Britvic)

### Multi-Language Agent App
- Spanish (for US Hispanic market — large gig worker segment)
- Portuguese (for Brazil market — future expansion signal)

### Fraud Detection Enhancement
- GAN-generated image detector in validation pipeline
- Device fingerprint anomaly detection (flags new device + old GPS pattern)
- Agent behavior analytics (flags unusual acceptance/rejection patterns)

---

## Roadmap Visualization

```
Month 0          Month 3–6         Month 12–18        Month 24+
LAUNCH (MVP)     V1                 V2 / Series A      Global Scale

Basic capture    AI extraction      Live streaming     EU launch
Face redaction   Price OCR          Custom AI models   100 cities
GPS validation   Shelf analytics    UK expansion       Training data API
Photo gallery    REST API           Snowflake export   $100M ARR path
Manual QA        C2PA proof chain   Fraud detection
Stripe billing   Subscriptions      Advanced analytics
Hyperwallet      Salesforce         Spanish language
```

---

## Feature Decision Framework

For every proposed feature, ask:
1. Does it increase fulfillment rate? (supply quality)
2. Does it increase customer retention? (demand quality)
3. Does it reduce fraud? (trust)
4. Does it enable a higher-paying use case?

If none of the above: defer to post-Series A.

Features deferred to post-Series A:
- Consumer-facing app (agents as a brand, not just workers)
- Autonomous agent (drone integration)
- Augmented reality overlay in capture
- Real-time collaborative task review
- Native mobile customer app (web dashboard sufficient for Year 1)
- Predictive inventory alerts (requires 6+ months of baseline data per location)

---

## Series A Product Vision

At Series A close (~Month 18), the product must demonstrate:
- 10 cities with >80% fulfillment rate
- AI extraction accuracy >90% on shelf detection
- Customer dashboard that CPG VPs use as a primary data source (not a supplement)
- C2PA-verified submissions accepted by enterprise legal/compliance teams
- API with 5+ customer integrations live
- First live streaming pilot with a transit authority or retail chain

The Series A product isn't bigger — it's more trusted. Trust is the product at enterprise scale.
