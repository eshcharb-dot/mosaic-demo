# Mosaic — Business Model (V2)
*Three-tier architecture: Consumer / SMB / Enterprise*

---

## Architecture Overview

Mosaic operates a three-tier marketplace addressing the full demand spectrum — from an individual who wants one restaurant photo to a Fortune 500 CPG company monitoring 50,000 stores.

The Uber parallel is instructive: Uber didn't build just corporate accounts. The consumer app is what created scale, virality, agent density, and ultimately the enterprise value. Mosaic's three-tier model applies the same logic to physical world intelligence.

---

## Tier 1: Consumer / Hobbyist

**Model**: Credit wallet. Pay-per-task. No commitment. No account required for first task.

**Who**: Individual consumers with specific, one-time questions about physical places.

**Task Types and Pricing**:

| Task | Consumer Price | Agent Payout | Platform GM |
|------|---------------|--------------|-------------|
| Crowd level check (30-sec video pan) | $5 | $2.00 | 52% |
| In-stock check (1 product, 1 store) | $8 | $3.20 | 52% |
| Exterior photo (1–3 shots) | $8 | $3.20 | 52% |
| Restaurant scout (5 photos + video) | $15 | $6.00 | 52% |
| Neighborhood preview (6 photos + video) | $20 | $8.00 | 52% |
| Shelf check (1 aisle, consumer) | $15 | $6.00 | 52% |
| Property exterior documentation | $20 | $8.00 | 52% |
| Video task (60 seconds) | $18 | $7.20 | 52% |

**Credit Pack Pricing**:

| Pack | Price | Tasks | Effective Rate |
|------|-------|-------|---------------|
| Starter | $15 | 3 | $5.00 |
| Explorer | $35 | 5 | $7.00 |
| Local | $75 | 10 | $7.50 |
| Adventurer | $150 | 25 | $6.00 |

Credits never expire. Annual equivalent: $180 (Explorer user, ~5 tasks/month).

**Freemium Entry**:
- First 3 tasks free (new users), limited to crowd level / exterior types
- Results delayed 24 hours + partial AI output (upgrade to see full analysis)
- Conversion target: 25% → paid within 14 days

---

## Tier 2: SMB / Self-Serve

**Model**: Monthly subscription with task allotment. Credit card only. No sales call. Self-serve checkout in <5 minutes.

**Who**: Small brand owners (50–2,000 store distribution), local restaurant and retail chains, independent real estate agencies, event companies, journalists.

**Plans**:

| Plan | Price/Month | Tasks | Overage | API | AI Output | SLA | Annual Price |
|------|------------|-------|---------|-----|-----------|-----|-------------|
| Spark | $49 | 5 | $12/each | No | Summary | 48hr | $499 |
| Brand | $149 | 20 | $10/each | No | Full JSON | 24hr | $1,519 |
| Growth | $349 | 60 | $8/each | Read | Full + Alerts | 12hr | $3,350 |
| Agency | $749 | 150 | $6.50/each | Full | Full + White-label | 8hr | $7,190 |

**Feature gates**:
- Recurring task scheduling: Growth+
- Slack webhook integration: Growth+
- API access: Growth (read-only), Agency (full)
- White-label PDF exports: Agency
- Sub-user seats: 1 (Spark), 2 (Brand), 3 (Growth), Unlimited (Agency)

**Gross Margin**: 62% (lower infrastructure % at volume, zero sales overhead)

---

## Tier 3: Enterprise

**Model**: Annual contracts, custom SLAs, dedicated CSM. Payment by invoice (NET 30/60).

**Who**: CPG brands ($100M–$5B), P&C insurers, national retailers, franchise operators, government.

**Plans**:

| Plan | Monthly Price | Tasks | ACV | Features |
|------|--------------|-------|-----|---------|
| Business | $2,500 | 200 | $30,000 | SOC 2, 5 users, email + Slack |
| Scale | $7,500 | 750 | $90,000 | + Salesforce, dedicated CSM, 10 users |
| Platform | $25,000 | 3,000 | $300,000 | + Custom AI, webhooks, unlimited users, 4hr SLA |
| Enterprise+ | $50,000+ | 10,000+ | $600,000+ | + Co-branded output, 2hr SLA, QBRs |

**Overage rates by tier**: Business $11/task, Scale $9.50/task, Platform $8/task, Enterprise+ $6.50/task

**Professional services**:
- Custom AI model training (customer's SKU set): $15,000 one-time + $1,500/month
- Salesforce integration setup: $5,000
- Snowflake connector: $3,000
- QBR package (Business tier): $2,000/quarter

---

## Agent Earnings Model

### Core Principle
Agent payout is consistently **40% of customer-facing task price** across all tiers. This is the stable, trusted rate that drives agent acquisition and retention.

### Payout Rates by Task Type

| Task Type | Consumer Price | Agent Payout | Notes |
|-----------|---------------|--------------|-------|
| Crowd check | $5 | $2.00 | |
| Stock check / exterior | $8 | $3.20 | |
| Shelf check / restaurant scout | $15 | $6.00 | |
| Neighborhood preview / video | $20 | $8.00 | |
| Enterprise shelf audit (full AI) | $25 | $10.00 | |
| Insurance inspection | $55 | $22.00 | |
| Construction weekly | $75 | $30.00 | |
| Live stream (per minute) | $10 | $4.00 | |

### Surge Multipliers (Agent Payout × Surge Rate)

| Level | Multiplier | Trigger |
|-------|-----------|---------|
| Low | 1.25× | Agent density moderate-low |
| Medium | 1.5× | High demand, <4hr SLA requested |
| High | 2.0× | Peak event, major demand spike |
| Emergency | 3.0× | CAT event, breaking news |
| Crisis | 5.0× | Disaster response |

### Bonus Structure

| Bonus | Amount | Trigger |
|-------|--------|---------|
| Quality bonus | +20% per task | Score ≥ 4.8/5.0 |
| Streak bonus | +10% | 7+ consecutive active days |
| Referral bonus | $25 cash | Per referred agent completing 10+ tasks |
| Mentor bonus | 0.5% of referree earnings | For 90 days after referral joins |
| Welcome bonus | $15 | First task completed |
| Milestone | $50/$250/$1,000 | At 50/500/2,000 tasks |

### Level System

| Level | Tasks | Benefits |
|-------|-------|---------|
| Rookie | 0–100 | Standard rates |
| Scout | 101–500 | +5% base rate, priority task access |
| Expert | 501–2,000 | +10% base rate, early surge notifications |
| Elite | 2,001+ | +15% base rate, auto-approval, dedicated support |

### Payout
- Minimum: $10
- Methods: PayPal, ACH/SEPA, Hyperwallet (200+ countries)
- Speed: Instant available (1% fee), standard weekly
- Tax: Automatic 1099 for US agents >$600/year

---

## Unit Economics (Per Task)

### Early Stage (Blended Tier Mix, Month 12)

| Line Item | Amount |
|-----------|--------|
| Customer revenue (blended across tiers) | $14.00 |
| Agent payout (40%) | $(5.60) |
| AI processing | $(0.18) |
| Payment processing (~2.9% + $0.30) | $(0.71) |
| Platform infrastructure | $(0.36) |
| **Gross Profit per Task** | **$7.15** |
| **Gross Margin** | **51%** |

### At Scale (Month 24, 500K+ tasks/month)

| Improvement Driver | Impact |
|-------------------|--------|
| AI inference cost reduction (volume) | -$0.08/task |
| Infrastructure cost spreading | -$0.15/task |
| Payment processing optimization | -$0.10/task |
| **Projected Gross Margin** | **61%** |

---

## Revenue Mix Evolution

| Revenue Stream | Month 12 | Month 18 | Month 24 |
|---------------|----------|----------|----------|
| Tier 1 Consumer | 25% | 27% | 34% |
| Tier 2 SMB | 30% | 29% | 24% |
| Tier 3 Enterprise | 39% | 33% | 29% |
| AI Training Data | 6% | 10% | 13% |

**Key shift**: Consumer tier grows fastest due to virality and very low CAC. Training data grows consistently as task volume scales. Enterprise share declines as % but grows in absolute terms.

---

## Consumer + SMB Acquisition — Viral Growth Loops

### The Five Growth Loops

**Loop 1 — Task Result = Share Card**
Brand owner receives shelf audit → "Brand Pulse" share card generated → posts to Instagram/LinkedIn → peers who are also brand owners discover Mosaic → sign up.

**Loop 2 — Agent Earnings Card**
Agent earns $73 in 2.5 hours → one-tap earnings card post → friends see "I just made $73 exploring my city" → new agent sign-ups. k-factor target: 0.5+

**Loop 3 — Surprise and Delight**
Consumer scouts restaurant, agent goes slightly beyond instructions with a helpful detail → consumer posts "I sent a spy to scout my date night restaurant" → organic viral moment.

**Loop 4 — Referral Program**
Customer: +$30 credit per referral. Agent: $25 cash + 0.5% of referree earnings for 90 days.

**Loop 5 — PLG (Product-Led Growth)**
3 free tasks → delayed/partial results → "upgrade for full analysis" → 25% conversion to paid within 14 days.

### SMB Acquisition Channels

| Channel | Target | CAC | Notes |
|---------|--------|-----|-------|
| Shopify App Store | DTC brands selling retail | $80 | "Shelf Intelligence" plugin |
| Faire Wholesale | Small brand wholesale distributors | $120 | In-platform ads + 20% rev share |
| LinkedIn brand communities | Brand managers, DTC founders | $150 | Content marketing |
| TikTok (brand owner community) | Indie brand owners | $40 | "Reality Check" viral content |
| Google Ads | "shelf audit software" keyword | $200 | High intent |
| Affiliate / partner referrals | Agency partners | $60 | Agency tier incentivizes referrals |

### Consumer Acquisition Channels

| Channel | Target | CAC | Notes |
|---------|--------|-----|-------|
| App store organic | Gig workers | $5 | Viral reviews |
| Agent earnings TikTok | Gig workers | $12 | Earnings screenshot content |
| Facebook/IG ads | Gig workers, consumers | $20 | "Earn while walking" |
| Campus ambassadors | Students | $15 | Existing program, now also consumer-facing |
| Commuter transit ads | Urban workers | $25 | "Earn on your commute" |
| Parent community content | Parents checking parks/stores | $18 | Facebook groups |

---

## Freemium Strategy (Revised)

**Previous decision**: No free tier (wrong for consumer/SMB layer)
**Revised**: Free tier exists for Tier 1 only; never for enterprise

**Free tier**:
- 3 tasks (crowd level or exterior only)
- Results delayed 24 hours
- Partial AI output (full output requires payment)
- Conversion target: 25% to paid within 14 days
- Enterprise landing pages: zero free tier references (protect enterprise positioning)

**$49 Spark plan** serves the same "low-friction entry" role for SMB that the $500 Starter Pack serves for enterprise.

---

## Data Moat + Flywheel

```
More customers (3 tiers) → more tasks across diverse use cases
     ↓
More agent completions → richer, more diverse training data
     ↓
Better AI models → higher accuracy → more use cases unlocked
     ↓
Higher value delivered → more pricing power + more customers
     ↓
Consumer tier creates viral acquisition → more customers with zero CAC
     ↓
Agent supply grows with task demand → better fulfillment
     ↓
Better fulfillment → more enterprise contracts
     ↓ [cycle repeats]
```

The three-tier model accelerates the flywheel: consumer tasks create agent base load, which improves fulfillment, which enables enterprise SLAs, which funds growth investment back into consumer virality.

---

## Competitive Pricing Benchmarks

| Alternative | Cost | Speed | Format | Self-Serve |
|-------------|------|-------|--------|-----------|
| Mystery shopping agency | $50–$300/visit | 2–3 weeks | PDF report | No |
| Field Agent | $30–$175/task | 1–7 days | Raw photos | Partial |
| Placer.ai (foot traffic) | $12,000–$60,000/year | Historical only | Dashboard | No |
| Trax retail CV | $30–$80/store/visit equiv | Near-real-time | Structured | No (hardware) |
| Manual field rep | $100–$200/visit equiv | 1–2 weeks | Spreadsheet | No |
| **Mosaic (Tier 1)** | **$5–$20/task** | **2–48 hours** | **AI-extracted + photos** | **Yes — 90 sec** |
| **Mosaic (Tier 2 SMB)** | **$49–$749/month** | **8–24 hours** | **Full AI JSON** | **Yes — self-serve** |
| **Mosaic (Tier 3 Enterprise)** | **$2,500–$50K/month** | **2–48 hours** | **Custom AI + integrations** | **No — AE sales** |

Mosaic is the only option that is: (1) on-demand, (2) AI-extracted, (3) verified, AND (4) accessible without a sales call.
