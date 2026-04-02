# Pixie — Research: Competitive Landscape + Market Sizing

## Competitive Landscape

### Direct Competitors: Crowdsourced Data Collection

**Premise Data**
- Raised: $188M total ($85M Series E led by WestCap, 2021)
- Scale: 2.6M contributors globally
- Model: Gig-style tasks — price checks, surveys, photos
- AI layer: Machine learning quality control, automated business rules
- Focus: Market intelligence, government/humanitarian data, financial intelligence
- 2024 launch: "Prime" retail data insights product
- Weakness vs Pixie: Survey/price-check focused, not rich visual intelligence; no real-time AI extraction; no tamper-proof proof chain

**Field Agent**
- Founded: 2010
- Scale: 2M+ app downloads, 320K+ agents (Canada alone)
- Agent earnings: $2–$20/task (5–15 min tasks)
- Payout: Direct Deposit, PayPal, Interac e-Transfer
- Customer pricing: Custom per-task + audit packages
- Services: Retail audits, mystery shops, in-store surveys, market research
- Weakness vs Pixie: No AI-extracted structured data output; slow (days, not hours); no cryptographic proof; not real-time

**EasyShift** (acquired by Field Agent)
- Simple photo tasks, lower-end market
- Absorbed into Field Agent's platform

**Observa** (acquired)
- Similar model to Field Agent; acquired and wound down

**Storesight**
- 3M+ shopper network
- AI-powered analysis of gathered information
- Dashboard with intuitive presentation
- Similar to Field Agent with more AI polish

**Mapillary** (acquired by Meta/Facebook, 2020)
- Crowdsourced street-level imagery
- Used for mapping, not on-demand enterprise intelligence
- Not a competitor — potential validation of model

---

### Direct Competitors: Computer Vision Retail Intelligence

**Trax Retail**
- Raised: $1.03B total ($640M Series E, SoftBank Vision Fund 2; $50M venture debt, Deutsche Bank 2024)
- Revenue: $170.4M (reported)
- Model: Computer vision for shelf monitoring — uses fixed cameras, field reps, and proprietary image recognition
- Capability: Planogram compliance, out-of-stock detection, competitive share of shelf
- Weakness vs Pixie: Requires hardware installation in stores; enterprise sales cycle 6–18 months; can't cover ad-hoc locations; no crowdsourced on-demand
- Signal: $1B+ raised proves the market exists; Trax's hardware dependency is the opening

**Focal Systems**
- Shelf cameras + IoT sensors
- Real-time inventory monitoring
- Hardware-dependent (same weakness as Trax)

**VusionGroup**
- Electronic shelf labels + computer vision
- Deep retailer relationships
- Hardware-dependent

**Neurolabs**
- Synthetic data for training CV models
- Not a deployment platform — potential technology partner

**Vision Group**
- Retail execution software with image recognition
- Smaller scale than Trax

---

### Adjacent Competitors / Potential Pivots

**DoorDash / Uber**
- Have agent networks, location infrastructure, app expertise
- Could add "photo tasks" to driver downtime as a feature
- Threat timeline: 18–36 months if Pixie proves the market
- Mitigation: Proprietary AI models + enterprise contracts create switching costs before they move

**Appen (AI training data)**
- 1M+ global contributors
- Focuses on data labeling, annotation — not physical capture
- Potential partnership rather than competition

**Scale AI**
- AI training data and labeling
- Enterprise-focused
- No physical capture capability — potential customer (buy Pixie's labeled datasets)

**Google Street View / Apple Maps**
- Passive, route-based capture — not on-demand, not intelligence-focused
- Not competing in enterprise intelligence market

**GroundTruth (formerly xAd)**
- Location-based advertising platform
- Uses location/visitation data — not visual capture
- Different market, name conflict consideration (registered trademark)

---

### Competitive Positioning Summary

Pixie occupies the white space in a 2x2 matrix:
- X-axis: Physical location coverage (fixed hardware → crowdsourced on-demand)
- Y-axis: AI extraction quality (raw photos → structured data)

**Pixie**: Top-right (high coverage + high AI extraction)
**Trax**: Mid-right (high AI, limited coverage — hardware-bound)
**Field Agent**: Top-left (wide coverage, low AI — raw photos only)
**Mystery shopping agencies**: Mid-left (limited coverage, no AI)
**Manual field teams**: Bottom-left (minimal coverage, no AI)

---

## Market Sizing

### Retail Intelligence Market

**Shelf Image Recognition AI**
- 2024: $1.43B
- 2025: $1.82B
- 2029 forecast: $4.64B
- CAGR: 26.4%
- Source: GlobeNewswire, January 2026

**AI-Powered Retail Shelf Monitoring**
- 2024: $2.1B
- 2033 forecast: $15.1B
- CAGR: 21.8%
- Source: DataIntelo

**AI-Powered Shelf Management Software**
- 2025: $387M
- 2032 forecast: $940M
- CAGR: 16.8%
- Source: IntelMarketResearch

**Mystery Shopping Services (proxy for WTP)**
- 2025: $2.31B–$2.8B (varies by source)
- 2032 forecast: $2.5B–$3.5B
- CAGR: 8.6%
- North America: 43.89% of global market
- Cost per audit: $30–$175 (simple photo tasks at lower end)
- Source: FortuneBusinessInsights, OpenPR

---

### Government/Traffic/Smart City Market

**Intelligent Traffic Management Systems**
- 2025: $13.77B
- 2033 forecast: $48.67B
- CAGR: 17.8%
- Source: GrandViewResearch

**AI for Smart City Traffic Optimization**
- 2025: $10.21B
- 2035 forecast: $164.72B
- CAGR: 32.06%
- Source: PrecedenceResearch

**Smart Cities Overall**
- 2025: Estimated $580B+ (broad definition)

---

### AI Training Data Market

**Total AI Training Dataset Market**
- 2024: $2.77B
- 2025: $3.59B
- 2033 forecast: $19.62B
- CAGR: 24.3%
- Source: GrandViewResearch, MarketDataForecast

**Image/Video segment**
- 41.9% of total AI training market in 2025
- = ~$1.5B in 2025, growing to ~$8.2B by 2033
- Key players: Scale AI, Appen (1M+ global contributors), AWS

---

### TAM / SAM / SOM

**TAM: $35B by 2030**
Retail intelligence + traffic/infrastructure monitoring + visual AI training data (combined)

**SAM: $8B by 2027**
On-demand, crowdsourced-compatible slice: mystery shopping, field audits, competitive intelligence, event monitoring, AI training data from real-world capture

Excluded from SAM: hardware-installed retail monitoring (Trax), satellite imagery, CCTV

**SOM — Year 1: $3.6M ARR**
25 enterprise customers × $12K/month avg = $300K MRR × 12 = $3.6M ARR

**SOM — Year 3: $50M+ ARR**
100 enterprise customers × avg $42K/month = $4.2M MRR × 12 = $50M ARR

---

## Technology Landscape

### Face Redaction / Privacy
- **MediaPipe Face Detection** (Google): On-device, <5ms on modern phones, iOS 12+ / Android 7+. Best for real-time preview.
- **Celantur Edge SDK**: Real-time anonymization SDK, faces + license plates + bodies. Commercial licensing.
- **BlurMe**: Enterprise API, live stream capable, up to 95% workload reduction.
- **SecureRedact**: SaaS + API, GDPR-focused, post-capture batch processing.
- **Deface** (open-source): Batch processing only, not mobile-compatible.

**Pixie approach**: MediaPipe on-device for real-time preview + custom TFLite model as secondary validator. Server-side secondary check confirms no faces in uploaded frames.

### Computer Vision / Extraction
- **YOLO v9/v10**: Real-time object detection, runs on-device (TFLite) and server-side. Best for product/SKU detection.
- **EfficientNet**: Classification tasks (brand recognition, product type).
- **Tesseract + custom transformers**: Price tag OCR. Tesseract for standard printed tags; custom model for electronic shelf labels.
- **SKU-110K dataset**: 11,762 retail shelf images, 1.73M bounding box annotations — key training dataset for shelf detection models.
- Industry accuracy: 90–99% in controlled conditions; ~80% in real-world retail (Trax benchmark).

### Tamper-Proof Proof Chain
- **C2PA standard** (Coalition for Content Provenance and Authenticity): Backed by Adobe, Microsoft, Google, Intel. Emerging industry standard for photo provenance / "content credentials."
- **Ed25519 cryptography**: Fast, compact signatures for device-level signing.
- **OriginStamp**: Blockchain timestamping — immutable external proof of existence at time T.
- **Android SafetyNet / Apple DeviceCheck**: Hardware attestation — proves signing happened on a real, unrooted device.

### Gig Worker Earnings Benchmarks (2025)
- Uber: $23.33/hr average gross
- DoorDash: $11/hr average
- TaskRabbit: $38/hr average (skilled tasks)
- Field Agent: $2–$20/task ($8–$80/hr equivalent for 15-min tasks)
- Pixie target: $8–$35/task → $25–$70/hr equivalent (competitive with TaskRabbit, 3x DoorDash)
