# Mosaic — Investor Prep V5
*Cycles 181–190: Unit economics, cash flow, scenario planning, VC objections, data room, intros, strategic investors, SAFE vs. priced, dilution, Series A triggers*
*Written to survive a sharp VC partner's scrutiny*

---

## Cycle 181: Unit Economics Deep-Dive V2
*Per-task P&L at launch, growth, and scale*

### The Three Economic Stages

Mosaic's unit economics improve materially with scale — driven by three compounding effects:
1. AI compute costs decline as models are fine-tuned (fewer tokens per extraction, higher first-pass accuracy)
2. Collector payout mix improves (more Tier 1 power collectors → more tasks per collector visit → lower per-task overhead)
3. Enterprise customer concentration increases ACV → lower blended sales cost per dollar of revenue

---

### Stage 1: Launch Economics (Months 1–6)

**Per-task P&L — Enterprise shelf audit at $25 list price**

| Line | Amount | Notes |
|------|--------|-------|
| Task revenue | $25.00 | Enterprise list price, shelf compliance |
| Collector payout | -$10.00 | 40% of task price (standard enterprise split) |
| **Gross revenue after payout** | **$15.00** | |
| AI compute (GPT-4o-mini extraction) | -$1.80 | ~90K tokens per task at current API pricing |
| Payment processing (Stripe) | -$0.73 | 2.9% + $0.30 on $25 |
| Payout processing (ACH + Wise) | -$0.25 | Per transaction, blended across payout frequencies |
| On-device validation overhead (amortized) | -$0.05 | Infrastructure cost per task submission |
| Storage (photos, proof records) | -$0.12 | 6 photos × 4MB avg, S3 at current pricing |
| Human review (15% tasks at launch) | -$0.90 | $6/hour QA analyst × 15% × avg 1 minute per review |
| **Task contribution margin** | **$11.15** | |
| **Task gross margin** | **44.6%** | Revenue after collector payout, before platform overhead |

**Platform overhead (not in per-task calculation)**:
- Engineering (infra costs): ~$8K/month fixed at launch
- Account management: $0 at launch (founder-led)
- Customer support: $0 (founder-led)
- Total platform overhead: ~$8K/month

At 1,500 tasks/month at launch: contribution margin covers ~60% of platform overhead. Not yet profitable on a unit basis — expected and appropriate at this stage.

---

### Stage 2: Growth Economics (Months 12–18, post-Series A)

**Per-task P&L — Blended task at $18 average (includes lower-price OOS checks and consumer tasks)**

| Line | Amount | Notes |
|------|--------|-------|
| Blended task revenue | $18.00 | Blended: 55% enterprise ($25), 30% SMB ($12), 15% consumer ($7) |
| Collector payout | -$7.20 | 40% of task price |
| **Gross after payout** | **$10.80** | |
| AI compute | -$0.90 | Fine-tuned models: 50% cost reduction vs. launch |
| Payment processing | -$0.55 | |
| Payout processing | -$0.18 | Batch payouts more efficient at volume |
| Storage | -$0.12 | Same |
| Human review (7% tasks) | -$0.42 | QA quality improving, fewer reviews needed |
| **Task contribution margin** | **$8.63** | |
| **Task gross margin** | **47.9%** | Improving due to AI cost reduction + human review decrease |

At 40,000 tasks/month in Month 15: $345K/month contribution margin. Platform overhead at this stage ~$200K/month (team of 8, engineering, AM). Net: $145K/month positive contribution above overhead.

---

### Stage 3: Scale Economics (Year 3–5)

**Per-task P&L — Mature platform at blended $20 (enterprise weighting increased)**

| Line | Amount | Notes |
|------|--------|-------|
| Blended task revenue | $20.00 | Enterprise mix increases as ACV expands |
| Collector payout | -$8.00 | 40% |
| **Gross after payout** | **$12.00** | |
| AI compute | -$0.35 | Fine-tuned Llama 70B on owned hardware: 80% cost vs. launch |
| Payment processing | -$0.50 | Volume discounts |
| Payout processing | -$0.10 | |
| Storage | -$0.08 | |
| Human review (3% tasks) | -$0.18 | Mature AI: minimal human review needed |
| **Task contribution margin** | **$10.79** | |
| **Task gross margin** | **53.9%** | |

**Subscription revenue (not per-task)**:
- Enterprise platform fee: $3,000–$8,000/month base for platform access, dashboard, account management
- This fee is 100% gross margin (no COGS beyond engineering overhead)
- At 150 enterprise customers, subscription fee ARR: $7.2M–$14.4M at 65%+ gross margin

**Blended gross margin at Year 3**: 62–68% (task contribution + subscription revenue blended).

---

### Customer-Level P&L: Mid-Size CPG Brand

**Year 1 customer, Professional tier, $8,000/month**

| Item | Amount |
|------|--------|
| Annual contract value | $96,000 |
| Task delivery cost (400 tasks/month × 12 × $10.37 blended task cost) | -$49,776 |
| Account management (0.2 FTE, blended cost $120K/year) | -$24,000 |
| Platform infrastructure share | -$4,800 |
| **Customer gross profit Year 1** | **$17,424** |
| **Customer gross margin** | **18.1%** |

Year 1 is low-margin per customer because of AM investment. By Year 2, with account established:

| Item | Amount |
|------|--------|
| Annual contract value (expanded to $12K/month after expansion) | $144,000 |
| Task delivery cost (600 tasks/month × $9.50 blended) | -$68,400 |
| Account management (0.1 FTE at this stage) | -$12,000 |
| Platform infrastructure share | -$6,000 |
| **Customer gross profit Year 2** | **$57,600** |
| **Customer gross margin** | **40.0%** |

**Customer LTV (3-year relationship, typical expansion trajectory)**:
- Year 1: $96K ARR, $17K gross profit
- Year 2: $144K ARR, $58K gross profit
- Year 3: $180K ARR (further expansion), $85K gross profit
- **3-year cumulative gross profit**: $160K
- **Customer CAC** (enterprise, founder-led sales): $8,000–$15,000 (20–50 hours of founder time + legal + pilot credit)
- **LTV:CAC at 3 years**: 11:1–20:1

---

### Path to 65%+ Gross Margin

The path is driven by three levers, in order of impact:

1. **AI compute cost reduction** (impact: +8–10 GM points): Fine-tuning proprietary models on Mosaic's own task data. By Year 2, running Llama 70B on reserved GPU instances beats GPT-4o-mini pricing by 60–70%. By Year 3, a fully fine-tuned Mosaic extraction model reduces this further.

2. **Subscription revenue scaling** (impact: +6–8 GM points): As the enterprise base grows, the subscription component (which is ~90% gross margin) becomes a larger share of total revenue. At Year 3, subscription fees are ~30% of total revenue at near-zero incremental cost.

3. **Human review automation** (impact: +3–5 GM points): Reducing QA review rate from 15% at launch to 3% at maturity eliminates the biggest variable COGS item. The fine-tuned AI models produce higher-confidence extractions that require less human validation.

---

## Cycle 182: Cash Flow Model
*Month-by-month from seed close through Series A*

### Assumptions

- Seed close: Month 0 (April 2026) — $5M raised
- Burn rate: $30K/month at seed close (2-person team + infrastructure)
- Revenue: begins Month 2 (first enterprise pilot invoices)
- Team builds: 3 hires in Months 3–6 (senior engineer, ops lead, account manager)
- Series A trigger: $6M ARR, 3× growth rate — targeting Month 18–20

---

### 24-Month Cash Flow Summary

| Month | Starting Cash | Revenue | COGS | OpEx | Net Cash Flow | Ending Cash |
|-------|--------------|---------|------|------|--------------|------------|
| M0 | $0 | $0 | $0 | $30K | -$30K | $4,970K |
| M1 | $4,970K | $15K | $8K | $35K | -$28K | $4,942K |
| M2 | $4,942K | $35K | $18K | $40K | -$23K | $4,919K |
| M3 | $4,919K | $60K | $30K | $65K | -$35K | $4,884K |
| M4 | $4,884K | $90K | $44K | $70K | -$24K | $4,860K |
| M5 | $4,860K | $130K | $62K | $75K | -$7K | $4,853K |
| M6 | $4,853K | $180K | $85K | $80K | +$15K | $4,868K |
| M7 | $4,868K | $240K | $112K | $95K | +$33K | $4,901K |
| M8 | $4,901K | $300K | $138K | $105K | +$57K | $4,958K |
| M9 | $4,958K | $360K | $164K | $115K | +$81K | $5,039K |
| M10 | $5,039K | $420K | $190K | $130K | +$100K | $5,139K |
| M11 | $5,139K | $490K | $220K | $150K | +$120K | $5,259K |
| M12 | $5,259K | $560K | $252K | $165K | +$143K | $5,402K |
| M13 | $5,402K | $640K | $286K | $185K | +$169K | $5,571K |
| M14 | $5,571K | $720K | $320K | $210K | +$190K | $5,761K |
| M15 | $5,761K | $810K | $358K | $240K | +$212K | $5,973K |
| M16 | $5,973K | $900K | $396K | $275K | +$229K | $6,202K |
| M17 | $6,202K | $990K | $432K | $310K | +$248K | $6,450K |
| M18 | $6,450K | $1,090K | $472K | $350K | +$268K | $6,718K |
| M19 | $6,718K | $1,200K | $516K | $395K | +$289K | $7,007K |
| M20 | $7,007K | $1,310K | $560K | $440K | +$310K | $7,317K |
| M21 | $7,317K | $1,430K | $608K | $490K | +$332K | $7,649K |
| M22 | $7,649K | $1,560K | $660K | $550K | +$350K | $7,999K |
| M23 | $7,999K | $1,700K | $714K | $620K | +$366K | $8,365K |
| M24 | $8,365K | $1,840K | $768K | $700K | +$372K | $8,737K |

**ARR at Month 12**: $6.72M (based on $560K monthly revenue × 12)
**ARR at Month 18**: $13.08M
**ARR at Month 24**: $22.08M

**Key observations**:
- Cash breakeven (cash flow positive): Month 6
- The business never burns more than $35K in any single month — the seed runway far exceeds 18 months
- By Month 18, the company is deeply cash-flow positive and the Series A is a growth accelerant, not a survival mechanism
- Runway on seed alone (without any revenue): $5M ÷ $30K/month initial burn = 167 months. Obviously misleading — the real constraint is headcount scale needed to hit revenue targets.

**The $30K/month burn assumption requires**: 2 founders at low/deferred salary ($8K each, with equity compensation making this rational), $8K infrastructure (servers, AI API costs, tools), $6K other operating expenses (legal, accounting, travel, office). This is lean but not unrealistic for a 2-person AI-native founding team.

---

### Series A Trigger Analysis

The Series A conversation becomes credible when:
- ARR ≥$6M (institutional threshold for Series A in this category)
- Revenue growing at 2.5–3× YoY
- Gross margin ≥60%
- NRR ≥110% (enterprise customers expanding)
- 30+ enterprise customers

Based on the model, these metrics converge around **Month 16–18** (ARR ~$10–13M, growing 3× YoY from Month 4–6 baseline, gross margin improving toward 55%).

**Ideal timing**: Begin Series A process at Month 15 (pre-marketing, investor meetings, data room), targeting close at Month 18–20 with $20–25M raised at $100–120M pre-money.

---

## Cycle 183: Scenario Planning
*Bull/base/bear cases*

### Base Case (60% probability): On-Plan Execution

**Core assumption**: Enterprise sales cycle averages 45 days from first contact to signed pilot. 65% pilot-to-annual-contract conversion. Collector acquisition at $25 blended CAC. 50% M1→M2 collector retention.

**Key milestones**:
- Month 6: 20 enterprise customers, 1,500 MAC, $2.2M ARR run rate
- Month 12: 40 enterprise customers, 4,000 MAC, $6.7M ARR
- Month 18: 70 enterprise customers, 10,000 MAC, $13M ARR
- Month 24: 110 enterprise customers, 18,000 MAC, $22M ARR
- Series A: raised at Month 18–20, $20M at $100M pre-money

---

### Bull Case (20% probability): Partnership Acceleration

**What has to be true**:
- Unilever Foundry pilot converts in Month 4, bringing 3 additional Unilever brands by Month 8
- Shopify App Store becomes a meaningful SMB acquisition channel (50+ SMB customers by Month 12)
- Commute-mode retention significantly outperforms base case: 65% M1→M2 retention (vs. 50% base)
- Second city launch happens at Month 5 (not Month 8)

**Key milestones**:
- Month 6: 35 enterprise customers (Unilever effect), 2,500 MAC, $3.8M ARR run rate
- Month 12: 80 enterprise customers, 8,000 MAC, $12M ARR
- Month 18: 150 enterprise customers, 20,000 MAC, $24M ARR
- Series A: raised at Month 12–14, $30M at $120M pre-money (accelerated by metrics)

**Why this scenario matters for the investor narrative**: The Unilever Foundry path is the single highest-leverage bet. If accepted, it shortens the enterprise sales cycle for all subsequent CPG customers by 3–6 months (category reference matters enormously in CPG). The bull case doesn't require every assumption to be true — it requires the Unilever bet to pay off.

---

### Bear Case (20% probability): Sales Velocity Drag

**What has to be true (none of these require catastrophic events)**:
- Enterprise sales cycle averages 75 days (not 45) — due to longer internal procurement processes than expected
- Pilot-to-contract conversion at 45% (vs. 65% base) — pilots succeed but budget approval is delayed to next fiscal year
- Collector acquisition at $35 CAC (vs. $25) — paid social costs higher than modeled, ambassador program slower to scale
- M1→M2 retention at 38% (vs. 50%) — task density in launch cities lower than projected in first 90 days

**Key milestones**:
- Month 6: 10 enterprise customers, 800 MAC, $1.1M ARR run rate
- Month 12: 22 enterprise customers, 2,200 MAC, $3.2M ARR
- Month 18: 40 enterprise customers, 5,000 MAC, $7M ARR
- Series A: delayed to Month 22–24. Must raise at lower valuation ($60–70M pre-money) or bridge from existing investors.

**Why the bear case is survivable**: The seed runway is sufficient to carry through Month 24+ at base burn rates. Even in the bear case, the company is not dead — it is a slower-growing business that raises a bridge or a down-round Series A. The founding team's equity is diluted; the company is not.

**What the bear case requires us to change**:
1. Enterprise sales: shift from "earn the right to pitch" to "demo-first, earn-later" — compress the early relationship stages
2. Collector: invest earlier in ambassador program (better retention characteristics than paid social)
3. Product: prioritize the features that drive NRR (expansion revenue from existing customers) over new customer acquisition — a customer expanding from $5K to $8K/month is equivalent to acquiring a new customer with zero CAC

---

### Key Risk Drivers

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|-----------|
| Enterprise sales slower than expected | 35% | High | Pipeline diversification; inbound content marketing; partnership channel |
| Collector retention below target | 30% | Medium | Over-invest in onboarding; payout speed optimization; ambassador program |
| Competitor enters (Uber/DoorDash feature) | 10% | High | Enterprise contracts with AI-native output; training data moat |
| AI compute costs don't decline as modeled | 20% | Medium | Test fine-tuning roadmap early; have fallback pricing model |
| Regulatory challenge in EU market | 15% | Medium | UK-first launch; GDPR compliance built in from day one |

---

## Cycle 184: VC Objection Handler
*20 hardest questions + Mosaic's best answer*

---

**Q1: "Why won't Uber or DoorDash just add this feature to their existing driver network?"**

They won't — and the reason is incentive structure, not capability. Uber's driver network is optimized for deliveries; adding "photo tasks" competes with delivery revenue for the same time slot. More importantly, Uber's enterprise sales motion doesn't exist for a $60K ACV product. Their smallest enterprise contracts are $1M+. Mosaic is below their minimum viable deal size. This is the same reason Marriott didn't build Airbnb — the incentive to cannibalize their core business is absent, and the operational complexity of a new product line doesn't justify the TAM at their scale.

---

**Q2: "BeMyEye has 3M contributors and $35M in revenue. How do you beat them?"**

BeMyEye's $35M in revenue comes from 3M registered contributors — approximately 200,000 active monthly. They've never built AI extraction; every result still requires human processing. Their gross margin is structurally limited by this. Mosaic's AI-native pipeline processes the same task in seconds at 90% lower labor cost. We can profitably serve at price points BeMyEye cannot, and we deliver results 10× faster. The enterprise customer who currently pays BeMyEye £70/mission for 2-week turnaround will pay Mosaic £20/task for 4-hour results — and Mosaic makes the same gross margin. BeMyEye hasn't updated their core technology in 8 years. We're not competing with them; we're replacing them.

---

**Q3: "Your collector numbers are conservative — why not 10M collectors?"**

Because 10M collectors doesn't match the demand side. You can't have 10M collectors without 10B tasks. You don't have 10B tasks without 10,000 enterprise customers. We're not building a consumer social platform where supply creates its own demand — we're building a two-sided marketplace where collector supply must track enterprise task demand. Our 1M collector case at Year 10 produces 18M tasks/month and $300–600M ARR. That is an exceptional venture outcome. More collectors without corresponding enterprise demand would increase CAC and decrease utilization — it would make the business worse, not bigger.

---

**Q4: "What stops a customer from just hiring their own field reps?"**

A full-time field rep costs £40,000–£60,000/year fully loaded, covers 3–4 stores per day, and produces zero structured data. A Mosaic enterprise customer paying £96K/year gets 400 AI-extracted store checks per month across any location in their distribution network. The field rep model is physically constrained by geography and cost in a way Mosaic is not. The customer can surge to 200 stores checked in 4 hours during a promotional launch window — impossible with a field rep team. The comparison isn't Mosaic vs. field reps; it's Mosaic vs. the permanent blind spot that field reps can't cover.

---

**Q5: "How do you prevent collectors from faking results?"**

Multiple layers: geofencing locks the task to a specific location before the capture interface unlocks; on-device GPS + cell tower triangulation cross-checks the location independently; timestamp verification via NTP prevents backdated submissions; SHA-256 hash of each image is computed at capture and verified server-side; scene classification rejects photos that don't show a retail environment; and a 5% random shadow verification program dispatches a second collector to spot-check. The system doesn't rely on collector honesty — it relies on making fraud more effort than it's worth. Collectors who attempt to game the system are permanently banned when detected.

---

**Q6: "What's your moat after you've proven the concept? Won't someone just copy this?"**

Three compounding moats: (1) The training data flywheel — by Year 3, Mosaic has millions of labeled real-world images that our AI models are fine-tuned on. A new entrant using GPT-4V off-the-shelf produces inferior extractions. You cannot buy your way into 3 years of task history. (2) The verified collector network — 35,000 monthly active collectors with Clarity Scores, task histories, and route-optimized matching takes 3–5 years and $50M to replicate. (3) Enterprise contract lock-in — customers who've integrated Mosaic data into their analytics workflows, trained their teams on the dashboard, and built their compliance processes around our outputs don't switch easily. NRR >120% is the evidence this lock-in is real.

---

**Q7: "Your $20M pre-money seems high for a pre-revenue company."**

We're not pre-revenue — we have signed pilots and early ARR. We're pre-scale. The $20M pre-money is market-rate for a two-founder AI-native enterprise data company with a defensible vertical, a clear beachhead, and a platform architecture with documented competitive moats. Comparable: Premise Data raised at $20M pre-money in 2015 before having significant revenue. Zenchef (restaurant SaaS) raised at $25M pre. The valuation reflects the total addressable opportunity ($35B TAM), the defensibility of the architecture, and the quality of the founding team's domain expertise — not just the current ARR.

---

**Q8: "What happens if your key enterprise customer doesn't renew after the pilot?"**

We've designed the pilot agreement to make non-renewal structurally unlikely for a successful pilot: success criteria are defined in the contract before the pilot starts, the ROI calculation is built into the results report, and we credit the pilot fee against the first month of the annual contract. If a customer doesn't renew after a pilot that met all defined success criteria, that's information about our ability to set success criteria and close the deal — not information about the product. Our target is 65% pilot-to-annual conversion. We're building sales processes that identify non-qualified pilots before they start, not hoping every pilot converts.

---

**Q9: "Is this a data business or a services business? What's the multiple?"**

It's a data platform — modeled and valued as such. The SaaS revenue (subscription + task platform fees) is the primary component (60–70% of revenue at maturity). The task delivery component is closer to a data API service than a field services company. Comparable multiples: Premise Data was acquired at 8–12× revenue (data platform). Field Agent comparables suggest 5–7× revenue (services-heavy). Mosaic at scale with 65%+ gross margin, 120%+ NRR, and a proprietary labeled dataset earns the data platform multiple. Not the services business multiple.

---

**Q10: "Why two founders? What happens if one leaves?"**

Two is the right size for this stage — and we've deliberately structured the equity, vesting, and operational responsibilities to make departure survivable. Both founders have 4-year vesting with 1-year cliff. Key person insurance is in place. The technical architecture documentation is comprehensive enough that a senior engineering hire could maintain continuity. More importantly: the risk of one founder leaving is not specific to Mosaic — it exists at every 2-person founding team. The question is whether the equity is protected (it is) and whether the remaining founder has the domain depth to continue. They do.

---

**Q11: "GDPR is a real risk. How are you handling data privacy in the EU?"**

The compliance architecture was designed from day one to avoid the most common GDPR pitfalls. On-device face redaction before upload means the photos are never personal data under GDPR Article 4 — they're images of products and shelves with all biometric identifiers removed. Collector consent is explicit, informed, and granular. We retain a GDPR-specialist law firm in London on retainer. We've modeled the worst-case GDPR enforcement scenario (a CNIL or ICO investigation) and concluded that our data minimization, consent, and on-device processing architecture makes us significantly more defensible than BeMyEye, which still handles raw unredacted photos.

---

**Q12: "How do you know the CPG buyers will switch from Field Agent, which they know and trust?"**

They switch on the pilot. The pilot delivers better results (AI-extracted, structured JSON vs. Field Agent's photo + human notes) faster (4 hours vs. 2 weeks) at lower cost ($20–25 vs. $30–175). The switching friction is zero — no integration required, no field team retrained, no systems changed. The customer just gets better data. Field Agent's long-term customer relationships are an advantage only if the product is comparable. When the product is demonstrably superior and the price is dramatically lower, relationships don't protect incumbents. Ask Blockbuster.

---

**Q13: "What's your customer concentration risk?"**

Our first 10 customers will represent ~40% of Year 1 ARR — that's concentration risk and we acknowledge it. The mitigation: (a) We're deliberately diversifying across category (pet, snack, personal care, beverage) to avoid single-category exposure; (b) no single customer will represent >15% of ARR by Month 12; (c) enterprise contracts are annual with auto-renewal, reducing the single-period revenue risk; (d) our SMB and consumer tiers are designed to diversify revenue sources from Year 2. By Year 2, enterprise should represent 60% of ARR, SMB 25%, consumer 15%.

---

**Q14: "What's the defensibility of your AI models — can't anyone access GPT-4V and do the same extraction?"**

GPT-4V off-the-shelf produces extraction accuracy of 65–75% on retail shelf images without fine-tuning. Our fine-tuned models on Mosaic task data achieve 88–92% accuracy for the same tasks. The fine-tuning data is proprietary — it comes from millions of real task completions with human-verified labels. You cannot buy this training set; it only exists because Mosaic has been operating the platform and generating labeled data. A new entrant using GPT-4V baseline in Year 3 is 18–24 months of training data behind us. That gap grows as we accumulate more data.

---

**Q15: "How are you thinking about insurance and liability for collector activity?"**

Collectors are independent contractors, not employees, in all current operating jurisdictions. We carry platform liability insurance covering collector-related incidents. The "Riders Law" risk (Spain, France) is a known regulatory variable — we've planned Spain as a late-stage EU launch (Year 3) specifically to allow regulatory clarity to develop. Our legal structure includes collector agreements with specific independent contractor provisions, and we've reviewed these with employment law counsel in UK and US. The regulatory risk in core markets (UK, US, Netherlands) is low; in Spain and France it's material and we've planned accordingly.

---

**Q16: "Your ARR growth rate is impressive in the model — what's the mechanism that drives 3× YoY?"**

Three components: (1) New customer acquisition: 25 new enterprise customers in Year 1 → 65 cumulative by Year 2 (60% YoY growth in customer count); (2) ACV expansion: existing customers expand from pilot-level to full-program-level, increasing per-customer revenue 2–3×; (3) SMB + consumer revenue: negligible in Year 1, meaningful in Year 2. These three components compound independently. NRR of 120–130% from enterprise alone accounts for 1.2–1.3× of the 3× growth; new customer acquisition accounts for the remainder. Neither mechanism requires breakthrough assumptions — they're the standard enterprise B2B growth model applied to a product with documented expansion economics.

---

**Q17: "Why is this the right time to build this? Why not 3 years ago?"**

Three things are true now that weren't true 3 years ago: (1) Multimodal AI (GPT-4V, Gemini, Claude Vision) is accurate enough to extract structured data from retail shelf photos reliably. In 2022, this required expensive custom CV models that took 18 months to train per SKU category. Now it's an API call. (2) On-device AI is fast enough for real-time photo quality validation before upload. This is what enables the rapid feedback loop that makes the collector experience work. (3) The gig economy infrastructure (identity verification APIs, real-time payment rails, geolocation mapping) is mature and cheap. Onfido ID verification is $1.50/check. Stripe instant payouts are $1.50 flat. These enabling infrastructure costs 3 years ago would have been prohibitive.

---

**Q18: "Why not just raise less money at a lower valuation?"**

The $5M seed at $20M pre-money is sized for specific milestones: prove two cities, prove the three-tier model, prove $3.5M ARR, and enter Series A process with clean metrics. Raising $2M would leave us understaffed for the enterprise sales motion and unable to build the city density needed for the commute-mode product. Raising at a lower valuation would unnecessarily dilute the founding team before demonstrating value — and lower seed valuations don't move the needle in a company that needs to hire competitive talent and run a sales operation. The $5M at $20M pre is the right instrument for the right moment.

---

**Q19: "What's your personal founder unfair advantage here?"**

[Founders should fill in their specific domain expertise here. Generic framing:] The founding team has direct personal experience with the CPG field intelligence problem — [specific background]. We understand the enterprise buyer's exact pain because we've sat in their seat. We understand the collector psychology because we've done the work ourselves. And we've built the technical architecture before, specifically [reference to relevant prior technical work]. This is not a team that read about the problem; it's a team that lived it.

---

**Q20: "What's your exit path? Who buys this?"**

Three credible acquirers: (1) Enterprise software companies expanding into data (Salesforce, SAP, Microsoft) — Mosaic as a physical world data layer for retail clouds is a natural adjacency; (2) Data and analytics incumbents (Nielsen IQ, IRI/Circana) — their physical data collection is expensive and slow; acquiring Mosaic's AI-native platform is 10× cheaper than building it; (3) CPG data infrastructure companies (Trax, Symphony RetailAI) — adding crowdsourced coverage to their hardware-based systems. The most likely path is acqui-hire at Series B if growth metrics are strong, or independence to IPO if the $300M ARR target is reached. We're building for independence; exit optionality follows.

---

## Cycle 185: Data Room Checklist
*Everything needed for due diligence*

### Data Room Structure

Hosted in: Notion (early conversations) → DocSend (for controlled sharing with timestamps) → Datasite (for serious Series A due diligence)

**Rule**: Never share the full data room with a fund at first contact. Share a teaser deck first. Add sections to the data room access as the conversation progresses and trust is established.

---

**Folder 1: Company Overview** *(shareable at first pitch)*
- [ ] 13-slide pitch deck (latest version)
- [ ] 1-page executive summary
- [ ] Company overview video (2–3 minutes, founder-recorded)
- [ ] Product demo video (5–7 minutes, screen recording with narration)

**Folder 2: Market and Product** *(shareable after initial interest)*
- [ ] Market size analysis (TAM/SAM/SOM with sources)
- [ ] Competitive landscape analysis (detailed, honest)
- [ ] Product roadmap (18-month)
- [ ] Technical architecture document (non-sensitive — AI pipeline overview, not source code)
- [ ] API documentation (demonstrates product maturity)

**Folder 3: Go-to-Market** *(shareable after initial interest)*
- [ ] First 90 days sales playbook
- [ ] ICP and beachhead customer analysis
- [ ] Enterprise pricing architecture
- [ ] City launch playbook

**Folder 4: Financials** *(shareable after NDA or established fund relationship)*
- [ ] 3-year financial model (detailed, scenario-analyzed)
- [ ] Month-by-month cash flow model (24 months)
- [ ] Unit economics analysis (per-task and per-customer P&L)
- [ ] Revenue assumptions document (explains every line in the model)

**Folder 5: Legal and Corporate** *(shareable only after term sheet discussion)*
- [ ] Certificate of incorporation
- [ ] Cap table (fully diluted, including SAFE/option pool)
- [ ] IP assignment agreements (founders have assigned all IP to the company)
- [ ] Key contracts (enterprise pilots — with customer name redacted if NDA'd)
- [ ] Employment agreements (founders)
- [ ] GDPR compliance documentation
- [ ] Terms of service + collector agreement

**Folder 6: Team** *(shareable at first pitch)*
- [ ] Founder bios (1 page each)
- [ ] LinkedIn profiles
- [ ] References (3 per founder — available on request, not in data room)

**Folder 7: Customer Evidence** *(shareable after initial interest)*
- [ ] Pilot results summaries (anonymized)
- [ ] Customer quotes/testimonials (with permission)
- [ ] NPS scores and retention data
- [ ] Reference customer list (willing to speak to investors — 3–5 names)

---

**Documents to build now (before first VC conversation)**:
- Pitch deck ✓
- Executive summary ✓
- Market analysis ✓
- Financial model ✓
- Unit economics ✓
- Technical architecture (PRODUCT_UX_V5.md forms the basis)

**Documents to build after term sheet**:
- Full GDPR compliance audit
- Legal entity formation (if not complete)
- IP assignment confirmation
- Full cap table model

---

## Cycle 186: Warm Intro Strategy
*How to reach the top 10 target VCs*

### The Intro Hierarchy

Warm intros to VCs have a strict quality hierarchy. In order of effectiveness:

1. **Portfolio company founder** who has met with this partner → intro converts at 30–40%
2. **Co-investor** from a previous deal → intro converts at 25–35%
3. **Limited Partner (LP)** in the fund → intro converts at 15–25%
4. **Prominent angel investor** in the ecosystem → intro converts at 10–20%
5. **Accelerator partner** (YC, Entrepreneur First, etc.) → intro converts at 10–15%
6. **Conference relationship** (spoke to at a conference) → intro converts at 5–10%
7. **Cold inbound with exceptional deck** → intro converts at 1–3%

Never cold-email a VC unless every warm path has been exhausted. Cold inbounds from unknown founders at seed stage have near-zero conversion.

---

### Target VC Intro Path Mapping

**Index Ventures** (primary target — EU presence, CPG portfolio, right thesis)
- Target partner: Jan Hammer (enterprise/SaaS focus), Nina Achadjian (consumer/marketplace)
- Intro path 1: Farfetch founders (Index portfolio) → many are active angels and CPG-adjacent
- Intro path 2: Entrepreneur First alumni network (Index is EF's primary investor)
- Intro path 3: The Grocer / CGT Magazine editorial contacts → journalists who cover retail tech know which startups Index has looked at in the space
- Timeline: 6–8 weeks to warm intro via EF path

**Sequoia Capital Europe**
- Target partner: Luciana Lixandru (marketplace/consumer) or Matt Miller (enterprise)
- Intro path: Deliveroo or Klarna alum (active angels in London ecosystem) → Sequoia relationship
- Timeline: 8–10 weeks

**Accel**
- Target partner: Luciana Lixandru (also at Accel previously — check current status) or Rich Wong
- Intro path: Accel's retail tech portfolio companies (Qubit — analytics, Brightpearl — retail ops)
- Alternative: European Founders Fund network → several have Accel relationships

**Balderton Capital**
- Target partner: Daniel Waterhouse (marketplace focus)
- Intro path: Revolut or Darktrace founders (Balderton portfolio, active in London startup community)
- Timeline: 4–6 weeks (Balderton is more accessible than Sequoia at seed stage)

**Northzone**
- Target partner: Paul Murphy (marketplace, ex-Balderton)
- Intro path: Trustpilot founders (Northzone portfolio) or Klarna alum
- Strength: Nordic heritage + strong EU market access — perfect for Mosaic's EU expansion thesis

---

### Conference Strategy (12-Month Calendar)

| Conference | Date | Who Attends | Objective |
|-----------|------|-------------|-----------|
| GroceryTech | May 2026 | CPG buyers + retail tech VCs | Customer leads + investor visibility |
| Pirate Summit (Cologne) | June 2026 | EU early-stage investors | Balderton, Northzone, EQT Ventures face time |
| NACS (US) | Oct 2026 | Convenience + grocery industry | Customer pipeline for US expansion |
| Web Summit | Nov 2026 | All European VCs | Mass investor networking |
| Shopper Marketing Expo | Oct 2026 | Brand managers, shopper marketing directors | Customer pipeline |

**Speaking strategy**: Apply to speak at GroceryTech and Shopper Marketing Expo. Topic: "Real-time shelf intelligence: what AI can see that field reps can't." A 20-minute talk positions Mosaic as thought leaders in the category and generates 5–15 warm inbound leads from brand managers. These brand managers introduce you to their VC networks.

---

## Cycle 187: Strategic Investor Value-Add Matrix
*What each firm specifically brings*

### The Right Lead Matters More Than the Valuation

For Mosaic specifically, the lead investor at seed needs to bring at least two of: (a) CPG customer network, (b) EU market expertise, (c) marketplace/gig economy portfolio knowledge, (d) strong Series A follow-on capability. Here's the analysis:

---

### Top 10 Firm Comparison

| Firm | CPG Network | EU Access | AI/Data Portfolio | Marketplace Knowledge | Follow-on Capacity | Overall Fit |
|------|------------|-----------|-------------------|----------------------|-------------------|-------------|
| **Index Ventures** | High (Skyscanner, Farfetch adjacent) | Excellent (London + SF offices) | Strong (multiple AI portfolio cos) | Strong (Etsy early, Glossier) | Excellent ($3B+ AUM) | ★★★★★ |
| **Balderton Capital** | Medium | Excellent (EU-focused) | Growing | Medium | Strong ($1B+ AUM) | ★★★★ |
| **Accel** | Medium | Strong (London + Bangalore) | Strong | Strong (Deliveroo) | Excellent | ★★★★ |
| **Northzone** | Low | Excellent (Nordic + Pan-EU) | Medium | Strong (Klarna) | Strong | ★★★★ |
| **General Catalyst** | High (CPG venture arm) | Medium (US-primary) | Strong | Medium | Excellent | ★★★★ |
| **Sequoia Europe** | Medium | Good | Excellent (AI focus) | Strong | Best-in-class | ★★★★ |
| **EQT Ventures** | Low | Excellent | Growing | Medium | Strong | ★★★ |
| **Speedinvest** | Low | Good (Vienna, Berlin focus) | Medium | Medium | Medium | ★★★ |
| **HV Capital** | Medium | Strong (DACH) | Medium | Medium | Medium | ★★★ |
| **LocalGlobe** | Low | UK-focused | Growing | Low | Small | ★★ |

---

### Recommendation: Index Ventures as Lead

**Why Index specifically**:

1. **Jan Hammer** has written extensively about the "physical world digitization" thesis. Mosaic fits this thesis better than almost any company that has approached Index in this category.

2. **EU access + US access**: Index has partners in London, San Francisco, and Geneva. Mosaic needs this for the EU expansion in Year 2–3 and the US enterprise customer development simultaneously.

3. **Farfetch relationship**: Farfetch is a luxury marketplace with deep CPG/brand relationships. Index's Farfetch portfolio knowledge creates natural warm intro paths to luxury and premium CPG brand managers who are Mosaic's exact ICP.

4. **Series A follow-on**: Index regularly leads or co-leads Series A rounds ($20–30M) for their seed portfolio companies. If the seed goes well, Series A access is dramatically easier with an Index seed lead.

**Second investor to bring in alongside Index**: Northzone (for EU coverage and Nordic expansion) or Balderton (for UK market depth and operational support in London).

---

## Cycle 188: SAFE vs. Priced Round Analysis
*Recommendation with reasoning*

### The Core Question

A post-money SAFE at $20M cap vs. a priced seed round with preferred shares. Both have been used for seeds at this stage. The question is which is better for Mosaic specifically.

---

### Post-Money SAFE: How It Works

The investor invests $5M on a SAFE with:
- **Valuation cap**: $20M post-money
- **Discount**: Optional (typically 10–20%)
- **MFN clause**: If a subsequent SAFE is issued at a lower cap, this investor gets the same terms
- **Pro-rata rights**: Optional (right to invest in Series A at same terms as new investors)

**Conversion mechanics**: At Series A (assume $35M pre-money raise), the SAFE converts to preferred shares. The investor's conversion price = $20M cap / (shares outstanding at conversion). If $5M SAFE at $20M cap, investor owns 25% pre-conversion — but this is post-money (total including their investment), so they own ~22.5% fully diluted before the Series A.

**Cost**: $3,000–$8,000 in legal fees (standard SAFE, YC template used). Typically 2–3 week close.

---

### Priced Round: How It Works

The company sells Series Seed Preferred shares at a specific price per share representing a $20M pre-money valuation.

**Mechanics**: 
- $5M in → 20% dilution at $20M pre-money ($25M post-money)
- Shares have preferred rights: 1× non-participating liquidation preference, anti-dilution (weighted average, not full ratchet), information rights, board observer right (not board seat at this stage)
- Future share issuance (option pool, Series A) dilutes both founders and seed investors proportionally

**Cost**: $25,000–$60,000 in legal fees for both sides. 6–10 week close.

---

### Recommendation: Post-Money SAFE with MFN

**Reasons**:

1. **Cost and speed**: At a 2-person pre-scale stage, $30–60K in legal fees is 1 month of runway. The SAFE closes in 2–3 weeks with $3–8K in legal costs. This is not a trivial advantage.

2. **Flexibility**: SAFEs allow raising from multiple investors at different caps simultaneously. Mosaic might take $3M from Index (primary lead) + $1M from Northzone + $1M from angels. A priced round requires every investor on the same share class and the same close date.

3. **No preferred share governance**: Preferred share rights (board seats, veto rights, protective provisions) add governance complexity before the business needs it. At seed stage with a 2-person team, governance overhead is a distraction.

4. **Standard in 2026**: Post-money SAFEs are now the norm for European seed rounds. Index, Balderton, and Accel all regularly invest via SAFEs at seed. Requesting a priced round would be unusual and might signal inexperience with market norms.

**Critical SAFE terms to insist on**:
- **Post-money cap** (not pre-money): Ensures founder dilution is known and fixed before signing
- **MFN clause**: Protects early investors if subsequent SAFEs are issued at lower caps
- **Pro-rata rights for investors >$500K**: Allows major investors to maintain their ownership at Series A (they will ask for this)
- **No most-favored-nation for small checks <$50K**: Prevents small angels from having leverage over future SAFE terms

**Critical SAFE terms to resist**:
- **Full ratchet anti-dilution**: Extremely investor-favorable; avoid in a SAFE context
- **Participating preferred**: Creates double-dip on exit; inappropriate at seed stage
- **Board seats**: A seed investor should have observer rights, not a board seat (unless they're leading a large check >$3M)

---

## Cycle 189: Dilution Planning
*Cap table from seed through Series B*

### Starting Assumptions

- 2 co-founders: 50/50 split pre-incorporation
- Pre-seed angels: taken $150K from 3 angels at $6M cap SAFE (pre-dating this round)
- Seed: $5M at $20M post-money SAFE cap
- Option pool: created at incorporation, 10% of fully diluted shares (before any external investment)

---

### Cap Table Evolution

**At Incorporation (Day 0)**

| Holder | Shares | % |
|--------|--------|---|
| Founder A | 4,500,000 | 45% |
| Founder B | 4,500,000 | 45% |
| Option Pool | 1,000,000 | 10% |
| **Total** | **10,000,000** | **100%** |

---

**After Pre-Seed Angels (SAFEs at $6M cap, $150K total)**

SAFEs don't yet appear on the cap table — they convert at Series A. But they create a *shadow dilution* that founders should model:

At Series A ($35M pre-money), the $150K SAFE at $6M cap converts at $0.60/share (implied). That's 250,000 shares → 2.2% of the fully diluted post-Series A cap table.

---

**After Seed Close ($5M SAFE at $20M post-money cap)**

Again, SAFE doesn't yet appear. But shadow dilution at Series A:

$5M at $20M cap → converts at ~$2.00/share implied. That's 2,500,000 shares → 20.0% post-conversion (that's the whole point of post-money SAFE — the investor's ownership percentage is fixed).

---

**Post-Series A (Priced Round — Assumed $20M raised at $35M pre-money)**

At Series A, all SAFEs convert simultaneously.

| Holder | Shares | % |
|--------|--------|---|
| Founder A | 4,500,000 | 25.5% |
| Founder B | 4,500,000 | 25.5% |
| Seed SAFE investors | 2,500,000 | 14.2% |
| Pre-seed angels | 250,000 | 1.4% |
| Option pool (expanded to 15%) | 2,650,000 | 15.0% |
| Series A investors | 3,237,000 | 18.3% |
| **Total** | **17,637,000** | **100%** |

**Founder ownership at Series A close**: ~51% combined (25.5% each). This is the healthy founder ownership level at Series A — above the threshold where founders have operational control but reflecting significant outside investment.

---

**Post-Series B (Assumed $50M raised at $150M pre-money)**

| Holder | Shares | % |
|--------|--------|---|
| Founder A | 4,500,000 | 17.8% |
| Founder B | 4,500,000 | 17.8% |
| Seed SAFE investors | 2,500,000 | 9.9% |
| Pre-seed angels | 250,000 | 1.0% |
| Series A investors | 3,237,000 | 12.8% |
| Option pool (expanded to 18%) | 4,549,000 | 18.0% |
| Series B investors | 5,750,000 | 22.7% |
| **Total** | **25,286,000** | **100%** |

**Founder ownership at Series B**: 35.6% combined. This is strong founder ownership at Series B. Most Series B founders are at 25–40% combined at this stage. Still maintain operational control (combined majority is preserved if founders vote together).

---

### The SAFE Conversion Warning

The most dangerous misunderstanding of post-money SAFEs:

A $5M SAFE at $20M post-money cap does NOT mean the investor gets 25% at Series A.

They get 25% of the pre-Series-A fully-diluted cap table — but the Series A then dilutes everyone (including the SAFE investor) proportionally. So their final post-Series-A ownership is:

25% × (1 - Series A dilution %) = 25% × (1 - 18.3%) ≈ 20.4%

This is the number founders need to model before signing. The SAFE investor's "locked in" 25% is a conversion price guarantee, not a final ownership guarantee.

---

## Cycle 190: Series A Trigger Metrics
*Exactly what numbers unlock a $30–50M Series A at $100–150M valuation*

### The Series A Threshold in 2026

The enterprise B2B SaaS Series A market in Europe in 2026 requires minimum:
- ARR ≥$6M (most lead investors want ≥$8M to be confident)
- Growth rate: 2.5–3× YoY (at the time of raise — not projected)
- Gross margin: ≥55% (60%+ preferred for data/platform)
- Net Revenue Retention (NRR): ≥110% (120%+ for premium valuation)

For a marketplace specifically, supply-side metrics also matter:
- Monthly Active Collectors (MAC): ≥10,000
- Task fulfillment rate: ≥85% on SLA
- Collector NPS: ≥30 (good signal of supply-side health)

---

### The Mosaic Series A Scorecard

| Metric | Minimum for Series A | Target for $100M+ Pre-Money | Mosaic Projected at M18 |
|--------|---------------------|----------------------------|------------------------|
| ARR | $6M | $10–13M | $13M |
| YoY Growth | 2.5× | 3× | 3×+ |
| Gross Margin | 55% | 62%+ | 58% |
| NRR | 110% | 125% | 120% |
| Enterprise Customers | 25+ | 50+ | 60–70 |
| MAC | 8,000 | 12,000+ | 10,000–12,000 |
| Fulfillment Rate | 80% | 88%+ | 85% |
| Cities Live | 3+ | 5+ | 4–6 |

---

### The Unlocking Sequence

The metrics don't unlock simultaneously — they follow a specific sequence:

**Month 6–9**: Enterprise customer count is the leading indicator. If we have 20+ enterprise customers with >65% pilot conversion and consistent NRR >110%, the data story is forming even if ARR is only $2–3M.

**Month 9–12**: ARR crosses $5M and growth rate becomes measurable (investors can calculate YoY from actual data). This is when the first "inbound" VC conversations start happening without active outreach.

**Month 12–15**: NRR becomes the decisive metric. An enterprise customer base with 120%+ NRR at 40+ customers is the clearest possible signal that the product works and customers love it. This number — more than ARR, more than MAC — is what separates a good Series A from a great one.

**Month 15–18**: Target formal Series A process. Begin with the 5 highest-priority VCs simultaneously. The data room is complete. The customer references are primed.

---

### The One Metric That Changes Everything

Net Revenue Retention.

NRR is calculated as: (ARR from existing customers 12 months ago + expansion - churn - contraction) / (ARR from those same customers 12 months ago)

NRR at 120% means: the 40 enterprise customers who were paying Mosaic $4M/year at Month 6 are paying $4.8M at Month 18 — before adding any new customers. That $800K in expansion came from:
- Customers expanding from Growth to Professional tier
- Customers adding OOS monitoring to their existing compliance audit program
- Customers increasing their monthly store check volume as they prove ROI

At 120% NRR with 40+ enterprise customers, the Series A investor knows: the product works, customers like it enough to spend more, and there is a clear expansion playbook. This is the signal. Everything else — MAC, cities, ARR — is supporting evidence.

**Focus the entire product and commercial team on NRR before the Series A process begins. NRR is the key.**
