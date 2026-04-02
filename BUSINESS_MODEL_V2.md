# Mosaic — Three-Tier Business Model (V2)
*Cycles 113–116: Full 3-tier architecture, consumer acquisition, revised financials, exact pricing*

---

## Cycle 113: Three-Tier Business Model Architecture

### The Uber Lesson Applied

Uber didn't just sell to corporate travel managers. They made it dead simple for any individual to request a ride. The result: $100B+ company instead of a $5B corporate travel tool.

Mosaic in its current form is "Uber for corporate accounts only." We're fixing this.

---

### Tier 1: Consumer / Hobbyist

**Who They Are**
- Individual consumers with a specific one-time question about a place
- Tourists, homeowners, renters, daters, parents, sports fans
- People who will never need more than 5 tasks per month
- Budget: $5–50 per task, pay-as-you-go, no commitment

**Model**: Credit wallet. Buy credits, use when needed. Credits never expire.

**Credit Packages**
| Package | Price | Credits | Per-Task Equivalent |
|---------|-------|---------|-------------------|
| Starter | $15 | 3 tasks | $5/task (crowd check tier) |
| Explorer | $35 | 5 tasks | $7/task |
| Local | $75 | 10 tasks | $7.50/task |
| Adventurer | $150 | 25 tasks | $6/task |

**Features Included**
- Standard task templates (restaurant scout, crowd check, stock check, neighborhood preview)
- Results within 24–48 hours
- 3 photos + basic AI summary (people count, condition score, availability flag)
- Email delivery
- Mobile app access

**Features NOT Included**
- API access
- Scheduled/recurring tasks
- Full AI extraction (JSON output)
- Priority fulfillment
- Analytics dashboard

**Acquisition Motion**: App store, social media, word of mouth, product-led growth
**Average Monthly Revenue per User**: $15–35 (sporadic usage)
**Expected Volume by Month 18**: 5,000 active users → $100K–175K/month
**Gross Margin on Tier 1 Tasks**: 52% (small task sizes = higher infrastructure % but no sales cost)

---

### Tier 2: SMB / Self-Serve

**Who They Are**
- Small brand owners (50–2,000 store distribution)
- Local and regional businesses (restaurants, retail chains 3–15 locations)
- Independent journalists and media outlets
- Real estate agencies (50–200 listings)
- Event production companies
- Marketing agencies buying on behalf of small brand clients

**Model**: Monthly subscription with task allotment + credit add-ons. Credit card only. No sales call.

**SMB Subscription Plans**
| Plan | Monthly Price | Tasks Included | Add-on Tasks | API | AI Output | SLA |
|------|--------------|---------------|--------------|-----|-----------|-----|
| Spark | $49 | 5 tasks | $12/each | No | Basic summary | 48hr |
| Brand | $149 | 20 tasks | $10/each | No | Full AI extraction | 24hr |
| Growth | $349 | 60 tasks | $8/each | Yes (read-only) | Full AI + anomaly alerts | 12hr |
| Agency | $749 | 150 tasks | $7/each | Yes (full) | Full AI + white-label export | 8hr |

**Annual Discount**: 20% off for annual prepay (vs 15% previously — more aggressive to lock in SMBs)

**Features Included in All SMB Plans**
- Self-serve task posting (90-second flow)
- Standard + custom task templates
- AI-extracted structured output
- Email + dashboard delivery
- Analytics: task history, store comparison
- Mobile app for customers to track tasks in real time

**Additional SMB Features (Growth+)**
- Anomaly alerts: immediate notification if AI detects OOS, compliance violation, or unusual finding
- Slack/email webhook integration
- Recurring task scheduling (monthly audits, automated)
- CSV/Excel export for spreadsheet users
- 3 sub-user seats

**Acquisition Motion**: Content marketing, product-led growth (free-to-paid), community partnerships (Shopify, Faire, Inman), affiliate program
**Average Monthly Revenue per Account**: $249 blended (mix of Spark + Brand + Growth)
**Expected Volume by Month 18**: 500 accounts → $124,500/month SMB MRR
**Gross Margin on Tier 2**: 62% (lower infrastructure per task at volume, no sales overhead)
**LTV:CAC Target**: 15:1 (CAC: $50–200 via self-serve channels; LTV: $249/month × 18-month avg retention × 62% margin = ~$2,760)

---

### Tier 3: Enterprise

**Who They Are**
- CPG brands ($100M–$5B revenue) with established competitive intelligence or retail execution budgets
- P&C insurers with claims operations teams
- National/regional retailers doing site selection
- Government transit authorities
- Fortune 500 brands with OOH advertising spend
- Data-hungry companies (hedge funds, investment research)

**Model**: Annual contracts. Custom scoping. Dedicated customer success. Quarterly business reviews.

**Enterprise Plans**
| Tier | Monthly Price | Tasks Included | Key Features |
|------|--------------|---------------|--------------|
| Business | $2,500 | 200 tasks | All Growth features + SOC 2, 5 users |
| Scale | $7,500 | 750 tasks | + Salesforce integration, 10 users, dedicated CSM |
| Platform | $25,000 | 3,000 tasks | + Custom AI models, webhooks, unlimited users, 4hr SLA |
| Enterprise+ | $50,000+ | 10,000+ tasks | + Co-branded output, white-glove QBRs, 2hr SLA |

**Enterprise-Only Features**
- SOC 2 Type II certification (required for most enterprise IT approval)
- Custom AI model trained on customer's specific SKU set / task type
- Salesforce + Snowflake + Tableau integration
- Webhooks for real-time data delivery to customer systems
- Dedicated Customer Success Manager (Scale tier+)
- SLA with financial penalty clauses (Platform tier+)
- Custom legal agreements, BAAs, NDAs
- Multi-year pricing (discounts at 2yr and 3yr terms)

**Acquisition Motion**: Founder-led sales → AE-led sales → channel partnerships (IRI, Nielsen, broker/consultant)
**Average ACV**: $60,000 (blended $5,000/month × 12 months)
**Expected Volume by Month 18**: 50 accounts → $250,000/month Enterprise MRR
**Gross Margin on Tier 3**: 58% (higher enterprise service cost offset by large volume per account)
**LTV:CAC**: 20:1 (CAC: $5,000–12,000; LTV: $60K ACV × 3 years × 115% NRR = ~$207K)

---

### Three-Tier Summary

| | Tier 1 (Consumer) | Tier 2 (SMB) | Tier 3 (Enterprise) |
|--|-------------------|-------------|---------------------|
| Revenue per account/month | $15–35 | $50–749 | $2,500–50,000+ |
| Sales motion | Self-serve | Self-serve + email | Founder → AE → CSM |
| CAC | $5–15 | $50–200 | $5,000–15,000 |
| Sales cycle | Instant | 0–7 days | 30–90 days |
| Contract | None | Monthly/annual | Annual |
| Payment | Credit card | Credit card | Invoice (NET 30) |
| Gross margin | 52% | 62% | 58% |
| LTV | $50–200 | $2,000–5,000 | $100,000–300,000 |
| LTV:CAC | 10:1 | 15:1 | 20:1 |
| Churn risk | High (sporadic) | Medium (monthly) | Low (annual) |
| Revenue diversification | High (thousands of accounts) | Medium | Low (concentration risk) |

---

## Cycle 114: Consumer Acquisition — Virality + Growth Loops

### Growth Loop 1: The Task Result Becomes Shareable Content

**The Mechanism**:
When a brand owner receives their shelf audit results, the AI generates a "Share Card" — a visual summary designed for Instagram, LinkedIn, and TikTok:

> "We just checked [Brand Name]'s shelf presence at 20 Texas stores 📊
> ✅ 14/20 stores: in stock, correct position
> ⚠️ 4/20 stores: placement issues identified
> ❌ 2/20 stores: out of stock
> Powered by @MosaicIntel"

The brand owner shares this to:
1. Show their team/investors they're data-driven
2. Flex their distribution ("we're in 20 Texas stores!")
3. Tag their distributor publicly (gentle pressure)

**Result for Mosaic**: Every brand that shares this card reaches 1,000–50,000 followers who are also indie brand owners. This is word-of-mouth at scale with zero marginal cost.

**Conversion funnel**: Share card → "what is Mosaic?" → landing page visit → free trial → paid conversion

---

### Growth Loop 2: The Agent Earnings Card Goes Viral

**The Mechanism**:
After every active day, agents see their earnings summary with a one-tap share button:

> "I made $73 today exploring my city for @MosaicIntel ⚡
> [Map showing 6 locations visited]
> [Time: 2.5 hours]
> No car needed. No boss. Just my phone.
> How to join 👉 link"

DoorDash drivers post their earnings screenshots constantly. This has the same energy but better positioning ("exploring your city" vs "delivering food").

**Targeting for paid amplification**: Facebook/Instagram ads boosting the highest-performing organic earnings posts from real agents. Social proof at scale.

---

### Growth Loop 3: The "Surprise and Delight" Moment

**The Story**: A user posts a $12 restaurant scout task before their first date. They get back:
- 5 current photos of the restaurant
- A note from the agent: "Just left — it's really nice, soft jazz playing, not too crowded"
- Crowd level: Moderate (good for a date night)
- Agent bonus: "I also photographed the dessert menu since it was displayed — looks amazing"

The user shares this to their Instagram Story: "I sent a spy to scout my date night restaurant 😂 @MosaicIntel"

This is a product moment that becomes marketing content. The surprise and delight is the agent going slightly beyond instructions in a helpful way. Agent guidelines: "If you notice something helpful that the customer didn't ask for, include it."

---

### Growth Loop 4: The Referral Program — Customers and Agents

**Customer Referral (SMB Tier)**:
- Customer A shares referral link → Customer B signs up + posts first task
- Customer A gets $30 credit. Customer B gets 3 free tasks.
- Tracked in dashboard with real-time status
- Email prompt at month 1 milestone: "You've found 3 out-of-stock events. Know someone else who'd want this?"

**Agent Referral (unchanged from existing model but amplified)**:
- Agent A shares referral code → Agent B completes 10 tasks → Agent A earns $25 cash
- **New**: Agent A also earns a percentage of Agent B's earnings for 90 days (0.5% of B's earnings)
- This creates a mentor incentive: Agent A helps Agent B succeed because it benefits Agent A
- Lifetime network: a power agent who recruits 10 active agents earns passive income

**Viral Coefficient Target**:
- Customer side: k > 0.3 (every 10 customers refer 3 more)
- Agent side: k > 0.5 (every 10 agents recruit 5 more)

---

### Growth Loop 5: Product-Led Growth

**Free Task → See Results → Upgrade Funnel**:
1. New user posts 3 free tasks (crowd level checks)
2. Results arrive with a "watermark" — blurred AI details, delayed by 24 hours
3. Notification: "Your full analysis is ready. Upgrade for instant results + complete AI extraction — $15 credit pack"
4. 25% of users convert within 7 days

**The "Saved Search" Feature**:
Once a user has posted 3+ tasks to the same location, the app offers a "Location Monitor" subscription:
"You've checked [Store Name] 3 times. Subscribe to monthly monitoring for $8/month — we'll send you a report automatically."

This converts sporadic consumers into recurring subscribers automatically.

---

### Growth Loop 6: Channels for Small Brand Owners

**Shopify App Store**:
- A "Mosaic: Shelf Intelligence" Shopify plugin
- Brand owners who sell DTC on Shopify can directly connect their distribution data and post shelf audit tasks from within Shopify
- Target: 10,000 brands that sell both DTC (Shopify) and retail (wholesale)

**Faire Wholesale Platform**:
- Faire has 700,000+ brands selling wholesale to retailers
- Partnership: "Verify your Faire retail placement" feature inside Faire's seller dashboard
- Revenue share with Faire: 20% of Mosaic revenue from Faire-referred brands

**LinkedIn Brand Communities**:
- Target: "Brand Manager" + "Independent Brand" + "Consumer Goods" LinkedIn groups (500K+ combined members)
- Content strategy: "What your distributor isn't telling you" data stories
- Case study format: "[Brand Name] found 12% of their displays weren't set up correctly — here's how"

**TikTok Native Play**:
- "Brand reality check" TikTok series: posting verified shelf photos and comparing to brand's planned placement
- Content hook: "I paid someone $12 to check my hot sauce at Whole Foods — here's what they found"
- Target audience: DTC/CPG brand owner community on TikTok (huge and growing)

---

### TikTok-Native Product Feature

**"Reality Check"** — designed specifically for social sharing:

When a brand posts a task and gets results, they can choose "Reality Check Mode":
- Side-by-side: their expected shelf planogram vs actual shelf photo
- AI comparison score: "Your shelf is 71% compliant with planned placement"
- One-tap to post as a TikTok with music, brand logo overlay

This turns shelf audit data into shareable content. Every Reality Check posted becomes a Mosaic advertisement.

**Why this works on TikTok**: The "expectation vs reality" format is one of the highest-performing content formats on TikTok. Applied to brand shelf intelligence, it's novel, relatable to brand owner audiences, and inherently shareable.

---

## Cycle 115: Revised Financial Model — Three-Tier Architecture

### New Revenue Model Structure

Three separate revenue streams model from the ground up, Month 1–24.

#### Assumptions

**Tier 1 (Consumer)**
- Average revenue per user/month: $22 (mix of pack sizes, not all users active every month)
- Month 3 active users: 500 → Month 12: 4,000 → Month 18: 10,000 → Month 24: 25,000
- Gross margin: 52%
- CAC: $10 (app store + viral + referral)
- Monthly churn: 15% (irregular users; mitigated by credits not expiring)

**Tier 2 (SMB)**
- Average MRR per account: $249 (blended across Spark/Brand/Growth/Agency)
- Month 3 accounts: 25 → Month 12: 250 → Month 18: 600 → Month 24: 1,200
- Gross margin: 62%
- CAC: $120 (content + community + Shopify/Faire partnership)
- Monthly churn: 5%

**Tier 3 (Enterprise)**
- Average MRR per account: $5,500 (blended $66K ACV / 12)
- Month 3 accounts: 3 → Month 12: 25 → Month 18: 50 → Month 24: 85
- Gross margin: 58%
- CAC: $8,000 (founder/AE sales)
- Monthly churn: 2.5%

**Training Data Revenue** (starts Month 12, scales with task volume)

#### Monthly Revenue Projections

| Month | T1 Users | T1 MRR | T2 Accounts | T2 MRR | T3 Accounts | T3 MRR | Data Rev | Total MRR |
|-------|----------|--------|-------------|--------|-------------|--------|----------|-----------|
| 1 | 50 | $1,100 | 5 | $1,245 | 2 | $11,000 | — | **$13,345** |
| 2 | 150 | $3,300 | 12 | $2,988 | 3 | $16,500 | — | **$22,788** |
| 3 | 300 | $6,600 | 25 | $6,225 | 4 | $22,000 | — | **$34,825** |
| 4 | 500 | $11,000 | 40 | $9,960 | 5 | $27,500 | — | **$48,460** |
| 5 | 750 | $16,500 | 65 | $16,185 | 7 | $38,500 | — | **$71,185** |
| 6 | 1,100 | $24,200 | 100 | $24,900 | 9 | $49,500 | — | **$98,600** |
| 7 | 1,500 | $33,000 | 145 | $36,105 | 11 | $60,500 | — | **$129,605** |
| 8 | 2,000 | $44,000 | 195 | $48,555 | 14 | $77,000 | — | **$169,555** |
| 9 | 2,500 | $55,000 | 255 | $63,495 | 17 | $93,500 | — | **$211,995** |
| 10 | 3,000 | $66,000 | 310 | $77,190 | 20 | $110,000 | $8,000 | **$261,190** |
| 11 | 3,500 | $77,000 | 370 | $92,130 | 22 | $121,000 | $15,000 | **$305,130** |
| 12 | 4,000 | $88,000 | 430 | $107,070 | 25 | $137,500 | $22,000 | **$354,570** |

**Month 12 ARR Run Rate: $4.25M** (vs $3.0M in original enterprise-only model)

#### Month 13–24 Projections (Condensed)

| Month | T1 MRR | T2 MRR | T3 MRR | Data Rev | Total MRR |
|-------|--------|--------|--------|----------|-----------|
| 15 | $132,000 | $161,850 | $192,500 | $45,000 | **$531,350** |
| 18 | $220,000 | $242,100 | $275,000 | $85,000 | **$822,100** |
| 21 | $363,000 | $314,430 | $357,500 | $140,000 | **$1,174,930** |
| 24 | $550,000 | $398,800 | $467,500 | $210,000 | **$1,626,300** |

**Month 18 ARR Run Rate: $9.87M** — Series A trigger achieved ✓
**Month 24 ARR Run Rate: $19.5M** — Series B territory

---

### Consumer + SMB vs Enterprise-Only: Path to $1M ARR

**Enterprise-Only Path (original model)**:
- Requires 28 enterprise customers at $3K/month average
- Timeline: Month 10–12 (as modeled)
- Single point of failure: one enterprise customer loss = 3–4% revenue hit

**Three-Tier Path (new model)**:
- $1M ARR achieved through:
  - 2,500 consumer users × $22/month = $55,000/month T1
  - 200 SMB accounts × $249/month = $49,800/month T2
  - 15 enterprise accounts × $5,500/month = $82,500/month T3
  - Total: $187,300/month = **$2.25M ARR at Month 10**
- The three-tier model reaches $1M ARR faster AND with dramatically lower concentration risk

**Verdict**: The three-tier model is superior in every dimension: faster to $1M ARR, more diversified, lower average CAC, higher total LTV potential.

---

### Blended Unit Economics (New Model)

| Metric | Tier 1 | Tier 2 | Tier 3 | Blended |
|--------|--------|--------|--------|---------|
| Avg revenue/task | $10 | $14 | $22 | $14 |
| Agent payout/task | $4 | $5.60 | $8.80 | $5.60 |
| AI processing/task | $0.15 | $0.20 | $0.25 | $0.18 |
| Infrastructure/task | $0.30 | $0.40 | $0.50 | $0.36 |
| Payment processing | $0.60 | $0.71 | $0.94 | $0.70 |
| Gross profit/task | $4.95 | $7.09 | $11.51 | $7.16 |
| Gross margin | 50% | 51% | 52% | 51% |

Note: Per-task margins appear similar across tiers; the enterprise advantage is volume per account (fewer accounts, more tasks per account, lower sales overhead per dollar of revenue).

---

## Cycle 116: Pricing Architecture Finalization

### Consumer Task Prices by Type

| Task Type | Consumer Price | Agent Payout | Notes |
|-----------|---------------|--------------|-------|
| Crowd level check (1 video pan, 30 sec) | $5 | $2.00 | Highest frequency, gateway product |
| In-stock check (1 product, 1 store) | $8 | $3.20 | Single photo + AI stock flag |
| Exterior photo (1–3 shots) | $8 | $3.20 | Building/signage/parking exterior |
| Restaurant scout (5 photos + video) | $15 | $6.00 | Multi-angle interior/exterior |
| Neighborhood preview (6 photos, street tour) | $20 | $8.00 | For Airbnb/travel use case |
| Shelf check (1 product category, 1 aisle) | $15 | $6.00 | Consumer checking specific item |
| Property inspection (exterior, all 4 sides) | $20 | $8.00 | Homeowner/renter |
| Video task (60 sec, any location) | $18 | $7.20 | Events, venues, streets |

**Consumer credit pack effective rate**: $6.00–$7.50/task (vs standard $8–20 — creates incentive to pre-buy)

---

### SMB Subscription Tiers (Exact Pricing + Feature Gates)

| Feature | Spark ($49/mo) | Brand ($149/mo) | Growth ($349/mo) | Agency ($749/mo) |
|---------|---------------|-----------------|------------------|------------------|
| Monthly tasks included | 5 | 20 | 60 | 150 |
| Task rollover | No | 1 month | 2 months | 3 months |
| Add-on task price | $12 | $10 | $8 | $6.50 |
| Task types | Standard | Standard + Custom | All | All + Priority |
| AI extraction | Basic summary | Full JSON | Full + anomalies | Full + white-label |
| Fulfillment SLA | 48hr | 24hr | 12hr | 8hr |
| Dashboard | View-only | Full | Full + trends | Full + multi-client |
| Email delivery | Yes | Yes | Yes + Slack | Yes + Slack + webhooks |
| API access | No | No | Read-only | Full API |
| Sub-users | 1 | 2 | 3 | Unlimited |
| Annual discount | 15% | 15% | 20% | 20% |
| Onboarding support | Self-serve | Email | Email + 1 video call | Dedicated setup call |

**Annual pricing**:
- Spark Annual: $499/year (saves $89 vs monthly)
- Brand Annual: $1,519/year (saves $269)
- Growth Annual: $3,350/year (saves $838)
- Agency Annual: $7,190/year (saves $1,798)

---

### Enterprise Pricing (Per-Tier, Per-Task, Platform Fee)

**Structure**: Monthly platform fee (covers access, infrastructure, account management) + per-task fee for volume above included allotment.

| Tier | Platform Fee/Month | Tasks Included | Overage Per Task | Annual ACV |
|------|--------------------|---------------|-----------------|-----------|
| Business | $2,500 | 200 | $11.00 | $30,000 |
| Scale | $7,500 | 750 | $9.50 | $90,000 |
| Platform | $25,000 | 3,000 | $8.00 | $300,000 |
| Enterprise+ | $50,000+ | 10,000+ | $6.50 | $600,000+ |

**Annual prepay discount**: 15% off for 12-month commitment, 20% for 24-month.

**Professional services** (separate line items):
- Custom AI model training (customer's SKU set): $15,000 one-time + $1,500/month maintenance
- Salesforce integration setup: $5,000 one-time
- Snowflake data connector setup: $3,000 one-time
- Custom report template design: $2,500 one-time
- Quarterly business review (QBR) package: included from Scale tier, $2,000/quarter for Business tier

---

### Agent Payout Rates by Task Type

| Task Type | Consumer Price | Agent Payout | Agent % | Notes |
|-----------|---------------|--------------|---------|-------|
| Crowd level check | $5 | $2.00 | 40% | |
| In-stock check | $8 | $3.20 | 40% | |
| Exterior photo | $8 | $3.20 | 40% | |
| Shelf check (consumer) | $15 | $6.00 | 40% | |
| Shelf audit (enterprise, basic) | $12 | $4.80 | 40% | |
| Shelf audit (enterprise, full AI) | $25 | $10.00 | 40% | |
| Insurance inspection | $55 | $22.00 | 40% | |
| Construction monitoring | $75 | $30.00 | 40% | |
| Restaurant scout | $15 | $6.00 | 40% | |
| Neighborhood preview | $20 | $8.00 | 40% | |
| Video task (60 sec) | $18 | $7.20 | 40% | |
| Live stream (per minute) | $10 | $4.00 | 40% | |
| Premium inspection (thorough, multi-area) | $45 | $18.00 | 40% | |

**Note**: Agent payout is consistently 40% across all task types. The 40% is the stable commitment that drives agent trust and retention. The platform's margin advantage comes from AI extraction value, not from compressing agent pay.

---

### Surge Multipliers

**When Surge Applies**:
- Demand exceeds agent density: fulfillment probability <60% without surge
- Time-sensitive tasks: customer requests <4hr SLA
- Rare/difficult locations (rural, remote, industrial)
- CAT events (insurance surge deployment)
- Holiday/event periods (Black Friday retail monitoring surge)

**Surge Rates**:
| Surge Level | Multiplier | When | Who Pays |
|-------------|-----------|------|---------|
| Low surge | 1.25× | Agent density low, normal demand | Customer (optional "priority" tier) |
| Medium surge | 1.5× | High demand, limited supply | Customer (required for <4hr SLA) |
| High surge | 2.0× | Major event, peak demand | Customer + platform absorbs agent incentive |
| Emergency surge | 3.0× | CAT event, breaking news | Customer (pre-agreed in enterprise contract) |
| Crisis surge | 5.0× | Disaster response, extreme urgency | Pre-agreed contractual rate |

**Surge economics example** (Medium Surge, 1.5× on $25 task):
- Customer pays: $37.50 (1.5× $25)
- Agent earns: $18.00 (1.5× $12 base payout vs 40% of $37.50 = $15 — we give agent extra to incentivize)
- Platform earns: $19.50 (vs $15 baseline) — 18% margin boost

---

### Volume Discount Tiers

**For Enterprise (annual contract volume)**:
| Monthly Task Volume | Discount on Overage Rate |
|---------------------|--------------------------|
| 500–2,000 tasks/month | Standard rate |
| 2,001–5,000 tasks/month | 10% discount |
| 5,001–15,000 tasks/month | 20% discount |
| 15,001–50,000 tasks/month | 30% discount |
| 50,000+ tasks/month | Custom negotiated |

**For SMB (add-on tasks)**:
- Standard add-on: $10/task
- 50+ tasks in a single purchase: $8.50/task
- 100+ tasks in a single purchase: $7.50/task

**For Consumer (credit packs)**:
- Already factored into pack pricing above (larger packs = better per-task rate)
