# Pixie — Financial Model

## Unit Economics

### Per Task

| Line Item | Amount | Notes |
|---|---|---|
| Customer revenue (blended avg) | $35.00 | Mix of task types + tiers |
| Agent payout (40%) | $(14.00) | Guaranteed agent take rate |
| AI processing (inference + storage) | $(0.20) | Cloud GPU inference + S3 |
| Payment processing (Stripe, 2.9% + $0.30) | $(1.32) | On customer side only |
| Platform infrastructure (allocated) | $(0.50) | Kafka, EKS, Redis |
| **Gross Profit per Task** | **$19.00** | |
| **Gross Margin** | **54%** | |

**At scale** (Year 2, 500K+ tasks/month):
- AI inference cost drops to $0.05/task (volume pricing + model efficiency)
- Infrastructure allocation drops to $0.20/task (fixed cost spreading)
- Agent payout % holds at 40% (competitive necessity)
- **Target gross margin: 65%+**

---

### Customer Unit Economics

| Metric | Year 1 | Year 2 |
|---|---|---|
| Average ACV (Annual Contract Value) | $36,000 ($3K/month) | $72,000 ($6K/month) |
| Average Contract Length | 12 months | 18 months |
| Net Revenue Retention | 115% | 130% |
| LTV (3-year, 85% retention) | $108,000 | $250,000 |
| Customer CAC (Year 1, founder-led) | $3,000 | $8,000 |
| Customer CAC (Year 2, AE-led) | $8,000 | $12,000 |
| LTV:CAC | 35:1 (Year 1) | 20:1 (Year 2) |
| CAC Payback Period | 1 month | 2 months |

LTV:CAC of 35:1 in Year 1 reflects founder-led sales (low cash CAC, high time cost). At Year 2 with a sales team, still 20:1 — excellent.

---

### Agent Unit Economics

| Metric | Amount | Notes |
|---|---|---|
| Agent CAC (blended) | $22 | Ambassador: $15, Paid social: $45, Referral: $20 |
| Avg tasks in first month | 12 | After sign-up and first task completion |
| Monthly retention (M2) | 45% | % who complete tasks in 2nd consecutive month |
| Avg tasks per active agent-month | 35 | Power law distribution: 20% of agents do 80% of tasks |
| Platform contribution per task (above direct cost) | $1.50 | After payout but before platform fixed costs |
| LTV per agent (50 tasks over lifetime) | $75 | 50 tasks × $1.50 contribution |
| LTV:CAC | 3.4:1 | Minimal but positive |
| Agents needed for LTV positivity | 15 tasks | Break-even vs $22 CAC |

**Agent retention is the key lever**: if agent retention improves from 45% to 60% M2, LTV doubles without spending more on acquisition.

---

## Revenue Model — Monthly Projections

### Conservative Case (Base)

| Month | Customers | Avg MRR/Customer | MRR | Cumulative ARR |
|---|---|---|---|---|
| 1 | 2 | $2,500 | $5,000 | n/a |
| 2 | 3 | $2,800 | $8,400 | n/a |
| 3 | 4 | $3,000 | $12,000 | $144K |
| 4 | 5 | $3,500 | $17,500 | $210K |
| 5 | 7 | $4,000 | $28,000 | $336K |
| 6 | 9 | $4,500 | $40,500 | $486K |
| 7 | 11 | $5,000 | $55,000 | $660K |
| 8 | 13 | $5,500 | $71,500 | $858K |
| 9 | 16 | $6,000 | $96,000 | $1.15M |
| 10 | 19 | $7,000 | $133,000 | $1.6M |
| 11 | 22 | $8,000 | $176,000 | $2.1M |
| 12 | 25 | $10,000 | $250,000 | **$3.0M ARR** |

### Upside Case (Strong Execution)

| Month | Customers | MRR | ARR (run rate) |
|---|---|---|---|
| 6 | 12 | $64,000 | $768K |
| 12 | 30 | $360,000 | **$4.3M ARR** |
| 18 | 55 | $825,000 | **$9.9M ARR** |

**Note**: Upside case requires 2 early enterprise logos (>$20K/month) and strong word-of-mouth in CPG community.

---

## Path to $1M ARR

**Method A**: 28 customers at $3K MRR average
**Method B**: 17 customers at $5K MRR average
**Method C**: 10 customers at $8.3K MRR average + expansion revenue

Founder sales pace required (Method B): 1.4 new customers/month, every month for 12 months.

This is achievable: 3 prospect meetings/week × 40% pilot rate × 60% pilot-to-paid × 1.2 month avg sales cycle = 1.7 new customers/month.

**$1M ARR timeline**: Month 10–12 (conservative), Month 8–9 (upside)

---

## Path to $100M Series A

**Series A trigger criteria**:
- $7–10M ARR (10x ARR multiple at $100M valuation)
- 3x YoY growth rate
- >115% Net Revenue Retention
- 12+ cities with >80% fulfillment rate
- 50+ enterprise customers
- 15,000+ active agents

**Month 18 forecast (upside case)**: $9.9M ARR → justifies $100M round at 10x ARR multiple

**Key growth driver, Month 12–18**: Net Revenue Retention. If existing customers expand from $5K/month to $15K/month (adding more cities, more task volume), the revenue doubles without a single new customer.

---

## Cost Structure

### Year 1 (Seed Stage)

| Category | Monthly | Annual |
|---|---|---|
| Salaries (2 founders + 2 eng + 1 ML + 1 sales) | $80,000 | $960,000 |
| Cloud infrastructure (AWS) | $8,000 | $96,000 |
| AI/ML compute (SageMaker) | $5,000 | $60,000 |
| Agent acquisition (paid ads + ambassador) | $15,000 | $180,000 |
| Legal + compliance | $7,000 | $84,000 |
| Misc (tools, office, travel, conferences) | $5,000 | $60,000 |
| **Total Monthly Burn** | **$120,000** | **$1,440,000** |

**Revenue offset**: $250,000 (Year 1 ARR ramp, ~$120K cash collected in Year 1 given ramp)
**Net Year 1 burn**: ~$1,320,000

### Year 2 (Post-Seed, Pre-Series A)

| Category | Monthly | Annual |
|---|---|---|
| Salaries (14 people) | $200,000 | $2,400,000 |
| Cloud infrastructure | $25,000 | $300,000 |
| AI/ML compute | $20,000 | $240,000 |
| Agent acquisition | $30,000 | $360,000 |
| Legal + compliance (SOC 2, GDPR, pen test) | $15,000 | $180,000 |
| Sales & marketing | $20,000 | $240,000 |
| Misc | $10,000 | $120,000 |
| **Total Monthly Burn** | **$320,000** | **$3,840,000** |

**Year 2 revenue**: $5–7M (growing throughout year)
**Year 2 net**: Break-even to cash flow positive by end of Year 2

---

## Funding Requirements

### Seed Round: $2.5M

**Runway**: 18 months (to $3–4M ARR, Series A metrics in sight)
**Use of funds**:
- Engineering (mobile app + AI pipeline): 50% = $1,250,000
- Agent acquisition (first 3 cities, 1,500 agents): 25% = $625,000
- Enterprise sales (outreach, conferences, 1 AE hire): 15% = $375,000
- Legal/compliance (privacy attorney, SOC 2 start): 10% = $250,000

**Milestones to hit with seed**:
- 10 cities with >80% fulfillment rate
- 25 paying enterprise customers
- $3.6M ARR run rate
- SOC 2 Type I certified
- Series A raise begins

### Series A: $100M

**Target timing**: Month 18–24
**Valuation**: ~$100M pre-money (10x ARR at $8–10M ARR)
**Lead investor profile**: Growth VC with enterprise software or marketplace expertise (Tiger Global, Andreessen Horowitz, Insight Partners, General Catalyst)
**Use of funds**:
- Engineering + AI (scale team, model quality): 50% = $50,000,000
- City expansion (10 new cities, international): 20% = $20,000,000
- Enterprise sales team (10 AEs + 2 SEs + CSM team): 20% = $20,000,000
- Legal/compliance/international: 10% = $10,000,000

---

## Key Financial Assumptions

| Assumption | Value | Source |
|---|---|---|
| Blended task price | $35 | Mix of task types, competitive benchmark |
| Agent take rate | 40% | Competitive with TaskRabbit, above DoorDash |
| Gross margin (early) | 54% | Unit economics calculation |
| Gross margin (scale) | 65%+ | AI cost reduction + fixed cost spreading |
| Customer monthly churn | 3% | ~85% annual retention (SaaS benchmark for this price point) |
| Net Revenue Retention | 115% | Expansion revenue from adding cities/task volume |
| Agent retention (M2) | 45% | Moderate; improves with platform maturity |
| Agent CAC | $22 | Blended channel CAC |
| Customer CAC (Year 1) | $3,000 | Founder-led sales |
| Fulfillment rate target | >80% | Enterprise SLA floor |
| AI validation pass rate | >85% | Quality gate target |

---

## Training Data Revenue (Bonus Revenue Stream)

Not included in base model — upside case only.

| Month | Tasks/Month | Images/Task | Total Images | Blended $/image | Monthly Revenue |
|---|---|---|---|---|---|
| 12 | 30,000 | 8 | 240,000 | $0.08 | $19,200 |
| 18 | 150,000 | 8 | 1,200,000 | $0.10 | $120,000 |
| 24 | 500,000 | 8 | 4,000,000 | $0.12 | $480,000 |
| 36 | 2,000,000 | 8 | 16,000,000 | $0.15 | $2,400,000 |

At Month 36, training data revenue alone is $2.4M/month at 95% gross margin. This is the "hidden" revenue stream that investors will undervalue and the market won't anticipate. It's real and it's defensible.
