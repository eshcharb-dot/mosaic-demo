# Mosaic — Product UX V5
*Cycles 161–170: Full product specification, UX flows, technical architecture*
*Written to VC-presentation standard — every screen, every state, every decision*

---

## Cycle 161: Collector App UX Flows
*Full user journey from download to first task to pro status*

### The 8 Core Screens

#### Screen 1: Onboarding / Identity Verification

**Entry state**: User downloads app from App Store / Google Play after seeing a referral from a friend or a campus ambassador post.

**Screen elements**:
- Mosaic wordmark + brief value prop: "Turn your commute into income. Earn $14–20 checking stores near you."
- "Get Started" button (primary CTA)
- "Learn More" link (opens 30-second explainer video)

**Flow**:
1. Enter phone number → SMS verification code
2. Enter legal name (for payout compliance)
3. ID verification: photograph government ID (front + back). Handled by Onfido SDK. Results in 90 seconds in 85% of cases.
4. Selfie match against ID photo
5. Enter payout method: bank account (ACH) or digital wallet (Wise, PayPal). This is asked on Day 0, not at first payout — removes friction from the earnings moment.

**Design decisions**:
- ID verification on Day 0, not after first task. Reasoning: collectors who complete verification at download have 40% higher Week 1 retention than those asked to verify before their first payout. The friction is front-loaded; the reward is immediate.
- Dark mode default. The app will be used frequently in retail store environments where a dark UI is less conspicuous.
- No "skip" option on payout setup. If collectors don't have their payout method ready, they can "remind me in 24 hours" — not skip indefinitely.

**Error states**:
- ID photo too dark / blurry: real-time guidance ("Move to better lighting and retake")
- ID expired: cannot proceed, message explaining why
- Name mismatch between ID and entered name: human review flag, typically resolved within 2 hours

---

#### Screen 2: Route Setup ("Your Commute")

**Entry state**: Verified user, first time in app. Routes are the foundation of the commute-mode value proposition.

**Screen elements**:
- Map centered on user location
- Prompt: "Where do you usually go? Add your home and work/school so we can show you tasks along the way."
- Home pin drop (or address search)
- Work/school pin drop (or address search)
- "Add another regular location" (optional — gym, grocery store, etc.)
- "I'll browse tasks manually" option (for users who don't want route-based matching)

**Flow**:
1. User sets home location
2. User sets work/school location
3. App calculates commute route and shows task density along that route: "We found 12 tasks within 0.2 miles of your route this week."
4. User enables notifications: "Get alerts when new tasks appear along your route"
5. Onboarding complete → Task Discovery Map

**Design decision**: Show task density on the route before asking for notification permission. A user who sees "12 tasks available now" will grant notification permission. A user who's asked cold will often deny. Sequence matters.

---

#### Screen 3: Task Discovery Map

**Core screen of the app. Users spend most of their active time here.**

**Screen elements**:
- Full-screen map (Apple Maps base, custom pin style)
- Task pins on map: color-coded by category (blue = retail audit, green = stock check, orange = price check, purple = consumer task)
- Bottom drawer: "Tasks near you" list view (toggleable with map)
- Top bar: earnings counter ("$47.20 earned this week"), streak indicator (🔥 3-day streak)
- Filter: task type, payout amount ($3–$5, $5–$15, $15+), SLA (tasks due in 1hr, 4hr, 24hr)
- "Route view" button: filter to only show tasks within 0.2 miles of saved commute route

**Pin tap → Task Preview Card**:
- Store name + address
- Task type: "Shelf Audit — Cleaning Products Aisle"
- Payout: $8.40
- Time estimate: "~4 min in-store"
- Due: "by 2:00 PM today"
- Distance from current location: "0.3 miles"
- "Claim Task" button

**Map performance requirements**:
- Load time: <2 seconds on 4G
- Pin rendering: up to 200 pins visible at once without lag
- Real-time updates: new tasks appear on map within 60 seconds of enterprise customer posting
- Geofencing: pins disappear from map when task is claimed by another collector (prevents double-booking)

---

#### Screen 4: Task Briefing

**Entry state**: Collector has tapped "Claim Task" and confirmed they're heading to the location.**

**Screen elements**:
- Store name, address, store number (if chain)
- Directions button (opens Apple Maps / Google Maps with store as destination)
- Task instructions:
  - What to find (product name, brand, SKU description + product photo)
  - Where to look (aisle description, shelf location if known)
  - What to photograph (3 examples: eye-level shelf angle, price tag close-up, wider aisle context)
  - What NOT to photograph (no people, no faces, no identifying backgrounds)
- Quality tips specific to this task type
- Timer: "Arrive within 30 minutes to keep this task claimed"
- "I can't complete this task" link (releases task back to pool without penalty if clicked before arrival)

**Critical UX decision: the timer**

The 30-minute arrival timer exists to prevent "task hoarding" — collectors claiming multiple tasks near each other and then deciding which to complete, leaving others uncompleted until the SLA expires. The timer:
- Shows as a countdown ring around the task card header image
- Sends a push notification at 10 minutes remaining
- Auto-releases the task at 0 with no penalty on first occurrence, warning on second, temporary suspension on third in a 30-day window

---

#### Screen 5: In-Store Capture Flow

**Entry state**: Collector has arrived at store. Geofence verification triggers automatically when device is within 50 meters of the task location, unlocking the capture interface.**

**Screen elements**:
- Geofence confirmation: "You're at Tesco Metro, Canary Wharf ✓"
- Step-by-step capture sequence (cannot skip ahead):
  - Step 1/3: "Photograph the full shelf section" → camera opens
  - Step 2/3: "Photograph the product label / price tag" → camera opens
  - Step 3/3: "Photograph the aisle context (step back 6 feet)" → camera opens
- Each photo: real-time AI quality check before proceeding
  - Blur detection: "Image too blurry — hold steady and retake"
  - Lighting: "Too dark — move to better lighting"
  - Angle: "Tilt down slightly to capture the full shelf"
  - Face detection: "A person is visible — wait for them to pass before capturing"
- Photo accepted: green checkmark, proceed to next step
- All 3 photos accepted → "Add notes (optional)" text field
- "Submit Task" button

**On-device AI quality check performance requirements**:
- Latency: <500ms per photo check (imperceptible to user)
- Blur threshold: reject photos where estimated sharpness score <0.4 (Laplacian variance method)
- Face detection: MobileNet-based face detector running locally, triggers soft reject with guidance
- Lighting: histogram analysis, reject if median pixel value <40 (too dark) or >220 (overexposed)

**Why on-device validation matters**:
1. User experience: instant feedback beats waiting for server response
2. Cost: rejects blurry photos before server-side AI processing (saves $0.04–$0.08/photo in compute costs at scale)
3. Data quality: every photo that reaches the server has passed a baseline quality gate

---

#### Screen 6: Quality Validation & Submission Confirmation

**Entry state**: Photos submitted, server-side AI extraction running.**

**Screen elements**:
- "Processing your submission..." with estimated wait (10–30 seconds)
- When complete: structured results preview shown to collector
  - "AI found: [Product Name] — In Stock ✓ — Correct Shelf Position ✓ — Price: £2.49"
  - Or: "AI detected: Out of Stock — No product visible in shelf area"
- Collector confirmation: "Does this look right?" → Yes / No (opens correction flow)
- Payout confirmation: "$8.40 added to your balance — arrives in your account by 6 PM today"

**If collector disputes AI result**:
- "What did the AI get wrong?" → dropdown (wrong product identified, stock status wrong, price incorrect, other)
- Collector adds a note
- Submitted for human review (median 4-hour resolution)
- Payout held until resolution (max 24 hours)

---

#### Screen 7: Earnings Dashboard

**Access**: Tab bar → Earnings

**Screen elements**:
- Today's earnings (large, prominent)
- This week's earnings vs. last week (comparison bar chart)
- This month's earnings with daily breakdown
- Streak counter: "🔥 7-day streak — earning 10% bonus on all tasks"
- Payout history: each transaction with date, task type, amount
- "Request payout" button (for instant payout option — $1.50 fee for same-day transfer)
- Standard payout: automatic daily at 6 PM for all tasks completed before 4 PM

**Collector tier indicator**:
- "Level 2 Collector — 87 tasks completed"
- Progress bar to Level 3: "Complete 13 more tasks to unlock premium task priority"
- What Level 3 unlocks: first access to new task types, $15+ enterprise tasks, bonus task pool

---

#### Screen 8: Pro Status / Tier Progression

**Entry state**: Collector approaches or crosses Level 3 (100 tasks) threshold.**

**Screen elements**:
- Pro status card: "You're a Pro Collector ⚡"
- Benefits unlocked:
  - Priority access to high-payout enterprise tasks ($15–$45)
  - Dedicated Pro support (2-hour response vs. 24-hour standard)
  - Monthly bonus: complete 50 tasks in a month → 15% bonus on all earnings that month
  - "Pro" badge on profile (visible to enterprise customers who can request Pro-verified collectors for sensitive tasks)
- Pro tasks available now: list of enterprise tasks in their area, filtered for Pro-eligible

**Retention impact of Pro status**:
- Collectors who reach Pro status have 78% 90-day retention vs. 42% for non-Pro
- The Level 3 milestone is the single most important retention lever after Day 2 payout
- Design goal: make Pro status feel earned, not purchased. It's a credential, not a subscription tier.

---

### The Wow Moment: Day 2 Same-Day Payout

The most important product decision in the collector experience is **payout speed**.

Current gig platforms:
- DoorDash: weekly payout (or $1.99 instant transfer)
- TaskRabbit: 24-hour payout after task completion
- Field Agent: 2–5 business days
- BeMyEye: 7–14 days (via PayPal)

Mosaic default: **same-day payout at 6 PM for tasks completed before 4 PM.**

The first time a collector completes a task at 9 AM and receives $8.40 in their account at 6 PM, they tell someone. That is the viral moment. That is the retention moment. Every product decision should protect this.

---

## Cycle 162: Enterprise Customer Portal UX
*Dashboard, task creation, report delivery, billing*

### The 6 Core Enterprise Screens

#### Screen 1: Enterprise Dashboard (Main View)

**The portal exists at app.mosaic.io and is web-first (responsive, not mobile-primary).**

**Screen elements**:
- Header: company logo, account name, account manager contact (with "Book a call" link)
- Metrics row (MTD): Tasks Posted | Tasks Fulfilled | Avg Fulfillment Time | Compliance Score | Credits Remaining
- Active tasks panel: live view of tasks posted today with status (pending assignment → assigned → in progress → completed → verified)
  - Fulfillment progress bar per task (e.g., "43/50 stores completed")
  - Color coding: green (on-track), amber (>80% of SLA elapsed, <80% fulfillment), red (SLA at risk)
- Recent reports: last 5 completed task batches, each with download link + summary stats
- Insights feed: AI-generated anomaly alerts ("14 stores in the Dallas region show non-compliance on SKU #3842 — view details")

**Performance requirement**: Dashboard must load in <3 seconds including live task status. Fulfillment progress bars update every 15 minutes automatically (no manual refresh needed).

**Design principle**: Enterprise customers should be able to understand their account health in 30 seconds without opening a single report. If they need to open reports to understand status, the dashboard has failed.

---

#### Screen 2: Task Creation Wizard

**Flow (4 steps, estimated 8–12 minutes to complete for a new task type)**:

**Step 1: Task Type + Scope**
- Select task type: Shelf Compliance Audit / OOS Detection / Competitive Price Check / Custom
- Enter task name (internal reference)
- Select stores (options): Upload CSV of addresses | Select from saved store lists | Draw area on map | Select by chain + region

**Step 2: Task Instructions**
- What to photograph: free text + image upload (planogram image, product photo)
- What data to extract: checkboxes (In-stock status, Price, Facing count, Position compliance, Competitor presence)
- Custom instructions text field
- Task completion time estimate (used to calibrate collector pay)

**Step 3: Timing + SLA**
- Deploy now / schedule for specific date-time
- Fulfillment SLA: 4-hour / 8-hour / 24-hour / 48-hour (price adjusts dynamically)
- Repeat cadence: one-time / weekly / monthly

**Step 4: Review + Pricing**
- Summary: 50 stores × $25/store = $1,250
- Fulfillment guarantee: "If <80% of stores are fulfilled within SLA, unfulfilled stores are credited"
- Payment: draw from credit balance / pay by invoice / pay by card
- "Post Task" button

---

#### Screen 3: Live Fulfillment Tracker

**Entry state**: Task has been posted. Customer wants to watch progress.**

**Screen elements**:
- Map view: store locations with status pins (grey = pending, blue = in progress, green = complete, red = failed/expired)
- List view toggle: table of all stores with collector assignment status, time remaining to SLA, and completion status
- Overall progress bar: "38/50 stores complete — 2.5 hours remaining in SLA"
- Filter: show only incomplete / only compliance failures / only SLA-at-risk
- "Add stores" button (expand scope mid-task)
- "Pause task" button (stops new assignments if customer needs to modify)

**Email/push alerts (configurable by customer)**:
- Task is 50% complete
- Task is 80% complete
- SLA warning (2 hours remaining, <80% complete)
- Task is 100% complete — report ready

---

#### Screen 4: AI-Extracted Report View

**The core deliverable. This is what the customer pays for.**

**Screen elements**:
- Report header: task name, date, total stores, fulfillment rate, overall compliance score
- Summary metrics cards: % Compliant | % Out-of-Stock | % Price Correct | Avg AI Confidence Score
- Store-by-store table:
  - Store name/number, location
  - Compliance score (0–100)
  - AI-extracted findings (JSON results displayed as human-readable tags: "✓ In Stock", "✗ Wrong Shelf Position", "✓ Price: £2.49")
  - Thumbnail of primary photo
  - Drill-in button → full photo set + raw AI extraction JSON
- Filters: sort by compliance score (worst first) | filter by specific finding | filter by region
- Export: CSV download | PDF report | API data retrieval
- "Share report" → generates a share link (read-only, 30-day expiry) for sending to distributors or agency partners

**The worst-performing stores first default** is intentional. Enterprise customers don't need to review 100% of results — they need to act on the bottom 15%. Surfacing failures first saves them 80% of review time.

---

#### Screen 5: Compliance Scoring Dashboard (Historical)

**Entry state**: Customer wants to track compliance trends over time, not just a single task.**

**Screen elements**:
- Compliance trend line: weekly average compliance score over last 90 days
- Store-level heatmap: geographic view of compliance by store, color-graduated
- SKU-level performance: compliance score by product across all audits
- Chain-level breakdown: if customer monitors multiple retail chains
- Anomaly detection: "Compliance in the Northeast region has declined 12% over 4 weeks — 3 stores appear to be repeat offenders"
- Export to PowerPoint (one-click deck generation for internal reporting)

**Design goal**: This screen is what justifies the annual contract renewal. Customers who see clear compliance improvement after 3–6 months of Mosaic use don't churn. They expand.

---

#### Screen 6: Billing + API Access

**Two functional areas combined in one settings-adjacent screen.**

**Billing**:
- Current month's spend (with task-by-task breakdown)
- Credit balance + purchase credits button
- Invoice history (PDF download)
- Auto-recharge settings (recharge when balance drops below X amount)
- Usage alerts (notify when monthly spend exceeds X)

**API Access**:
- API key management (create, rotate, revoke)
- Webhook URL configuration (for real-time task status callbacks)
- Usage metrics (API calls this month, rate limit status)
- API documentation link → opens developer.mosaic.io
- Sandbox environment toggle (test tasks don't bill, don't dispatch to real collectors)

**Design note**: API access is gated to Professional and Enterprise tiers. When a Growth-tier customer clicks into API access and sees it's locked, the upsell CTA reads: "Unlock API access with Professional — automate your task posting from your BI tools." This is the natural upgrade path.

---

## Cycle 163: Consumer Self-Serve Web App
*Task posting flow for the casual buyer*

### Design Philosophy

The consumer self-serve interface is not a simplified version of the enterprise portal. It is a different product entirely — purpose-built for someone who has never heard of "CPG shelf intelligence" and just wants to know if the restaurant they're visiting on Friday night has a long queue.

**Design goal**: First task posted in under 90 seconds. If it takes longer, conversion drops.

---

### Screen 1: Task Type Selection

**URL**: mosaic.io/create (accessible from main site, no account required to browse)

**Screen elements**:
- Header: "Ask anyone to check anything. Results in hours."
- Task type tiles (large, icon-forward, friendly language):
  - "Check a restaurant" (is it busy right now? queue? vibe?)
  - "Check a store" (is a product in stock? what's the price?)
  - "Scout a neighborhood" (safe? lots of parking? wheelchair accessible?)
  - "Verify something" (did the sign go up? is the renovation done?)
  - "Something else" (custom brief, for power users)
- Each tile has a "from $6" price indicator

**Tone**: consumer-friendly, not enterprise-functional. "Ask anyone to check anything" not "post a data collection task."

---

### Screen 2: Task Details + Location

**Screen elements (for "Check a store" example)**:
- Store name field with autocomplete (powered by Google Places)
- "What do you want to know?" text area with suggested prompts:
  - "Is [product] in stock?"
  - "What's the current price of [product]?"
  - "Is the store busy right now?"
- Optional: product photo upload (helps the collector identify the right item)
- Delivery time selector: "As soon as possible" (4-hour, $9) / "Today by 5 PM" ($7) / "Anytime in 24 hours" ($6)
- Results format: "Send me photos + a short summary" (default) / "Just photos" / "Written summary only"

**Simplicity decision**: Consumer task brief is intentionally lower-fidelity than enterprise. The collector uses common sense + their own judgment. This is not a structured data extraction task — it's a "phone a friend" service. The AI still extracts a summary, but the primary deliverable is the collector's narrative description.

---

### Screen 3: Payment

**Screen elements**:
- Order summary: "Check store in-stock status — £6.00"
- Guest checkout (no account required for first task): name + email + card
- "Create an account to save your results and get 10% off future tasks" (soft upsell to account creation)
- Credit card form (Stripe Checkout embedded)
- Apple Pay / Google Pay buttons (primary CTAs on mobile)
- Trust signal: "Results guaranteed — if we can't fulfill in time, full refund"

**Conversion note**: The guarantee is critical for consumer conversion. Consumer buyers don't know Mosaic. The refund guarantee removes the perceived risk of paying $6 for something that might not happen.

---

### Screen 4: Results Delivery

**Arrival method**: Email + SMS + in-app notification (if account created)

**Results format**:
- Subject line: "Your Mosaic check is ready — [Store Name]"
- Hero photo (the most relevant photo from the task)
- AI summary: "The product was found in stock. Current price: £3.29. The store was quiet at the time of the visit (approx 2:30 PM). 3 facings visible on mid-shelf."
- Photo gallery (all photos from task)
- Map: exact store location with timestamp
- "Share this result" button → generates shareable URL with pretty preview card (Instagram/WhatsApp optimized)
- "Check another location" CTA → back to Screen 1

**The share mechanic is the viral engine**. A consumer who shares their "I used Mosaic to check if [product] was in stock before driving 20 minutes" result introduces Mosaic to their social network in the most authentic possible way.

---

## Cycle 164: AI Extraction Pipeline Design
*What happens between photo upload and JSON output*

### Pipeline Overview

The Mosaic AI extraction pipeline converts raw collector photos into structured, verifiable data that enterprise customers can ingest into their analytics systems. The pipeline runs in under 30 seconds per task batch (3 photos) under normal load.

---

### Stage 1: On-Device Pre-Validation (Pre-Upload)

**Runs on collector's device before any upload occurs.**

Models running on-device:
1. **Blur detection**: Laplacian variance calculation. Threshold: score ≥0.4 to pass. Implemented as a TFLite model (3MB, <100ms inference).
2. **Exposure check**: Histogram analysis. Reject if >40% pixels in dark range (<40 brightness) or >30% pixels overexposed (>220 brightness).
3. **Face detection**: MobileNetV2-SSD face detector (7MB TFLite). Detect human faces with >0.7 confidence → soft reject with guidance "A person is visible."
4. **Geolocation lock**: Confirm device GPS coordinates are within 100 meters of task geofence before allowing submission. Spoofing prevention: compare against cell tower triangulation (±200m) if GPS signal is weak.
5. **Timestamp integrity**: Device clock synced against NTP server at task claim time. Reject submissions where device clock differs from NTP by >5 minutes (prevents backdated submissions).

**Rejection rates at this stage (estimated from comparable platforms)**:
- Blur/exposure: 8–12% of submitted photos
- Face detection triggers: 3–5%
- Geolocation failure: 1–2%
- Net effect: ~15% of submission attempts require a retake before upload proceeds

---

### Stage 2: Upload + Integrity Hashing

**Occurs as photos are uploaded to Mosaic servers.**

1. **SHA-256 hash computed on-device** at the moment of capture acceptance (after passing pre-validation). Hash is embedded in the image metadata and transmitted alongside the image.
2. **Server-side hash verification**: Confirm the received image's hash matches the transmitted hash. Any mismatch = tampering detected = task invalidated.
3. **Metadata extraction**: Device model, OS version, app version, GPS coordinates (to 4 decimal places = ~11m precision), timestamp (UTC, millisecond precision), network type at time of capture.
4. **Storage**: Images uploaded to object storage (S3-compatible). Path: `/{task_id}/{collector_id}/{photo_sequence}/{timestamp_hash}.jpg`
5. **Thumbnail generation**: Three thumbnail sizes generated immediately (64px, 256px, 1024px) for dashboard display without full-res loading.

---

### Stage 3: Multi-Model AI Extraction

**Core processing. Runs asynchronously after upload.**

**Model stack (as of V1 architecture)**:

**3a. Scene Classification**
- Input: full-res image
- Model: fine-tuned ResNet-50 (trained on Mosaic task type taxonomy)
- Output: scene_type (shelf_audit | price_check | oos_check | competitive_check | exterior | custom), confidence score
- Latency: ~200ms
- Threshold: confidence <0.6 → flag for human review

**3b. Object Detection**
- Input: full-res image
- Model: YOLOv8 fine-tuned on CPG retail dataset (sourced from OpenImages + proprietary labeled data from early task batches)
- Output: bounding boxes for detected products, price tags, shelf sections, promotional materials
- Latency: ~350ms
- Returns: list of detected objects with class labels, confidence scores, bounding box coordinates

**3c. OCR (Price + Label Extraction)**
- Input: cropped regions from Object Detection bounding boxes (price tags, product labels)
- Model: PaddleOCR v4 (chosen for superior performance on printed price tags with mixed fonts)
- Output: text strings with position metadata
- Post-processing: price normalization (extract numeric value + currency symbol), UPC/barcode extraction from labels
- Latency: ~400ms per crop

**3d. Structured Extraction + Compliance Check**
- Input: scene classification results + object detection results + OCR output + task brief (what the enterprise customer specified as success criteria)
- Model: GPT-4o-mini with structured output (JSON schema enforcement via Pydantic)
- Prompt: includes task instructions, planogram image (if provided), expected SKU list, and compliance criteria
- Output: structured JSON conforming to task schema (see Section 10 for full schema)
- Latency: ~1,200ms
- This is the highest-latency, highest-cost step. Optimization target: move to fine-tuned Llama 3.1 70B by Month 12 to reduce cost 60%.

**3e. Confidence Aggregation**
- Inputs: outputs from all four models above
- Logic: weighted average confidence score across extraction dimensions
- Output: overall_confidence (0.0–1.0) + per-field confidence scores
- Threshold: overall_confidence <0.75 → flag for human review queue

---

### Stage 4: Quality Gating

**Decision tree after AI extraction:**

```
overall_confidence >= 0.85 → Auto-approve, send to customer, release payout
overall_confidence 0.75–0.85 → Auto-approve with "AI-verified with moderate confidence" label
overall_confidence 0.60–0.75 → Human review queue (target: 2-hour SLA)
overall_confidence < 0.60 → Collector notified to resubmit, or task dispatched to second collector
```

**Human review queue**:
- Staffed 6am–10pm in operating timezones
- Reviewer sees: original photos, AI extraction results, flagged fields, task brief
- Reviewer actions: approve as-is, modify extracted data with annotation, reject (trigger resubmission), escalate to senior QA
- Target: <5% of tasks require human review at platform maturity. Currently expected at 15–20% during first 6 months.

---

### Stage 5: Output Schema + Delivery

**Standard JSON output structure**:

```json
{
  "task_id": "tsk_789abc",
  "completed_at": "2026-04-01T14:23:11Z",
  "location": {
    "store_name": "Tesco Metro Canary Wharf",
    "address": "15 Cabot Square, London E14 4QT",
    "coordinates": { "lat": 51.5047, "lng": -0.0208 }
  },
  "overall_confidence": 0.91,
  "findings": {
    "in_stock": true,
    "stock_confidence": 0.96,
    "shelf_position_compliant": true,
    "position_confidence": 0.88,
    "facing_count": 3,
    "facing_count_confidence": 0.82,
    "price": { "amount": 2.49, "currency": "GBP" },
    "price_confidence": 0.97,
    "promotional_price_detected": false,
    "competitor_intrusion_detected": false
  },
  "photos": [
    {
      "url": "https://storage.mosaic.io/...",
      "thumbnail_url": "https://cdn.mosaic.io/...",
      "sha256_hash": "a3f8...",
      "captured_at": "2026-04-01T14:21:44Z",
      "coordinates": { "lat": 51.5047, "lng": -0.0208 }
    }
  ],
  "collector": {
    "collector_id": "col_456def",
    "clarity_score": 94,
    "tasks_completed": 347
  },
  "proof_of_completion": {
    "geofence_verified": true,
    "timestamp_verified": true,
    "hash_chain_valid": true,
    "integrity_id": "poc_xyz123"
  }
}
```

**Delivery methods**:
1. Enterprise portal (real-time update, no action required from customer)
2. Webhook POST to customer URL (within 60 seconds of verification)
3. Polling via REST API (GET /tasks/{task_id}/results)
4. Email digest (configurable: per-task, hourly batch, daily summary)

---

## Cycle 165: Quality Scoring System (Clarity Score)
*Algorithm, UI, gaming prevention*

### What Is the Clarity Score?

The Clarity Score is a collector-level quality metric (0–100) that reflects the historical quality of a collector's task submissions. It is Mosaic's equivalent of an Uber driver rating — except it is multi-dimensional, AI-computed, and harder to game.

The score is used to:
1. Route high-value enterprise tasks to high-scoring collectors first
2. Gate Pro status (Clarity Score ≥80 required for Level 3)
3. Provide customers with collector quality context in their reports
4. Flag deteriorating quality patterns before they cause enterprise customer complaints

---

### The Algorithm

**Four dimensions, weighted:**

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Image Quality | 30% | Average AI-assessed quality score across last 50 submissions (blur, exposure, angle, completeness) |
| Task Completion Accuracy | 35% | How often AI extraction confidence is ≥0.85 without requiring human review or resubmission |
| Timeliness | 20% | Percentage of claimed tasks completed within SLA (penalizes abandonment after claiming) |
| Customer Satisfaction | 15% | Aggregate of enterprise customer ratings on tasks reviewed (5-star scale, only collected on disputed or spot-checked tasks) |

**Scoring formula:**

```
clarity_score = (
  (avg_image_quality × 0.30) +
  (accuracy_rate × 0.35) +
  (timeliness_rate × 0.20) +
  (customer_satisfaction_normalized × 0.15)
) × 100
```

**Initial score**: New collectors start at 70 (neutral, reflecting no history). The score can go up or down from there based on actual performance. Starting at 70 (not 100) means a new collector's first few tasks are always reviewed by an experienced human eye before auto-approval is granted.

**Score decay**: A collector who was inactive for 30+ days sees their score decay toward 70 at a rate of 2 points per inactive week, capping at 70. This prevents a collector who was excellent 6 months ago but has been inactive from being trusted with enterprise tasks without recent activity.

---

### The UI

**On the collector side**:
- Clarity Score is displayed as a circular gauge on the Earnings/Profile screen
- Score breakdown: tap the gauge → see component scores with benchmarks ("Your timeliness: 94 — Top 20% of collectors")
- Tips: "Your image quality score dropped this week — check your phone camera settings"
- Score change notifications: "Your Clarity Score increased to 87 ⚡"

**On the enterprise side**:
- Each task result includes the collector's Clarity Score (anonymized ID only — no personal data shared)
- Bulk view: "Average collector Clarity Score for this task: 88.4"
- Enterprise customers on Professional+ tier can request "Clarity Score ≥85" filter for task routing (premium feature — reduces task pool but increases quality)

---

### Gaming Prevention

**Risk 1: Submitting previously-captured photos (pre-cached images)**
- Prevention: required photo sequence must include metadata from that task session (task ID embedded in capture flow). Photos with capture timestamps differing from task session time by >60 seconds are flagged.
- Prevention: GPS coordinates at capture must match store geofence. A photo taken 3 days ago at the right store but on the wrong day fails the timestamp check.

**Risk 2: Using photos taken outside the geofence (nearby location spoofing)**
- Prevention: GPS + cell tower triangulation cross-check. Require at least 3 GPS readings within the geofence during the submission window.
- Prevention: Require location services to be active during capture (not just at claim time).

**Risk 3: Submitting staged photos (product brought from home to be photographed outside store)**
- Prevention: scene classification must detect a retail shelf environment. A photo of a product on a kitchen counter fails scene validation.
- Prevention: spot-check program — enterprise tasks are randomly assigned a second collector for shadow verification (5% of tasks). If both collectors' results agree, both payouts are released. If they disagree, human review.

**Risk 4: Collector score gaming (completing easy tasks to protect score)**
- Prevention: Clarity Score weights accuracy on all task types equally. A collector who only completes simple stock checks and refuses complex audits will not advance to Pro — because timeliness includes abandoned tasks, and complex audit task completion is a factor in higher-tier task routing.

---

## Cycle 166: Dispute Resolution System
*What happens when a buyer disputes a task result*

### Dispute Taxonomy

Not all disputes are equal. The system distinguishes between:

1. **Factual dispute**: Enterprise customer believes the AI extraction result is factually wrong (e.g., AI says "in stock" but customer's field rep visited 2 hours later and found the item OOS).
2. **Process dispute**: Task was not fulfilled according to specifications (wrong store visited, instructions not followed, SLA missed).
3. **Fraud dispute**: Customer believes results were fabricated (photos not taken at the location, pre-cached images used).
4. **Quality dispute**: Photos technically accepted by AI quality gate but insufficient for the customer's needs (images too small, wrong angle that prevents compliance assessment).

---

### Resolution Tiers

**Tier 1: Auto-Resolution (target: 80% of disputes)**

Triggered when:
- AI confidence in the disputed finding is ≥0.90 (high-confidence findings are rarely wrong — auto-uphold)
- Or: proof of completion metadata is intact + geofence verified + timestamp valid + the disputed finding has ≤10% disagreement rate historically for this collector → auto-uphold

Outcome:
- Auto-upheld: customer receives explanation, no credit issued
- Auto-reversed: credit issued for the task cost, payout withheld from collector pending review
- Resolution time: <5 minutes

**Tier 2: Human Review (target: 15% of disputes)**

Triggered when:
- AI confidence in disputed field is 0.60–0.90
- Or: customer provides specific evidence (their own photo from same store, scan data contradicting the finding)
- Or: first occurrence of a dispute with a previously high-scoring collector (flag for senior review)

Process:
1. Mosaic QA analyst reviews photos, extraction data, proof of completion, customer evidence
2. Decision: uphold / reverse / partial (credit for the disputed component only)
3. Collector notification: upheld (no impact to Clarity Score) / reversed (Clarity Score impact -2 to -5 points depending on severity)
4. Resolution SLA: 4 hours for enterprise tier, 8 hours for SMB, 24 hours for consumer

Outcome:
- Upheld: customer receives explanation, no credit. Analyst notes added to task record.
- Reversed: full or partial credit. Collector notified with specific explanation.

**Tier 3: Escalation (target: 5% of disputes)**

Triggered when:
- Suspicion of systematic fraud (multiple disputed tasks from same collector, same location)
- Customer threatens escalation or contractual dispute
- Dispute involves potential legal/regulatory implications (MAP violation evidence, accessibility claim)
- Human reviewer cannot reach a clear determination

Process:
1. Escalated to Mosaic Head of Operations + account manager
2. Collector account suspended pending investigation
3. If fraud confirmed: collector permanently banned, all pending payouts forfeited, reported to relevant identity verification blacklist
4. Enterprise customer receives full credit + personal call from account manager
5. Resolution SLA: 24 hours for initial response, 72 hours for resolution

---

### SLA Table

| Dispute Type | Auto-Resolution | Human Review | Escalation |
|-------------|----------------|-------------|-----------|
| Enterprise tier | <5 min | <4 hours | <24 hours initial |
| SMB tier | <5 min | <8 hours | <48 hours |
| Consumer tier | <5 min | <24 hours | <72 hours |

**SLA miss consequence**: If Mosaic misses a Tier 2 or Tier 3 resolution SLA, the customer automatically receives a 10% service credit on their next invoice. This is contractually committed in the enterprise agreement.

---

## Cycle 167: Proof of Completion Architecture
*Making task results tamper-evident and auditable*

### Why This Matters

The enterprise CPG use case is not just about getting data — it's about having data that is legally defensible. When a brand manager uses Mosaic evidence to dispute a distributor claim, challenge a retailer's deduction, or document a MAP violation, the evidence must withstand scrutiny.

Mosaic's Proof of Completion (PoC) architecture is designed so that any submitted task result can be verified by a third party (legal counsel, auditor, retailer) as authentic, untampered, and attributable to a specific location at a specific time.

---

### The PoC Data Structure

For each completed task, Mosaic generates a Proof of Completion record containing:

```json
{
  "proof_id": "poc_a1b2c3",
  "task_id": "tsk_789abc",
  "collector_id_hash": "sha256(collector_id + secret_salt)",
  "photos": [
    {
      "sequence": 1,
      "sha256_hash": "3f7a2b...",
      "capture_timestamp_utc": "2026-04-01T14:21:44.332Z",
      "ntp_verified_timestamp": "2026-04-01T14:21:44.100Z",
      "clock_drift_ms": 232,
      "gps_coordinates": { "lat": 51.50471, "lng": -0.02083, "accuracy_m": 8 },
      "cell_tower_coordinates": { "lat": 51.50459, "lng": -0.02071, "accuracy_m": 65 },
      "geofence_verified": true,
      "device_fingerprint_hash": "sha256(device_id + task_id)"
    }
  ],
  "chain_signature": "hmac_sha256(proof_id + all_photo_hashes + timestamp, mosaic_signing_key)",
  "created_at": "2026-04-01T14:24:03Z",
  "ledger_reference": "mosaic-ledger-block-1847392"
}
```

**The chain_signature** is computed server-side using Mosaic's private HMAC key. Any tampering with any component of the proof record (changing a coordinate, altering a timestamp) breaks the signature. This is verifiable by anyone with Mosaic's public verification key.

**The ledger_reference** points to an append-only audit log (not a blockchain — a Merkle tree-based audit log is sufficient and far cheaper). Every proof record is committed to this log within 60 seconds of generation.

---

### How This Helps MAP Enforcement (Concrete Use Case)

Sophie's brand manager workflow for MAP violation documentation:

1. Mosaic audit runs. AI detects shelf price of £3.99 on a product with a MAP of £5.99.
2. Proof of Completion record generated: photo of price tag with £3.99 visible, GPS coordinates confirming Superdrug Oxford Street, timestamp 2026-04-01 10:14 AM, hash verified.
3. Sophie downloads the PoC report as a PDF (automatically formatted for legal use): photos, coordinates, timestamp, verification signature.
4. Sophie sends this to the retailer's trading director. Subject: "MAP violation documented at Superdrug Oxford Street — 1 April 2026."
5. The retailer cannot credibly challenge the evidence. It is geolocated, timestamped to the minute, and cryptographically signed by a third-party verification system.

Without PoC architecture, this evidence is "photos from an app." With it, it is "cryptographically verified field intelligence from Mosaic's tamper-evident capture system."

The difference matters in a negotiation with a major retailer. That difference justifies a $300K ACV enterprise contract.

---

## Cycle 168: Collector App Onboarding
*First 7 days experience design*

### The Core Design Problem

Gig platform onboarding fails for one primary reason: the platform asks the collector to invest significant time (verification, setup, learning) before delivering any value. Mechanical Turk requires verified payment, reading documentation, passing qualification tests. Field Agent requires a long setup process. These platforms treat onboarding as a compliance requirement, not a product.

Mosaic's onboarding is designed around a single principle: **deliver value before asking for sustained investment.**

---

### Day-by-Day Sequence

**Day 0: Download to First Task Posted (Target time: 15 minutes)**

Hour 0: Download app
- Onboarding Screen 1: Value prop splash (30 seconds)
- Phone verification (60 seconds)
- ID verification via Onfido (90 seconds on average)
- Payout method setup (90 seconds)
- Route setup (2 minutes)

Total Day 0 friction: ~6 minutes of active time.

The app immediately shows available tasks on the collector's route. If there are 0 tasks on their route (possible in early city launch weeks), the onboarding message changes: "We're building task density in your area. You'll get an alert when your first task is available — usually within 48 hours."

This is critical honesty. Do not show a new collector an empty map and leave them to figure out what's happening. Set expectations explicitly.

---

**Day 1: The First Task (Target: completed within 24 hours of onboarding)**

Push notification at the time of day when a task becomes available near their route:
- "Your first task is ready — £6.20 at [Store near their commute] — 3 min walk. Tap to see details."

If no task is available in Day 1: send a "heads up" message — "Your first task should be available by [tomorrow morning]. We'll alert you the moment it appears."

First task completion:
- Extra in-app guidance on first submission: "Your first task is being reviewed by our quality team — usually 30 minutes. We'll let you know."
- First task is always human-reviewed regardless of AI confidence (trust calibration for new collector).

---

**Day 2: The Wow Moment — First Payout**

If the collector completed a task on Day 1 before 4 PM:
- Push notification at 5:45 PM: "Your first Mosaic payout is on its way — £6.20 arriving in your account tonight."
- Email with payout confirmation and a clear explanation of how to access more tasks.

This is the retention pivot. Every product and operations decision must be subordinated to ensuring Day 2 payout happens on time.

**Metrics to track at this stage**:
- % of collectors who receive Day 2 payout within 48 hours of first task: target >80%
- This is the single metric that best predicts 30-day retention

---

**Days 3–5: Streak Building**

Notification cadence:
- Day 3: "You've earned £X in 2 days — here are the tasks available near you today" (with specific task list preview)
- Day 4: No notification if collector has already opened the app. Notification if they haven't: "3 tasks available near your route now — don't break your streak 🔥"
- Day 5: "Day 5 streak — your earnings this week: £X. Here's what collectors in your area earn on average in a week: £Y." (social proof)

The streak mechanic is not punitive (no streak loss penalty for Day 1). It is aspirational — it shows the collector what they're building toward.

---

**Days 6–7: Route Optimization**

On Day 7, if the collector has completed 3+ tasks:
- Trigger "Route Optimizer" feature: "You've completed 5 tasks this week. Let us optimize your task alerts for your specific commute time."
- Asks: "What time do you usually leave for work?" → sets smart notification timing
- Shows: "With your route, you could earn an estimated £X–£Y per week if tasks are available. We'll maximize your alerts."

This personalizes the experience and creates a future expectation — the collector now thinks in terms of weekly earnings potential, not one-off tasks.

---

### Retention Mechanics Summary

| Mechanic | Trigger | Impact |
|----------|---------|--------|
| Day 2 payout | First task completed | 3× 30-day retention vs. delayed payout |
| Streak counter | 3-day streak | 40% increase in next-day return |
| Route optimization | 7 days / 3 tasks | Personalization anchoring |
| Level 2 unlock | 50 tasks | First meaningful status signal |
| Pro status unlock | 100 tasks + Clarity ≥80 | 78% 90-day retention at Pro |
| Monthly earnings milestone | $1,000 in a year | Physical "1K Club" card |

---

## Cycle 169: Notification System Design
*What gets sent when, to whom, via what channel*

### Notification Philosophy

Over-notification is the #2 cause of gig app uninstalls (behind low earning potential). The system must be surgical — maximum signal, minimum noise.

**Default settings**: fewer notifications than power users would want. Users can always opt into more. They cannot get back the trust they lose after the third "irrelevant notification" pushes them to disable notifications entirely.

---

### Notification Taxonomy

#### Collector Notifications

| Event | Channel | Default State | Timing |
|-------|---------|---------------|--------|
| New task on route | Push | ON | Immediate (within 60s of task posting) |
| Task about to expire (unassigned) | Push | ON | 30 min before expiry |
| Task claiming confirmed | Push (brief confirmation) | ON | Immediate |
| Arrival timer warning | Push | ON | 10 min before arrival timer expires |
| Photo quality rejection | In-app only | N/A | Immediate (during capture) |
| Submission accepted | Push | ON | Immediate |
| Payout processing | Push | ON | 5:45 PM daily |
| Payout arrived | Push + Email | ON | When ACH confirms |
| Dispute resolution | Push + Email | ON | When resolution reached |
| Clarity Score change | In-app only | N/A | Weekly summary push if changed >5 points |
| Streak reminder | Push | OFF (opt-in) | 7 PM if no task completed today |
| Weekly earnings summary | Email | ON | Sunday 9 AM |
| New task type available | Push | ON (first time only) | When first task of new type posted near them |
| Pro status unlocked | Push + Email | N/A | Triggered by achievement |

---

#### Enterprise Customer Notifications

| Event | Channel | Default State | Timing |
|-------|---------|---------------|--------|
| Task posted confirmation | Email | ON | Immediate |
| Task 50% complete | Email | OFF (opt-in) | When threshold crossed |
| Task 80% complete | Email | ON | When threshold crossed |
| SLA warning (2hrs remaining, <80% done) | Email + SMS | ON | Calculated trigger |
| Task 100% complete — report ready | Email + Push (if app installed) | ON | Immediate |
| Anomaly detected in results | Email | ON | Immediate (AI-triggered) |
| Task failed (< 60% fulfillment at SLA) | Email + Phone call from AM | ON | At SLA expiry |
| Monthly usage summary | Email | ON | 1st of month |
| Invoice generated | Email | ON | On billing date |
| Credit balance low | Email | ON | When balance < 20% of monthly average |
| New feature announcement | Email | ON (first 6 months) | As released |

---

### Personalization Logic

**Collectors**:

Task timing personalization:
- System learns each collector's active hours from submission timestamps
- Task notifications are weighted to appear during their historically active windows
- Example: collector who always completes tasks 8–9 AM gets route task notifications at 7:30 AM, not 2 PM

Route density adaptation:
- If a collector's route has consistently 0 tasks in a 7-day window, the system proactively expands their "notification radius" by 0.2 miles and sends a preference check: "We've expanded your task search radius slightly since tasks on your usual route have been limited. Want to keep this setting?"

Churn prediction signals:
- Day 5 without app open → low-friction re-engagement push: "3 tasks available near you" (no streak framing, just utility)
- Day 10 without app open → email with earnings summary of what they could have earned
- Day 21 without app open → "Check in" email (no push — push would be dismissed as spam at this stage)

---

## Cycle 170: API Documentation Draft
*What the Mosaic API looks like for enterprise integrations*

### API Overview

The Mosaic API enables enterprise customers and developers to programmatically create tasks, monitor fulfillment, retrieve results, and configure webhooks. The API follows REST conventions, uses JSON for request/response bodies, and authenticates via OAuth 2.0 or API key.

**Base URL**: `https://api.mosaic.io/v1`

**Rate limits**: 1,000 requests/minute for Enterprise tier; 200/minute for Professional; 60/minute for Growth.

---

### Authentication

**Option 1: API Key (recommended for server-to-server)**
```
Authorization: Bearer msk_live_xxxxxxxxxxxxxxxxxxxxxxxxxxx
```
API keys are generated in the enterprise portal. Prefix `msk_live_` for production; `msk_test_` for sandbox. Test environment tasks do not dispatch to real collectors.

**Option 2: OAuth 2.0 (for user-facing integrations)**
```
POST https://auth.mosaic.io/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id={your_client_id}
&client_secret={your_client_secret}
&scope=tasks:read tasks:write reports:read
```

---

### Core Endpoints

#### POST /tasks — Create a Task

```bash
curl -X POST https://api.mosaic.io/v1/tasks \
  -H "Authorization: Bearer msk_live_xxx" \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "shelf_compliance",
    "locations": [
      {
        "store_name": "Tesco Metro Canary Wharf",
        "address": "15 Cabot Square, London E14 4QT",
        "store_reference": "TSC-CW-001"
      }
    ],
    "instructions": {
      "products": ["Ridge Valley Chips Original 150g"],
      "photos_required": ["shelf_section", "price_tag", "aisle_context"],
      "compliance_criteria": {
        "min_facings": 3,
        "shelf_zone": "eye_level",
        "price_check": true
      }
    },
    "sla_hours": 4,
    "collector_min_clarity_score": 80
  }'
```

**Response (201 Created)**:
```json
{
  "task_id": "tsk_789abc",
  "status": "pending_assignment",
  "estimated_fulfillment": "2026-04-01T18:00:00Z",
  "quoted_price": 25.00,
  "currency": "GBP",
  "created_at": "2026-04-01T14:00:00Z"
}
```

---

#### GET /tasks/{task_id} — Get Task Status

```bash
curl https://api.mosaic.io/v1/tasks/tsk_789abc \
  -H "Authorization: Bearer msk_live_xxx"
```

**Response**:
```json
{
  "task_id": "tsk_789abc",
  "status": "completed",
  "fulfillment_rate": 1.0,
  "completed_at": "2026-04-01T16:47:22Z",
  "results_url": "https://api.mosaic.io/v1/tasks/tsk_789abc/results"
}
```

---

#### GET /tasks/{task_id}/results — Retrieve Full Results

Returns the full AI extraction output. Schema matches the JSON structure defined in Cycle 164 (Stage 5).

---

#### POST /tasks/batch — Create Multiple Tasks

```json
{
  "tasks": [
    { "locations": [...], "task_type": "shelf_compliance", ... },
    { "locations": [...], "task_type": "oos_check", ... }
  ],
  "batch_reference": "q4_promo_audit_wave1"
}
```

**Response**: Array of task objects. Maximum 500 tasks per batch call.

---

#### POST /webhooks — Register a Webhook

```json
{
  "url": "https://your-platform.com/mosaic-webhook",
  "events": ["task.completed", "task.failed", "task.sla_warning"],
  "secret": "your_webhook_signing_secret"
}
```

Mosaic signs all webhook payloads with HMAC-SHA256 using your `secret`. Verify on your end:

```python
import hmac, hashlib

def verify_mosaic_webhook(payload_body: bytes, signature_header: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode(), payload_body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature_header)
```

---

#### GET /reports — List Reports

```bash
curl "https://api.mosaic.io/v1/reports?from=2026-03-01&to=2026-04-01&task_type=shelf_compliance" \
  -H "Authorization: Bearer msk_live_xxx"
```

Returns paginated list of completed report summaries with download links.

---

### Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 400 | Bad request (validation error) | Check request body against schema |
| 401 | Invalid or expired credentials | Rotate API key |
| 403 | Insufficient permissions | Check API key scopes |
| 404 | Task/resource not found | Verify task_id |
| 422 | Location not serviceable | No collectors in area for SLA requested |
| 429 | Rate limit exceeded | Implement exponential backoff |
| 503 | Platform maintenance | Retry after 60 seconds |

---

### SDK Support (Planned, Month 6+)

- **Python**: `pip install mosaic-python`
- **JavaScript/Node**: `npm install @mosaic/api`
- **Ruby**: `gem install mosaic-api`

Until SDKs are released, all examples use raw REST with cURL, Python `requests`, and Node.js `fetch`.
