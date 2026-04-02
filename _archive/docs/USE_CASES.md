# Mosaic — Use Cases (V2)
*15+ use cases, scored with self-serve potential criteria*

---

## Priority Scoring Matrix (V2)

**Scoring dimensions** (1–5 each):
- **Mkt**: Market size
- **WTP**: Willingness to pay
- **RegRisk**: Regulatory safety (5 = lowest risk)
- **Tech**: Technical feasibility (5 = easiest)
- **Sales**: Sales ease / self-serve potential (5 = fully self-serve)
- **Freq**: Use frequency / retention driver (5 = highest frequency)
- **New criterion — Self-Serve**: Can a non-enterprise customer access this with no sales call?

| # | Use Case | Mkt | WTP | Reg | Tech | Sales | Freq | Score |
|---|----------|-----|-----|-----|------|-------|------|-------|
| 1 | Retail shelf audit (own brand) | 5 | 4 | 4 | 4 | 3 | 5 | **25** |
| 2 | Competitor store checks | 4 | 3 | 5 | 4 | 4 | 5 | **25** |
| 3 | Consumer in-stock check | 5 | 4 | 5 | 4 | 5 | 5 | **28** |
| 4 | Crowd level check (park/gym/venue) | 4 | 3 | 5 | 5 | 5 | 5 | **27** |
| 5 | Restaurant scout (pre-visit) | 4 | 4 | 5 | 4 | 5 | 5 | **27** |
| 6 | Small brand shelf intelligence | 4 | 4 | 5 | 4 | 5 | 5 | **27** |
| 7 | Travel neighborhood scout | 4 | 4 | 5 | 4 | 5 | 4 | **26** |
| 8 | Insurance claims inspection | 5 | 5 | 3 | 3 | 3 | 3 | **22** |
| 9 | OOH ad monitoring | 4 | 3 | 5 | 3 | 3 | 4 | **22** |
| 10 | Construction progress monitoring | 3 | 4 | 5 | 3 | 3 | 4 | **22** |
| 11 | RE site selection | 2 | 3 | 5 | 4 | 4 | 3 | **21** |
| 12 | Franchise standards audit | 4 | 4 | 4 | 4 | 4 | 4 | **24** |
| 13 | Contractor work verification | 3 | 4 | 5 | 4 | 5 | 3 | **24** |
| 14 | Event crowd documentation | 3 | 3 | 4 | 4 | 4 | 3 | **21** |
| 15 | Infrastructure inspection | 4 | 4 | 4 | 2 | 2 | 3 | **19** |
| 16 | Transit occupancy monitoring | 3 | 3 | 3 | 3 | 2 | 3 | **17** |
| 17 | Journalism / breaking news | 3 | 3 | 4 | 3 | 4 | 3 | **20** |
| 18 | Storm damage documentation | 4 | 4 | 4 | 3 | 3 | 2 | **20** |
| 19 | Hedge fund intelligence feed | 3 | 5 | 4 | 3 | 2 | 4 | **21** |
| 20 | AI training data | 5 | 5 | 4 | 5 | 2 | 5 | **26** |

**Launch priority**: Use cases 1–7 (consumer + SMB tier accessible), supported by Enterprise use cases 1–2. Insurance (8) in Year 2. OOH/Construction (9–10) in Year 2. Transit and Infrastructure (15–16) in Year 3.

---

## Use Case 1: Competitor Store Checks (Enterprise Beachhead)

### Customer Persona
**Name**: Priya Sharma | **Title**: Brand Manager, Beverage Category
**Company**: Mid-size CPG brand ($300M revenue), 8,000 US retail locations
**Budget**: $150K–$400K/year competitive intelligence
**Tier**: Enterprise (Growth plan, $5,000/month)

### The Problem
Priya needs weekly competitive pricing and promotional activity data from 500 key accounts. Her 5-person field team can visit maybe 100 stores/week. When a competitor drops price 15% on Friday, she doesn't find out until Monday.

### The Task
"Photograph the [product category] shelf section in [store_name] at [address]. Capture all competitive SKUs, visible price tags, and any promotional signage."

### AI Extraction Output
```json
{
  "shelf_analysis": {
    "competitive_share_of_shelf": {"Competitor A": 0.38, "Competitor B": 0.22},
    "price_changes_detected": [{"brand": "Competitor A", "from": 2.69, "to": 2.49, "promo": "2 for $4.00"}],
    "capture_proof": {"c2pa_verified": true, "gps_verified": true}
  }
}
```

### Pricing
- Per task: $10–$15
- Volume: 500 stores/week × 4 weeks × $12 = $24,000/month
- Self-serve option: Available at SMB tier for small brands needing <50 tasks/month

---

## Use Case 2: Retail Shelf Audit — Own Brand (Enterprise + SMB)

### Customer Persona (Enterprise)
**Name**: Sarah Chen | **Title**: VP Category Management
**Company**: Established CPG ($500M revenue), 8,000+ US stores
**Tier**: Enterprise (Scale plan, $10,000/month)

### Customer Persona (SMB)
**Name**: Jake Torres | **Title**: Founder, Fuego Foods (regional hot sauce brand)
**Company**: 47 SKUs, 200 stores, Texas + Louisiana
**Tier**: SMB Brand plan ($149/month, 20 audits/month)

### The Problem
Both customers need to know: Is their product in stock? Is it in the right position? Is the promotional display up? Neither can answer this for >90% of their distribution.

### ROI (Enterprise)
- $40M/year out-of-stock losses × 20% recovery with early detection = $8M/year recovered
- Mosaic cost: 8,000 stores × $20/task × 2 audits/month = $3.84M/year
- Net ROI: $4.16M benefit = 2.1:1 ROI

### ROI (SMB)
- Jake catches that 6/20 stores have wrong placement. Calls distributor with photo evidence. Gets compliance fees reimbursed.
- Monthly value: $200–500 in recovered compliance fees + better distributor relationship
- Monthly cost: $149. Payback: immediate.

---

## Use Case 3: Consumer In-Stock Check (NEW — Tier 1)

### Customer Persona
**Name**: Keisha Williams, 38 | **Situation**: Parent searching for specific baby formula
**Tier**: Consumer (credit pack, $8/task)

### The Problem
Consumer wants to know if a specific product is in stock at a specific store before driving across town. E-commerce has real-time stock data. Physical stores don't.

### The Task
"Check if [specific product + SKU] is in stock at [Store Name, Address]. Photo the relevant shelf section."

### What They Get Back
- "Enfamil Gentlease 30oz: IN STOCK — ~7 units visible"
- Current photo of the shelf
- Price: $34.99
- Captured 15 minutes ago

### Pricing
$8/task — single credit purchase, no account required for first task.

### Viral Mechanism
Facebook mom groups, Reddit parenting communities. "This app found me baby formula when no store would tell me the truth" is a powerful, shareable story.

---

## Use Case 4: Crowd Level Check (NEW — Tier 1, High Frequency)

### Customer Persona
**Multiple personas**: Parent with kids, gym member, concert-goer, shopper, student
**Tier**: Consumer (credit pack or $9.99/month subscription)

### The Problem
People don't know if a place is crowded before they commit to going. No app provides verified real-time crowd data for specific locations.

### The Task
"Stand at the entrance to [Location]. Take a 30-second video pan showing crowd level. One photo of parking."

### What They Get Back
A "Crowd Card" — mobile-optimized:
- Current density: MODERATE (estimated 30–50 people)
- Wait time: ~5 minutes
- Parking: Available
- Captured: 12 minutes ago

### Pricing
$5/task — lowest-friction entry point. Or $9.99/month for 10 checks.

### Frequency Play
A gym member who checks their gym 4× per week is a $20/month customer. The crowd check is the gateway product that brings users in and builds habit.

---

## Use Case 5: Restaurant Scout — Pre-Visit Intelligence (NEW — Tier 1)

### Customer Persona
**Name**: Alex Morgan, 31 | **Situation**: First date, unfamiliar restaurant
**Tier**: Consumer ($15/task)

### The Problem
Restaurant photos on Yelp/Google are 3 years old and taken by the marketing department. Alex wants current, honest photos of the vibe, crowd level, and ambiance.

### The Task
"Visit [Restaurant] between 7–8pm Saturday. Photos of dining room (5), entrance line (1), video pan of atmosphere (30 sec)."

### What They Get Back
A "Pre-Visit Card":
- 5 verified current photos
- Vibe Score: Romantic/Casual/Lively
- Crowd: 70% full
- Wait: ~15 min
- Agent note: "Soft music, not too loud — good for conversation"

### Pricing
$15/task. One-time credit card payment. No account required.

### Virality
User shares "I sent a spy to scout my date night restaurant" to Instagram Story. Every share = Mosaic exposure to 300–5,000 followers.

---

## Use Case 6: Small Brand Shelf Intelligence — Self-Serve (NEW — Tier 2)

### Customer Persona
**Name**: Jake Torres, 42 | **Company**: Fuego Foods, 200 stores
**Tier**: SMB Brand plan ($149/month)

*(See full persona in Use Case 2. This entry focuses on the self-serve purchasing journey.)*

### How Jake Buys Without Talking to Anyone
1. Google search: "check my shelf display without a field team"
2. Mosaic.com/brands landing page → pricing visible immediately
3. Selects "Brand Monitor — $149/month"
4. Enters store addresses (or uploads CSV)
5. Sets recurring schedule: monthly, 20 stores
6. Credit card checkout
7. Done — no demo, no sales call, no procurement process

### Task Type
Monthly shelf presence audit: stock status, shelf position, facing count, competitor share.

### What He Gets Back
A "Brand Pulse Dashboard" — mobile and desktop:
- Status grid: 20 stores, red/yellow/green by compliance
- AI anomaly alerts via Slack: "Store 14 (H-E-B Austin): Fuego Foods OUT OF STOCK"
- Month-over-month trend: share of shelf improving or declining

---

## Use Case 7: Travel Neighborhood Scout (NEW — Tier 1)

### Customer Persona
**Name**: Emma Larsson, 29 | **Situation**: Booking Airbnb in unfamiliar city
**Tier**: Consumer ($20/task)

### The Problem
Airbnb marketing photos show the apartment interior; listing says "charming neighborhood." Emma has no idea if the neighborhood looks like the photos.

### The Task
"Walk the block around [Airbnb address]. Photo the building exterior, street from both directions, nearby restaurants/cafes visible. 30-second street video."

### What She Gets Back
A "Neighborhood Reality Check":
- 6 verified street photos
- Building condition: 4/5
- Street activity: Active, several cafes visible
- Agent note: "Nice neighborhood. Some construction noise from adjacent building."

### Pricing
$20/task. Or offered as an Airbnb add-on integration ("Verified Neighborhood" badge).

### B2B Partnership Angle
Airbnb could license this as a premium feature for hosts who want to prove their neighborhood is accurately described, or for travelers willing to pay extra for verified pre-arrival intelligence.

---

## Use Case 8: Insurance Claims Inspection (Enterprise, Year 2)

### Customer Persona
**Name**: David Park | **Title**: Head of Claims Innovation
**Company**: Regional P&C insurer, 200,000 claims/year
**Tier**: Enterprise (Scale plan, $15,000/month + surge contract)

### The Problem
Physical inspection is required for most P&C claims. Adjusters cost $150–$500/visit. Major weather events create simultaneous claim surges that overwhelm adjuster capacity.

### AI Extraction Output
- Damage classification: structural/cosmetic/total loss
- Severity score: 1–10
- Repair cost estimate range
- Fraud flags: inconsistencies with claimed incident date/type

### Pricing
$35–$75/inspection (vs $150–$500 for adjuster). Savings: 70–85% per inspection.
Annual contract: $180,000–$900,000 depending on volume.

### CAT Event Surge Contract
Pre-negotiated surge deployment: insurer can trigger "Storm Response Mode" and deploy up to 500 agents across an affected region within 24 hours. Priced at $75/task during emergency surge.

---

## Use Case 9: OOH Advertising Compliance (Enterprise)

### Customer Persona
**Name**: Kevin O'Brien | **Title**: VP Marketing, Fortune 500 CPG
**Company**: $50M OOH advertising spend/year, 10,000 placements per campaign
**Tier**: Enterprise (Platform plan)

### The Problem
15–30% of OOH placements have compliance issues. Kevin has no scalable way to verify that all 10,000 placements are live, correctly printed, and properly positioned.

### AI Extraction Output
- Creative match score: 0–100% vs reference image
- Condition: excellent/good/fair/poor/missing
- Visibility score (obstruction assessment)
- GPS + timestamp proof

### Pricing
$10–$30/check. 10,000 placements/month × $15 = $150,000/month. $1.8M/year for one advertiser.

---

## Use Case 10: Construction Progress Monitoring (Enterprise + SMB)

### Customer Persona (Enterprise)
**Name**: Maria Santos | **Title**: Project Manager, $500M GC
**Tier**: Enterprise (Business plan + per-site billing)

### Customer Persona (SMB)
**Name**: James Liu | **Title**: Owner, 5-property real estate developer
**Tier**: SMB Growth plan ($349/month, 60 tasks)

### The Task (Weekly Subscription)
"Photo construction site at [address] from 6 specified positions. Capture progress vs last week, safety issues, equipment present."

### Pricing
Enterprise: $200/site/week → $50 × 50 sites = $10,000/month per customer.
SMB: $349/month for 5 sites × weekly = 20 tasks/month + 60-task plan covers it.

---

## Use Case 11: Real Estate Site Selection (Enterprise + SMB)

### Customer Persona
**Name**: Rachel Kim | **Title**: Director of Real Estate, 500-location retail chain
**Tier**: Enterprise (Business plan)

### The Task
"Photo [site address] at 3 time periods (8–10am, 12–2pm, 5–7pm). Foot traffic, neighboring businesses, parking, street conditions."

### AI Extraction Output
- Foot traffic estimate per time period
- Competitor density score
- Site accessibility score
- Street condition assessment

### Pricing
$150–$250 per site assessment (3 time periods). 200 sites/year × $200 = $40,000/year per customer.

---

## Use Case 12: Franchise Standards Audit (Enterprise + SMB)

### Customer Persona
**Name**: Tom Erikson | **Title**: VP Operations, 200-location franchise chain
**Tier**: Enterprise or SMB depending on franchise size

### The Problem
Franchisor needs to verify 200 locations are meeting brand standards without sending an official inspector for every routine check.

### The Task
"Photograph exterior of [franchise location]. Verify: signage matches brand standards, parking lot clean, window displays correct, hours posted. Score against reference images."

### AI Output
Compliance score per location with specific violations flagged. Photo evidence attached.

### Pricing
$25–$40/location/visit. 200 locations × monthly = $5,000–$8,000/month.

---

## Use Case 13: Contractor Work Verification (Consumer + SMB)

### Customer Persona
**Name**: Linda Park, 52 | **Situation**: Home renovation, can't check in person
**Tier**: Consumer ($10–15/task)

### The Problem
Homeowner is paying a contractor but can't be at the property. Wants to verify work is actually in progress.

### The Task
"Photo the exterior of [property address] from the street. Is there any visible construction activity? Vehicles, equipment, workers visible?"

### What They Get Back
3 exterior photos + AI assessment: "Active construction: Yes — 2 vehicles, scaffolding visible on north side."

### Pricing
$10–$15/task. Impulse purchase, no account required.

---

## Use Case 14: Event Crowd Documentation (SMB + Enterprise)

### Customer Persona
**Name**: Jordan Park | **Title**: Owner, Blueprint Events (event production)
**Tier**: SMB ($20–35/task, occasional use)

### The Task
"Document crowd at [event venue] at T-1hr, T+1hr, and T+3hr. Photos of entrance queue and venue fill level each time."

### Pricing
$20–$35/task × 3 time points = $60–$105/event.
SMB event company does 30 events/year = $1,800–$3,150/year — well within credit pack usage.

---

## Use Case 15: Infrastructure Inspection (Enterprise, Year 2–3)

### Customer Persona
**Name**: Patricia Williams | **Title**: Director of Asset Management, Utility Company
**Tier**: Enterprise (Scale plan)

### The Task
"Inspect [infrastructure asset] at [address]. Photograph from 4 angles. Flag any visible deterioration, graffiti, safety hazards, or access obstructions."

### AI Extraction Output
- Defect detection: crack, rust, obstruction, graffiti
- Severity score: 1–5
- Priority flag: urgent/routine
- GPS-verified location

### Pricing
$30–$75/inspection. Annual contract for routine inspection schedule.

---

## Use Case 16: Transit Occupancy Monitoring (Enterprise, Year 3)

*(See VENTURE.md — complex government sales cycle, Year 3 target)*

Platform occupancy via agent capture + AI crowd density. $5,000–$20,000/month subscription.

---

## Use Case 17: Journalism / Breaking News Coverage (SMB + Consumer)

### Customer Persona
**Name**: Riya Patel | **Title**: Independent investigative journalist
**Tier**: SMB (per-task credits, $10–25/task)

### The Task
"Photograph [location] right now. Something may be happening. Capture all visible activity. Include video if possible."

### Special Feature
"Journalist verification" enhanced C2PA chain of custody for published journalism. +$5/task premium.

---

## Use Case 18: Storm Damage Documentation (Enterprise Surge)

Pre-negotiated CAT event response contracts with P&C insurers. Surge deployment of up to 500 agents within 24 hours of a weather event. $75/task during emergency surge. Potential: $3.75M revenue from a single major storm event.

---

## Use Case 19: Hedge Fund Intelligence Feed (Data Product, Year 2–3)

Aggregate anonymized intelligence across all Mosaic tasks: retail foot traffic trends, CPG promotion intensity by region, real estate site activity, construction output by city. Sold as alternative data subscription to investment research firms and hedge funds. Pricing: $50K–$500K/year. Target: 5 subscribers by Year 2 = $1M–$2.5M ARR.

---

## Use Case 20: AI Training Data (Internal Revenue Stream)

Every task produces labeled visual data sold to AI labs, automotive companies, and robotics firms. Pricing: $0.05–$2.00/image depending on type and quality. At 500K tasks/month × 8 images/task = 4M images/month × $0.12 blended = $480K/month by Month 24. See FINANCIAL_MODEL.md for full projection.

---

## Interesting Combinations (8 Non-Obvious)

See USE_CASES_V2.md Cycle 109 for full detail on each:

1. **Multi-Buyer Single Capture**: Same agent visit fulfills tasks for 3 different buyers simultaneously — compound take rate
2. **Consumer-Sponsored Enterprise Task**: Brand co-sponsors consumer tasks to get discounted shelf data
3. **Incidental Intelligence**: Agent captures secondary data they didn't know was valuable; AI surfaces it
4. **Competitor as Customer**: Store owners monitoring each other, both paying Mosaic
5. **Bounty Pool**: Multiple buyers co-fund an expensive ongoing location surveillance task
6. **Location Subscription**: Subscribe to a geo-fenced area, not a task type
7. **Social Intelligence / Ambient Earn**: Earn by documenting places you're already visiting
8. **Intelligence Feed as Product**: Aggregate task output becomes an alternative data subscription for hedge funds
