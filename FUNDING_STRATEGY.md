# Mosaic — Funding Strategy
*Cycles 129–132: Lean AI-native team, pre-seed strategy, seed strategy, investor targeting*

---

## The Model: 2 Humans + AI Team

The central thesis: in 2026, a 2-person founding team equipped with the right AI stack can do the work of a 12-person team from 3 years ago. This is not a limitation — it's the story. Mosaic isn't just building an AI-native product. It's an AI-native company, and that's a structural advantage that compounds as AI gets better.

---

## Part 1: Two-Person Founding Team Design

### The Two Roles

**Role 1: CEO / Commercial Founder**

Owns: Revenue, GTM, investor relations, enterprise sales, partnerships, brand.

Profile: Has sold to CPG enterprise buyers OR has CPG brand management experience. Understands retail intelligence as a buyer. Has enough technical literacy to speak credibly about AI but doesn't need to write code. Network in CPG/retail/gig economy. Has raised capital before (or has strong warm intro network to investors).

Day-to-day Year 1: Closing the first 10 enterprise customers (calls, demos, pilots), raising pre-seed and seed capital, hiring first employees post-seed, managing AI agent teams.

**Role 2: CTO / Technical Founder**

Owns: Product, engineering, AI/ML, infrastructure, data pipeline, agent app.

Profile: Mobile engineering or full-stack background. Has shipped a consumer app before. Comfortable with computer vision fundamentals. Can direct AI coding agents (Cursor, Claude Code, Devin) at a senior level — knows what good output looks like, reviews PRs, debugs architecture decisions. Experience with AWS/GCP, geospatial APIs, real-time data pipelines.

Day-to-day Year 1: Building and shipping the MVP with AI coding agents, managing the AI-assisted development pipeline, making all architectural decisions, reviewing AI-generated code.

### Division of Responsibilities

| Function | Owner | How It's Done |
|----------|-------|---------------|
| Enterprise sales | CEO | Founder-led outreach; CEO conducts all demos and pilots |
| SMB/consumer product marketing | CEO + AI agents | AI drafts content; CEO approves strategy |
| Investor relations | CEO | CEO builds VC relationships; writes investor updates |
| Mobile app development | CTO + AI coding agents | Claude Code, Cursor, Devin write code; CTO reviews |
| Backend/API | CTO + AI coding agents | Same model |
| AI/ML pipeline | CTO + AI agents | CTO designs architecture; AI assists implementation |
| Legal/compliance | CEO manages, external counsel | GDPR, entity formation, contracts via Clerky/Stripe Atlas + privacy attorney retainer |
| Finance/accounting | CEO manages, tools | Pilot.ai for bookkeeping, Stripe for billing, fractional CFO |
| Design (UI/UX) | CTO + AI design tools | v0 for UI components, Figma AI, Midjourney for brand assets |
| Content/SEO | AI content agents | CEO sets strategy; Claude/GPT-4 drafts; CEO approves |
| Customer success | CTO for technical, CEO for business | Intercom AI chatbot first line; human escalation |
| Data analysis | AI analytics | Tableau AI, custom Python agents for task quality analysis |
| PR/communications | CEO manages, AI drafts | Claude drafts press releases; CEO approves and sends |
| HR (post-seed) | CEO + Rippling | Rippling handles payroll, benefits, onboarding |

---

## Part 2: AI Tool Stack + Monthly Burn Rate

### Pre-Seed AI Stack (2 Founders)

| Tool | Category | Monthly Cost | Notes |
|------|----------|-------------|-------|
| **Claude Code (Anthropic)** | AI coding agent | $100/founder = $200 | Primary coding assistant; code review, architecture |
| **Cursor Pro** | AI IDE | $40/founder = $80 | Real-time code completion, inline AI |
| **Devin (Cognition)** | Autonomous coding agent | $500 | For multi-step engineering tasks; ~50 ACUs/month |
| **v0 by Vercel** | AI UI generation | $20 | React component generation from prompts |
| **Midjourney** | AI image generation | $30 | Brand assets, pitch deck visuals |
| **Figma** | Design | $45 | UI design; AI-assisted with Figma AI |
| **Notion AI** | Knowledge management | $16 | Internal docs, product specs |
| **Linear** | Engineering project management | $8 | Issue tracking, sprint management |
| **Vercel Pro** | Hosting (web/API) | $20 | Fast deployment of Next.js frontend |
| **AWS (EC2/S3/Lambda)** | Cloud infrastructure | $500 | Backend API, S3 image storage, Lambda for AI pipeline |
| **Supabase Pro** | Database | $25 | PostgreSQL, Auth, Realtime |
| **Stripe** | Payments | 2.9% + $0.30 per txn | No monthly fee; variable |
| **Intercom** | Customer support | $39 | AI chatbot + human escalation |
| **Pilot.ai** | Bookkeeping | $599 | Automated bookkeeping, connects to Stripe |
| **Rippling** | HR/payroll (post-hire) | $8/employee | Needed at first hire |
| **Wise Business** | International payments | $0 | Agent payouts in GBP/EUR; no monthly fee |
| **1Password Teams** | Security | $19 | Credentials management |
| **Loom** | Video comms | $12.5/user = $25 | Async communication, customer demos |
| **Calendly** | Meeting scheduling | $10/user = $20 | VC meetings, customer demos |
| **Apollo.io** | Sales intelligence | $49 | CPG contact database for outbound sales |
| **HubSpot** | CRM | $0 (free tier) | Starter CRM for pipeline; upgrade at seed |
| **Google Workspace** | Email/docs | $12/user = $24 | Business email, Docs, Drive |
| **Expo (React Native)** | Mobile build | $99 | App build/publish infrastructure |
| **GitHub** | Code repo | $0 (free) | Public repos; private for $4/user |

**Total Monthly AI + Tools Burn: ~$2,400**

### Pre-Seed Full Monthly Burn Rate

| Category | Monthly | Notes |
|----------|---------|-------|
| 2 founder salaries | $20,000 | $10K each — survival wages, primarily equity-driven |
| AI + tools stack (above) | $2,400 | Full breakdown above |
| AWS + cloud infrastructure | $500 | Included in tools but isolated for visibility |
| Legal retainer (privacy attorney) | $2,000 | GDPR, BIPA avoidance, agent contractor agreements |
| Accounting/finance | $600 | Pilot.ai bookkeeping |
| Agent acquisition (first city test) | $3,000 | Facebook ads for first 100 agents |
| Conference/travel (1 event) | $1,500 | Expo West or similar CPG conference |
| Miscellaneous | $500 | Unexpected costs buffer |
| **Total Monthly Burn** | **$30,000** | |

**Annual burn at pre-seed**: ~$360,000
**Pre-seed raise of $400K**: ~13 months of runway
**Pre-seed raise of $500K**: ~16 months of runway — enough to reach seed metrics

**This is the number that makes VCs lean forward**: A $500K pre-seed gives 16 months of runway for a 2-person AI-native team. Most companies burn $500K in 3 months with a 6-person team. Mosaic's burn rate is a proof point, not a vulnerability.

---

## Part 3: Hiring Roadmap

### Pre-Seed (Month 0–16): 2 Founders Only

No hires. AI tools handle every function. Founders focus exclusively on: (1) building MVP with AI coding agents, (2) closing first 5 enterprise customers, (3) recruiting 500+ agents in first city, (4) raising seed round.

**What doesn't happen at pre-seed**:
- No AEs (CEO sells)
- No designers (v0 + Figma AI + CTO)
- No DevOps (Vercel + AWS managed services)
- No customer success (Intercom AI + founders respond to escalations)
- No marketing hires (AI content + founder LinkedIn)

### Seed (Month 16–30): Hire to Revenue

With $5M seed, first 6 months of hiring:

| Month | Hire | Why Now |
|-------|------|---------|
| Month 16 | Head of Engineering ($160K) | CTO needs to stop writing code and start managing AI coding agents at scale |
| Month 18 | Account Executive #1 ($120K OTE) | CEO can't close 20+ deals alone; sales starts compounding |
| Month 20 | ML Engineer ($150K) | AI model quality becomes the moat; requires specialist oversight |
| Month 22 | Head of Marketing ($130K) | Scale SMB/consumer acquisition; content strategy |
| Month 24 | Account Executive #2 ($120K OTE) | Scale enterprise pipeline |
| Month 26 | Customer Success Manager ($90K) | Enterprise churn prevention; expansion revenue |
| Month 28 | Data Engineer ($140K) | Training data pipeline; AI flywheel monetization |
| Month 30 | Operations Manager ($100K) | City launches, agent quality, operational complexity |

**Month 30 team size**: 10 people (2 founders + 8 hires). Burn rate: ~$200K/month. Revenue: $500K+ MRR.

### Series A (Month 30+): Scale to 30 People

With $10M Series A:
- Engineering: +4 engineers, +1 mobile specialist
- Sales: +4 AEs, +2 Sales Engineers
- Marketing: +2 content/demand gen
- Operations: +3 city managers
- CS: +2 CSMs

---

## Part 4: Pre-Seed Strategy ($250K–$500K)

### What Pre-Seed Capital Buys

| Use of Funds | Amount | What It Accomplishes |
|-------------|--------|---------------------|
| Legal entity formation + IP assignment | $5,000 | Delaware C-Corp via Stripe Atlas ($500) + attorney review ($4,500) |
| GDPR/legal compliance foundation | $15,000 | Privacy attorney to draft GDPR documentation, agent contractor agreements, customer DPAs |
| AWS infrastructure (12 months) | $6,000 | Backend API, database, storage; scalable from 0 to first 1,000 tasks |
| First city agent acquisition | $15,000 | Facebook/Instagram ads → 500 verified agents in Atlanta + London |
| Conference (Expo West) | $5,000 | Registration, travel, materials — first enterprise leads |
| AI tool stack (12 months) | $29,000 | Full stack above × 12 months |
| Founder salaries (12 months) | $240,000 | $10K/month × 2 founders × 12 months |
| Buffer/unexpected | $25,000 | |
| **Total** | **$340,000** | (~$400K raise with 15% buffer) |

### Sources of Pre-Seed Capital

**Option A: Angel round (best for speed)**
- 3–5 angels at $50–100K each
- Ideal angels: CPG industry operators, ex-founders who've sold in adjacent spaces, marketplace operators (ex-DoorDash/Uber executives), data company founders
- Instrument: SAFE with a $8–10M cap, 20% discount
- Timeline: 4–8 weeks to close

**Option B: Pre-seed fund**
- Firms that write $150–500K checks at pre-seed with minimal product required:
  - **Precursor Ventures** (Charles Hudson): $250K–500K, pre-product fine, marketplace experience (Just Eat in portfolio)
  - **Hustle Fund** (Elizabeth Yin): Small checks, fast decisions, supports solo/duo teams
  - **Backstage Capital** (Arlan Hamilton): Underrepresented founders, small checks
  - **Operator Partners** (Sean Griffin): Pre-seed, operator-angels, very founder-friendly
- Timeline: 6–12 weeks (slower than angels due to process)

**Option C: Accelerator (best for network, slowest)**
- **Y Combinator**: $500K for 7% equity. The gold standard. Takes 2 application cycles to get in. Massive network value.
- **Techstars**: $120K for 6% equity. City-specific, strong corporate partnership network (could be valuable for CPG sales).
- **EF (Entrepreneur First)**: For pre-co-founder stage; helps find co-founders. Not applicable if both founders are already in place.
- Timeline: YC next batch starts in January and July; 3–4 months before capital arrives

**Option D: Founder personal capital**
- If founders have savings or prior startup income: self-fund the first 3–6 months to prove concept before raising
- Reduces dilution; increases leverage in pre-seed negotiations
- Risk: bootstrapping a two-sided marketplace is genuinely hard — agent acquisition requires real marketing spend

**Recommended approach**: Self-fund first 60 days to build MVP prototype, then raise a $400K angel SAFE from 3–4 operators/angels who have CPG or marketplace experience. This gives the fastest runway with the most valuable advisors.

---

### What You Need to Show for Pre-Seed

Pre-seed at $250K–$500K requires almost nothing in terms of revenue. What investors are betting on:

1. **Team**: Two credible founders. Combined: (a) CPG/enterprise sales experience OR gig platform experience AND (b) technical mobile/AI capability. No single founder can fake both.
2. **Insight**: A sharp, defensible explanation of why BeMyEye/Field Agent have left a gap and why the three-tier model + location-aware design wins.
3. **MVP or mockup**: Working prototype of agent app OR functional web app where customers can post tasks. Not shipped — working enough to demo.
4. **Early signal**: One LOI from a potential customer. One conversation with a CPG brand manager who said "this solves my problem." 200 people on an agent waitlist. Any signal at all that the market exists and wants what you're building.
5. **Pre-seed valuation**: SAFE at $8–12M cap is appropriate. On $400K raise at $10M cap → ~4% dilution.

**Realistic timeline from idea to pre-seed close**: 3–4 months if you have the team and move fast. 6 months if you need to find a co-founder or do additional market validation.

---

## Part 5: Seed Strategy ($5–10M)

### What You Need to Show for a Large Seed

Large seeds ($5–10M) are available when the following are true:

| Metric | Threshold for $5M Seed | Threshold for $10M Seed |
|--------|------------------------|-------------------------|
| ARR | $150–300K | $500K–1M |
| Growth rate | 20% MoM | 25% MoM |
| Agent count | 500+ active | 2,000+ active |
| Fulfillment rate | 75%+ | 85%+ |
| Enterprise customers | 3–5 (with pilots active) | 8–12 (with contracts) |
| Cities | 2 | 3–4 |
| NRR | 110%+ | 115%+ |
| Team | 2 founders, 1 engineer | 2 founders, 2–3 engineers |

**Mosaic's projected timeline**: Pre-seed closes Month 0 → first agents Month 1 → first enterprise pilots Month 2 → $100K ARR Month 5 → first enterprise contract Month 6 → **raise $5M seed at Month 8–10** → use seed to hire, scale to 4 cities → raise $10M seed or Series A at Month 18 with $1M ARR run rate.

---

### Seed Use of Funds ($5M)

| Use of Funds | Amount | Months |
|-------------|--------|--------|
| Engineering team (3 hires) | $1.5M | 18 months salary |
| ML/AI model development | $500K | Training data, model improvements, ML engineer |
| Agent acquisition (4 cities) | $1M | $250K/city × 4 cities |
| Enterprise sales (1 AE + CEO) | $500K | AE salary + commissions + conferences |
| Marketing (SMB/consumer) | $500K | Content, paid acquisition, partnerships |
| Legal/compliance (GDPR, SOC 2) | $300K | Privacy attorney, ISO 27001 or SOC 2 Type I |
| Operations (city launches) | $400K | City captains, ambassador programs |
| Buffer/runway | $300K | |
| **Total** | **$5M** | 18 months runway |

### Target Seed Investors — Specific Funds and Partners

| Fund | Partner | Stage/Check | Why Mosaic Fits | Intro Path |
|------|---------|-------------|-----------------|-----------|
| **a16z (Consumer)** | Andrew Chen | $1–5M | Andrew literally wrote the book on network effects, marketplaces, and gig economy. Portfolio: Airbnb, Lyft, Hipcamp. | Through a portfolio founder (Hipcamp CEO) or AngelList mutual connections |
| **NFX** | Pete Flint, James Currier | $500K–3M | Deep marketplace thesis ("network effects bible"), backed DoorDash, Lyft, Wolt. Pete Flint is ex-Trulia (real estate data). | NFX Signal platform; they have a self-serve intro form; or through DoorDash alumni |
| **Spark Capital** | Megan Quinn, Natalie Sandman | $1–5M | Consumer + marketplace; portfolio includes Twitter, Slack, Wayfair, Arc'teryx. | Through existing portfolio CEOs |
| **Bessemer** | Byron Deeter, Elliott Robinson | $1–5M | Enterprise SaaS + marketplace; strong enterprise go-to-market thesis; AI-native company thesis (published). | BVP Atlas blog community; Bessemer has an open application form |
| **General Catalyst** | Kyle Doherty | $1–5M | Invests across enterprise/consumer; portfolio includes Stripe, Airbnb, Snap. | Warm intro through YC or EF network |
| **USV (Union Square Ventures)** | Albert Wenger, Rebecca Kaden | $500K–2M | Marketplace theory from Fred Wilson era; data network effects thesis. | Through AngelList, Substack connections |
| **Homebrew** | Hunter Walk, Satya Patel | $500K–1M | Consumer + marketplace, pre-seed/seed, very founder-friendly, strong gig economy thesis. | Cold outreach works; Hunter Walk is responsive on Twitter/X |
| **Haystack** | Semil Shah | $500K–2M | 117+ seed investments, averaging $2.24M, very data-forward. Portfolio: Instacart, DoorDash, HashiCorp. | LinkedIn outreach; Semil Shah is active on social media |
| **Precursor Ventures** | Charles Hudson | $250K–1M | Pre-seed/seed specialist; backed gig and marketplace companies; very accessible. | Cold email works per public guidance |
| **Kleiner Perkins** | Ilya Fushman | $1–5M | Strong marketplace portfolio; former Index Ventures partner; DoorDash, Figma. | Through YC or Techstars network |
| **Founders Fund** | Keith Rabois | $1–10M | Physical world + AI thesis; Opendoor, Square, PayPal. Keith specifically writes about crowdsourced data. | Through PayPal mafia connections or Patrick Collison intro |
| **Sequoia** | Shaun Maguire | $1–5M | Seed + A; strong AI and consumer thesis; AirBnb, Uber at seed. Mosaic's trajectory exactly matches Sequoia seed profile. | Through YC (Sequoia scouts all YC batches); or through portfolio CEOs |
| **Accel** | Ryan Sweeney (US) / Luciana Lixandru (EU) | $1–5M | Strong EU+US presence (critical for Mosaic's dual-market strategy). Portfolio: Deliveroo, Fiverr, Etsy. | Accel EU office in London — direct cold outreach; or through Deliveroo alumni |
| **Index Ventures** | Jan Hammer | £500K–3M | European HQ (London); portfolio includes Deliveroo, Robinhood, Figma. Perfect for EU-first story. | London office — cold outreach; or through Deliveroo/Farfetch alumni |
| **LocalGlobe** | Saul Klein, Robin Klein | £250K–1.5M | London-based seed fund, champions European startups. Portfolio includes Transferwise, Zoopla. | Direct outreach via email or London startup community |

---

### Seed Valuation

**$5M seed on $20–30M pre-money**: Standard for a team with $150–300K ARR, strong growth trajectory, two credible founders. Precedent: gig economy and marketplace seed rounds in 2025 closed at $15–35M pre-money.

**$10M seed on $35–50M pre-money**: Requires $500K+ ARR, proven multi-city model, clear path to Series A metrics.

**How to justify valuation**:
- Revenue multiple: $300K ARR × 100x = $30M pre-money (software ARR multiples at seed stage commonly 80–120x)
- Comparables: BeMyEye's implied valuation at $35M revenue is $70–100M (3–4x revenue). Mosaic with faster growth trajectory, better product, AI advantage deserves a premium over BeMyEye's early-stage equivalent
- Team quality: Each year of relevant experience adds $1–2M to pre-money in VC mental models. Two seasoned founders with deep domain experience supports $20M+ pre-money

---

## Part 6: The AI-Native Startup Narrative

### The Pitch to VCs

> "We built this entire company — from concept to first 10 enterprise customers — with 2 people and AI agents. Here's what that means for your investment:
>
> Our burn rate is $30K/month — not $120K. That means your $5M seed gives us 14 months of runway instead of 4. Every month we're not burning cash is a month we're building data moat and tightening product-market fit.
>
> Our development velocity is 4× a traditional team. Claude Code, Cursor, and Devin let 2 engineers ship what took 8 engineers two years ago. We've shipped the agent app, the customer portal, the AI extraction pipeline, and the route-matching algorithm in 8 weeks.
>
> Our cost structure means our unit economics work from Day 1. We don't need 50 enterprise contracts to cover a $200K/month burn. We need 10 customers at $3K/month to cover our costs. That changes the risk profile of this investment fundamentally.
>
> The AI team isn't a weakness. It's the moat. The faster AI agents get, the cheaper and faster we build. Every improvement in Claude or GPT-5 makes us faster, not slower. We're not a company that will eventually hire people when we get big enough — we're a company that scales by deploying better AI agents. Our headcount will grow 3× while our team grows 10×."

### Proof Points That Demonstrate the Narrative

1. **Concrete burn rate**: Share the actual monthly burn figure ($30K) vs industry average for comparable stage ($120–200K). The contrast is dramatic.
2. **Build velocity**: "We shipped our MVP in 6 weeks with 2 people and AI coding agents. Time to 1,000 lines of tested, production-ready code: 3 days." Show the GitHub commit history.
3. **Tool stack transparency**: Share the actual AI tool list and costs. VCs love specificity. A $2,400/month AI stack replacing $80,000/month in salaries is a compelling narrative.
4. **Quality metrics**: "95% of our agent app code was AI-generated; our CTO reviewed every PR. Crash rate: <0.1%. App Store rating: 4.6 stars. AI can write production code at senior engineer quality when supervised correctly."
5. **Speed of iteration**: "We shipped 14 features in our first 8 weeks. Our closest competitor (BeMyEye) last shipped a major feature 4 months ago."

### VCs Who Are Explicitly Excited About AI-Native Teams

- **Andrew Chen (a16z)**: Has written about "Zero to One with AI Agents" — specifically discusses small teams + AI reaching significant scale
- **Elad Gil** (Angel investor): His book "High Growth Handbook" is now being updated to discuss AI-native team structures; he invests based on founder quality, not team size
- **Nat Friedman / Daniel Gross**: Running AI Grant (AI-focused angel program); explicitly fund AI-native companies
- **YC (2025 batch)**: YC's current application explicitly asks "How are you using AI in your development process?" — signal that AI-native teams get preferential attention
- **Bessemer Venture Partners**: Published "State of AI 2025" report emphasizing AI-native company formation as a key investment theme — explicitly says small teams with AI can now build what previously required Series B companies

---

## Part 7: Bridge Round Strategy

**The bridge question**: Pre-seed closes at $400K (Month 0). You're raising seed at Month 8. What if the raise takes longer?

**Pre-empt the bridge**:
- Set pre-seed use of funds to last 16 months at $30K/month burn = $480K needed → raise $500K, not $400K
- Begin seed investor outreach at Month 6 (not Month 10) — this gives 4 months to close
- Use monthly investor updates from Month 1 to warm investors before the formal raise begins (see IR Playbook)

**If you need a bridge**:
- Existing pre-seed angels extending for $100–200K SAFE at same cap
- Revenue-based financing on existing enterprise contracts (Capchase or Pipe advance on annual prepays)
- Convertible note with 20% discount and 60-day maturity → bridge to seed close

**Avoid**: A bridge round signals that the primary raise didn't meet expectations. It's not fatal, but it adds noise. The best bridge is not needing one.
