# MOSAIC — Investor FAQ
**Top 20 VC Questions + Best Answers**

---

## MARKET & COMPETITION

### Q1: Who are the customers?
**A:** Three distinct buyer profiles:

1. **Enterprise CPG brands** (Unilever, P&G, Nestlé, Reckitt) — currently spending $50–$300 per store visit on traditional field audit firms (BeMyEye, Nielsen, CROSSMARK). Budget owner: VP Commercial, Trade Marketing, Sales Ops. Pain: data is 3 weeks old and covers <5% of stores.

2. **SMB brands and food/beverage startups** — currently have no affordable audit option at all. They make gut-call decisions or pay for consultant visits. Self-serve $49–$749/month unlocks this untapped segment.

3. **One-time buyers** (insurance, property, event managers) — consumer tier, $5–$25/task, no relationship required.

### Q2: Why not just use BeMyEye?
**A:** BeMyEye is an enterprise-only, sales-led, European-focused company with a 15-year history and $35M revenue. Their weaknesses are our moat:
- **No consumer tier** (ever — it's a structural business choice, not an oversight)
- **No route-matching algorithm** — tasks are manually assigned
- **No on-device AI processing** — GDPR compliance is a patchwork
- **2–3 week turnaround** — they batch tasks, not real-time
- **4× more expensive per task** — their cost basis is higher

They're the right company to point VCs at when explaining why this market hasn't been disrupted yet.

### Q3: Why not use Field Agent or Premise?
**A:** Field Agent is US-only, enterprise-only, and has no AI extraction layer. Premise (now Fulcrum) pivoted to market research. Neither has a consumer tier, commute-mode matching, or a training data monetization path.

### Q4: What's the moat?
**A:** Three compounding moats:

1. **Data network effect**: Every task generates labeled, geotagged, AI-verified visual data. At scale, our training data is worth more than the task revenue. Competitors can't replicate 3 years of proprietary visual data.

2. **Supply-side density**: Once we have 2,000 active agents in a city, task completion rates hit 95%+. That makes us faster and cheaper than any competitor who arrives late.

3. **On-device GDPR architecture**: MediaPipe face redaction runs on-device before upload. No biometric data ever leaves the phone. This is technically difficult to retrofit into an existing cloud-first platform — and legally required in the EU.

The moat deepens with every task completed.

### Q5: Google/Amazon could do this. Why can't they?
**A:** They could — in 5 years, after building the supply side. Meanwhile, we'll have locked up enterprise contracts, built supply density in 15+ cities, and generated 50M+ proprietary labeled images. The window is execution, not innovation.

---

## BUSINESS MODEL

### Q6: What are the unit economics?
**A:**
- Customer pays: $14 (blended task price)
- Agent payout: $5.60 (40% fixed)
- AI + infra + payment: $1.26
- **Gross profit: $7.14 (51%)**

At enterprise pricing ($18–25/task), GM improves to 58%. At training data tier (95% GM), pure margin. The 40% agent payout is non-negotiable — it's our trust signal and why agent churn is <10%/month.

### Q7: Why 40% to agents? Won't they demand more?
**A:** We benchmarked against Uber (25%), TaskRabbit (30%), and Fiverr (20%). 40% is the highest in the category. High payout = high retention = high fulfillment rate = better SLA = more customers willing to pay premium. It's a strategic choice, not a cost problem.

### Q8: Training data revenue — how does that work?
**A:** Every compliance task produces geotagged, AI-verified, timestamped shelf imagery. At 100K tasks/month, that's ~200K labeled images. AI labs (OpenAI, Google, Anthropic), autonomous retail companies, and robotics firms pay $0.10–$0.15/image for real-world labeled visual data. We project $210K/month from this by Month 24, at 95% gross margin. This tier is only possible because we operate at consumer scale — BeMyEye never will.

### Q9: What does the revenue model look like at scale?
**A:**
| Month | MRR |
|-------|-----|
| 3 | $35K |
| 6 | $99K |
| 12 | $355K |
| 18 | $822K |
| 24 | $1.6M |

Built bottom-up from task economics — not top-down market share assumptions. 3-city launch, expanding to 8 cities by Month 12.

---

## TRACTION & EXECUTION

### Q10: You're pre-revenue. Why invest now?
**A:** Three reasons:

1. **The product works** — full three-tier marketplace built and functional. Agent app, enterprise portal, AI pipeline, route-matching, on-device GDPR. 8 weeks, $30K/month burn.

2. **The window is real and closing** — BeMyEye's last meaningful product update was 2020. US gig platforms haven't noticed Europe. Enterprise AI adoption is 3× faster than 2023. Whoever builds supply density in the top 10 cities first owns this category.

3. **The seed metrics are achievable** — $98K MRR by Month 6 requires 10 enterprise customers at $2.5K/month and 500 active agents per city. BeMyEye built to $35M over 15 years without a consumer tier or AI. We'll do it in 18 months with both.

### Q11: What's your burn rate?
**A:** $30K/month pre-seed (2-person team + AI stack). Post-seed: $120K/month (8-person team). At $5M raised, that's 41 months of runway at seed burn or 18 months at post-seed burn — both intentionally beyond Series A trigger.

### Q12: Why two founders? Isn't that risky for marketplace complexity?
**A:** It's a feature, not a bug. Two founders with AI-native development practices deliver 12-person team output. The AI stack handles design, testing, infrastructure, documentation. Traditional startups hire 6 engineers; we ship faster with 2 by not managing headcount. Post-funding, we hire 3 engineers and 1 AE — the company scales, the philosophy stays.

---

## SUPPLY SIDE

### Q13: Why would gig workers use this instead of Deliveroo/Uber Eats?
**A:** Different task profile entirely:
- **No bicycle/car required** — tasks are pedestrian
- **No restaurant dependency** — we never have a "restaurant is busy" constraint
- **Higher per-hour equivalent** — $14.50 for 8 minutes = $109/hour equivalent
- **Commute Mode** — tasks are matched to your existing route. It's additive income, not a second job.

Worker psychographics: office commuters (trains/tubes), students between classes, hospital workers on breaks. Not gig drivers — gig walkers. Different supply pool, less competitive.

### Q14: What's agent retention like? (projected)
**A:** Target churn <10%/month based on comparable platforms. Key retention drivers:
- 40% payout (highest in category)
- Instant payout to bank (Stripe Connect)
- Gamification: badges, leaderboards, bonus tiers
- Commute Mode reduces friction from "go somewhere" to "earn on the way"

LTV:CAC target for commute-mode agents: 90:1.

---

## TEAM & FUNDRAISE

### Q15: Why you?
**A:** The commercial co-founder has spent years in CPG enterprise sales — they know exactly what a trade marketing director at Unilever needs to see to sign a contract and why the current solutions are inadequate. The technical co-founder has shipped consumer mobile products at scale and built AI inference pipelines. Neither of us is guessing at the buyer or the tech. We built the product before raising because we could — and we knew exactly what to build.

### Q16: What's the fundraise structure?
**A:** $5M Seed. Priced preferred round (Series Seed). Pre-money: $20–25M. Standard YC-style terms (1× liquidation preference, no participating preferred). Looking to close in 60–90 days. Target lead: one institutional fund ($3M) + angels ($2M).

### Q17: Why $5M and not $3M or $10M?
**A:** $3M gets us to 2 cities but not proof-of-concept at scale. $10M is over-capitalized for seed — we don't need it yet. $5M at $120K/month burn buys exactly 18 months to Series A triggers: 3 cities proven, $10M ARR run rate, 15K active agents.

### Q18: What are the Series A metrics?
**A:** $9.87M ARR ($822K MRR), 15,000 active agents, 3 cities at 90%+ task fulfillment rate, at least 1 EU enterprise anchor. We start the Series A raise at Month 16. Target: $50–100M valuation.

---

## RISK & OBJECTIONS

### Q19: What's the biggest risk?
**A:** Supply-side cold start in a new city. To fulfill a task, we need an agent already near the store. Solution: city launch playbook that seeds 500 agents before opening to enterprise customers. Agents are acquired via TikTok/Instagram creator campaigns targeting commuters — CPAs run $8–12. We build supply before demand.

Second risk: enterprise sales cycle length. Mitigation: SMB and consumer tiers provide revenue while enterprise deals close. The 90-second self-serve flow means we don't need an enterprise customer to start generating revenue.

### Q20: How do you handle GDPR and data privacy?
**A:** It's our competitive advantage, not a compliance checkbox:
- **Face and plate redaction runs on-device** via MediaPipe/TFLite before upload
- **No biometric data ever reaches our servers**
- **Agent consent** is explicit and GDPR-compliant at sign-up
- **Store data ownership** is clear in enterprise contracts (brand owns their compliance data)
- DPO engaged. Data Processing Agreements templated. Architecture reviewed.

EU-first privacy design is why we can sell to EU enterprises like Unilever, Heineken, and Nestlé — and why US competitors can't enter EU without rebuilding from scratch.

---

*Questions not covered here? investors@mosaic-intel.com*
