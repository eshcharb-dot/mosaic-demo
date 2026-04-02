# Pixie — AI/ML Architecture

## Overview

Pixie's AI layer is not a feature — it's the core value differentiator. Raw photos are a commodity; AI-extracted structured data is the product.

The AI system has four components:
1. **On-device Redaction** — faces/bodies blurred before upload (privacy + compliance)
2. **Validation Pipeline** — quality gate before task is accepted and agent paid
3. **Extraction Pipeline** — structured data extraction for customer delivery
4. **Training Flywheel** — production data continuously improves models

---

## 1. On-Device Redaction

### Goal
Faces and identifying information must never leave the agent's device. Redaction happens in the camera preview, before any data is encoded for transmission.

### Architecture

**Primary model**: MediaPipe Face Detection (Google)
- Runs entirely on-device
- Latency: 5–10ms on mid-range Android (Pixel 4a, Samsung A54); 3–7ms on iPhone 12+
- Activation: fires on every preview frame before display
- No internet connection required

**Implementation** (Flutter):
```dart
// Preview pipeline
cameraController.startImageStream((CameraImage frame) {
  final faces = mediaPipeFaceDetector.detect(frame);
  for (final face in faces) {
    canvas.drawBlurredRect(face.boundingBox, blurRadius: 25);
  }
  displayRedactedPreview(frame);
  // Original frame with faces is NEVER stored or transmitted
});
```

**License plate detection**: Separate YOLOv8 model fine-tuned on license plate dataset. Runs alongside face detection for vehicle-related use cases. Same on-device execution.

**Full-body silhouette blur**: Optional, configurable per-task for high-privacy jurisdictions (EU). Uses MediaPipe Pose detection to identify body silhouettes when faces are not visible.

### Fallback Protocol
If on-device model fails to initialize (device incompatibility, corrupted model file):
1. Camera capture is disabled
2. Agent sees: "Checking privacy protection — please wait..."
3. App attempts model reload (3 attempts)
4. If still failing: "This device requires an update to use Pixie. Please update the app."
5. Camera NEVER opens without confirmed active redaction.

### Server-Side Secondary Check
A secondary face detection model runs on every uploaded frame server-side:
- If detectable faces found in upload: submission rejected immediately
- Agent notified: "Submission failed privacy check — please recapture with a different angle"
- Incident logged for privacy compliance audit trail
- If pattern of failures: agent flagged for review

**Design principle**: On-device redaction prevents faces from leaving the device. Server-side check is the compliance backstop — catches any edge case the on-device model missed.

---

## 2. Validation Pipeline

### Goal
Verify a submission contains the requested content, was captured at the right location, at the right time, by an authentic device, without tampering.

### Pipeline (runs server-side, <30 second SLA)

```
STEP 1: Cryptographic Validation (< 1 second)
   ├── Verify Ed25519 signature (device key matches registered key)
   ├── Verify task token (signed by server, not expired)
   └── Check nonce uniqueness (prevents replay attacks)

STEP 2: Physical Validation (< 2 seconds)
   ├── GPS coordinates within acceptable radius of task location
   ├── Timestamp within task window
   ├── Accelerometer signature consistent with claimed movement
   └── Device attestation valid (SafetyNet / DeviceCheck)

STEP 3: Privacy Validation (< 3 seconds)
   ├── Secondary face detection (no faces in uploaded frames)
   ├── License plate detection (blur applied if any detected)
   └── Log: "privacy_check: passed / failed"

STEP 4: Content Validation (< 10 seconds)
   ├── Content presence: "Does this image contain requested content type?"
   │   (shelf → product detection; street → relevant objects; etc.)
   ├── Coverage check: "Was the required area captured?"
   │   (% of shelf visible, all required angles present for insurance)
   └── Quality check:
       ├── Blur score (Laplacian variance, reject if <100)
       ├── Exposure (histogram analysis, reject if >20% overexposed/underexposed)
       └── Resolution check (minimum 2MP effective resolution)

STEP 5: Decision (< 1 second)
   ├── ACCEPT → queue for extraction, trigger agent payout, notify customer
   ├── REJECT_WITH_FEEDBACK → specific actionable message to agent
   └── ESCALATE_TO_HUMAN → complex case requiring judgment
```

### Rejection Feedback Design
Specific, actionable rejection messages (not vague):
- "Product labels not visible — please move 30cm closer to the shelf"
- "Shelf section partially obscured — move to a clear sightline"
- "Required coverage incomplete — the left section of the shelf is missing"
- "GPS location doesn't match task address — please confirm you're at the correct store"
- "Image too blurry — ensure your hand is steady during capture"

**Vague rejections ("image quality insufficient") are banned**. They kill agent retention.

### Human Review Queue
Target: <5% of submissions reach human review.
Human review triggers: low-confidence content detection (model confidence <70%), apparent safety concern, agent flagged for pattern of issues.
Human reviewers: initially founders/team; scale to trained contractors at >50K tasks/month.

---

## 3. Extraction Pipeline

### Goal
Convert validated images/video into structured data that customers can query, analyze, and integrate into their systems.

### Models by Use Case

#### Retail — Product/SKU Detection
- **Base model**: YOLOv9 fine-tuned on SKU-110K dataset (11,762 images, 1.73M annotations)
- **Input**: shelf image or video frame
- **Output**: `[{sku_id, brand, product_name, bounding_box, confidence}]`
- **Accuracy target**: >85% precision/recall in standard retail conditions
- **Month 1 accuracy**: ~75% (generic model)
- **Month 12 accuracy**: ~90% (fine-tuned on Pixie production data)
- **Month 24 accuracy**: ~95% (mature fine-tuned model)

#### Retail — Price Tag OCR
- **Base model**: Custom transformer (encoder-decoder architecture)
- **Handles**: Printed shelf labels, electronic shelf labels (ESL), handwritten tags, promotional stickers
- **Input**: Cropped price tag region (detected via object detection first)
- **Output**: `{price_value, currency, unit, promotional_price (if any)}`
- **Challenge**: Variety of store label formats requires store-specific fine-tuning over time

#### Retail — Share of Shelf
- **Derived metric**: Sum of detected facings per brand / total facings detected
- **Output**: `{brand_a: 0.38, brand_b: 0.22, ...}`
- **No separate model needed**: computed from SKU detection output

#### Retail — Planogram Compliance
- **Input**: Detected SKU positions + customer-provided planogram specification
- **Model**: Position matching + classification
- **Output**: `{compliance_score: 72, violations: ["SKU-003 at knee level, expected eye level"]}`
- **Year 2 feature**: requires customer to provide planogram data to Pixie

#### Insurance — Damage Assessment
- **Base model**: ResNet-50 fine-tuned on insurance damage datasets (EagleView + proprietary)
- **Input**: Property/vehicle damage photos
- **Output**: `{damage_class, severity_score (1-10), repair_cost_range, fraud_indicators}`
- **Training data**: Accumulated from insurance customer use cases

#### Traffic — Vehicle Counting
- **Model**: YOLOv9 fine-tuned for vehicle detection (cars, trucks, buses, motorcycles)
- **Input**: Video frames or still images of traffic
- **Output**: `{vehicle_count, by_class: {cars: n, trucks: n, ...}, estimated_flow_rate}`

#### Crowd Occupancy
- **Model**: CSRNet or transformer-based crowd density estimation
- **Critical**: All faces are already redacted before this model runs — counts body positions/silhouettes, not faces
- **Output**: `{estimated_count, density_class, zone_heatmap}`
- **Message to customers**: "We count crowds, not people"

### Model Serving Infrastructure
- **Production**: SageMaker multi-model endpoints (auto-scaling, pay-per-inference)
- **Latency target**: <3 seconds for full extraction pipeline per image
- **Batch processing**: Night-time batch jobs for low-priority tasks at 1/3 the cost (spot instances)
- **A/B testing**: Traffic split between model versions for continuous evaluation

---

## 4. Training Flywheel

### How It Works

```
Customer tasks generate images
         ↓
Extraction pipeline produces predictions
         ↓
Customers confirm/correct predictions (implicit feedback)
         ↓
High-confidence predictions become training labels
         ↓
Weekly fine-tuning job re-trains models on new data
         ↓
Models improve → extraction accuracy increases
         ↓
Higher accuracy → more customer value → more tasks
```

### Label Generation

**Automatic labels** (high confidence, >0.95): Used directly as training data.
**Uncertain labels** (0.70–0.95 confidence): Routed to human review. Human confirmation + model prediction become training pair.
**Rejected by customer** (<0.70 or explicit customer correction): Customer correction becomes gold-standard label.

### Fine-Tuning Cadence
- **Weekly**: Incremental fine-tuning with previous week's new labels
- **Monthly**: Full re-training with all historical data
- **Triggered**: Evidently AI drift alert fires re-training immediately

### Proprietary Data Value
- By Month 6: 500K labeled shelf images (generic value)
- By Month 12: 5M labeled images from 8 US cities, 25 retail chains (moderate moat)
- By Month 24: 50M+ labeled images, 100 retail chains, 12 countries (significant moat)

The Year 24 dataset is worth ~$5M+ as a standalone AI training asset. It cannot be replicated without operating the platform for 24 months.

---

## AI Training Data Monetization

Pixie's production data is a byproduct with standalone commercial value.

**What we have** (by Month 18):
- 20M+ labeled retail shelf images with SKU annotations
- 2M+ traffic/crowd scenes with density labels (faces redacted)
- 500K+ damage assessment images with severity labels
- All geo-tagged, time-stamped, task-type-labeled

**Buyers**:
- AI labs (Scale AI, Appen, Cohere, OpenAI for vision model training)
- Automotive companies (Waymo, Tesla, Mobileye — for in-store/pedestrian scene understanding)
- Retail AI companies (building competing or complementary products)
- Academic ML research

**Pricing**:
- Standard labeled retail images: $0.10–$0.50/image
- Premium (multi-annotated, verified): $0.50–$2.00/image
- Curated dataset packages: $5K–$50K
- Annual data subscription: $100K–$500K/year

**Gross margin on training data**: ~95% (zero incremental cost — data produced from customer tasks)

---

## Privacy-by-Design Architecture

The AI architecture is designed so that privacy protection is technically enforced, not policy-dependent:

1. **On-device redaction**: Faces never leave the device unredacted — not policy, technical fact
2. **Hash-not-image**: What's verified and stored for the proof chain is the hash of the image, not the image itself
3. **30-day deletion**: Raw images auto-deleted after 30 days (configurable per customer)
4. **Structured data only (long-term)**: Only AI-extracted structured data (SKUs, prices, counts) retained indefinitely — contains no PII
5. **Differential privacy**: When publishing aggregate statistics (shelf share by city), differential privacy noise added to prevent re-identification
6. **Data minimization at model level**: Models are trained only on what's needed for the task — no "extracting extra information" in model design

This architecture means Pixie can truthfully say: "We have never stored an image of an identifiable person's face. Technically impossible, not just policy."
