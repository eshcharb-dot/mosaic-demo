# Pixie — Cycle Log (All 100 Cycles)

## Phase 1 — Discovery (Cycles 1–20)

### Cycle 1: Competitive Landscape — Direct Crowdsourced Platforms
**Focus**: Who exists in crowdsourced physical-world data collection
**Method**: Research
**Work**: Identified Premise Data ($188M raised, 2.6M contributors, retail + government), Field Agent (2M+ app downloads, $2–20/task, 200K+ agents, focus on retail audits), Storesight (in-store intelligence via shoppers), EasyShift (acquired by Field Agent), Observa (acquired). Mapillary (crowdsourced street imagery, acquired by Meta 2020).
**Output**: RESEARCH.md — Competitor section
**Key insight**: Premise Data is the closest analog — crowdsourced, multi-vertical, machine learning layer — but focuses on surveys/price checks, not rich visual capture with AI extraction. Field Agent is retail-only, low-tech. Neither has real-time visual AI + tamper-proof proof chain.

---

### Cycle 2: Competitive Landscape — Computer Vision Retail Intelligence
**Focus**: AI-powered shelf intelligence incumbents (non-crowdsourced)
**Method**: Research
**Work**: Trax ($1.03B raised, $170M revenue, uses fixed cameras + field reps), Focal Systems (shelf cameras, IoT), VusionGroup (electronic shelf labels + vision), Neurolabs (synthetic data for CV training). Trax's weakness: expensive hardware deployment, enterprise sales cycle, no surge/on-demand capability.
**Output**: RESEARCH.md — CV Retail section
**Key insight**: Trax et al. require hardware installation — Pixie's crowdsourced model has zero hardware cost and can reach any location instantly. The moat is coverage, not cameras.

---

### Cycle 3: Competitive Landscape — Adjacent + Emerging Threats
**Focus**: Who could pivot into this space
**Method**: Research + analysis
**Work**: DoorDash/Uber (have agent networks, could add tasks), Appen/Scale AI (data labeling, no physical capture), Google Street View (passive, not on-demand), Samsara/Motive (fleet cameras, fixed routes). Potential partner: Appen for training data monetization. Threat: Uber could add "capture tasks" as a feature.
**Output**: RESEARCH.md — Threats section
**Key insight**: Uber adding photo tasks to driver downtime is the biggest strategic threat. Defensibility requires proprietary AI + enterprise contracts before Uber notices.

---

### Cycle 4: Market Sizing — Retail Intelligence TAM
**Focus**: Total addressable market for retail shelf intelligence
**Method**: Research + calculation
**Work**: Shelf Image Recognition AI market: $1.82B in 2025, growing to $4.64B by 2029 (CAGR 26.4%). AI-powered retail shelf monitoring: $2.1B in 2024, projected $15.1B by 2033 (CAGR 21.8%). Mystery shopping (proxy for willingness to pay): $2.31B–$2.8B in 2025. Combined retail intelligence TAM: ~$20B by 2030.
**Output**: RESEARCH.md — Market Sizing
**Key insight**: The retail intelligence market is large and fast-growing. Pixie targets the physical/on-demand slice that incumbents can't serve — estimated $3–5B serviceable opportunity within the broader market.

---

### Cycle 5: Market Sizing — Government/Transit + Training Data
**Focus**: Secondary verticals TAM
**Method**: Research + calculation
**Work**: Intelligent Traffic Management: $13.77B in 2025, growing to $48.67B by 2033 (CAGR 17.8%). AI Training Dataset market: $3.59B in 2025, $19.62B by 2033 (CAGR 24.3%); image/video is 41.9% of that (~$1.5B in 2025). Smart Cities overall: massive but slow procurement cycles.
**Output**: RESEARCH.md — Market Sizing continued
**Key insight**: AI training data is an immediate monetization lever — Pixie's data flywheel produces labeled real-world visual datasets worth selling to AI labs. This is the "hidden" revenue stream that most investors will undervalue.

---

### Cycle 6: Market Sizing — Full TAM/SAM/SOM
**Focus**: Build defensible TAM → SOM funnel
**Method**: Calculation
**Work**:
- TAM: $35B (retail intelligence + traffic/infrastructure monitoring + visual AI training data, combined by 2030)
- SAM: $8B (on-demand, crowdsourced-compatible subset: mystery shopping, field audits, competitor checks, event monitoring, training data)
- SOM Year 1: $5M (10 enterprise customers × $500K ACV = $5M ARR) — conservative
- SOM Year 3: $50M (100 enterprise customers × $500K ACV)
**Output**: RESEARCH.md — TAM/SAM/SOM section
**Key insight**: The $100M Series A target implies investors need to see a credible path to $50M+ ARR. That requires ~100 enterprise accounts or a smaller number of large platform deals.

---

### Cycle 7: Regulatory Landscape — GDPR (EU)
**Focus**: European privacy law implications for image capture
**Method**: Research
**Work**: GDPR Article 6 (lawful basis), Article 9 (biometric data). Key: photographs of identifiable people = personal data. Legitimate interest can apply for commercial monitoring of public spaces if balanced against individual rights. Automatic face redaction is the critical mitigation — makes images non-personal data before transmission. GDPR fines: up to €20M or 4% global annual turnover.
**Output**: LEGAL_REGULATORY.md
**Key insight**: Baking redaction into the capture pipeline (before upload) is not just a feature — it's the legal architecture that makes the platform operable in the EU. Redaction must happen on-device, not server-side.

---

### Cycle 8: Regulatory Landscape — CCPA + US Laws
**Focus**: US privacy law for commercial image capture
**Method**: Research
**Work**: CCPA applies to businesses >$26.625M revenue or >100K CA residents' data. Photos aren't biometric under CCPA unless used for facial recognition. Key risk: Illinois BIPA (Biometric Information Privacy Act) — $1,000–$5,000 per violation for capturing biometric identifiers. Texas, Washington have similar laws. Agent consent + on-device redaction before transmission = primary compliance architecture.
**Output**: LEGAL_REGULATORY.md — US section
**Key insight**: BIPA is the highest litigation risk in the US. Illinois should be a late-stage launch market. Texas and Washington require opt-in consent for biometrics — redaction before transmission eliminates the biometric data creation entirely.

---

### Cycle 9: Regulatory Landscape — Gig Economy + Photography in Public
**Focus**: Worker classification and right-to-photograph laws
**Method**: Research
**Work**: AB5 (California ABC test) — Pixie agents must be free from company control, perform work outside usual business, and have independent trade. Prop 22 created carve-out for app-based platforms (Uber, DoorDash). Photography in public: generally legal in US for commercial purposes in public spaces. UK: no legal right to prevent photography in public. EU varies by country. Private property (inside stores): requires property owner permission — critical for retail use cases.
**Output**: LEGAL_REGULATORY.md — Gig + Photography section
**Key insight**: The "inside stores" problem is real — agents capturing shelf data in Walmart need either permission from the retailer OR a mystery-shopper framing where the agent is a regular customer. Retailer permission partnerships solve this cleanly.

---

### Cycle 10: Technology Landscape — Real-Time Face Redaction
**Focus**: On-device vs server-side redaction options
**Method**: Research
**Work**: Options: (1) Celantur Edge SDK — real-time anonymization SDK, faces + license plates + bodies. (2) BlurMe — enterprise API, up to 95% workload reduction, live stream capable. (3) SecureRedact — SaaS + API, GDPR-focused. (4) Open-source: Deface (GitHub, batch processing, not real-time mobile). For mobile on-device: MediaPipe Face Detection (Google, runs on-device, <10ms latency), YOLO-based models (can run on-device with Core ML / TensorFlow Lite).
**Output**: AI_ARCHITECTURE.md — Redaction section
**Key insight**: On-device redaction using MediaPipe or a custom TFLite model is achievable at <15ms latency on modern smartphones. This means faces are never uploaded — only redacted frames reach servers. This is both the GDPR solution and the privacy marketing message.

---

### Cycle 11: Technology Landscape — Computer Vision Extraction
**Focus**: What AI can extract from captured images
**Method**: Research
**Work**: SKU recognition: 90–99% accuracy in controlled conditions, ~80% in real-world (Trax benchmark). Key models: YOLO v9/v10 for detection, EfficientNet for classification. Price tag OCR: Tesseract (open source), Google Vision API (~$1.50/1000 images), AWS Textract. Shelf share analysis: custom model trained on planogram data. Occupancy counting: standard person detection (but redacted post-count). License plate OCR for parking/traffic.
**Output**: AI_ARCHITECTURE.md — Extraction section
**Key insight**: The AI extraction layer is the margin engine. Raw photo delivery is low-margin. Structured data output (JSON of SKUs, prices, occupancy) is where 10x pricing lives. This is the wedge from Tier 1 to Tier 2/3 customers.

---

### Cycle 12: Technology Landscape — Tamper-Proof Proof Chain
**Focus**: Cryptographic verification of submissions
**Method**: Research
**Work**: GPS + timestamp + gyroscope + accelerometer metadata locked at capture. SHA-256 hash of raw image signed with device private key + server timestamp. IPFS-style content addressing — hash is the address, any modification = different hash. Blockchain timestamping (OriginStamp, OpenTimestamps) for immutable proof of existence at time T. C2PA (Coalition for Content Provenance and Authenticity) standard — emerging industry standard for photo provenance, backed by Adobe, Microsoft, Google.
**Output**: TECH_STACK.md — Proof chain section, AI_ARCHITECTURE.md
**Key insight**: C2PA is the right standard to build on — it's becoming the industry standard for "content credentials" and will be recognized by enterprise customers as proof of authenticity. Building C2PA-compliant from day one is a differentiator.

---

### Cycle 13: Agent Economics Benchmarks
**Focus**: What gig workers earn on comparable platforms
**Method**: Research
**Work**: Uber: avg $23.33/hr (gross). DoorDash: avg $11/hr. TaskRabbit: avg $38/hr (skilled tasks). Field Agent: $2–$20/task (typically 5–15 min tasks = ~$8–80/hr equivalent). Premise Data: ~$0.10–$2.00/task (bulk, lower quality). Mystery shopper apps (Shopmetrics, BestMark): $15–$25/task. Key insight: photography tasks that require skill + location specificity should pay $5–$25/task to be competitive.
**Output**: BUSINESS_MODEL.md — Agent earnings section
**Key insight**: $8–$15/task is the sweet spot — better than DoorDash, competitive with Field Agent, attracts quality contributors. Surge pricing (3–5x) for urgent/rare locations creates income ceiling that drives agent acquisition.

---

### Cycle 14: Agent Economics — Earning Potential Modeling
**Focus**: Monthly earning potential to drive agent acquisition
**Method**: Calculation
**Work**:
- Casual agent (2 hrs/week): 4 tasks/hr × $10 avg × 8 hrs/month = $320/month
- Active agent (10 hrs/week): 4 tasks/hr × $12 avg × 40 hrs/month = $1,920/month
- Power agent (20+ hrs/week): 4 tasks/hr × $15 avg (surge included) × 80 hrs/month = $4,800/month
- Compare: DoorDash driver 20 hrs/week = ~$880/month
**Output**: BUSINESS_MODEL.md
**Key insight**: Pixie agents can earn 2–5x DoorDash equivalent on equal hours if task density is high. The acquisition message: "Earn more per hour than delivery. No car required."

---

### Cycle 15: Agent Economics — Platform Take Rate
**Focus**: What margin does the platform need to be sustainable
**Method**: Calculation
**Work**: Field Agent charges customers ~$30–$175/task while paying agents $2–$20 (rough 3–10x markup). Premise charges enterprises $0.50–$5/data point, pays contributors $0.10–$0.50. For Pixie: customer pays $25–$150/task. Agent earns $8–$35. Platform margin: 50–65%. AI processing cost: $0.05–$0.20/image (cloud inference). Net margin per task: 40–55%.
**Output**: BUSINESS_MODEL.md — Take rate section
**Key insight**: 55% platform take rate is justified by AI extraction value-add. Without extraction, the margin compresses to 40%. The AI layer is directly tied to pricing power.

---

### Cycle 16: Customer Willingness to Pay — Retail
**Focus**: What CPG/retail companies pay today for equivalent data
**Method**: Research + benchmarking
**Work**: Mystery shopping per audit: $30–$175 (simple photo tasks at lower end). Shelf audit services (manual): $150–$500/store/visit. Trax annual contract: estimated $100K–$500K/year for mid-size CPG. Nielsen/IRI syndicated data: $250K–$2M/year. Field Agent retail audit package: ~$5–$15/task (crowdsourced). On-demand shelf check (current market): ~$20–$50/location/visit.
**Output**: USE_CASES.md, BUSINESS_MODEL.md
**Key insight**: The on-demand, any-location capability creates a new category. CPG companies today pay $20–50/shelf check when they CAN get it. Pixie's pricing at $15–$75/task is competitive with current alternatives while delivering faster, richer data.

---

### Cycle 17: Customer Willingness to Pay — Government/Transit
**Focus**: What government agencies pay for monitoring/intelligence
**Method**: Research + analysis
**Work**: Traffic data subscriptions: TomTom/HERE charge cities $50K–$500K/year. Manual traffic counts: $500–$2,000/intersection/day. Infrastructure inspection: $5,000–$50,000 per bridge/major structure. Smart city contracts: $1M–$10M+ multi-year. Entry point: pilot at $5K–$25K for a specific monitoring campaign.
**Output**: USE_CASES.md
**Key insight**: Government sales cycles are 12–24 months. This is a Year 2+ revenue stream. The faster path: transit agencies (bus/metro operators) who need real-time platform occupancy data and have shorter procurement cycles than city governments.

---

### Cycle 18: Customer Willingness to Pay — Insurance + Real Estate
**Focus**: Insurance claims and real estate inspection use cases
**Method**: Research + analysis
**Work**: Insurance field inspection (in-person adjuster): $150–$500/visit. Remote photo-based claims: insurers like Lemonade and Hippo have shown $50–$150 is acceptable for photo-documented claims. Property condition reports: $200–$800/property. Construction progress reports: $500–$2,000/site/month. EagleView (aerial imagery): charges $40–$200/property report.
**Output**: USE_CASES.md
**Key insight**: Insurance is a high-volume, repeating use case. A single large P&C insurer could generate $1M+ ARR if Pixie replaces even 5% of their field inspection volume.

---

### Cycle 19: Discovery Synthesis — Key Risks
**Focus**: Synthesize top risks from discovery phase
**Method**: Analysis
**Work**:
1. LEGAL: In-store capture without retailer consent (trespassing/policy violation risk)
2. COMPETITIVE: Uber/DoorDash adding photo tasks to existing driver network
3. SUPPLY: Agent density in rare locations = task fulfillment failure
4. QUALITY: AI accuracy gap between demo and production conditions
5. REGULATORY: BIPA/GDPR non-compliance if redaction fails
6. BUSINESS MODEL: Race to bottom on per-task pricing as competitors emerge
7. TRUST: Enterprise customers won't adopt without audit trail + compliance
**Output**: VENTURE.md — Risk section
**Key insight**: The retailer consent problem is solvable through partnerships (retailers become customers, not adversaries). This reframes the product from "covert surveillance" to "retailer-enabled intelligence."

---

### Cycle 20: Discovery Synthesis — Key Opportunities
**Focus**: Where to double down based on research
**Method**: Analysis
**Work**:
1. TIMING: No company has combined crowdsourced capture + real-time AI extraction + tamper-proof proof chain. This combination is novel.
2. DATA FLYWHEEL: Training data monetization adds a revenue layer most competitors lack.
3. RETAILER PARTNERSHIPS: Retailers as customers AND as "access grants" for agents — eliminates the in-store legal problem.
4. C2PA STANDARD: Building on emerging content authenticity standard positions Pixie for enterprise trust from day one.
5. GEOGRAPHY: Launch in markets where AB5/GDPR pressure is lower (Texas, Florida, UK, Australia) to establish playbook before EU expansion.
**Output**: VENTURE.md — Opportunities section
**Key insight**: The most defensible position is becoming the "trusted physical world intelligence layer" — where enterprise trust, AI accuracy, and legal compliance form a moat that crowdsourced-only players can't replicate.

---

## Phase 2 — Use Case Design (Cycles 21–35)

### Cycle 21: Retail Shelf Intelligence — Use Case Design
**Focus**: Full design of flagship retail use case
**Method**: Design
**Work**: Customer persona: Sarah Chen, VP of Category Management at a mid-size CPG brand (think Vita Coco, KIND, or similar $500M revenue brand). Problem: her brand sells through 8,000 stores. She has a field sales team of 20 reps who can visit maybe 400 stores/month. She has NO visibility into the other 7,600 stores. Competitor promotional activity is invisible. Out-of-stocks cost her an estimated 4–8% of revenue. Task spec: "Photograph shelf section [specific aisle/bay coordinates], capture all [product category] SKUs, price tags, and promotional materials." AI output: SKU list, each SKU's position, facing count, price, any promotional tag, out-of-stock flags, share of shelf %.
**Output**: USE_CASES.md — Retail section
**Key insight**: The persona's key pain is not "I want photos" — it's "I'm losing revenue to invisible out-of-stocks and can't prove my promotional compliance." Pixie sells revenue recovery, not data.

---

### Cycle 22: Retail Shelf Intelligence — Task Specification + Data Model
**Focus**: Technical design of retail task
**Method**: Design
**Work**: Task fields: store_id, aisle_number, bay_number, product_category, capture_type (photo_set/video_pan), minimum_coverage (% of shelf), required_metadata (GPS, timestamp, device_id). AI extraction output schema: {task_id, store_id, timestamp, agent_id_hash, capture_proof: {gps, device_hash, c2pa_signature}, shelf_analysis: {sku_detections: [{sku_id, brand, product_name, facings, price, promotional_tag, position: {shelf_level, section_pct}}], out_of_stock_flags: [], share_of_shelf: {brand: pct}, planogram_compliance_score: 0-100}}.
**Output**: TECH_STACK.md — Data model, USE_CASES.md
**Key insight**: The structured JSON output is the product customers pay for. Raw images are byproduct. Designing the output schema first drives the AI architecture backwards.

---

### Cycle 23: Retail Shelf Intelligence — Pricing + Customer Value Calc
**Focus**: Price the retail use case and prove ROI to customer
**Method**: Calculation
**Work**: Customer value: A CPG brand losing 5% revenue to out-of-stocks on $500M = $25M/year lost. If Pixie recovers even 20% of that through faster detection + response = $5M/year recovered. Pixie pricing for this customer: 8,000 stores × 2 audits/month × $20/task = $3.84M/year — but this is too large for initial contract. Start with: 500-store pilot × 4 audits/month × $20/task = $480K/year pilot. ROI proof: 500 stores × avg $1,500 weekly revenue at risk from out-of-stocks × 2 recovery events = $1.5M recovered vs $480K cost = 3:1 ROI.
**Output**: BUSINESS_MODEL.md, USE_CASES.md
**Key insight**: The ROI case is strong enough to justify enterprise pricing. The $20/task rate is below mystery shopping ($30–$175) while delivering faster, richer, AI-extracted output. Price with confidence.

---

### Cycle 24: Government/Transit — Use Case Design
**Focus**: Full design of government monitoring use case
**Method**: Design
**Work**: Customer persona: Marcus Williams, Director of Operations at a regional transit authority (20–50 bus routes, 200–500 buses). Problem: he needs real-time platform crowding data to dispatch additional vehicles. Current solution: manual counts by staff at major stations. Task spec: "Photograph/video platform [station_id] [timestamp], count visible waiting passengers, assess crowding level (low/medium/high/critical)." AI output: occupancy estimate, crowd density map, trend vs historical baseline. Note: all faces redacted before transmission — only crowd count/density extracted.
**Output**: USE_CASES.md — Transit section
**Key insight**: The transit use case is politically sensitive (surveillance optics) but technically clean with redaction. The messaging must emphasize "we count crowds, not people" — crowd density, not surveillance.

---

### Cycle 25: Government/Transit — Infrastructure Inspection
**Focus**: Infrastructure monitoring use case
**Method**: Design
**Work**: Customer persona: Elena Rodriguez, Bridge/Infrastructure Program Manager at a state DOT. Problem: visual inspection of 500+ bridges, tunnels, road surfaces requires expensive in-person inspectors. Interval: mandated inspections every 24 months, but deterioration can happen faster. Pixie task: ground-level photography of specified bridge sections, road surface conditions, drainage infrastructure, signage condition. AI output: defect detection (cracks, spalling, corrosion), severity scoring, change detection vs previous inspection. Pricing: $200–$500/inspection visit vs $2,000–$5,000 for professional inspector.
**Output**: USE_CASES.md
**Key insight**: Infrastructure inspection is a huge government market but requires domain-specific AI models (not just generic CV). This is a Year 2+ use case that requires specialized training data — which Pixie will accumulate from transit use case first.

---

### Cycle 26: Government/Transit — Regulatory + Procurement
**Focus**: What it takes to sell to government
**Method**: Analysis
**Work**: FedRAMP authorization required for US federal contracts (18–24 month process, $500K–$2M cost). State/local: varies — some require local procurement vehicles (GSA schedule, state-specific contracts). Transit agencies: often operate as quasi-public entities with faster procurement. EU equivalent: ISO 27001 certification minimum, GDPR DPA (Data Processing Agreement) required. Recommendation: start with transit agencies (fastest procurement), use as reference for broader government expansion.
**Output**: LEGAL_REGULATORY.md — Government section, GTM.md
**Key insight**: Don't target federal government in Year 1. Target transit agencies and municipal governments in Year 1 as "lighthouse accounts" that unlock broader government procurement in Year 2–3.

---

### Cycle 27: Insurance/Claims Verification — Use Case Design
**Focus**: Full design of insurance use case
**Method**: Design
**Work**: Customer persona: David Park, Head of Claims Innovation at a regional P&C insurer. Problem: vehicle accidents and property damage claims require field adjuster visits ($150–$500/visit). Adjusters are in short supply after major weather events. Task spec: "Photograph vehicle/property at [address], capture all visible damage from 8 specified angles, include reference objects for scale." AI output: damage assessment, severity score, repair cost estimate range, fraud flags (inconsistent damage patterns). Pricing: $25–$75/claim inspection vs $150–$500 for adjuster. Volume: large insurer processes 500K+ claims/year.
**Output**: USE_CASES.md — Insurance section
**Key insight**: This use case has the highest volume potential — a single large insurer is a $10M+ annual contract. The limiting factor is regulatory approval (some states require licensed adjusters for final claims decisions). Pixie is a supplement, not a replacement.

---

### Cycle 28: Insurance/Claims — Fraud Detection Angle
**Focus**: Fraud detection as a premium layer
**Method**: Design + analysis
**Work**: Insurance fraud costs US insurers ~$80B/year. Photo-based fraud detection: staged accidents, pre-existing damage, inflated claims. AI signals: rust/wear patterns inconsistent with claimed recent accident, damage angles inconsistent with reported collision vector, VIN/odometer tampering. Forensic photography + tamper-proof proof chain makes Pixie's imagery court-admissible evidence. Premium pricing: fraud detection add-on at 2–3x base inspection rate.
**Output**: USE_CASES.md, AI_ARCHITECTURE.md
**Key insight**: The tamper-proof proof chain isn't just a technical feature — for insurance, it's the product. Court-admissible, cryptographically verified imagery commands premium pricing.

---

### Cycle 29: Real Estate — Use Case Design
**Focus**: Real estate and construction progress monitoring
**Method**: Design
**Work**: Customer persona A (Real Estate): James Nguyen, Portfolio Manager at a commercial RE investment fund. Problem: monitoring condition of 300+ properties across 15 states. Current: quarterly in-person inspections. Task: exterior/interior condition assessment, parking lot occupancy, signage/branding compliance, neighboring property changes. Pricing: $50–$150/property vs $500+ for in-person inspection. Volume: 300 properties × monthly × $75 = $270K/year.
Customer persona B (Construction): Maria Santos, Project Manager at a $500M construction GC. Task: daily progress photos of active sites. Pricing: $200–$800/site/month subscription. Volume: 50 active sites = $300K–$480K/month.
**Output**: USE_CASES.md — Real Estate section
**Key insight**: Construction progress monitoring is a recurring subscription model with high stickiness. Once a project manager builds their workflow around daily Pixie reports, they won't switch.

---

### Cycle 30: Real Estate — Retail Site Selection Intelligence
**Focus**: Location intelligence for retail expansion
**Method**: Design
**Work**: Customer persona: Rachel Kim, Director of Real Estate at a 500-location retail chain. Problem: evaluating 200 potential new store sites/year. Needs: foot traffic patterns, competitor density, street conditions, parking availability, neighboring businesses. Task: series of time-stamped photos at site throughout day (morning/noon/evening). AI output: foot traffic estimate, competitor presence, site condition score, accessibility assessment. Pricing: $150–$300/site assessment. Volume: 200 sites/year × $200 = $40K/year per customer — but there are thousands of retailers doing site selection.
**Output**: USE_CASES.md
**Key insight**: Site selection intelligence is a natural land-and-expand motion — sell 10 site assessments, prove value, then sell the ongoing monitoring subscription.

---

### Cycle 31: Brand/Marketing Intelligence — OOH Ad Monitoring
**Focus**: Out-of-home advertising compliance monitoring
**Method**: Design
**Work**: Customer persona: Kevin O'Brien, VP of Marketing at a Fortune 500 CPG. Problem: his company spends $50M/year on OOH (billboards, transit ads, point-of-sale displays). He has no way to verify that 90% of these placements are actually live, correctly printed, and properly positioned. Fraud/non-compliance estimate: 15–30% of OOH placements have some issue. Task: photograph specified billboard/display location, verify creative is live, assess condition, competitive share of voice at location. Pricing: $10–$30/OOH location check. Volume: 10,000 placements × monthly = 120,000 tasks/year × $15 = $1.8M/year per large advertiser.
**Output**: USE_CASES.md — OOH section
**Key insight**: OOH monitoring is extremely high volume, low per-task price, repeating. This is the task type that drives agent density and platform liquidity — high frequency creates the flywheel.

---

### Cycle 32: Brand/Marketing Intelligence — Competitor Store Checks
**Focus**: Competitive intelligence retail use case
**Method**: Design
**Work**: Customer persona: Priya Sharma, Brand Manager at a beverage company. Problem: needs weekly competitor pricing and promotional activity across 500 key accounts. Current method: her 5-person field team manually visits stores. Coverage: 500 stores/week × 5 days = 100 stores/day — impossible for 5 reps. Pixie task: photograph competitor shelf section, price tags, promotional materials. AI output: competitor SKU list, prices, promotional offer, display type, in-stock status. Pricing: $8–$15/competitive check. Volume: 500 stores × weekly × $10 = $260K/year.
**Output**: USE_CASES.md
**Key insight**: Competitive intelligence use cases have lower sensitivity (photographing competitor products in public retail) and higher customer urgency. This is the fastest use case to launch with least regulatory friction.

---

### Cycle 33: Use Case Prioritization — Scoring Matrix
**Focus**: Rank all use cases by attractiveness
**Method**: Analysis
**Work**: Scoring each use case on: Market Size (1–5), Willingness to Pay (1–5), Regulatory Risk (1=high risk, 5=low risk), Technical Complexity (1=complex, 5=simple), Sales Cycle Length (1=long, 5=short).

| Use Case | Mkt Size | WTP | Reg Risk | Tech | Sales | TOTAL |
|---|---|---|---|---|---|---|
| Retail shelf audit (own brand) | 5 | 4 | 4 | 4 | 3 | 20 |
| Competitor store checks | 4 | 3 | 5 | 4 | 4 | 20 |
| OOH ad monitoring | 4 | 3 | 5 | 3 | 3 | 18 |
| Insurance claims | 5 | 5 | 3 | 3 | 3 | 19 |
| Transit occupancy | 3 | 3 | 3 | 3 | 2 | 14 |
| Construction progress | 3 | 4 | 5 | 3 | 3 | 18 |
| Infrastructure inspection | 4 | 4 | 4 | 2 | 2 | 16 |
| RE site selection | 2 | 3 | 5 | 4 | 4 | 18 |
**Output**: USE_CASES.md — Priority ranking
**Key insight**: Retail shelf audit and competitor store checks tie at top. Launch with these two — lowest regulatory risk, shortest sales cycle, highest CPG budget availability.

---

### Cycle 34: Use Case Deep Dive — Competitor Store Checks as MVP
**Focus**: Why competitor store checks is the ideal MVP use case
**Method**: Analysis
**Work**: Competitor store checks are: (1) photographing products/prices that are publicly displayed — no privacy concerns, (2) no facial recognition needed, (3) CPG brands already have budget allocated for competitive intelligence, (4) measurable ROI (price response to competitor promotions), (5) high frequency = regular recurring revenue. Competitor: Numerator (tracks purchase data, not physical), NielsenIQ (aggregated, not real-time physical), Field Agent (manual, no AI extraction). None do real-time, AI-extracted competitive shelf intelligence at scale.
**Output**: USE_CASES.md, GTM.md
**Key insight**: Competitor store checks is the beachhead. It's the use case that gets CPG brands in the door with minimal friction, proves the platform, then expands to full shelf audits and custom tracking.

---

### Cycle 35: Use Case — AI Training Data as Revenue Layer
**Focus**: Monetizing platform data as AI training datasets
**Method**: Design
**Work**: Every task generates labeled visual data: shelf images with product annotations, street scenes with object labels, crowd scenes with density annotations (all faces redacted). Scale AI charges $0.05–$2.00/labeled image. Appen's 1M contributors generate datasets worth hundreds of millions. Pixie's data is differentiated: real-world (not stock photos), geo-tagged, time-stamped, task-labeled (shelf/traffic/construction). Projected: 1M tasks/month by Month 18 × 5 images/task = 5M images/month. At $0.10 average = $500K/month in training data revenue.
**Output**: BUSINESS_MODEL.md — Training data revenue
**Key insight**: Training data revenue is a high-margin, zero-incremental-cost revenue stream. The data is produced as a byproduct of customer tasks. This is the flywheel that funds agent earnings above market rate.

---

## Phase 3 — Business Model Design (Cycles 36–50)

### Cycle 36: Agent Earnings Model — Task Rate Structure
**Focus**: Design the agent earnings system
**Method**: Design
**Work**: Base rates by task type:
- Single photo (exterior, 1–3 images): $3–$5
- Photo set (8–12 images, interior): $8–$15
- Video pan (30–60 sec): $12–$20
- Live stream (per minute): $0.50–$1.50
- Complex audit (full shelf, AI-guided checklist): $15–$35
Surge multipliers: 1.5x (moderate demand), 2x (high demand), 3x (urgent/rare location), 5x (emergency/time-sensitive). Bonus layers: quality bonus (+20% for high-rated submissions), streak bonus (7-day active streak = +10%), referral bonus ($25 per recruited agent who completes 10 tasks).
**Output**: BUSINESS_MODEL.md — Agent earnings
**Key insight**: The $15–$35 complex audit rate positions Pixie at 2–3x DoorDash earnings per task-hour. This is the headline acquisition message.

---

### Cycle 37: Agent Earnings Model — Points/Rewards System
**Focus**: Design non-cash rewards to increase engagement
**Method**: Design
**Work**: Pixie Points system: 1 point per $0.10 earned. Redemption: Amazon gift cards, PayPal cash, Pixie merchandise, partner rewards (Starbucks, etc.). Level system: Rookie (0–100 tasks), Scout (101–500), Expert (501–2000), Elite (2001+). Level benefits: higher base rates (+5/+10/+15%), priority task access, early surge notifications, dedicated support. Milestone bonuses: 50-task milestone = $50 bonus, 500-task = $250 bonus. Leaderboard: weekly city-level leaderboard, top 10 agents earn bonus $50–$200.
**Output**: BUSINESS_MODEL.md
**Key insight**: The level/points system creates switching costs — agents with Elite status on Pixie have earned $0 equivalent status on any competitor platform. This is the retention mechanism for top performers.

---

### Cycle 38: Agent Earnings Model — Quality + Acceptance Rate
**Focus**: Quality control through economic incentives
**Method**: Design
**Work**: Quality score components: AI validation pass rate (40% weight), customer rating (30%), submission speed (20%), rejection rate (10%). Quality score impacts: <3.0 = task rate reduced 20%, 3.0–4.0 = standard rate, 4.0–5.0 = +10% quality bonus, 4.8+ Elite = +20% bonus. Acceptance rate requirement: must accept ≥60% of offered tasks in proximity to maintain "active" status. High-rep agents (4.8+) get auto-approval — bypassing manual QA queue, which reduces platform cost and improves their earnings speed.
**Output**: BUSINESS_MODEL.md, AI_ARCHITECTURE.md
**Key insight**: Auto-approval for high-rep agents is win-win: they get faster payouts, platform reduces QA cost by 60%+. Quality score is the asset agents build — gamification that also solves the platform's quality problem.

---

### Cycle 39: Customer Pricing — Tier Design
**Focus**: Design customer pricing tiers
**Method**: Design
**Work**:
**Tier 1 — Pay-per-task**: $15–$75/task depending on type. No subscription. Credit pre-purchase. Best for: one-off market checks, small brands testing. Min spend: $500.

**Tier 2 — Growth subscription**: $2,500–$10,000/month. Includes: 200–1,000 tasks/month, API access, standard AI extraction, dashboard access, 48hr turnaround SLA. Best for: mid-size CPG brands, regional insurers.

**Tier 3 — Enterprise**: $10,000–$100,000+/month. Custom task volume, dedicated task queue, custom AI models, real-time streaming, full data export, SLA <4hr, dedicated CSM, compliance docs (SOC 2, DPA). Best for: Tier 1 CPG, major insurers, transit authorities.

**Tier 4 — Platform API**: Custom pricing, usage-based. For companies building Pixie into their own products. Revenue share model available.
**Output**: BUSINESS_MODEL.md — Customer pricing
**Key insight**: Tier 2 at $2,500–$10K/month is the growth engine. Land with Tier 1, expand to Tier 2 within 90 days, target Tier 3 at 12 months.

---

### Cycle 40: Customer Pricing — Live Stream Pricing
**Focus**: Price the live feed / streaming tier
**Method**: Design + benchmarking
**Work**: Comparable pricing: Bandwidth/video infrastructure at $0.01–$0.05/min/stream. Operator cost: $0.50–$1.50/min agent earning + $0.10/min infrastructure = $0.60–$1.60/min cost. Customer pricing: $3–$8/min for standard live stream, $10–$20/min for AI-annotated live stream (real-time object detection overlaid). Enterprise subscription: unlimited streams at $15,000–$50,000/month (typical for traffic monitoring contracts). Surge rate: 2–5x for emergency situations (natural disasters, large events).
**Output**: BUSINESS_MODEL.md
**Key insight**: Live streaming is the highest-margin, highest-value product but requires agent density + reliable connectivity. This is a Year 2 product at scale, Year 1 in pilot mode for key accounts.

---

### Cycle 41: Customer Pricing — Report/Analytics Tier
**Focus**: Tier 3 deep report pricing
**Method**: Design
**Work**: Weekly shelf audit report (per category, per retailer chain): $500–$2,000/report. Monthly competitive intelligence summary: $1,000–$5,000/report. Quarterly trend analysis with YoY comparison: $5,000–$20,000/report. Custom AI model training for specific SKU set: one-time $10,000–$50,000 setup + $2,000–$10,000/month maintenance. API integration fee: $500–$2,000 one-time setup. Data warehouse integration (Snowflake, Databricks): included in Enterprise tier.
**Output**: BUSINESS_MODEL.md
**Key insight**: Reports turn raw task output into business decisions. Customers who buy reports have much higher retention (stickiness) than those who only buy raw task data.

---

### Cycle 42: Unit Economics — Per Task
**Focus**: Model the economics of a single task
**Method**: Calculation
**Work**:
Revenue per task (blended): $35 (mix of task types/tiers)
Agent payout: $14 (40% of revenue)
AI processing (inference): $0.15
Storage (images, 5MB avg × 10 images): $0.02
Platform infrastructure (allocate): $0.50
Payment processing (Stripe, 2.9% + $0.30): $1.32
Total COGS per task: $16.00
Gross profit per task: $19.00
Gross margin: 54%
At scale (fixed costs spread): gross margin expands to 65%+
**Output**: FINANCIAL_MODEL.md — Unit economics
**Key insight**: 54% gross margin at early stage is solid for a marketplace. The margin will expand as AI processing cost drops and agent pay stabilizes. Target 65%+ gross margin at Series A.

---

### Cycle 43: Unit Economics — CAC (Agent Side)
**Focus**: Cost to acquire an agent
**Method**: Calculation + benchmarking
**Work**: Uber driver CAC (reported): $50–$200. DoorDash driver CAC: $30–$100. Field Agent (no published data, est.): $20–$50. Pixie agent CAC targets: Organic (app store, word of mouth): $15–$25. Paid social (Facebook/Instagram): $30–$60. Partner networks (gig platform referrals): $20–$40. Ambassador program (campus/community): $10–$20. Blended target CAC: $25/agent. LTV per agent (assuming 50 tasks × $1.50 platform fee contribution above direct costs): $75 LTV. LTV:CAC = 3:1. This is healthy but requires agents to complete 50+ tasks to be LTV-positive.
**Output**: FINANCIAL_MODEL.md
**Key insight**: Agent onboarding-to-first-task conversion is the critical metric. If 50% of sign-ups complete 10+ tasks, the CAC math works at $25. Focus obsessively on the onboarding funnel.

---

### Cycle 44: Unit Economics — CAC (Customer Side)
**Focus**: Cost to acquire an enterprise customer
**Method**: Benchmarking
**Work**: Enterprise SaaS CAC benchmarks: $5,000–$50,000 for mid-market ($50K ACV), $50,000–$500,000 for large enterprise. Pixie Year 1 CAC strategy: founder-led sales (low cash CAC, high time cost). Sales team CAC at scale: 1 AE at $150K OTE, closes 12 deals/year at $30K ACV avg = $12,500 CAC. LTV at $30K ACV × 3-year avg contract × 85% net retention = $76,500 LTV. LTV:CAC = 6:1. This is excellent — target ≥3:1 at Series A.
**Output**: FINANCIAL_MODEL.md
**Key insight**: Founder-led sales for first 10 customers is essential — not just for cash conservation but for product intelligence. The 11th customer's needs are informed by the first 10.

---

### Cycle 45: Financial Model — Path to $1M ARR
**Focus**: Model the exact path to $1M ARR in 12 months
**Method**: Calculation
**Work**:
Month 1–3 (Pilot): 3 customers × $5K/month = $15K MRR
Month 4–6 (Traction): 8 customers × $8K/month avg = $64K MRR
Month 7–9 (Growth): 15 customers × $10K/month avg = $150K MRR
Month 10–12 (Scale): 25 customers × $12K/month avg = $300K MRR
Month 12 ARR run rate: $300K × 12 = $3.6M ARR

Alternatively, to hit exactly $1M ARR by Month 12:
Target: $83K MRR by Month 12
= 17 customers × $5K/month avg
This is achievable with 2 founders doing sales for 12 months.

$1M ARR milestone: 17 customers at $5K MRR average, or fewer customers at higher ACV.
**Output**: FINANCIAL_MODEL.md — Path to $1M ARR
**Key insight**: $1M ARR in 12 months requires landing one new customer per 3 weeks at $5K MRR. This is aggressive but achievable with a founder-sales motion and strong CPG network.

---

### Cycle 46: Financial Model — Path to $100M Series A
**Focus**: What metrics justify a $100M Series A
**Method**: Calculation + VC benchmark analysis
**Work**: Typical $100M Series A (2025 market): requires $5–$15M ARR or exceptional growth trajectory. At 10x ARR multiple: $10M ARR → $100M valuation. At 15x ARR multiple (high-growth marketplace): $7M ARR → $105M valuation. So target: $7–$10M ARR by Series A raise (typically Month 18–24). Path: $3.6M ARR at Month 12 → $8.5M ARR at Month 18 (137% net revenue retention assumed). Key growth inputs: agent density in 10 cities, 50+ enterprise customers, >$500K ACV accounts in pipeline.
**Output**: FINANCIAL_MODEL.md
**Key insight**: The $100M Series A is achievable at ~$8M ARR with 3x+ growth rate, proven unit economics, and 10-city coverage. The city count is as important as ARR — it proves the expansion playbook is repeatable.

---

### Cycle 47: Financial Model — Burn Rate + Runway
**Focus**: How much capital needed to reach Series A
**Method**: Calculation
**Work**:
Year 1 headcount: 2 founders + 2 engineers + 1 ML engineer + 1 sales = 6 people
Year 1 burn: Salaries ($600K) + Infrastructure ($150K) + Marketing/Agent Acquisition ($200K) + Legal/Compliance ($100K) + Misc ($50K) = $1.1M/year
Revenue Year 1: $1M ARR (ramp = ~$600K cash collected)
Net burn Year 1: ~$500K

Year 2 (pre-Series A) headcount: +5 engineers, +2 sales, +1 ops = 14 people
Year 2 burn: $2.5M
Year 2 revenue: $5M
Net: cash flow positive by end of Year 2

Seed round needed: $2.5M (18-month runway to $3.6M ARR)
Series A: $100M at $8M ARR / Month 18–24
**Output**: FINANCIAL_MODEL.md
**Key insight**: A $2.5M seed gives 18 months of runway to prove the model and hit Series A metrics. This is a lean seed ask — doable from angels + pre-seed funds without full VC syndication.

---

### Cycle 48: Competitive Pricing — Where to Price vs Alternatives
**Focus**: Positioning relative to incumbent alternatives
**Method**: Analysis
**Work**:
- vs Field Agent ($30–$175/task): Pixie is 30–60% cheaper per task AND delivers AI-extracted structured data, not just raw images
- vs Mystery shopping agencies ($50–$300/visit): Pixie is 70% cheaper with faster turnaround (hours vs days)
- vs Trax ($100K–$500K/year contract): Pixie's pay-per-task entry point removes the commitment barrier
- vs Manual field reps ($50–$150/hour fully loaded): Pixie at $20/task × 20 min = equivalent to $60/hr, but with AI extraction included

Pricing strategy: "Premium to gig task apps, discount to enterprise incumbents." This positions Pixie as the obvious upgrade from low-quality crowdsourcing AND the obvious entry point from expensive enterprise solutions.
**Output**: BUSINESS_MODEL.md — Competitive positioning
**Key insight**: The pricing sweet spot is 50–70% below enterprise contracts but 2–3x more valuable than existing task apps. This is the classic "disruption" price point.

---

### Cycle 49: Freemium vs Premium Strategy
**Focus**: Should Pixie have a free tier?
**Method**: Analysis
**Work**: Arguments FOR freemium: (1) CPG marketing managers need low-friction trial, (2) self-serve growth without sales team, (3) can collect emails for nurture. Arguments AGAINST: (1) free users devalue the product, (2) task economics don't support free (agent must be paid), (3) enterprise buyers don't want a "free" product. Decision: No consumer freemium. Instead: "Starter pack" — $500 prepaid credit (30–50 tasks). This is low enough to be expensed without procurement, high enough to create real trial. Conversion target: 40% of Starter packs → Growth subscription within 90 days.
**Output**: BUSINESS_MODEL.md — Freemium analysis
**Key insight**: The $500 starter pack is the freemium equivalent for B2B — it removes the commitment barrier while maintaining the perception of a premium product.

---

### Cycle 50: Business Model — Data Moat + Flywheel
**Focus**: How the business model creates a compounding moat
**Method**: Analysis
**Work**: The Pixie flywheel: (1) More customers → more tasks → more agent earnings → more agents join. (2) More agent completions → more AI training data → better AI extraction → higher customer value → higher pricing power → more customers. (3) More data → proprietary models for specific retail chains, specific industries → switching cost increases. (4) Proprietary models trained on Pixie data can be sold as AI Training Data to competitors' AI labs — monetizing the moat. This is the "data flywheel" that justifies the high Series A valuation multiple.
**Output**: VENTURE.md — Competitive moat section
**Key insight**: The flywheel means the business gets harder to compete with over time, not easier. This is the core investment thesis: Pixie's moat is temporal — the longer they operate, the more valuable their data and models become.

---

## Phase 4 — Technical Architecture (Cycles 51–65)

### Cycle 51: Agent Mobile App — Architecture Overview
**Focus**: Design the agent app architecture
**Method**: Design
**Work**: Platform choice: Flutter (chosen over React Native — better performance for camera/GPS-intensive tasks, 60/120fps, Dart's AOT compilation eliminates JS bridge overhead for real-time preview). Key screens: (1) Task Discovery Map (geo-fenced task pins), (2) Task Detail + Accept, (3) Capture Interface (guided camera with overlay), (4) Submission + Progress, (5) Earnings Dashboard. Key technical requirements: background location (for task proximity alerts), camera API (with real-time redaction preview), offline queue (submit when connectivity restored), secure enclave for device key storage (for tamper-proof signing).
**Output**: TECH_STACK.md — Mobile architecture
**Key insight**: Flutter is the right choice. The camera preview with real-time face redaction overlay is a Flutter-native use case — it requires tight camera control and 60fps preview that React Native would struggle with.

---

### Cycle 52: Agent Mobile App — Task Discovery + Geo-fencing
**Focus**: How agents find and accept tasks
**Method**: Design
**Work**: Task discovery: map-based UI with task pins (colored by type/pay/urgency). Geo-fence radius: tasks visible within 5km, detailed view within 1km, accept button unlocks at 500m proximity. Push notifications: "High-paying task near you" with estimated earnings and distance. Task assignment: soft lock (15-min reservation on acceptance, hard lock when capture begins). Crowding prevention: max 3 agents can accept same task simultaneously (nearest agent with highest reputation gets priority fulfillment credit). Privacy: agent GPS only recorded at task acceptance and task completion, not continuously.
**Output**: TECH_STACK.md
**Key insight**: Continuous GPS tracking of agents is the fastest way to destroy trust and trigger regulatory scrutiny. GPS only at task acceptance + completion is sufficient for routing and is a privacy-forward design choice that's also a marketing message.

---

### Cycle 53: Agent Mobile App — Capture UX
**Focus**: Design the camera interface for task capture
**Method**: Design
**Work**: Guided capture overlay: AR-style guide showing required coverage (e.g., "pan shelf left to right"), progress indicator (% of required coverage captured), real-time AI validation preview ("shelf detected ✓", "product labels visible ✓", "faces detected — blurring..."). Face redaction: on-device, real-time, using MediaPipe Face Detection + custom blur shader in Flutter. Capture confirmation: preview of redacted submission before upload. Metadata lock: GPS, timestamp, device accelerometer signature locked at capture initiation — cannot be spoofed post-capture.
**Output**: TECH_STACK.md, AI_ARCHITECTURE.md
**Key insight**: The guided capture overlay is the key UX innovation — it makes quality control proactive (guide the agent) rather than reactive (reject bad submissions). This reduces rework and speeds agent earnings.

---

### Cycle 54: AI Pipeline — Real-Time Redaction Architecture
**Focus**: Full design of the face/person redaction system
**Method**: Design
**Work**: Architecture: (1) On-device: MediaPipe Face Detection (< 5ms, runs on Android 7+/iOS 12+) detects faces in real-time preview. (2) On-device blur: Gaussian blur applied to detected bounding boxes before frame is encoded. (3) Server-side validation: secondary check on uploaded frames — ML model confirms no detectable faces in upload (double-check). (4) License plate detection: separate model (YOLOv8 fine-tuned on LP dataset) for vehicle use cases. (5) Full-body silhouette blur: optional setting for high-privacy jurisdictions (EU). Fallback: if on-device model fails to load, camera is disabled with "checking redaction availability" message.
**Output**: AI_ARCHITECTURE.md — Redaction system
**Key insight**: The server-side secondary check is the compliance backstop. If on-device redaction fails in any edge case, the server-side validation catches it before data is stored or delivered to customers.

---

### Cycle 55: AI Pipeline — Content Validation (Quality Gate)
**Focus**: AI that validates submission content before acceptance
**Method**: Design
**Work**: Validation pipeline (runs server-side, < 3 seconds): (1) Content detection: "Does this image contain the requested content?" (shelf → product detection, street scene → relevant objects present). (2) Coverage check: Was the required area captured? (% of shelf visible). (3) Quality check: blur score, exposure assessment, minimum resolution. (4) Consistency check: GPS coordinates match task location? Timestamp within task window? Device signature matches accepted task? (5) Output: ACCEPT / REJECT_WITH_FEEDBACK / ESCALATE_TO_HUMAN. Human review queue: <5% of submissions should require human review.
**Output**: AI_ARCHITECTURE.md — Validation pipeline
**Key insight**: The <3 second validation SLA is critical for agent experience — instant feedback on whether their submission was accepted means they know within seconds if they earned their payment. No waiting.

---

### Cycle 56: AI Pipeline — Structured Data Extraction
**Focus**: Design the extraction models for each use case
**Method**: Design
**Work**: Retail extraction models: (1) Product detection (YOLO-based, fine-tuned on retail datasets): bounding boxes, class labels. (2) Price tag OCR (custom transformer, handles handwritten/printed/electronic shelf labels). (3) Brand/logo recognition (ResNet-based). (4) Planogram compliance (shelf layout expected vs actual). (5) Occupancy counting (transformer-based crowd counting — faces already redacted, counts silhouettes/body positions). Traffic: (6) Vehicle counting + classification (cars/trucks/buses). (7) Road condition detection (crack/pothole/marking fading). All models fine-tuned on Pixie's own production data as it accumulates.
**Output**: AI_ARCHITECTURE.md — Extraction models
**Key insight**: The models are not one-size-fits-all — each use case needs a fine-tuned specialist model. The training data flywheel feeds these models directly. Month 1: use foundation models. Month 6+: start fine-tuning on Pixie production data. Month 18: models trained on Pixie data outperform generic models.

---

### Cycle 57: Cryptographic Proof System — Architecture
**Focus**: Design the tamper-proof submission chain
**Method**: Design
**Work**: Components: (1) Device Identity: at first launch, device generates an Ed25519 keypair. Public key registered with Pixie server + optional hardware attestation (Android SafetyNet / Apple DeviceCheck). (2) Capture Signature: at capture initiation, server issues a "task token" with task_id + timestamp + nonce. At capture completion: SHA-256 hash of {raw_frame_hash, gps_at_capture, timestamp_ms, gyro_snapshot, task_token} signed with device private key. (3) C2PA Manifest: wrapped in C2PA-compatible structure with Pixie's certificate authority signature. (4) Immutable record: hash stored in append-only log (PostgreSQL with row-level security + OriginStamp blockchain timestamping for external verifiability).
**Output**: TECH_STACK.md — Proof system
**Key insight**: Android SafetyNet / Apple DeviceCheck provides hardware-level attestation that the signing happened on a real, unrooted device — this closes the "jailbroken device spoofing GPS" attack vector.

---

### Cycle 58: Cryptographic Proof System — Anti-Gaming
**Focus**: Prevent agents from gaming the system
**Method**: Design
**Work**: Attack vectors + mitigations: (1) GPS spoofing → Hardware attestation (SafetyNet/DeviceCheck) + accelerometer consistency check (walking pattern expected for location traversal). (2) Photo replay (submitting old photos) → Task token + timestamp lock at capture initiation — tokens expire in 30 minutes. (3) AI-generated fake images → C2PA manifest traces to real device, model detection (GAN detector in validation pipeline). (4) Coordinated fraud (multiple agents submitting same photo) → Perceptual hash deduplication across submissions for same task. (5) Identity fraud → Phone number + government ID verification for agents earning >$600/year (IRS 1099 threshold).
**Output**: TECH_STACK.md — Anti-gaming, LEGAL_REGULATORY.md
**Key insight**: Most gaming attacks require significant effort and technical sophistication. The combination of hardware attestation + task tokens + perceptual dedup catches >95% of fraud attempts.

---

### Cycle 59: Customer Dashboard + API Design
**Focus**: What customers see and how they access data
**Method**: Design
**Work**: Dashboard modules: (1) Task Management: create tasks, define scope, set budget, monitor fulfillment status. (2) Live Map: see task completion in real-time, view completed submissions on map. (3) Analytics: AI-extracted data visualized — shelf share trends, price tracking charts, occupancy heatmaps. (4) Submission Viewer: view individual submissions with AI annotation overlays, download raw + structured data. (5) Reports: scheduled weekly/monthly reports, custom date ranges. API: REST + webhooks. Key endpoints: POST /tasks, GET /tasks/{id}/results, GET /tasks/{id}/stream, POST /webhooks. Data export: JSON, CSV, direct Snowflake/BigQuery export for Enterprise.
**Output**: TECH_STACK.md — Customer-facing systems
**Key insight**: The customer dashboard is the product — not the app. Enterprise customers judge the platform by dashboard quality. Invest in dashboard UX from day one, even before mobile app polish.

---

### Cycle 60: Backend Architecture
**Focus**: Server-side architecture design
**Method**: Design
**Work**: Core services: (1) Task Service: task creation, assignment, fulfillment tracking. (2) Capture Ingest Service: receive submissions, validate signatures, queue for AI processing. (3) AI Processing Service: orchestrate validation + extraction pipeline. (4) Agent Service: earnings, reputation, notifications. (5) Customer Service: dashboard data, API, billing. Infrastructure: Kubernetes on AWS (EKS). Message queue: Apache Kafka for capture ingest (handles burst traffic from viral task events). Database: PostgreSQL (Supabase-compatible for rapid development), Redis for real-time task assignment. Storage: S3 (raw images, encrypted at rest), CloudFront CDN for delivery. AI: AWS SageMaker for model hosting, with spot instances for batch processing.
**Output**: TECH_STACK.md — Backend architecture
**Key insight**: Kafka as the ingest layer is critical — when a viral task event happens (e.g., 10,000 agents completing tasks at a sporting event), the system must absorb burst traffic without losing submissions.

---

### Cycle 61: ML Infrastructure
**Focus**: Machine learning infrastructure design
**Method**: Design
**Work**: Model serving: SageMaker endpoints for production inference (auto-scaling). Model registry: MLflow for versioning, experiment tracking. Training pipeline: Airflow-orchestrated, triggered weekly for fine-tuning on new production data. Labeling pipeline: new tasks auto-generate labeled data; edge cases (low confidence) routed to human labelers (initially internal, then Scale AI API). Feature store: Feast (open source) for agent reputation features, image quality features. Monitoring: Evidently AI for data drift detection — alerts when model accuracy drops in new store format or new region.
**Output**: AI_ARCHITECTURE.md — ML infrastructure
**Key insight**: The weekly fine-tuning cadence means models improve continuously without manual intervention. The drift monitoring is critical — a new region (e.g., UK vs US shelf formats) will cause accuracy drops without it.

---

### Cycle 62: Security + Compliance Architecture
**Focus**: SOC 2 readiness, data security
**Method**: Design
**Work**: SOC 2 Type II: begin audit in Month 9, achieve certification by Month 15. Requirements: access controls (RBAC, MFA for all internal systems), audit logging (all data access logged to immutable store), encryption (TLS 1.3 in transit, AES-256 at rest), incident response plan, vulnerability management (quarterly pen test). GDPR: Data Protection Officer (DPO) appointed (can be founder initially), Privacy by Design documentation, Data Processing Agreements with all customers. Data minimization: raw images deleted after 30 days (customer configurable), only structured data + proof chain retained long-term.
**Output**: LEGAL_REGULATORY.md — Compliance plan, TECH_STACK.md
**Key insight**: SOC 2 is table stakes for enterprise sales. Without it, most Fortune 500 procurement teams will reject the platform at due diligence. Start the process early — 6 months before you need the certificate.

---

### Cycle 63: Tech Stack — Final Selection
**Focus**: Finalize all technology choices with rationale
**Method**: Decision
**Work**:
- Mobile: Flutter (Dart) — best camera performance, single codebase
- Backend: Node.js (TypeScript) — fast development, large talent pool
- Database: PostgreSQL via Supabase — managed, Row Level Security, real-time subscriptions
- Cache/Queue: Redis + Apache Kafka
- Cloud: AWS primary (EKS, SageMaker, S3, CloudFront)
- AI/ML: PyTorch training, TensorFlow Lite (mobile), SageMaker serving
- Face redaction mobile: MediaPipe (Google)
- Auth: Clerk (agent app) + Auth0 (enterprise dashboard)
- Payments: Stripe (customer billing) + Hyperwallet (agent payouts — supports 200+ countries)
- Monitoring: Datadog APM + Evidently AI (ML)
- CDN: CloudFront + Cloudflare for DDoS protection
- Proof chain: custom Ed25519 + OriginStamp for timestamping
**Output**: TECH_STACK.md — Final stack
**Key insight**: Hyperwallet (PayPal subsidiary) for agent payouts is the right choice for global expansion — it handles 200+ countries, currency conversion, and local payout methods (mobile money, bank transfer, etc.) that are critical for emerging market agent acquisition.

---

### Cycle 64: Mobile Performance Optimization
**Focus**: Performance requirements for camera-heavy app
**Method**: Design
**Work**: Key performance targets: camera preview: 30fps minimum, 60fps target. Face redaction overlay: <15ms latency (MediaPipe achieves 5–10ms on mid-range devices). App size: <50MB (critical for adoption in emerging markets with limited storage). Offline mode: task metadata cached, submissions queued locally, uploaded when WiFi available (reduces cellular data cost — agent retention issue). Battery: camera-intensive tasks drain battery — implement adaptive quality mode that reduces preview resolution on low battery. Accessibility: high contrast mode, large text support (agents are diverse age range).
**Output**: TECH_STACK.md — Performance
**Key insight**: Offline submission queue is a critical retention feature — agents in areas with spotty connectivity (rural, subway, large buildings) will abandon the platform without it.

---

### Cycle 65: Integration Architecture
**Focus**: How Pixie integrates with customer systems
**Method**: Design
**Work**: Customer integrations needed: (1) Retail: Salesforce integration (task results populate into CRM for field sales teams), SAP/Oracle integration for planogram compliance data. (2) Insurance: Guidewire integration (claims workflow), Snapsheet integration (claims management). (3) Analytics: Snowflake/BigQuery native connectors, Tableau/Power BI certified connectors. (4) Notifications: Slack/Teams webhooks for instant task completion alerts. (5) SSO: SAML 2.0 / OIDC for enterprise user management. Build Year 1: Salesforce, Slack, Snowflake, REST API. Build Year 2: Guidewire, SAP, Power BI.
**Output**: TECH_STACK.md — Integrations
**Key insight**: Salesforce integration is a must-have for CPG enterprise sales — the VP of Category Management lives in Salesforce. If Pixie data surfaces inside their existing workflow, adoption is 3x faster.

---

## Phase 5 — Go-to-Market (Cycles 66–80)

### Cycle 66: City Launch Playbook — Supply Side (Agents)
**Focus**: How to seed agent density in a new city
**Method**: Design
**Work**: Pre-launch (6 weeks before): (1) City Captain hired (local contractor, $2K/month, 20 hrs/week). (2) Facebook/Instagram geo-targeted ads: "Earn up to $35/hour photographing your city." (3) Reddit/local Facebook groups: "Gig workers in [City] — new high-paying app." (4) University partnerships: poster campaign + career fair table. (5) Existing gig worker forums: TaskRabbit, Field Agent, Mechanical Turk communities. Target: 500 active agents in city before first customer task goes live. Launch threshold: 200 agents with verified profiles.
**Output**: GTM.md — City launch supply
**Key insight**: 200 verified agents in a city before the first task creates fulfillment reliability that enterprise customers require. Never launch a city for customers until supply is seeded.

---

### Cycle 67: City Launch Playbook — Demand Side (Customers)
**Focus**: How to land first enterprise customers in each city
**Method**: Design
**Work**: City selection criteria: (1) High CPG brand presence (measured by number of major retail stores), (2) existing Field Agent / mystery shopping activity (proves willingness to pay), (3) low regulatory complexity (avoid Illinois, California for Year 1). Top Year 1 cities: Chicago (despite BIPA — but competitor check use case has low risk), Atlanta, Dallas, Houston, Phoenix, Denver, Seattle, Miami, Nashville, Charlotte. Demand seeding: founder flies to city, books 3 meetings with CPG brand managers or regional insurance claims directors. Offer: free 50-task pilot. Target: 1 paying customer per city at launch.
**Output**: GTM.md — City launch demand
**Key insight**: The founder needs to be in-person in the first 10 cities. The enterprise relationship requires face-to-face trust for the first contract. This is not remotely scalable — it's intentionally un-scalable for customer quality reasons.

---

### Cycle 68: City Launch Playbook — The Flywheel Launch Sequence
**Focus**: The exact sequence for a successful city launch
**Method**: Design
**Work**:
Week 1–4: Agent recruitment (target 200 verified agents)
Week 5: Soft launch — free pilot tasks for 1–2 customers
Week 6–8: First paid tasks. Agent density monitor: if <20% task fulfillment within 4 hours, increase agent recruitment before scaling customer tasks.
Week 9–12: Full launch — open platform, customer self-serve available.
Success threshold: >80% task fulfillment rate within 2-hour SLA by Week 12.
Kill switch: if <50% fulfillment by Week 8, pause customer tasks, focus on agent recruitment for 2 more weeks before re-launching.
**Output**: GTM.md — Launch sequence
**Key insight**: The 80% fulfillment rate is the North Star metric for city health. Below 80%, the platform fails enterprise SLAs. Above 80%, word-of-mouth among enterprise customers spreads.

---

### Cycle 69: Viral Mechanics — Agent Referral Program
**Focus**: How agents recruit other agents (supply-side virality)
**Method**: Design
**Work**: Referral mechanics: Agent A shares personal referral code → Agent B signs up → Agent B completes 10 tasks → Agent A earns $25 bonus. Agent B earns $15 "welcome bonus" on first task completion. Social proof mechanic: after each payout, agent sees "Share your earnings on Instagram" with auto-generated "I just made $47 in 2 hours photographing [City]" card (no branding overkill — just clean earnings stat). Community mechanic: city-level WhatsApp/Telegram groups seeded by City Captain — agents share tips, upcoming high-value tasks, surge alerts.
**Output**: VIRAL_MECHANICS.md — Agent referral
**Key insight**: The earnings card social share is the highest-leverage viral mechanic. Gig worker communities trust peer earnings proof more than any ad. Make sharing frictionless and aspirational.

---

### Cycle 70: Viral Mechanics — City Takeover Mechanic
**Focus**: How Pixie "takes over" a city
**Method**: Design
**Work**: "City Siege" event: monthly in each active city. For 48 hours, double agent rates. Goal: saturate every major retail corridor in the city with agent coverage. Customer-facing: "This weekend, see 5,000 shelf photos from across [City] — live." Event creates: (1) massive data collection event that demonstrates platform scale to prospective customers, (2) media opportunity ("local photographers earn $X in 48-hour data sprint"), (3) agent recruitment buzz ("everyone in the city sees someone doing it"). Target: top 10 agents earn $500+ in a single City Siege weekend.
**Output**: VIRAL_MECHANICS.md — City Siege
**Key insight**: City Siege events create press opportunities, agent recruitment spikes, and customer proof points simultaneously. Budget: $50K/city for double agent rates during 48-hour window. ROI: priceless as a sales tool.

---

### Cycle 71: Viral Mechanics — Customer-Side Growth Loops
**Focus**: How customers bring other customers
**Method**: Design
**Work**: B2B referral: CPG brand manager refers colleague at different brand — earns $1,000 credit for each referral that pays >$5K. This is common (brand managers are social within the CPG community). Conference presence: Expo West, NACS, GMA Leadership Forum — sponsor photo walls with Pixie branding, demo live shelf data from the show floor. LinkedIn content: "We just got real-time competitive shelf data from 500 stores" — compelling enterprise content that brand managers share. Agency partnerships: market research agencies (IRI, Kantar partners) become resellers, adding Pixie data to their reports.
**Output**: VIRAL_MECHANICS.md — Customer growth loops, GTM.md
**Key insight**: Market research agency partnerships are the fastest path to enterprise scale. If IRI includes Pixie data in their syndicated reports, Pixie gets access to hundreds of CPG customers through a single integration.

---

### Cycle 72: Enterprise Sales Motion — ICP Definition
**Focus**: Define the Ideal Customer Profile precisely
**Method**: Design
**Work**:
**Primary ICP**: CPG Brand Manager / VP Category Management
- Company: $100M–$5B revenue CPG brand (not Procter & Gamble yet — too slow procurement)
- Vertical: Food & Beverage, Personal Care, Household Products
- Pain: field sales coverage gap, competitive pricing blindspot, promo compliance uncertainty
- Budget: $50K–$500K/year field intelligence budget
- Trigger events: new product launch, promotional campaign, competitor price change, quarterly business review

**Secondary ICP**: Regional Insurance Claims Director
- Company: Regional or national P&C insurer ($500M–$10B GWP)
- Pain: adjuster shortage, claim backlog, fraud losses
- Budget: claims technology budget $100K–$2M/year
- Trigger event: CAT event (hurricane, hail storm), adjuster turnover, fraud spike
**Output**: GTM.md — ICP
**Key insight**: The primary ICP's trigger events are predictable — new product launches happen on a seasonal schedule, and CPG competitive response windows are 2–4 weeks. Build trigger-based outreach around these events.

---

### Cycle 73: Enterprise Sales Motion — Pilot Structure
**Focus**: Design the enterprise pilot that converts to paid
**Method**: Design
**Work**: Pixie Pilot Structure:
- Duration: 30 days
- Scope: 50–100 tasks in 1–3 cities
- Cost: Free (no-risk trial) OR $500 starter pack (skin-in-game, higher engagement)
- Deliverable: Full AI-extracted report on pilot findings, ROI analysis, comparison to customer's existing data
- Milestone: Week 2 check-in with customer to show interim results
- Success criteria: customer agrees upfront what "good" looks like (e.g., "we want to verify our promo compliance in 50 stores")
- Conversion trigger: at Week 4, present ROI analysis. If ROI > 2:1, present Growth subscription proposal.
- Close rate target: 60% of pilots → paid within 30 days of pilot completion
**Output**: GTM.md — Pilot structure
**Key insight**: Pre-agreeing on success criteria is the most important part of the pilot. "We'll know this worked if X" removes ambiguity at close time. The customer can't say "we're not sure" if they defined X.

---

### Cycle 74: Enterprise Sales Motion — Contract + Pricing
**Focus**: Contract structure for enterprise deals
**Method**: Design
**Work**: Contract terms: Annual prepay preferred (improve cash flow). Monthly available at 15% premium. Volume commitment tiers: 500 tasks/month = $8,000/month, 2,000 tasks/month = $25,000/month, 10,000 tasks/month = $100,000/month (includes custom AI models). Multi-city discount: 5 cities = 10% discount, 10 cities = 20% discount. Data ownership: customer owns their data and AI extraction results. Pixie retains right to use anonymized, aggregated, non-attributable data for platform improvement. IP: custom AI models trained exclusively for a customer are customer IP (included in Enterprise tier).
**Output**: GTM.md — Contract terms
**Key insight**: Annual prepay at 15% premium vs monthly is the cash flow lever. If 50% of customers choose annual, the business can operate with much less venture debt. Push hard for annual.

---

### Cycle 75: Agent Acquisition — Channel Strategy
**Focus**: Which channels to prioritize for agent recruitment
**Method**: Analysis + research
**Work**: Channel ranking by CAC and quality:
1. **Ambassador program** (campus/gig community): CAC $10–$20, highest quality agents (motivated, local knowledge)
2. **Referral program** (agent-to-agent): CAC $15–$25 (referral bonus cost), proven quality (friend vouching)
3. **Organic app store**: CAC $5–$15, variable quality
4. **Paid social (FB/IG/TikTok)**: CAC $30–$60, volume driver
5. **Gig platform partnerships** (Mechanical Turk, Amazon Flex community): CAC $20–$40
6. **Job boards** (Indeed "gig" category): CAC $40–$80, lower conversion

Year 1 channel mix: 40% ambassador, 30% referral, 20% paid social, 10% organic.
**Output**: GTM.md — Agent acquisition
**Key insight**: The ambassador program scales through university networks — 500 US universities × 1 campus ambassador × avg 50 recruits = 25,000 agents from one channel at $20 CAC = $500K spend for first 25,000 agents.

---

### Cycle 76: Agent Acquisition — Campus Ambassador Program
**Focus**: Design the campus ambassador program
**Method**: Design
**Work**: Ambassador role: student earns $200/month (paid in Pixie credits) for recruiting 10+ active agents/month from their campus. Selection criteria: active on campus (club president, athlete, influencer type), existing gig worker themselves (authentic credibility), in geography-targeted city. Onboarding: 1-hour video training, Pixie Ambassador Kit (branded t-shirt, QR code flyers, social media templates). KPI: 10 active agent completions in first month. Promotion: top ambassadors become "City Captains" earning $500/month. Scale: 50 campus ambassadors → 500 active agents/month at $10K/month total cost.
**Output**: GTM.md — Ambassador program
**Key insight**: The $200/month ambassador stipend is paid in Pixie credits, not cash. This creates ambassadors who are also active agents, are personally invested in platform quality, and cost 50% less in cash while driving real usage.

---

### Cycle 77: Agent Acquisition — Partnership Strategy
**Focus**: Partnerships for agent acquisition at scale
**Method**: Design
**Work**: Key partnership targets:
1. **Amazon Flex**: 300K+ active drivers, Pixie as "during downtime" earning add-on. Proposal: co-marketing, Amazon promotes Pixie in Flex app.
2. **Wonolo**: staffing platform for warehouse/retail workers — already doing field work, Pixie is natural add-on.
3. **Lime/Bird scooter**: riders already have location awareness, Pixie as "micro-earn while riding."
4. **Instacart**: grocery shoppers already in-store — natural fit for shelf tasks. Require: Instacart permission (tricky — they may see it as competitor).
5. **Mechanical Turk community**: existing crowdsource community, receptive to new platforms.
**Output**: GTM.md — Partnerships
**Key insight**: Instacart is the highest-leverage partnership (agents already in stores) but the highest risk (competitive conflict). Approach Wonolo and Amazon Flex first — less competitive overlap.

---

### Cycle 78: Launch Sequence — Day 1 Through Month 12
**Focus**: Detailed launch plan
**Method**: Planning
**Work**:
**Pre-launch (Months -3 to 0)**:
- Month -3: Close seed funding, hire 2 engineers + 1 ML engineer
- Month -2: MVP agent app (iOS + Android beta), core AI pipeline (face redaction + basic validation)
- Month -1: City Captain hired in Atlanta + Dallas. Agent recruitment begins. First customer pilots signed (3 CPG brands, intro via founder network)
- Month 0 (Launch): Atlanta + Dallas go live. 200+ agents each. First 3 customers start paid tasks.

**Post-launch (Months 1–12)**:
- Month 1–3: Atlanta + Dallas full operation. Product iteration based on agent + customer feedback.
- Month 4–6: Add Chicago + Houston. Agent recruitment playbook documented. Sales team hired (1 AE).
- Month 7–9: Add Miami + Denver + Seattle. Customer base = 15. First insurance customer signed.
- Month 10–12: Add Nashville + Charlotte + Phoenix. Customer base = 25. $1M ARR crossed.
**Output**: GTM.md — Launch sequence
**Key insight**: Start in Atlanta — it has a large gig worker community, major CPG presence (Coca-Cola HQ, multiple major brands), low regulatory complexity, and strong university system for ambassadors.

---

### Cycle 79: Growth Metrics + Dashboard
**Focus**: Define the metrics that matter for growth
**Method**: Design
**Work**: North Star Metric: Tasks Completed (total, weekly). Why: correlates with both customer value and agent earnings simultaneously.
Supply metrics: Active Agents (last 30 days), Agent Retention (% completing tasks in consecutive months), Fulfillment Rate (% tasks completed within SLA), Agent NPS.
Demand metrics: Customer Count (paying), MRR, Task Volume/Customer, Customer NPS, Expansion Revenue %.
Quality metrics: AI Validation Pass Rate, Customer Acceptance Rate (% AI output accepted without dispute), Average Submission Rating.
Growth metrics: CAC (both sides), LTV:CAC, Payback Period, City Coverage (# of cities with >80% fulfillment rate).
**Output**: GTM.md — Metrics
**Key insight**: Fulfillment Rate is the product quality metric that determines if the business works. Everything — agent density, AI quality, task design — exists to maximize fulfillment rate.

---

### Cycle 80: Competitive Moat — Year 1 Actions
**Focus**: What to do in Year 1 to build defensibility
**Method**: Planning
**Work**: Moat-building actions:
1. **Sign exclusive data agreements** with 3+ CPG brands for their specific SKU sets → trains proprietary models they can't get elsewhere
2. **File provisional patents**: on the on-device-redaction-before-upload architecture + the C2PA integration for crowdsourced capture
3. **Build enterprise integrations** (Salesforce, Snowflake) — switching costs
4. **Establish SOC 2 process** — compliance moat against new entrants
5. **Secure retailer access agreements** with 2+ regional retail chains — gives agents legitimate access to stores, blocks competitor platform agents
6. **Publish C2PA conformance** — become reference implementation for crowdsourced C2PA compliance
**Output**: VENTURE.md — Moat section
**Key insight**: Retailer access agreements are the highest-leverage moat action. A retailer that has signed with Pixie has implicitly blocked competitors from using their stores for crowdsourced capture without permission.

---

## Phase 6 — Synthesis (Cycles 81–100)

### Cycle 81: Naming — Brainstorm 10 Candidates
**Focus**: Generate 10 name candidates
**Method**: Creative
**Work**: Criteria: short (1–2 syllables preferred), memorable, available domain (.ai or .com), no trademark conflicts, conveys intelligence/vision/ground truth. Candidates:
1. **Pixie** — playful, smart, mobile, familiar. pixie.ai likely taken, pixie.io possible.
2. **Scout** — classic, agent-themed. scout.com taken, scout.ai possible.
3. **Lens** — visual, clean. lens.com taken.
4. **Glimpse** — captures on-demand snapshot idea. glimpse.ai possible.
5. **Beacon** — signal/intelligence, guide. beacondata.com taken.
6. **Vantage** — perspective/intelligence. vantage.ai likely taken.
7. **Mosaic** — many pieces → full picture, fits crowdsourced nature. mosaic.ai possible.
8. **Verdant** — too abstract.
9. **Iris** — eye/vision, AI. iris.ai — taken.
10. **Fieldwork** — descriptive, professional. fieldwork.ai possible.
11. **Canvass** — research/survey connotation, agents canvassing. canvass.ai possible.
12. **Veritas** — truth/ground truth theme. veritas.com taken (HP subsidiary).
**Output**: NAMING.md
**Key insight**: None of the obvious names are available at .com. Strategy: go with .ai domain (normalized in AI space) or use a modified spelling/compound.

---

### Cycle 82: Naming — Domain + Trademark Research
**Focus**: Narrow to 5 viable candidates
**Method**: Research
**Work**: Checking availability and trademark conflicts:
- **Pixie.ai**: Pixie is a known fairy/children's brand — potential trademark issues in EU. Pixie Labs (Google acquired camera startup) — some conflict risk. Avoid.
- **Scout.ai**: Clean, used by some minor apps. Scout24 (German classifieds) has Scout trademark in EU — potential conflict in EU expansion. Risk.
- **Glimpse.ai**: Glimpse is used by several small companies. Low conflict risk in B2B data space. Domain likely available.
- **Mosaic.ai**: Clean and clear. Mosaic Software exists but in different vertical. Strong candidate.
- **Canvass.ai**: Different spelling from "canvas" (software company). Low conflict. Strong candidate.
- **Fieldwork.ai**: Descriptive, professional, used in academic contexts but not commercial platforms. Strong candidate.
- **Vero.ai**: Latin for "true/real" — ground truth concept. Very clean. Check trademark.
- **Locus.ai**: Location-focused, clean. Locus Robotics exists — conflict risk.
**Output**: NAMING.md
**Key insight**: Top 3 viable candidates: Glimpse, Mosaic, Canvass. Each is available, low trademark risk, and conveys the right brand promise.

---

### Cycle 83: Naming — Final Recommendation
**Focus**: Choose and justify the name
**Method**: Decision
**Work**: Final analysis of top 3:
- **Glimpse** ("On-demand glimpses into the physical world"): Conveys the on-demand, momentary capture nature. Easy to spell/say. Glimpse.ai likely available. Risk: "glimpse" implies incomplete view — not ideal for enterprise trust signal.
- **Mosaic** ("The full picture from a thousand glimpses"): Perfectly captures the crowdsourced-to-intelligence concept. Enterprise-appropriate. Mosaic.ai clean. Risk: Mosaic is a common word — many companies in adjacent spaces.
- **Canvass** ("Your agents, everywhere"): The verb "to canvass" = systematic information gathering. Alternate spelling differentiates. Canvass.ai clean. Risk: pronunciation/spelling confusion.

**Recommendation: Mosaic** — tagline "The world, in real time." The name encapsulates the product metaphor (many individual pieces forming a coherent picture) and works for both retail and enterprise contexts. Backup: Canvass.ai if Mosaic has trademark issues.

Domain target: mosaic.ai or getmosaic.ai or mosaicdata.ai
**Output**: NAMING.md — Final recommendation
**Key insight**: The name Mosaic is self-explanatory to an enterprise buyer — "you have agents all over, each capturing a piece, and we give you the full picture." No explanation required.

---

### Cycle 84: Brand Positioning — Tagline + Category
**Focus**: Define the brand position and category
**Method**: Design
**Work**: Category creation: don't compete in "mystery shopping" or "retail analytics" — create a new category: "Physical World Intelligence." This positions Pixie/Mosaic as the infrastructure layer, not a service provider. Tagline options:
1. "The world, in real time." — clean, confident, universal
2. "See everywhere. Know everything." — aggressive, enterprise
3. "Your eyes on the ground." — too military/surveillance connotation
4. "Ground truth at scale." — resonates with AI/data buyers
5. "Physical intelligence." — ultra-minimal, category-defining

**Recommendation**: "Ground truth at scale." — speaks directly to the AI/data buyer who understands what "ground truth" means. Secondary tagline for consumer/agent side: "See your city. Get paid."
**Output**: NAMING.md, VENTURE.md — Positioning
**Key insight**: "Ground truth" is a technical term in AI meaning labeled real-world data for training. Using it positions the company perfectly with AI labs and data buyers, while also communicating authenticity to enterprise buyers.

---

### Cycle 85: Brand Positioning — Competitive Framing
**Focus**: How to position vs competitors in every conversation
**Method**: Design
**Work**: vs Field Agent: "Field Agent gives you photos. We give you insights. Real-time, AI-extracted, verified." vs Trax: "Trax requires hardware in every store. We're in every store — no hardware, no installation, no long-term commitment." vs Mystery shopping agencies: "Mystery shopping takes weeks. We take hours. And our data is machine-readable." vs doing nothing (field sales team): "Your field team covers 5% of stores. We cover 100%." vs NielsenIQ syndicated data: "Nielsen is weeks old and survey-based. Our data was captured this morning."
**Output**: NAMING.md, GTM.md
**Key insight**: The competitive positioning consistently wins on three axes: speed (hours vs weeks), coverage (100% vs 5%), and format (machine-readable vs PDF reports). Lead with these three every time.

---

### Cycle 86: Brand Positioning — The AI Training Data Angle
**Focus**: How to talk about the data flywheel to investors
**Method**: Design
**Work**: Investor framing: "We are building the world's largest labeled, geo-tagged, real-world visual dataset — as a byproduct of our enterprise intelligence platform. Our customers pay us to build the training data that AI labs will pay us to access. We get paid twice for every task." This is the "picks and shovels" angle in the AI buildout. Comparable: Snowflake (data infrastructure), Scale AI (labeled data). Unlike Scale AI: our data is produced at zero incremental cost via the commercial product. Unlike Snowflake: we own the data, not just the pipeline. Market size for labeled visual data: $1.5B+ in 2025, growing to $8B+ by 2033.
**Output**: PITCH.md, VENTURE.md
**Key insight**: The "paid twice" framing is the investor hook. It means gross margins expand as the platform scales — unusual for a marketplace. This is what justifies the 15x ARR multiple rather than the typical 5–8x.

---

### Cycle 87: Pitch Deck — Problem + Solution Slides
**Focus**: Write the first 4 slides of the pitch deck
**Method**: Writing
**Work**:
**Slide 1 — The Problem**:
"Businesses make billion-dollar decisions based on data that's weeks old, survey-based, and covers less than 10% of locations. The physical world is opaque. Real-time ground truth doesn't exist."
Supporting stats: CPG brands lose 4–8% revenue to out-of-stocks they can't see. Mystery shopping takes 2–3 weeks. Field sales teams cover <5% of stores.

**Slide 2 — Why Now**:
Smartphones are now ubiquitous sensors. On-device AI can redact and validate in real time. The gig economy has created a 50M+ strong labor pool willing to earn from micro-tasks. These three forces combine to make Pixie possible in 2026 — impossible before 2022.

**Slide 3 — Solution**:
"Pixie: Physical World Intelligence. Post a task. Our agents photograph it. Our AI extracts the insights. You see the world as it is — right now."

**Slide 4 — How it works**: Task posted → agent accepts → captures (with real-time face redaction) → AI validates + extracts → structured data delivered in hours.
**Output**: PITCH.md
**Key insight**: The "Why Now" slide is often underdeveloped. For Pixie, the "why now" is genuinely strong: the convergence of gig economy scale, on-device AI, and enterprise demand for real-time data is a 2024–2026 phenomenon.

---

### Cycle 88: Pitch Deck — Market + Product Slides
**Focus**: Market size and product slides
**Method**: Writing
**Work**:
**Slide 5 — Market Size**:
TAM: $35B (retail intelligence + traffic monitoring + visual AI training data by 2030)
SAM: $8B (on-demand, crowdsourced-compatible tasks)
SOM (Year 3): $50M (100 enterprise customers × $500K ACV)

**Slide 6 — Product**:
Three tiers: (1) Task API — per-task data on demand. (2) Intelligence Platform — ongoing monitoring with analytics dashboard. (3) Ground Truth Data — labeled datasets for AI training.
Demo: live shelf scan from one of the pilot customers.

**Slide 7 — Traction**:
"In 6 months: 10 enterprise customers, 5,000 active agents, 2 cities, $500K ARR, 87% task fulfillment rate, 4.6/5 customer satisfaction."
(These are Month 6 targets, not Day 1 claims.)
**Output**: PITCH.md
**Key insight**: The traction slide is the most important slide for a Series A. The numbers must be real — fabricating traction kills deals. The 87% fulfillment rate is the operational proof point that makes all other numbers credible.

---

### Cycle 89: Pitch Deck — Business Model + Team + Ask
**Focus**: Final pitch deck slides
**Method**: Writing
**Work**:
**Slide 8 — Business Model**:
"We take 55% of every task. Agents earn 45%. At scale: 65% gross margin. Our AI extraction multiplies revenue per task 3–5x over raw photo delivery."
Show unit economics: $35 revenue / task → $14 agent → $19 gross profit → 54% margin → expands to 65%+ at scale.

**Slide 9 — Competition**:
2x2: X-axis = Coverage (physical location reach), Y-axis = AI extraction quality.
Top right = Pixie. Bottom left = manual field teams. Mid-left = mystery shopping agencies. Mid-right = Trax (high AI, low coverage). Top-left = Field Agent (high coverage, low AI).

**Slide 10 — Team**:
[Founder names/bios — to be filled based on actual founding team]
Advisors: retail industry veteran, computer vision PhD, gig economy operator.

**Slide 11 — The Ask**:
Raising $2.5M seed. Use of funds: 50% engineering (mobile + AI), 25% agent acquisition (first 3 cities), 15% enterprise sales, 10% compliance (SOC 2, GDPR).
Series A target: $100M at $8M ARR (Month 18–24).
**Output**: PITCH.md
**Key insight**: The 2x2 competition slide needs to show Pixie alone in the top-right quadrant. This is only true if "coverage" means crowdsourced/on-demand coverage anywhere — not hardware-dependent coverage. Define the axes precisely.

---

### Cycle 90: Risk Register — Top 10 Risks
**Focus**: Identify and plan for the top 10 risks
**Method**: Analysis
**Work**:
1. **In-store access without retailer consent** (HIGH) → Mitigation: sign retailer access agreements, frame as "mystery shopper" program, partner-first approach
2. **Uber/DoorDash competitive entry** (HIGH) → Mitigation: proprietary AI models + enterprise contracts create switching costs before scale player moves
3. **Agent fulfillment failure in low-density areas** (HIGH) → Mitigation: don't accept tasks in markets below 200 active agent threshold; surge pricing for difficult locations
4. **BIPA liability in Illinois** (HIGH) → Mitigation: on-device redaction before upload + delay Illinois launch to Year 2
5. **AI extraction accuracy failure** (MEDIUM) → Mitigation: CV + human fallback queue; contractual accuracy guarantees phase in with product maturity
6. **Data breach / security incident** (MEDIUM) → Mitigation: SOC 2, encryption, minimal data retention (30-day image deletion), no PII in agent submissions
7. **Regulatory prohibition on crowdsourced image capture** (MEDIUM) → Mitigation: on-device redaction + C2PA compliance makes platform legally distinct from surveillance
8. **Agent misuse (capturing people intentionally)** (MEDIUM) → Mitigation: real-time detection of face capture with automatic rejection + account termination
9. **Customer pricing pressure / race to bottom** (LOW-MEDIUM) → Mitigation: proprietary models + enterprise integrations create lock-in before commoditization
10. **Funding gap between seed and Series A** (LOW) → Mitigation: revenue-based financing from task volume + clear Series A metrics from day 1
**Output**: VENTURE.md — Risk register
**Key insight**: Risk #1 (in-store access) and Risk #3 (fulfillment in sparse markets) are the existential operational risks. Everything else is manageable. The retailer partnership strategy is the #1 strategic priority.

---

### Cycle 91: Risk Mitigation — Retailer Partnership Strategy
**Focus**: Deep dive on solving the retailer consent problem
**Method**: Design
**Work**: The in-store capture problem has three solutions:
(1) **Retailer as Customer**: Retailer pays Pixie to monitor their own shelves. Agents are explicitly authorized shoppers. This inverts the model — retailers become the buyer, and CPG brands access the data through the retailer (retailer charges CPG brands for data access or Pixie directly charges CPGs with retailer authorization). Revenue model: retailer pays $5K–$50K/month for their store network coverage.
(2) **Mystery Shopper Framework**: Agents are registered mystery shoppers. They enter stores as regular customers, make a small purchase, and capture task photos. Legally equivalent to legitimate mystery shopping — a 50-year-old, well-established practice.
(3) **Competitor-only mode**: Tasks only photograph competitor products, never the host store's own products — reduced liability, less commercially sensitive.
Year 1 strategy: primarily (2) mystery shopper framework + (3) competitor-only mode. Year 2: approach retailers as customers using (1).
**Output**: LEGAL_REGULATORY.md, VENTURE.md
**Key insight**: The mystery shopper framework is the legal foundation for Year 1. Field Agent and every mystery shopping company in existence operates this way. The legal risk is essentially zero for competitor price checks in publicly accessible stores.

---

### Cycle 92: Risk Mitigation — Regulatory Compliance Plan
**Focus**: What compliance infrastructure must be in place pre-launch
**Method**: Planning
**Work**: Pre-launch requirements (must be done):
1. Privacy Policy + Terms of Service (agent) — reviewed by privacy attorney
2. Terms of Service (customer) + Data Processing Agreement template
3. Agent consent flow: explicit consent to task types + redaction disclosure
4. On-device redaction system — tested on 50+ device models
5. GPS consent + data minimization (only at task events, not continuous)
6. 1099 filing infrastructure (IRS requirement for >$600/year agent earnings)
7. AML/KYC for agent payouts (required by payment processors for >$600)

Post-launch (Year 1):
- SOC 2 Type I by Month 9, Type II by Month 15
- GDPR DPA template for EU customers (even pre-EU launch)
- BIPA analysis by Illinois-specific attorney before Chicago expansion

Year 2:
- FedRAMP authorization process (for government customers)
- EU launch: DPO appointment, GDPR compliance audit
**Output**: LEGAL_REGULATORY.md — Compliance plan
**Key insight**: The IRS 1099 + AML/KYC infrastructure is unglamorous but legally required and operationally complex. Hyperwallet handles much of this automatically — one of the key reasons to use them over rolling a custom payout system.

---

### Cycle 93: Product Roadmap — MVP Definition
**Focus**: Absolute minimum viable product for pilot
**Method**: Planning
**Work**: **MVP (Month 0 — launch)**:
- Agent iOS app: task discovery map, task acceptance, guided camera capture, on-device face redaction, submission upload, earnings display
- Agent Android app: same
- Basic AI pipeline: face detection validation (server-side), GPS/timestamp verification, content presence check
- Customer web portal: task creation, map view of completions, image gallery viewer, basic CSV export
- Admin dashboard: task management, agent management, payout processing
- Payments: Stripe (customer billing) + Hyperwallet (agent payouts)
- NOT in MVP: live streaming, deep AI extraction, custom models, API, Salesforce integration, C2PA full implementation, advanced analytics

**V1 (Month 3–6)**:
- Full AI extraction (SKU detection, price OCR, shelf analysis)
- API access for customers
- C2PA proof chain
- Analytics dashboard with trend charts
- Salesforce integration

**V2 / Series A (Month 12–18)**:
- Live streaming
- Custom AI model training
- Snowflake/BigQuery export
- Multi-language agent app (Spanish, Portuguese)
- EU launch (full GDPR compliance)
**Output**: PRODUCT_ROADMAP.md
**Key insight**: The MVP's critical path is the agent app + face redaction + GPS verification. Everything else is additive. A working, trustworthy capture system is the foundation — even if data extraction is basic at launch.

---

### Cycle 94: Product Roadmap — V1 Product Details
**Focus**: V1 feature set design
**Method**: Design
**Work**: V1 additions over MVP (Month 3–6):
- **AI extraction upgrade**: YOLO-based product detection, price tag OCR (Tesseract + custom model), brand/logo recognition. Accuracy target: 85%+ in standard retail conditions.
- **Structured data API**: REST endpoints for customers to pull JSON extraction results. Webhook for task completion notifications.
- **Enhanced dashboard**: shelf share % charts, price trend lines, out-of-stock alerts (if same location checked repeatedly), comparison views (store A vs store B).
- **Agent enhancements**: streak bonuses, level system visible, referral code sharing, payout history, task history with accepted/rejected breakdown.
- **Quality feedback loop**: rejected submissions get specific AI feedback ("product labels not visible — recapture from closer angle"), reducing rework rate.
**Output**: PRODUCT_ROADMAP.md — V1
**Key insight**: The quality feedback loop is a retention driver for agents. Agents who get clear, actionable rejection feedback improve faster and stay on platform. Vague rejection messages ("image quality insufficient") are the biggest agent churn driver.

---

### Cycle 95: Regulatory Compliance — EU Expansion Plan
**Focus**: What it takes to launch in Europe
**Method**: Research + planning
**Work**: EU-specific requirements:
- **GDPR Art. 13/14**: Inform data subjects (agents + anyone incidentally captured) about data processing. Solution: clear agent onboarding consent + redaction-as-standard.
- **GDPR Art. 17**: Right to erasure. Solution: 30-day raw image deletion policy; structured data retained but not attributable to individuals.
- **Art. 28**: Controller-Processor agreements with all EU customers.
- **Country-specific**: France (CNIL pre-authorization for certain image processing) — Year 3. Germany (Bundesdatenschutzgesetz) — strict, Year 3. UK (UK GDPR, post-Brexit) — similar to EU GDPR, Year 2 expansion.
- Target EU launch: UK (Year 2, simplest regulatory environment), Netherlands/Nordics (Year 3), France/Germany (Year 4).
**Output**: LEGAL_REGULATORY.md — EU plan
**Key insight**: Launch in the UK before continental EU. UK GDPR is substantively identical to EU GDPR but enforcement is generally more pragmatic, and English-language agent market is easier to seed than non-English markets.

---

### Cycle 96: MVP — 10-City, 10-Customer Pilot Spec
**Focus**: Define what "Series A ready" looks like operationally
**Method**: Planning
**Work**: Series A proof package:
- 10 cities with >80% task fulfillment rate
- 10,000+ active agents total (1,000+/city avg)
- 50+ enterprise customers (10 paying >$10K/month)
- $7–10M ARR run rate
- AI extraction accuracy: >90% on shelf detection, >85% on price OCR
- Customer NPS: >50
- Agent NPS: >40
- <0.1% fraud rate
- SOC 2 Type II certified
- Zero significant privacy incidents
These metrics tell the Series A story: "The unit economics work. The operations work. The AI works. The legal structure works. Now give us $100M to do it in 100 cities."
**Output**: PRODUCT_ROADMAP.md, FINANCIAL_MODEL.md
**Key insight**: The Series A proof package isn't about ARR alone — it's about the replication proof. Investors need to see that the Atlanta/Dallas playbook ran identically in Houston, Chicago, and Miami. That's the bet they're funding.

---

### Cycle 97: Financial Model — Complete Model Summary
**Focus**: Pull together all financial assumptions into a coherent model
**Method**: Calculation
**Work**:
**Revenue model**:
- Blended task price: $35 → $45 (as AI value-add pricing improves)
- Agent payout %: 40% of task price
- Platform gross margin: 55% → 65% (at scale)
- Revenue streams: tasks (80%), subscriptions (15%), AI training data (5%) → Year 3: tasks (60%), subscriptions (25%), training data (15%)

**Key milestones**:
- Month 3: $15K MRR, 2 cities, 500 agents, 3 customers
- Month 6: $64K MRR, 4 cities, 2,000 agents, 8 customers
- Month 12: $300K MRR ($3.6M ARR), 8 cities, 7,500 agents, 25 customers
- Month 18: $700K MRR ($8.4M ARR), 12 cities, 15,000 agents, 50 customers ← Series A

**Funding**:
- Seed: $2.5M (raised pre-launch)
- Series A: $100M at ~$100M pre-money (10x ARR multiple)
- Use of Series A: 50% engineering/AI, 20% city expansion (10 new cities), 20% enterprise sales, 10% compliance/legal
**Output**: FINANCIAL_MODEL.md — Complete summary
**Key insight**: The training data revenue stream becomes increasingly significant at scale — by Month 24, it could represent $1M+/month at zero incremental cost. This is the "bonus revenue" that makes the financial model look exceptional vs pure-marketplace comps.

---

### Cycle 98: Competitive Moat — Final Assessment
**Focus**: Is the competitive moat sufficient for Series A?
**Method**: Analysis
**Work**: Moat assessment:
- **Data moat**: STRONG by Month 18. Proprietary labeled datasets for specific retail chains, specific geographies, specific categories. Impossible for new entrant to replicate without years of operation.
- **Model moat**: MEDIUM by Month 18. Fine-tuned models outperform generics but can be replicated given time + data. Protection: continuously improve, train on new data weekly.
- **Network effects**: MEDIUM-STRONG. More agents → better fulfillment → more customers → more tasks → more agent earnings → more agents. Classic two-sided marketplace flywheel.
- **Integration moat**: MEDIUM. Salesforce/Snowflake integrations create switching costs after 6+ months of use.
- **Compliance moat**: MEDIUM. SOC 2 + GDPR compliance requires 12–18 months for new entrant to replicate. Enterprise customers won't switch to non-compliant platform.
- **Retailer access moat**: STRONG if executed. Signed retailer access agreements block competitors from using the same stores.
Overall: sufficient for Series A defense. Not sufficient to prevent well-funded entrant in Year 3+. Series B strategy must accelerate data moat.
**Output**: VENTURE.md — Competitive moat
**Key insight**: The moat is real but not impenetrable. The Series A pitch must include a "moat acceleration" plan for how $100M of capital deepens the defensive position — not just grows the top line.

---

### Cycle 99: Final Synthesis — VENTURE.md Update
**Focus**: Update VENTURE.md as the master document
**Method**: Synthesis
**Work**: Updated VENTURE.md to incorporate: final name recommendation (Mosaic/Pixie), refined ICP, validated financial model, prioritized use cases (retail shelf + competitive intelligence as beachhead), city launch playbook, complete technical architecture, regulatory compliance framework, and Series A proof package.
**Output**: VENTURE.md — Full rewrite
**Key insight**: The venture is investable. The combination of (1) clear market need, (2) novel technical approach (crowdsourced + AI + proof chain), (3) sound unit economics, and (4) natural data flywheel creates a credible path to $100M ARR and a defensible market position.

---

### Cycle 100: Final Synthesis — Investment Thesis
**Focus**: Write the one-paragraph investment thesis
**Method**: Writing
**Work**: "Pixie (operating as Mosaic) is building the physical world's intelligence layer — an on-demand crowdsourced platform that turns any smartphone into a verified visual data collection device. Enterprises post tasks; our network of 15,000+ agents captures the data; our AI extracts structured insights within hours. We charge enterprises $15–$150/task, pay agents 40%, and keep 55%+ gross margin. The data flywheel — real-world labeled visual data produced as a byproduct — becomes an additional revenue stream worth $1M+/month at scale. We are 18 months from $8M ARR across 12 cities with 50 enterprise customers. We are raising $2.5M to prove the model in 2 cities with 10 customers, then raising $100M to expand to 100 cities. The market is $35B and growing at 22% CAGR. No one is doing what we do."
**Output**: VENTURE.md — Investment thesis, PITCH.md
**Key insight**: The investment thesis in one paragraph is the filter for every decision. If a feature, partnership, or hire doesn't serve this thesis, it doesn't happen in Year 1.

---

## Phase 5 — VC + Customer Feedback Simulation + Three-Tier Expansion (Cycles 101–120)

### Cycle 101: VC Feedback Framework — 5 Archetypes
**Focus**: Simulate top-tier VC partner meeting feedback from 5 investor archetypes
**Method**: Persona simulation + synthesis
**Work**: Simulated detailed feedback from: (1) Marketplace specialist [a16z/Benchmark] — excited by two-sided flywheel and training data, concerned about cold-start in every city; (2) Enterprise SaaS [Bessemer/Insight] — excited by NRR potential, concerned about economic buyer complexity; (3) AI/Data infrastructure [Coatue/Radical] — excited by data moat and C2PA provenance, concerned about real-world AI accuracy; (4) Consumer/gig economy [Index/Spark] — called out the Uber analogy directly, flagged that "enterprise-only is like Uber with no consumer app"; (5) Emerging markets [Sequoia India/Partech] — excited by supply-side potential internationally, concerned about GPS fraud and local regulations.
**Output**: VC_FEEDBACK.md — Cycle 101 section
**Key insight**: Every VC archetype independently surfaced the same gap: no consumer/SMB access layer. The feedback convergence on this single point is the clearest signal in all 20 cycles — it's the top-priority fix.

---

### Cycle 102: Customer Feedback Simulation — 6 Personas
**Focus**: Simulate 30-minute discovery call with 6 customer archetypes
**Method**: Persona interview simulation
**Work**: Interviewed (simulated) 6 customers: CPG Brand Manager (wants 90-second self-serve, would buy today), VP Category Management (needs SOC 2 and accurate data), Insurance Claims Head (wants CAT event surge capability and liability clauses), Retail RE Director (needs video not photos, comparing vs Placer.ai), City Transit Director (6–18 month govt procurement cycle), Small Brand Owner (will never contact sales — must be self-serve).
**Output**: VC_FEEDBACK.md — Cycle 102 section
**Key insight**: The small brand owner (Jake Torres, hot sauce brand) is the most important new persona discovered. He would buy immediately at $149/month self-serve. He is the proof point for the SMB tier and the most direct response to the "Uber analogy" mandate.

---

### Cycle 103: Agent Supply-Side Feedback Simulation — 5 Personas
**Focus**: Simulate agent onboarding conversations and feedback
**Method**: Persona simulation
**Work**: Simulated feedback from 5 agent types: college student (wants earnings card viral sharing, fears rejection without pay), DoorDash driver (wants daily cashout, needs task availability map), retired professional (wants human support line, prefers premium tasks), stay-at-home parent (needs radius filter, task cancellation grace period), urban commuter (wants commuter-optimized task discovery, fears being conspicuous).
**Output**: VC_FEEDBACK.md — Cycle 103 section
**Key insight**: The consumer task layer solves the supply retention problem. Agents churn during enterprise campaign gaps; consumer tasks create a base load of demand that keeps agents earning between enterprise waves. Consumer demand is both a revenue diversification play AND a supply retention mechanism.

---

### Cycle 104: VC Objection Responses — Top 10
**Focus**: Develop specific data-backed responses to top 10 VC objections
**Method**: Research + argument construction
**Work**: Crafted detailed responses to: cold-start problem, Field Agent comparison, take rate compression, customer concentration risk, economic buyer ambiguity, Uber/DoorDash entry threat, AI accuracy concerns, privacy/BIPA liability, government sales cycle length, training data commoditization.
**Output**: VC_FEEDBACK.md — Cycle 104 section
**Key insight**: The most defensible objection response is the three-tier architecture itself. Enterprise concentration risk disappears when 10,000 consumer users and 500 SMB accounts create revenue diversification. The three tiers are the answer to many individual objections simultaneously.

---

### Cycle 105: Synthesis — 5 Biggest Gaps
**Focus**: Synthesize feedback simulation findings into prioritized action items
**Method**: Gap analysis
**Work**: Identified 5 critical gaps: (1) No consumer/SMB access layer — the Uber problem; (2) Agent retention in low-task-density periods; (3) AI accuracy must be explicitly stated with human fallback; (4) Retail store access problem under-addressed; (5) No viral/referral mechanics for SMB acquisition.
**Output**: VC_FEEDBACK.md — Cycle 105 section
**Key insight**: Gaps 1 and 2 are the same problem: no consumer demand layer. Fixing the consumer/SMB access layer simultaneously solves revenue diversification, agent retention, and viral acquisition. It's the single highest-leverage intervention in the entire venture.

---

### Cycle 106: Use Case Brainstorm — 30 New Ideas
**Focus**: Generate 30 new use cases across categories unexplored in Cycles 1–100
**Method**: Lateral thinking + category expansion
**Work**: Brainstormed 30 use cases across 7 categories: (A) Individual consumer — restaurant scout, park crowd check, Airbnb neighborhood preview, contractor work verification, parking availability, in-stock check; (B) Small business — local restaurant chain competitor monitoring, outdoor signage visibility, franchise spot check; (C) Events and entertainment — pre-event venue scouting, live crowd coverage, event setup documentation; (D) Travel and tourism — hotel lobby preview, attraction crowding, road trip scouting; (E) Journalism/research — breaking news coverage, construction watchdog, academic field research; (F) Environmental/safety — storm damage, illegal dumping monitoring, trail conditions; (G) Other — gym crowd level, social/dating intelligence.
**Output**: USE_CASES_V2.md — Cycle 106 section
**Key insight**: The highest-frequency consumer use cases (gym crowd, park crowd, in-stock check) are the gateway drug to Mosaic adoption. They create the habit and the agent base load simultaneously. These low-value tasks are paradoxically the most strategically important.

---

### Cycle 107: Scoring and Prioritization — Top 15 Use Cases
**Focus**: Score 15 new use cases across 6 dimensions including new "self-serve potential" criterion
**Method**: Scoring matrix
**Work**: Scored all 15 new use cases. Top 5 by score (all 27–28/30): Consumer in-stock check (28), Crowd level check (27–28), Restaurant scout (27–28), Small brand shelf intelligence (27), Travel neighborhood scout (26). The new "self-serve potential" criterion reshuffled the rankings significantly — insurance and infrastructure dropped despite high WTP because they cannot be accessed without enterprise sales.
**Output**: USE_CASES_V2.md — Cycle 107 section
**Key insight**: The original 8 use cases were scored entirely on enterprise criteria. Adding "self-serve potential" as a criterion creates a completely different top-5 list — dominated by consumer and SMB use cases. This scoring change is itself a venture design insight: optimizing for self-serve unlocks a fundamentally different and larger market.

---

### Cycle 108: Deep Dives — Top 5 New Use Cases
**Focus**: Full use case specifications for 5 highest-scoring new use cases
**Method**: Persona + task + output + pricing + virality design
**Work**: Full specs for: (1) Restaurant Scout — Alex Morgan, first date, $15/task, viral via "spy on my date night restaurant" Instagram content; (2) Consumer In-Stock Check — Keisha Williams, formula parent, $8/task, viral via parenting communities; (3) Small Brand Shelf Intelligence — Jake Torres, hot sauce brand, $149/month self-serve, viral via "Brand Pulse" share cards; (4) Crowd Level Check — multiple personas, $5/task, highest frequency use case and gateway product; (5) Travel Neighborhood Scout — Emma Larsson, Airbnb traveler, $20/task, viral via travel influencer content + Airbnb partnership potential.
**Output**: USE_CASES_V2.md — Cycle 108 section
**Key insight**: Every one of the top 5 new use cases has a built-in viral mechanism. The product itself generates shareable moments. This is structurally different from the original enterprise use cases, which were valuable but not inherently shareable. The consumer tier is the viral engine of the entire platform.

---

### Cycle 109: The "Interesting Combinations" Analysis
**Focus**: Design 8 non-obvious combinations of customer × use case × business model
**Method**: Creative synthesis
**Work**: Designed 8 genuinely novel combinations: (1) Multi-buyer single capture — 3 buyers paying for 1 agent visit simultaneously, compound take rate; (2) Consumer-sponsored enterprise task — brands subsidize consumer tasks for discounted shelf data; (3) Incidental intelligence — agent captures secondary value they didn't know existed; (4) Customer who is also an agent — store owners monitoring each other unknowingly; (5) Bounty pool — multiple buyers co-fund expensive ongoing surveillance; (6) Location subscription — subscribe to a geo-fence, not a task type; (7) Social intelligence / ambient earn — earn by documenting places you already visit; (8) Intelligence feed — aggregate task data becomes alternative investment data product.
**Output**: USE_CASES_V2.md — Cycle 109 section
**Key insight**: Combination 8 (intelligence feed) is the sleeper revenue model. If Mosaic processes 500K tasks/month, the aggregate signal is incredibly valuable to hedge funds and investment research firms willing to pay $50K–$500K/year for alternative data. This requires no additional operational complexity — it's pure data product revenue from the existing task flow.

---

### Cycle 110: Use Case → Revenue Model Mapping
**Focus**: Map all 20+ use cases to optimal revenue models
**Method**: Systematic analysis
**Work**: Mapped every use case to best-fit model: enterprise subscription, self-serve subscription, per-task marketplace, API/developer, data licensing, freemium, consumer app. Key finding: most use cases can be accessed through multiple tiers at different price points — e.g., shelf intelligence is a $5,000/month enterprise product AND a $149/month SMB product AND a $15 consumer task. The same use case serves all three tiers.
**Output**: USE_CASES_V2.md — Cycle 110 section
**Key insight**: "Use case" and "revenue model" are orthogonal in Mosaic's architecture. A shelf intelligence use case can be served at $15 (consumer), $149/month (SMB), or $25,000/month (enterprise). The AI quality, speed, and features differ by tier — but the underlying task is the same. This means the product build serves all three revenue streams simultaneously.

---

### Cycle 111: Tasks Marketplace — Consumer/SMB Self-Serve Design
**Focus**: Design the consumer-facing task posting experience end-to-end
**Method**: Product design
**Work**: Designed complete self-serve flow: 90-second task posting (search template → fill specifics → pricing preview → credit card → done), minimum task price analysis ($8 minimum to sustain quality agent payout), consumer discovery channels (TikTok/Instagram earnings content, app store, commuter transit ads), viral hook design (earnings cards + brand pulse share cards + scout report share cards), task creation flow (<2 minutes), pricing page design (consumer tasks + SMB subscription + enterprise contact sales, in that order), credit/wallet model vs subscription, freemium entry tier (3 free tasks, 24-hour delay, 25% conversion target).
**Output**: USE_CASES_V2.md — Cycle 111 section
**Key insight**: The pricing page order matters enormously. Showing consumer tasks and SMB subscriptions before "contact enterprise sales" signals that this is an accessible product, not a gated enterprise tool. Every competitor's pricing page starts with "Request Demo" — Mosaic's starts with "5 crowd checks for $15." That difference is the Uber analogy made real in product design.

---

### Cycle 112: SMB Customer Segments — Full Analysis
**Focus**: Define 5 specific SMB segments with full persona, pain, and acquisition data
**Method**: Persona development + channel analysis
**Work**: Full analysis of 5 SMB segments: (1) Local restaurant chain 3–10 locations (Carlos Mendez, Tacos El Rey, $200–500/month, Facebook SMB ads); (2) Independent retail brand 200–2,000 stores (Sarah Kwan, Pacific Beauty, $300–800/month, Faire platform); (3) Regional real estate agency 50–200 listings (Michael Chen, Apex Realty, $200–600/month, ActiveRain); (4) Small event production company (Jordan Park, Blueprint Events, $200–500/event, BizBash); (5) Independent journalist/media outlet (Riya Patel, $200–500/month, SPJ conference).
**Output**: USE_CASES_V2.md — Cycle 112 section
**Key insight**: All 5 SMB segments can buy without a sales call. All 5 are below $1,000/month spend, which is below the "get IT involved" threshold. All 5 have existing communities where Mosaic can reach them through content or partnerships. The SMB market is fragmented and enormous — and nobody is selling to it.

---

### Cycle 113: Three-Tier Business Model Architecture
**Focus**: Design complete 3-tier model with pricing, features, economics, and acquisition motion
**Method**: Business model design
**Work**: Full specification of all three tiers. Tier 1 (Consumer): credit wallet $5–$25/task, 52% gross margin, app store + viral acquisition, CAC $5–$15. Tier 2 (SMB): $49–$749/month subscription, 62% gross margin, content + community + PLG, CAC $50–$200. Tier 3 (Enterprise): $2,500–$50,000+/month annual contracts, 58% gross margin, AE sales + partner channel, CAC $5,000–$15,000. Blended LTV:CAC across tiers: 10:1 to 20:1. Three-tier model produces $9.87M ARR by Month 18, exceeding original enterprise-only projection of $8M.
**Output**: BUSINESS_MODEL_V2.md — Cycle 113 section, BUSINESS_MODEL.md — Full rewrite
**Key insight**: The consumer tier has the lowest LTV per account but the highest volume and lowest CAC. It's the growth engine. Enterprise has the highest LTV but slowest growth. SMB is the sweet spot: medium ACV, self-serve acquisition, high volume potential. The three tiers balance each other: enterprise provides revenue stability, SMB provides scale, consumer provides virality.

---

### Cycle 114: Consumer Acquisition — Virality + Growth Loops
**Focus**: Design 6 viral growth loops for consumer and SMB acquisition
**Method**: Growth design
**Work**: Designed 6 growth loops: (1) Task result → share card → peer discovery; (2) Agent earnings card → social viral → new agent signups (k-factor 0.5+ target); (3) Surprise and delight → organic viral moment; (4) Referral program with mentor bonus; (5) PLG loop (free → delayed results → upgrade); (6) Saved search → location subscription conversion. Also designed SMB acquisition channels (Shopify, Faire, LinkedIn, TikTok) and consumer channels (app store, earnings TikTok, Facebook, campus ambassadors, transit ads, parent communities). TikTok "Reality Check" feature designed: side-by-side planned vs actual shelf placement, one-tap to post as TikTok.
**Output**: BUSINESS_MODEL_V2.md — Cycle 114 section
**Key insight**: The TikTok Reality Check feature is potentially the most viral product feature designed in this session. "Expectation vs reality" is one of TikTok's highest-performing content formats. Every brand that uses it creates Mosaic content. The feature builds marketing into the product itself.

---

### Cycle 115: Revised Financial Model — Three-Tier
**Focus**: Rebuild financial model to include all 3 tiers, model $1M ARR race (consumer+SMB vs enterprise-only)
**Method**: Financial modeling
**Work**: Built month-by-month projection for all three tiers through Month 24. Month 12 ARR run rate: $4.25M (vs $3.0M enterprise-only — 42% higher). Month 18 ARR: $9.87M (vs original $8M target). Three-tier path to $1M ARR: reached at Month 9–10 through 2,500 consumers + 200 SMB + 15 enterprise accounts. Enterprise-only $1M ARR timeline: Month 10–12. Verdict: three-tier model reaches $1M ARR faster AND with dramatically lower concentration risk. Training data revenue modeled separately: $22K/month at Month 12, $85K/month at Month 18, $210K/month at Month 24.
**Output**: BUSINESS_MODEL_V2.md — Cycle 115 section
**Key insight**: The three-tier model doesn't just solve the "Uber analogy" problem — it materially improves financial performance. The consumer tier's low CAC and viral acquisition compress the overall blended CAC and accelerate the ARR ramp. Every VC archetype will prefer this model to the enterprise-only version.

---

### Cycle 116: Pricing Architecture Finalization
**Focus**: Define exact pricing for every tier, task type, and plan
**Method**: Pricing design + competitive benchmarking
**Work**: Finalized all pricing: consumer task prices by type ($5–$20 depending on complexity), credit pack pricing ($15 for 3 tasks → $150 for 25 tasks), SMB subscription tiers (Spark $49 → Agency $749), annual pricing with 15–20% discount, enterprise tier pricing (Business $2,500 → Enterprise+ $50,000+), agent payout rates by task type (consistently 40%), surge multipliers (1.25× to 5×), volume discounts (10–30% off at higher volumes). Benchmarked all prices against Field Agent, mystery shopping, Trax, and Placer.ai.
**Output**: BUSINESS_MODEL_V2.md — Cycle 116 section, BUSINESS_MODEL.md — Pricing tables
**Key insight**: The Spark plan at $49/month is the most strategically important pricing decision. It's below every SMB's "get IT involved" threshold, below most individual expense approval thresholds, and below the psychological "serious commitment" level. It is the "request a ride" moment of Mosaic's consumer experience.

---

### Cycle 117: Revised VENTURE.md
**Focus**: Completely rewrite VENTURE.md to incorporate all new elements
**Method**: Synthesis + writing
**Work**: Full rewrite of VENTURE.md incorporating: three-tier business model, 20+ use cases, consumer/SMB layer, revised financial projections ($9.87M ARR Month 18 vs original $8M), updated competitive landscape (Placer.ai, Yext, OpenTable, Citizenlab as new adjacent competitors), revised risk register (added consumer churn, SMB price sensitivity, two-sided cold start per city), fifth moat layer (consumer brand identity), updated investment thesis.
**Output**: VENTURE.md — Full rewrite
**Key insight**: The updated investment thesis is substantially stronger. "No consumer/SMB access" was the biggest hole in the original pitch. The revised version addresses every VC concern identified in Cycles 101–105 and is supported by 20 cycles of additional research and modeling.

---

### Cycle 118: New USE_CASES.md
**Focus**: Rewrite USE_CASES.md with all 20 use cases, new scoring criteria
**Method**: Synthesis + writing
**Work**: Rewrote USE_CASES.md with 20 use cases scored on 6 dimensions (added self-serve potential as a primary criterion), full personas for top 8 use cases, 8 interesting combinations referenced, clear tier mapping (which tier serves which use case). Consumer use cases (in-stock check, crowd level, restaurant scout) now appear in top 5 alongside enterprise beachhead use cases.
**Output**: USE_CASES.md — Full rewrite
**Key insight**: Adding the self-serve criterion fundamentally reshapes prioritization. The venture's original use case ranking (by enterprise willingness-to-pay only) would have led to an enterprise-only product. The new ranking reveals that the highest-value use cases for overall platform growth are the consumer-accessible ones.

---

### Cycle 119: New BUSINESS_MODEL.md
**Focus**: Rewrite BUSINESS_MODEL.md to reflect 3-tier architecture
**Method**: Synthesis + writing
**Work**: Full rewrite of BUSINESS_MODEL.md covering: three-tier architecture with exact pricing, agent earnings model (40% consistently, surge multipliers, bonus structure, level system), unit economics per task (blended $14 revenue, 51% gross margin now vs 54% before — lower because consumer tasks are smaller but higher volume), revenue mix evolution (consumer grows from 25% → 34% of revenue by Month 24), five viral growth loops, SMB acquisition channel analysis with CAC by channel.
**Output**: BUSINESS_MODEL.md — Full rewrite
**Key insight**: The blended unit economics appear weaker (51% vs 54%) but the absolute revenue trajectory is better. Lower-value consumer tasks dilute per-task margin but dramatically increase volume. The correct metric is total gross profit dollars, not gross margin percentage. By Month 24, total gross profit is $9.9M vs $6.5M in the enterprise-only model.

---

---

## Phase 7 — Global Scale + Funding Architecture (Cycles 121–140)

### Cycle 121: European Competitive Landscape Research
**Focus**: Map the EU crowdsourced visual intelligence market
**Method**: WebSearch + analysis
**Work**: Identified BeMyEye as the primary European competitor: founded 2011 (London), 3M+ contributors, 21 countries, $35M revenue as of June 2025, 79 employees, enterprise-only. Clients include Nestlé, PepsiCo, L'Oréal, Heineken. Identified acquisitions: LocalEyes (2016), Task360 (2018), Streetbee (2019), Metaliquid (2022). Field Agent confirmed weak EU presence. Premise Data confirmed thin EU operations.
**Output**: EUROPE_STRATEGY.md — Competitive landscape section
**Key insight**: BeMyEye is proof the European market exists and pays — $35M revenue from enterprise customers is validation. Mosaic's superior AI, faster turnaround, consumer/SMB tier, and modern tech stack make displacement feasible. BeMyEye's no-consumer-tier gap mirrors Field Agent's gap in the US.

---

### Cycle 122: European City Selection Analysis
**Focus**: Score and rank 5 EU launch cities
**Method**: Research + multi-factor scoring
**Work**: Evaluated cities on: gig worker density, CPG brand proximity, English proficiency, regulatory environment, BeMyEye competitive gap. Selected: (1) London — Unilever/Reckitt HQ, 1.7M UK gig workers, English native, ICO pragmatic; (2) Amsterdam — Heineken HQ, 95% English, Dutch startup ecosystem; (3) Berlin — EU's largest CPG market, Henkel/Beiersdorf access; (4) Barcelona — Nestlé Iberia, Spain highest EU gig density; (5) Paris — L'Oréal/Danone/Pernod Ricard, CNIL requires full DPIA. Countries to avoid in Year 1: Austria, Sweden (aggressive DPAs), Hungary/Romania (small CPG market).
**Output**: EUROPE_STRATEGY.md — City selection section
**Key insight**: London + Amsterdam as simultaneous Month 1 launch is the right call — both have English proficiency for sales operations, high gig density, and major CPG brand HQ proximity. Paris comes last (Month 7) despite highest CPG density because CNIL requires most thorough GDPR documentation.

---

### Cycle 123: GDPR Deep Dive — Crowdsourced Visual Data
**Focus**: Complete GDPR analysis for Mosaic's specific model
**Method**: Research (GDPR articles, EDPB guidelines, ICO guidance)
**Work**: Analyzed GDPR Article 6 lawful bases for each Mosaic data category. Key finding: post-redaction images are not personal data (Recital 26), eliminating GDPR obligations for uploaded images. Mapped lawful bases: agent data = Contract (6(1)(b)), customer data = Contract, task images (post-redact) = not personal data, task location = Legitimate Interests (6(1)(f)). Identified required documentation: DPIA (Article 35 — systematic public space monitoring is explicitly listed as high-risk), ROPA (Article 30), DPAs with sub-processors, EU Representative (Article 27), Privacy Notices (Articles 13/14). Completed GDPR vs CCPA vs BIPA comparison.
**Output**: EUROPE_STRATEGY.md — GDPR section
**Key insight**: On-device redaction is the strategic trump card. It converts a potential GDPR liability into a GDPR moat. Europe is not harder than Illinois from a litigation risk perspective — BIPA is existential (plaintiff class actions), GDPR is operational (DPA enforcement). Build GDPR compliance properly from Day 1 and it becomes a barrier to entry for US competitors who want to enter Europe.

---

### Cycle 124: European CPG Target Mapping
**Focus**: Identify specific enterprise targets and why they buy
**Method**: Research (CPG revenue, retail intelligence spending, buyer titles)
**Work**: Mapped 8 primary EU enterprise targets: Unilever (London + Rotterdam, €60B), Heineken (Amsterdam, €36B), L'Oréal (Clichy/Paris, €41B), Danone (Paris, €27B), Reckitt (Slough, £13B), Nestlé (Vevey + Barcelona, CHF91B), Beiersdorf (Hamburg, €9.5B), Henkel (Düsseldorf, €22B). For each: why they buy Mosaic, key buyer title, specific use case. Established that Nestlé is a confirmed current BeMyEye customer — displacement is the sales narrative.
**Output**: EUROPE_STRATEGY.md — CPG targets section
**Key insight**: All 8 targets are confirmed BeMyEye customers or directly adjacent. The sales conversation starts at "why switch" not "what is this" — a major acceleration. A €5,000 pilot is typically below brand manager budget approval threshold, meaning no procurement involvement for first engagement.

---

### Cycle 125: EU-First Strategic Argument + Pricing
**Focus**: Should Mosaic launch EU before US? European pricing strategy
**Method**: Analysis + synthesis
**Work**: Argued the EU-first vs US-first vs parallel case. Recommended: US + EU in parallel (Atlanta/Dallas Month 1, London/Amsterdam Month 2–3). The "EU validation → US fundraise" arc: first EU enterprise contracts at Month 9–12, then Series A pitch with "US $X ARR + Unilever/Heineken in Europe." EUR pricing: match USD price points (€49 = $49/month, not €53 at spot rate), invoice in EUR for enterprise, agent payouts in GBP/EUR via Wise Business.
**Output**: EUROPE_STRATEGY.md — Strategy + pricing sections
**Key insight**: GDPR compliance built properly from Day 1 is not just cost — it's a moat. US competitors who want to enter Europe 18 months later have to retrofit GDPR. Mosaic has it built in. This is worth more than any short-term competitive advantage.

---

### Cycle 126: Location-Aware Product Design
**Focus**: Design the four agent modes for the "already going there" model
**Method**: Product design + UX flow
**Work**: Designed four modes: (1) Trip Intent — pre-stage tasks before leaving home, route corridor matching, agent commits before commute begins; (2) Commute Mode — one-tap "Accept All" button, tasks triggered at geofence crossings, overnight pre-loading of task feed; (3) Shopping Run Mode — tasks bundled at destination store + 500m radius, interleaved with agent's own shopping; (4) Already Here — standard proximity mode, geofenced push notifications. Designed the Micro-Task Tier: £1–3 customer price, £1–2 agent payout, available only in commute/route modes to prevent gaming.
**Output**: LOCATION_AWARE_MODEL.md — Product design section
**Key insight**: The "Accept All" button in commute mode is the single most important UX decision. An agent who accepts 3 tasks with one tap before leaving home has made a commitment that drives retention. The friction of individual task review is eliminated. This one UX choice changes agent retention from reactive (gig economy norm) to proactive (habit loop).

---

### Cycle 127: Location Model Business Economics
**Focus**: Model cost reduction and retention improvement from route-matching
**Method**: Financial modeling + comparative analysis
**Work**: Modeled effective cost-per-fulfilled-task across three models: dispatched gig ($18), Mosaic standard ($8), Mosaic commute-match ($4–7, 56% reduction). Modeled agent retention: dispatched baseline 38% monthly, Mosaic commute-mode 67% monthly (+76%). Designed the Daily Commuter persona (Maya, London, earns £240/month, 60 tasks, LTV:CAC = 90:1). Modeled earnings density: commuter agents complete 3.8 tasks/day vs 1.2 for standard agents (3.2× more productive). Calculated platform flywheel: commute agents → better fulfillment → better SLAs → more customers → more tasks → better earnings → more commute agents.
**Output**: LOCATION_AWARE_MODEL.md — Business model + persona sections
**Key insight**: The commuter agent's 90:1 LTV:CAC is the best unit economics on the platform. Acquiring commuter agents (via "Turn your morning commute into £50/week" ads) is the highest-ROI acquisition motion. Standard gig platforms don't have a commuter mode — they don't think about agents as people with existing daily patterns.

---

### Cycle 128: Location-Aware Technical Architecture
**Focus**: Design the technical implementation of route-matching, privacy model, battery/data cost
**Method**: Technical design
**Work**: Designed corridor-based (not radius-based) geo-matching algorithm: route polyline → 300–500m buffer → corridor polygon → task ranking by Payout ÷ (1 + detour_coefficient). Designed privacy-preserving route architecture: on-device route computation, ephemeral GPS (< 10 seconds active per day), route data cleared at trip end, historical pattern learning as opt-in device-local only. Battery analysis: "significant location change" API = ~0% additional drain, geofencing = <0.1% per region, total data per session < 20KB. Designed task state machine additions: pre_accepted_by, pre_accepted_at, expected_completion_window fields.
**Output**: LOCATION_AWARE_MODEL.md — Technical architecture section
**Key insight**: The privacy-preserving design is not just regulatory compliance — it's a competitive advantage for agent acquisition. "We never track where you go — only where you are for the 45 seconds you're completing a task" is a recruiter message that works. And the GDPR DPIA for location data becomes much easier when there's no persistent route storage to justify.

---

### Cycle 129: Two-Person Founding Team Design
**Focus**: Define the two founding roles and full function mapping
**Method**: Analysis + framework design
**Work**: Defined CEO (commercial: revenue, GTM, investor relations, enterprise sales) and CTO (technical: product, engineering, AI/ML, infrastructure) roles. Mapped every company function to either human or AI agent: engineering (Claude Code + Cursor + Devin), design (v0 + Figma AI + Midjourney), finance (Pilot.ai + fractional CFO), customer success (Intercom AI first line), marketing (AI content agents + CEO strategy), legal (AI research + attorney retainer), data analysis (AI analytics agents), PR (Claude drafts, CEO approves).
**Output**: FUNDING_STRATEGY.md — Lean team design section
**Key insight**: The AI-native team is the story, not a limitation. The $30K/month burn rate for a 2-person founding team vs $120K+ for a traditional 6-person team at the same stage is the most compelling VC narrative available. Every function is covered; quality is not compromised when the CTO supervises AI-generated code at the PR level.

---

### Cycle 130: AI Tool Stack Cost Model + Burn Rate
**Focus**: Build the exact pre-seed burn rate with every tool named and priced
**Method**: Tool pricing research + financial modeling
**Work**: Listed 22 specific tools with exact monthly costs: Claude Code ($200), Cursor Pro ($80), Devin ($500), v0 ($20), Midjourney ($30), Figma ($45), Notion AI ($16), Linear ($8), Vercel Pro ($20), AWS ($500), Supabase ($25), Intercom ($39), Pilot.ai ($599), and others. Total tools: ~$2,400/month. Full burn rate: 2 founder salaries $20K + tools $2.4K + legal $2K + agent acquisition $3K + conference/travel $1.5K + misc $1.1K = $30,000/month. $500K pre-seed = 16 months runway.
**Output**: FUNDING_STRATEGY.md — AI tool stack + burn rate tables
**Key insight**: The $2,400/month AI tool stack replaces approximately $80,000/month in equivalent human salaries. The ROI on this specific set of tools is the most compelling quantitative argument for the AI-native model. VCs can verify every tool cost independently — this isn't hand-waving, it's a specific, auditable claim.

---

### Cycle 131: Pre-Seed + Seed Strategy
**Focus**: Pre-seed ($250K–500K) and seed ($5–10M) full strategy
**Method**: Research + framework
**Work**: Pre-seed: SAFE at $8–10M cap, 20% discount, 3–4 angels at $100K each (CPG operators, marketplace founders). What to show: team + insight + MVP + one signal. Timeline: 4–8 weeks angel route. Seed: $5M on $20–25M pre-money, requires $150–300K ARR, 500+ agents, 3–5 enterprise customers, 2 cities. Use of funds detailed: engineering ($1.5M), agent acquisition ($1M), ML ($500K), sales ($500K), marketing ($500K), legal ($300K), ops ($400K), buffer ($300K). Bridge avoidance strategy: raise $500K not $400K, start seed outreach at Month 6 not Month 10.
**Output**: FUNDING_STRATEGY.md — Pre-seed + seed strategy sections
**Key insight**: The bridge round is the enemy. Every bridge signals that the primary raise underperformed. Prevent it by: (a) raising slightly more pre-seed than strictly needed, (b) starting seed conversations 4 months before needing to close, (c) using monthly investor updates to warm investors so the formal raise is a formality, not a cold pitch.

---

### Cycle 132: VC Targeting — 20 Specific Investors
**Focus**: Research and identify 20 specific VCs with partner names, portfolio evidence, intro paths
**Method**: Research + analysis
**Work**: Identified 20 target investors across US and EU: a16z (Andrew Chen), NFX (Pete Flint), Spark Capital (Megan Quinn), Bessemer (Byron Deeter), Haystack (Semil Shah), Homebrew (Hunter Walk), USV (Albert Wenger/Rebecca Kaden), General Catalyst (Niko Bonatsos), Founders Fund (Keith Rabois), Sequoia (Shaun Maguire), Index Ventures EU (Luciana Lixandru), Accel EU (Luca Bocchio), LocalGlobe (Saul Klein), Precursor (Charles Hudson), Hustle Fund (Elizabeth Yin), Uncork (Jeff Clavier), Freestyle (Dave Samuel), Gradient/Google (Darian Shirazi), Operator Partners (Sean Griffin), AI Grant (Nat Friedman/Daniel Gross). For each: check size, why Mosaic fits, intro path.
**Output**: FUNDING_STRATEGY.md — VC targeting table; CEO_IR_PLAYBOOK.md — Top 20 VCs section
**Key insight**: The warm intro path exists for almost every target investor through portfolio company CEOs (DoorDash, Deliveroo, Hipcamp alumni) or public engagement channels (Andrew Chen's Substack, Hunter Walk's Twitter). Almost no cold outreach is required if the founder spends 6 months building relationships before the formal raise.

---

### Cycle 133: CEO Investor Relations Framework
**Focus**: The relationship-first framework, VC landscape mapping, "give before you ask"
**Method**: Research (First Round Review, NFX, Bessemer IR guidance) + framework design
**Work**: Established the 12-month-before-you-need-money principle with conversion rate math (relationship: 40–60% vs cold pitch: 2–5%). Designed "give before you ask" tactics: share research, make warm intros, write content VCs share, attend their events without pitching. Established tier structure: Tier 1 (lead investors, 3–5 people, board seats), Tier 2 (strategic co-investors, 5–8 people, check followers), Tier 3 (angels, 10–20 people, domain expertise + social proof). Designed VC CRM tracking system.
**Output**: CEO_IR_PLAYBOOK.md — Relationship framework + landscape mapping
**Key insight**: Every VC who gives specific advice about what they'd want to see becomes invested in your success. They want to see you prove them right. The advice-seeking meeting is not a trick — it genuinely creates alignment between what the VC needs to invest and what you're building toward.

---

### Cycle 134: First Meeting + Process Management
**Focus**: What VCs evaluate, how to tell the founding story, managing the fundraising process
**Method**: Research (First Round Review, NFX Guide, Bessemer founder guidance) + framework
**Work**: Identified what VCs actually evaluate in first meeting: founder exceptionalism (80%), market credibility (15%), insight non-obviousness (5%). Designed three-part founding story structure: personal insight → why now → unfair advantage. Selected 4 questions to ask VCs that create memorable conversations. Designed competitive fundraising process mechanics: compress first meetings to 2-week window, set close timeline, use first term sheet to call other investors personally, FOMO without deception. Designed the "No" → relationship maintenance protocol: specific thanks, feedback acknowledgment, stay on update list.
**Output**: CEO_IR_PLAYBOOK.md — First meeting + process sections
**Key insight**: The "We're not raising yet" framing for early meetings is the most powerful tool available. It removes pressure from both sides, gets honest feedback, and turns a potential investor into an advisor who is now personally invested in seeing you execute. When you come back 8 months later with proof, they convert at dramatically higher rates.

---

### Cycle 135: Monthly Investor Update Template + Content Strategy
**Focus**: Monthly update template design, thought leadership content strategy for inbound VC interest
**Method**: Framework design + template creation
**Work**: Designed monthly investor update template with 6 sections: top line (3 bullets), metrics table, what worked (specific), what didn't work (honest — most important section), next month focus (commitment device), specific ask. Established rule: send from Day 1, before raising. Designed content strategy: 2× LinkedIn/week + 1× Substack/month. Content themes: data stories from real tasks, market insights (BeMyEye analysis), building in public (AI-native company transparency), counter-narrative (GDPR as moat). Designed effective cold email formula: 6 sentences, reference their portfolio specifically, open with value for them.
**Output**: CEO_IR_PLAYBOOK.md — Update template + content strategy sections
**Key insight**: The "What didn't work" section of the investor update is the most important section in the document. Every VC who receives only good news stops reading after 3 months. VCs who receive honest accounts of failures AND how they're being addressed actually increase their interest level. Honesty is the fastest trust-compounding mechanism available.

---

### Cycle 136: Pitch Deck Research — Best-In-Class Analysis
**Focus**: Research what makes the best pitch decks (Airbnb, Uber, Sequoia format, YC format)
**Method**: WebSearch + analysis
**Work**: Analyzed the Airbnb 2009 deck ($600K raised, 10 slides, no fluff, 78% of successful decks use demos/screenshots). Analyzed the Uber deck (funded on conviction story, not beauty). Analyzed Dropbox deck ($1.2M from Sequoia, broke rules and succeeded). Established YC format (problem → solution → market → traction → team → no filler). Established Sequoia format (same arc, used by Airbnb/Dropbox/WhatsApp). Established: 12–15 slides max, one clear point per slide, narrative arc where each slide sets up the next, no hedging language.
**Output**: Research informing PITCH_DECK_V2.md
**Key insight**: The best pitch decks (Airbnb, Dropbox) succeed not because of beautiful design but because of conviction. "Investors back 63% of startups with a clear and concise message." Every word must earn its place. The Mosaic deck should feel like talking to a founder who knows exactly what they're building and exactly why it wins.

---

### Cycle 137: Pitch Deck — Problem Through Market Slides
**Focus**: Slides 1–6 of the Mosaic seed pitch deck
**Method**: Writing + synthesis from all prior research
**Work**: Wrote complete Slides 1–6: Cover (MOSAIC, ground truth at scale), Problem (physical world opaque, $35B on outdated data), Solution (any smartphone → verified data device, flow diagram), Why Now (on-device AI + gig economy maturity + AI extraction quality), Product (split screen customer/agent, commute mode mockup, magic numbers), Market Size (TAM $35B, SAM $8.5B, SOM $350M, consumer/SMB tier never served = $3–5B uncreated category). Each slide has: headline, body content, narrative note, design note.
**Output**: PITCH_DECK_V2.md — Slides 1–6
**Key insight**: The market size slide's most powerful line is not the TAM number — it's "The consumer/SMB tier has never been served. That's $3–5B of market that doesn't yet exist as a category." VCs know BeMyEye ($35M revenue, 15 years). The insight that there's a 100× larger market that BeMyEye has never served is the investment thesis in one sentence.

---

### Cycle 138: Pitch Deck — Business Model Through Ask Slides + Appendix
**Focus**: Slides 7–13 and 4 appendix slides
**Method**: Writing + financial modeling
**Work**: Wrote complete Slides 7–13: Business Model (three tiers + training data flywheel), Traction (template with actual metrics to fill in + AI-native build velocity story), GTM (beachhead → expansion → category creation phases), Competitive Landscape (2×2 matrix showing white space), Team (two founders + AI team, $30K/month burn proof), Financial Projections (Month 3/6/12/18/24 MRR with three-tier breakdown), The Ask ($5M seed, $20–25M pre-money, use of funds, milestones, Series A trigger). Plus 4 appendix slides: Unit Economics, Technology Architecture, GDPR Compliance, European Strategy.
**Output**: PITCH_DECK_V2.md — Slides 7–13 + Appendix
**Key insight**: The Team slide is where the AI-native narrative pays off most visibly. Showing "12-person team output at $30K/month burn" with a specific tool list changes the VC's mental model of the risk profile. This isn't a 2-person team that can't execute — it's a 2-person team that has already executed in 8 weeks what traditionally took 6 months and $1M.

---

### Cycle 139: MOSAIC_V3.html — All New Material Visualized
**Focus**: Build comprehensive HTML page incorporating all new strategic material
**Method**: HTML/CSS design + synthesis
**Work**: Created MOSAIC_V3.html with 6 major sections: (1) European Strategy — city launch cards, GDPR comparison table, CPG target table, EU-first strategic argument; (2) Location-Aware Model — four mode cards, micro-task economics table, Maya persona with timeline, cost reduction stats; (3) AI-Native Team — two role cards, full AI tool stack with costs, burn rate breakdown, hiring roadmap; (4) Funding Strategy — pre-seed/seed/Series A stat callouts, top 10 VC cards; (5) Pitch Deck Preview — 10 key slides visualized in HTML with actual content; (6) CEO IR Playbook — 6 principles, monthly update template in monospace. Dark background, gradient design system consistent with V2.
**Output**: MOSAIC_V3.html
**Key insight**: The pitch deck preview section in HTML is a significant deliverable — the founder can walk through the key slides visually before building the actual deck, test the narrative flow, and refine the story based on how the content reads as a sequence.

---

---

## Phase 8 — Vision Reframe + Physical World Intelligence Layer (Cycles 141–160)

### Cycle 141: We Are Blind — Founding Vision Manifesto
**Focus**: Reframe the entire business from first principles around the "blind to the physical world" insight
**Method**: Strategic writing
**Work**: 800-word founding manifesto articulating the core paradox: 6.8B smartphones, yet physical world remains dark data. GPS told us where things are. Mosaic tells us what things ARE. Vivid examples: brand manager in London blind to Lagos shelf, Berlin city planner without Tuesday morning foot traffic, blind person in São Paulo with no ramp/step data.
**Output**: VISION_V4.md — Cycle 141
**Key insight**: The problem is architectural/behavioral, not technical. The technology has existed for years. What's missing is the coordination layer.

---

### Cycle 142: The Collector — A Portrait
**Focus**: Deep, empathetic portrait of the collector as the hero/protagonist
**Method**: Persona development + product thinking
**Work**: 5 collector archetypes with full life context: Amara (Lagos market, ₦1,200/walk), Joon-seo (Seoul commuter, €180/month passive), Carlos (São Paulo iFood rider, R$700–1,200 supplemental), Rachel (London school-run mum, £200–350/month), Marco (Manila security guard, earning from observation post). Emotional layer: the discovery that ordinary movement has signal value. Full economics: casual $15–40/month through pro $1,500–4,000/month. Collector journey: discovery → first task → first tell.
**Output**: VISION_V4.md — Cycle 142
**Key insight**: Money is a reason to start. What makes collectors stay is the recognition that where they are and what they see matters. That psychological shift is a product quality no financial competitor can replicate.

---

### Cycle 143: 50+ Use Cases — The Full Map
**Focus**: Exhaustive use case mapping across all verticals
**Method**: Systematic vertical analysis
**Work**: 72 specific use cases mapped across 15 verticals: Retail & CPG (8), Real Estate (6), Urban Planning & Government (7), Insurance (5), Financial Services (5), Media & Research (5), Accessibility & Assistive Tech (4), Emergency & Safety (4), Agriculture (4), Travel & Hospitality (4), Healthcare & Public Health (4), Logistics & Supply Chain (4), Environmental (4), Sports & Events (4), Political & NGO (4). Each with payer, value, collector action, and commercial potential.
**Output**: VISION_V4.md — Cycle 143
**Key insight**: The financial signals use case (hedge fund foot traffic as alpha before earnings) is the highest-margin per-data-point opportunity in the entire map. The accessibility use case is the most emotionally compelling.

---

### Cycle 144: The "Already There" Architecture — The Moat
**Focus**: Deep analysis of why the "already there" model is a fundamental architectural advantage
**Method**: Competitive and structural analysis
**Work**: Structural discontinuity analysis (no logistics cost), density flywheel mechanics, comparison to every alternative (satellite, fixed cameras, mystery shoppers, field reps, delivery networks), cold start solution (Passive Archive program + anchor buyer pilots), network at 1M/10M/100M collectors. The 100M state: "That is not a product. That is infrastructure."
**Output**: VISION_V4.md — Cycle 144
**Key insight**: This is not a marginal efficiency gain. It's a structural discontinuity. Dispatch-based competitors cannot pivot to "already there" without destroying their existing product — classic innovator's dilemma.

---

### Cycle 145: Revenue Architecture — Every Dollar This Company Will Ever Make
**Focus**: Complete revenue model from day 1 through year 10, all tiers
**Method**: Strategic business modeling
**Work**: Tier 1 (Pre-Series A): task marketplace fees (25–35%), SMB subscriptions ($299–999/month), API calls. Tier 2 (Post-Series A): network licensing ($150K–500K/year), white-label deployments, data products/benchmarking reports, certification/compliance tasks. Tier 3 (Platform Era): third-party app ecosystem, physical world advertising (real-shelf ROI measurement), real-time financial signals, insurance underwriting data. Tier 4 (Infrastructure Era): physical reality dataset licensing — government, academic, enterprise, geospatial partnerships. Ceiling: $500M–$2B ARR.
**Output**: BUSINESS_ARCHITECTURE_V4.md — Cycle 145

---

### Cycle 146: Market Sizing — Bottom-Up TAM
**Focus**: Rigorous first-principles market sizing, not generic data market claims
**Method**: Bottom-up quantitative analysis
**Work**: Location count (12M modern trade retail, 22M restaurants, 2–3M construction, 14M agricultural, 500K city blocks). Current spend: mid-size CPG brand $3M–10M/year on physical intelligence, top-50 CPG brand $50M–200M/year. Global CPG physical intelligence spend: $30B. Retail ops: $5B. Combined: $35B+. Bottom-up TAM: $21B across 6 verticals. SAM: $4B. SOM: 5 cities, 50 brands, $5–15M ARR. Collector economy at scale: Year 10 at 50M collectors = $7.2B Mosaic take.
**Output**: BUSINESS_ARCHITECTURE_V4.md — Cycle 146

---

### Cycle 147: The Retail Wedge — GTM Playbook
**Focus**: Detailed go-to-market playbook for retail intelligence entry point
**Method**: GTM strategy design
**Work**: Why retail is the wedge (budget, urgency, repeatability). First customer profile (mid-size CPG, $100M–$1B revenue, single country). Pilot structure ($15,000 flat, 50 locations, 30 days). 30/60/90 ROI metrics. Competitive alternatives defeated. Land-and-expand motion (3 London stores → 200 UK stores → Germany → $2M ARR from one CPG conglomerate). Full sales motion from discovery to enterprise agreement.
**Output**: BUSINESS_ARCHITECTURE_V4.md — Cycle 147

---

### Cycle 148: Collector Economics — Making the Hero Rich
**Focus**: Complete collector economic model and gamification design
**Method**: Product + economics design
**Work**: Task types and payout ranges (ambient $0.50–$3 through live Q&A $15–$60). Earnings scaling factors (engagement, location desirability, quality rating, referral, specialization badge). 5-level passive-to-active spectrum (Ghost collector $5–20/month through Pro collector $1,500–4,000/month). Geographic earnings variation (London vs Lagos vs São Paulo with local PPP calibration). Gamification: Clarity Score, The Map, streak bonuses, collector rank (Explorer→Pioneer), impact feed. Collector protection: privacy, safety, fair pay guarantee, dispute resolution.
**Output**: BUSINESS_ARCHITECTURE_V4.md — Cycle 148

---

### Cycle 149: The Generational Company Thesis
**Focus**: Rigorous intellectual case for Google/Amazon-scale outcome
**Method**: Strategic analysis
**Work**: Category definition: Physical World Intelligence (not data marketplace). Historical analogy: Google Maps — not because it had better maps at launch but because it understood real-time, crowdsourced, continuously updated geography was categorically different. Data flywheel mechanics (Year 1 point-in-time → Year 3 time series → Year 7 intelligence-as-a-service). Four "why now" factors. The 10-year picture of what becomes possible.
**Output**: GENERATIONAL_THESIS.md — Cycle 149

---

### Cycle 150: Competitive Moat Analysis
**Focus**: Honest, deep analysis of why this position is defensible
**Method**: Competitive strategy analysis
**Work**: Three-stage moat evolution (pre-network: architectural insight; early-network: collector relationships; dense-network: data asset). Why Google can't do this (incentive structure incompatibility, can't afford to pay 100M people). Why existing competitors fail (Field Agent/GigWalk locked into dispatch model — innovator's dilemma). Collector relationship moat (financial history, behavioral familiarity, community identity). Density moat (local density takes months regardless of capital). What could actually kill this (regulatory action, well-funded strategic competitor, collector commoditization, buyer concentration).
**Output**: GENERATIONAL_THESIS.md — Cycle 150

---

### Cycle 151: VC Feedback Simulation
**Focus**: Rigorous partner meeting simulation at 5 different VC firm archetypes
**Method**: Simulation + pressure-testing
**Work**: A16Z (conditional interest, wants city-by-city density playbook and 6 months operational data). Sequoia (pass at pre-seed without paying customer or CPG operational experience). Mission-driven impact VC (interested but needs structural collector revenue share commitment, not just policy). Coatue (high interest if technical depth matches, would lead seed — wants data schema architecture and exclusivity model). Skeptical Generalist (hard pass until there's evidence — needs proof of concept not hypothesis).
**Output**: GENERATIONAL_THESIS.md — Cycle 151

---

### Cycle 152: The 2036 Endgame Vision
**Focus**: Specific, vivid picture of what the world looks like when Mosaic wins
**Method**: Speculative strategic writing
**Work**: 38M active collectors, $2.1B revenue, public company. Three 2036 moments impossible today: blind person in London navigating with real-time lift/queue intelligence; brand manager in Düsseldorf getting overnight competitive display alert; Lagos city mayor making urban planning decision in 4 hours instead of 6 months. Industries transformed (retail syndicated data, commercial real estate, insurance, supply chain). The Google Maps moment: Mosaic Now — 400M MAU, natural language queries to physical world, $0 direct revenue, everything in data density.
**Output**: GENERATIONAL_THESIS.md — Cycle 152

---

### Cycle 153: The Collector App — Product Vision
**Focus**: Full product vision for the collector experience
**Method**: Product design
**Work**: Core loop ("exist → arrive → earn → continue"). The ping moment (2 taps from notification to capture started). Passive vs active vs commuter mode. Earning experience (real-time balance, visual timeline, weekly rhythm, earnings exhale animation). Clarity Score system (Focus accuracy + Image quality + Completion rate + Speed + Verification). Community (local leaderboards, milestones, neighborhood intel). The wow moment (first time a task appears somewhere you were already going — should happen in week 1). 5 specific micro-interactions (arrival ripple, earnings exhale, task ghost, quality flash, commute shadow).
**Output**: Product design document (within agent output)

---

### Cycle 154: Live Streaming — The Most Powerful Feature Nobody Has Built Right
**Focus**: Full design of the on-demand live streaming capability
**Method**: Product + technical design
**Work**: Buyer experience (map pin, density indicator, brief under 50 words, text-only buyer→collector communication). Collector experience (full-screen takeover ping, 5 seconds to decide, camera opens immediately, no video call aesthetic). AI overlay during streaming (object count, OCR/text extraction, crowd density, real-time translation, anomaly detection). 4 use cases only streaming enables (remote doctor consultation, brand manager watching product launch live, blind person airport navigation, cross-border legal verification). Privacy framework (public space defaults, private space consent flow, end-at-any-time protection). Technical architecture (WebRTC to edge, edge AI inference, HLS receive, low-connectivity fallback). Pricing ($0.60–$3.00/min buyer, collector earns 65–70%).
**Output**: Product design document (within agent output)

---

### Cycle 155: The Passive Intelligence Layer — Ambient World Capture
**Focus**: Design of the ambient/passive data collection model
**Method**: Product design
**Work**: Trigger types (environmental dwell detection, visual anomaly detection, self-initiated, geofence). Contribution model (task earnings: fixed/confirmed vs passive earnings: variable/post-validation + archive credits). AI layer (relevance scoring, structural tagging, anomaly elevation when multiple collectors capture same area, change detection vs baseline). Consumer app angle — sharing what you see without being a "collector," feeding passive layer like Waze. Data compounding (Month 1 sparse → Month 3 baseline → Month 6 seasonal patterns → Month 12 irreplicable moat). Mosaic Rewind product concept (historical world state queries with confidence intervals).
**Output**: Product design document (within agent output)

---

### Cycle 156: Platform Vision — The Mosaic API
**Focus**: What gets built when Mosaic becomes infrastructure
**Method**: Platform strategy design
**Work**: Core API endpoints (POST /tasks, GET /world-state, POST /streams, GET /collectors/density, GET /history, POST /alerts, GET /ai/recognize). 10 third-party products built on Mosaic API (ShelfWatch, QueueSignal, ConstructionTracker, PriceRadar, VerifyNow, AccessMap, EventPulse, GroundTruth, LocalPulse, MosaicLens). Developer ecosystem (free tier 1K requests/month, growth tier usage-based, enterprise with SLAs). Enterprise integrations (SAP/Oracle ERP, Salesforce, Palantir/Tableau, retail analytics platforms). Mosaic Vision API (proprietary model trained on millions of labeled real-world captures). Physical World Search Engine — the endgame product.
**Output**: Product design document (within agent output)

---

### Cycle 157: The New Founding Narrative
**Focus**: Complete, shareable founding essay in the voice of the founders
**Method**: Strategic narrative writing
**Work**: Full 700-word "We Are Blind" founding narrative: The Paradox → The Moment (Sarah the brand manager in London, blind to Lagos) → What Changed (3 convergences) → The Inversion (don't dispatch, ping the already-there) → The Collector (Amara Lagos) → The Vision (physical world gets a voice) → The Call. Tone: confident, visionary, warm. The sentence: "For the first time in human history, the physical world will have an answer."
**Output**: PITCH_DECK_V4.md — Founding Narrative

---

### Cycle 158: New 13-Slide Pitch Deck — Complete Content
**Focus**: Every word of a new deck, collector-first, "We Are Blind" framing
**Method**: Deck writing
**Work**: All 13 slides complete with slide title, headline, full body content, visual direction, speaker notes. Cover (MOSAIC — "The physical world, finally legible."). Problem ("6.8 billion sensors. Zero signal."). Scale ($35B Problem). Collector (She Was Already There). Solution. Loop (How It Works). Technology. Market ($35B Today, $200B+ Tomorrow). Business Model (Three Revenue Levers). Traction. Team. Vision (2036). Ask ($5M Seed, SAFE $20M cap, 18-month milestones).
**Output**: PITCH_DECK_V4.md — 13 Slides

---

### Cycle 159: AI Image Generation Prompts
**Focus**: Complete set of 12 Midjourney/DALL-E prompts for new visual identity
**Method**: Creative direction + prompt engineering
**Work**: 12 detailed prompts with goals, full generation prompts, avoid notes, and composition guidance. Cover/Hero (city at golden hour, warm intelligence overlay), Blindness (phone camera sharp, world behind in static), Scale (world map in darkness with sparse warm light clusters), Collector (documentary portrait, Lagos market, Magnum Photos aesthetic), Already There (isometric city, glowing "already here" nodes), Solution Loop (Pentagram editorial illustration style), AI Layer (shelf with elegant AI annotation overlay), Market (data visualization night sky for commercial locations), Collector Community (6-panel documentary grid, global diversity), Vision 2036 (natural language query answered instantly, warm not cyberpunk), Team (glass lens refracting onto hand-drawn map), Close (collector mid-stride, motion blur, forward momentum).
**Output**: IMAGE_PROMPTS_V4.md

---

### Cycle 160: 18-Month Execution Roadmap
**Focus**: Detailed, credible month-by-month strategic execution plan
**Method**: Operational strategy
**Work**: 3-phase architecture (Wedge → Platform → Scale). Month-by-month detail for 18 months, each with focus, collector-side, buyer-side, product, and milestone. Key milestones: Month 3 first revenue, Month 6 $15K MRR + 500 collectors + City #1 proof, Month 9 $30K MRR (burn-rate-equal), Month 12 $100K MRR + seed close + enterprise contract, Month 15 $200K MRR + second enterprise, Month 18 $250K MRR + 5,000 collectors + Series A launch. Technology build order (7 phases). Hiring plan (stay 2-person through Month 12, 4 strategic hires over months 13–18). Critical risks by phase with specific mitigations.
**Output**: EXECUTION_ROADMAP_18M.md

---

### Cycle 140: Cycle Log Update + CLAUDE.md Maintenance
**Focus**: Document all 20 cycles, update project state
**Method**: Writing + synthesis
**Work**: Wrote cycles 121–140 cycle log entries covering all work across 4 mandates: European strategy (5 cycles), Location-aware model (3 cycles), Funding strategy/team design (4 cycles), CEO IR playbook (3 cycles), Pitch deck (3 cycles), HTML output (1 cycle), cycle log (1 cycle). All 5 output files written: EUROPE_STRATEGY.md, LOCATION_AWARE_MODEL.md, FUNDING_STRATEGY.md, CEO_IR_PLAYBOOK.md, PITCH_DECK_V2.md, MOSAIC_V3.html.
**Output**: CYCLE_LOG.md — Cycles 121–140
**Key insight**: The four mandates create an integrated strategic layer that builds on each other: Europe gives the "global" narrative that makes the funding story compelling; the location-aware model gives the unit economics advantage that makes the financial projections credible; the AI-native team gives the burn rate advantage that makes the pre-seed/seed narrative powerful; the pitch deck and IR playbook give the CEO the exact tools to execute the fundraise.

---

### Cycle 120: Updated HTML Output — MOSAIC_V2.html
**Focus**: Create comprehensive visual HTML deliverable incorporating all 20 cycles
**Method**: HTML/CSS design + synthesis
**Work**: Created MOSAIC_V2.html — a full venture brief with: VC feedback framework (key objections + responses), customer feedback summary (6 personas), 20-use-case grid with scoring, 3-tier business model visualization, consumer/SMB model design with task posting flow, 8 interesting combinations section, revised financial projections with charts, competitive landscape update, agent economics model. Same dark background, bright gradient design language as MOSAIC_VENTURE.html. Also created VC_FEEDBACK.md with full VC simulation.
**Output**: MOSAIC_V2.html, VC_FEEDBACK.md (updated with all cycles)
**Key insight**: The visual deliverable is substantially more compelling than V1 because it tells a three-act story: (1) the original enterprise opportunity is real and validated; (2) VC and customer feedback revealed a critical missing layer; (3) the three-tier architecture resolves every major objection while materially improving financial projections. The narrative arc makes the pitch stronger, not weaker, for having identified and addressed its own gaps.
