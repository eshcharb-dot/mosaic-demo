# Mosaic — Pitch Deck V2
*Cycles 136–138: Best-in-class 13-slide deck, every word, every number, all design notes*

---

## Deck Architecture Notes

This deck follows the NFX/Sequoia/YC hybrid format that has produced the highest conversion rates for marketplace + AI companies at seed stage. The narrative arc is: Pain → Insight → Why Now → Product → Market → Model → Traction → GTM → Competition → Team → Money.

**Design system**: Dark background (#0F0F0F), accent gradients from deep purple (#7B2FF7) to electric blue (#00D4FF), clean sans-serif (Inter), data visualized in accent colors. Every chart is built for the projector — no tiny text, max 3 data points per chart.

**Tone**: Confident without being arrogant. We know exactly what we're building and why it wins. No hedging. No "we believe" or "we hope" — use present tense and future tense declaratively.

---

## Slide 1: Cover

**Headline**: MOSAIC

**Body**:
```
Ground truth at scale.

Physical world intelligence — on demand, AI-extracted, instantly.

[Founder Name] [Founder Name]
[Email] | mosaic-intel.com

Confidential | March 2026
```

**Narrative note**: Say nothing during this slide — let it breathe for 3 seconds. Then: "Every day, millions of decisions are made based on data that's weeks old, survey-based, or simply doesn't exist. Mosaic fixes that."

**Design note**: Full-bleed dark background. "MOSAIC" in large gradient text (purple → blue). A subtle mosaic tile pattern in the background at 5% opacity. Clean, premium, confident. No clip art, no stock photos of people in offices.

---

## Slide 2: The Problem

**Headline**: The physical world is opaque — and everyone pays for it

**Body**:
```
CPG BRANDS                         RETAILERS                      CONSUMERS
Lost 4–8% of revenue               Can't verify compliance         Can't trust
to out-of-stocks they              without 2-week delay            secondhand info
never knew about                   and $200/visit

         THE CORE PROBLEM

The physical world generates zero data
unless someone deliberately captures it.

Field checks cost $50–$300 per visit.
Take 2–3 weeks to complete.
Cover <5% of locations.
Deliver no machine-readable output.

$35B is spent on physical world intelligence per year.
Most of it produces data that's already outdated when it arrives.
```

**Narrative note**: "A brand manager at [CPG brand] told me something that stuck: 'I have 50,000 stores in our distribution network. My team visits 2,400 of them per year. For 95% of my stores, I have no idea what my shelf looks like right now.' That's the problem. And it's universal — from Fortune 500 CPG companies to a parent trying to check if the park is crowded before loading up the car."

**Design note**: Three columns with bold CPG | Retailers | Consumers headers. Below them, a single strong stat in large white text. Then a central block with the "CORE PROBLEM" text on a slightly lighter dark background card. Stats should be visually emphasized — big font.

---

## Slide 3: The Solution

**Headline**: Mosaic turns any smartphone into a verified data collection device

**Body**:
```
ENTERPRISE posts a task
"Check oat milk shelf compliance at 50 London Tesco stores"
         ↓
MOSAIC routes task to 12 agents
already near those stores during their morning commutes
         ↓
AGENTS capture verified photos and video
On-device AI: face redaction + quality validation before upload
         ↓
AI EXTRACTION delivers structured output
JSON data, compliance scores, anomaly flags — within 4 hours
         ↓
ENTERPRISE gets actionable intelligence
"6 stores: out-of-stock. 3 stores: wrong placement. 41 stores: compliant."

Consumer posts in 90 seconds. Enterprise integrates via API.
Everyone gets ground truth — faster and cheaper than anything else.
```

**Narrative note**: "The insight is simple: 50 million people in the gig economy are already going to the places we need data from. A commuter walks past a Sainsbury's every morning. A parent is already at the park. We just give them a way to earn $3 for 45 seconds of capture they're already positioned to do. And our AI turns those photos into structured business intelligence within hours, not weeks."

**Design note**: Vertical flow diagram with 5 steps, alternating left-right placement, connected by a gradient line. Each step has an icon (simple line icons). The final step has a mock "report card" showing the compliance summary. This is the "aha" visual — the whole product in one picture.

---

## Slide 4: Why Now

**Headline**: Three forces converged in 2026 that make Mosaic possible — and defensible

**Body**:
```
1. ON-DEVICE AI
MediaPipe + TFLite run face redaction in real-time on any 2020+ smartphone.
GDPR compliance without cloud roundtrip. No biometric data ever leaves the device.
This wasn't possible before 2024.

2. GIG ECONOMY MATURITY
50M+ gig workers globally. 43M in Europe alone.
They're comfortable completing smartphone micro-tasks for micro-pay.
Deliveroo, Uber, DoorDash trained the supply side.
We harvest the agent infrastructure they built.

3. AI EXTRACTION QUALITY
GPT-4V class models now extract structured data from photos with >90% accuracy.
A shelf photo becomes JSON data in 3 seconds.
What required a trained human analyst now requires $0.20 of API compute.

These three forces create a window:
The US gig platforms haven't noticed Europe.
The European competitor (BeMyEye) has no consumer tier.
The enterprise AI buyers are ready — they signed up for AI tools faster in 2025 than any year prior.
```

**Narrative note**: "Each of these trends individually has been discussed for years. What hasn't been discussed is that they all came together in 2025 in a way that makes our specific model not just possible but defensible. The on-device AI is the key — it's what makes us GDPR-native instead of GDPR-constrained, and it's something our competitors can't retrofit easily."

**Design note**: Three large numbered cards, side by side, each with a trend icon and brief explanation. Below them, a single statement: "These three forces create a 24-month window before the major platforms notice." Design this as a visual "three pillars" diagram.

---

## Slide 5: Product

**Headline**: The product your agents love to use and your customers can't stop checking

**Body**:
```
[CUSTOMER SIDE — LEFT PANEL]
"Post a task in 90 seconds"

1. Enter location + task type
2. Select 24hr or 4hr delivery
3. Pay by credit card
4. Receive AI-extracted JSON report

Task types: Shelf audit | Crowd check | Stock verification |
Brand compliance | Competitive pricing | Site inspection

[AGENT SIDE — RIGHT PANEL]
"Earn $15 on your morning commute"

1. Turn on Commute Mode before leaving home
2. Pre-accept 3 tasks along your route
3. Complete each task in 45–90 seconds
4. Earn £14.50 before arriving at work

Commute Mode: tasks matched to route, not just radius
Pre-acceptance: commit before you leave, earn on the way

[BOTTOM — MAGIC NUMBERS]
90 seconds    4 hours     45 seconds     £14.50
to post       to deliver  per task       per commute
```

**Narrative note**: "The product has two sides. On the customer side, it's simpler than posting a job on LinkedIn. On the agent side, it's the first gig platform that works *with* their existing life instead of requiring them to restructure it. The commute mode is our biggest product innovation — agents earn 4–5x more per hour of their time than any other platform because they're already at the locations."

**Design note**: Split screen — left panel customer flow (mobile mockup screenshots, mocked UI), right panel agent flow. Magic numbers at the bottom in large gradient text. This slide should look like a real product. Include 2–3 actual UI mockup screenshots (agent app home screen in commute mode, customer task result screen).

---

## Slide 6: Market Size

**Headline**: $35B market, 22% CAGR, and the largest segment has never had a self-serve product

**Body**:
```
TAM: $35B
Physical world intelligence:
retail intelligence + mystery shopping + insurance field services +
AI training data + brand compliance + site intelligence

SAM: $8.5B
Crowdsourced, on-demand, visual intelligence segment —
the portion addressable by a smartphone-first platform

SOM (Year 3): $350M
3 Tier SOM: 50K enterprise customers ($66K ACV avg) +
2M SMB customers ($500 avg ACV) + 50M consumer credits

GROWTH CATALYST:
Every AI model trained on physical world images increases demand for
the labeled real-world visual data that Mosaic produces as a byproduct.
The training data market alone: $19.6B by 2033 (24.3% CAGR)

WHY THE MARKET IS BIGGER THAN IT LOOKS:
BeMyEye: $35M revenue, enterprise-only, 15 years building
Field Agent: enterprise-only
Trax: hardware + enterprise only
THE CONSUMER/SMB TIER HAS NEVER BEEN SERVED.
That's $3–5B of market that doesn't yet exist as a category.
```

**Narrative note**: "The incumbent market is $35B, growing at 22%. But the real opportunity is larger than the incumbents know — because the incumbents only serve the enterprise segment. No one has built the self-serve product for the 10,000 indie CPG brands who can't afford BeMyEye. No one has built the consumer product for the 50 million people with a one-time question about a physical place. That's the Uber insight applied to physical world data."

**Design note**: Three concentric circle diagram (TAM/SAM/SOM) with dollar amounts. Beneath it, a single comparison bar chart: BeMyEye ($35M) vs Mosaic SAM ($8.5B). The size difference is the story.

---

## Slide 7: Business Model

**Headline**: Three tiers. One platform. 55%+ gross margin.

**Body**:
```
TIER 1: CONSUMER         TIER 2: SMB              TIER 3: ENTERPRISE
Pay-per-task             $49–$749/month           $2,500–$50,000+/month
Credit wallet            Self-serve sub           Annual contract

$5–$25/task              5–150 tasks/month        200–10,000+ tasks/month
52% gross margin         62% gross margin         58% gross margin

ACQUISITION              ACQUISITION              ACQUISITION
App store / viral        Content / PLG             Founder sales → AE

AGENT PAYOUT: 40% of task price across all tiers (non-negotiable)
PLATFORM TAKE: 60% gross, then infrastructure (~5%), AI processing (~1%)
NET MARGIN: 55% blended

BONUS REVENUE STREAM — AI TRAINING DATA
Every completed task produces labeled real-world visual data.
At scale (500K tasks/month), this data licenses for $0.10–$0.15/image.
Month 36 projection: $2.4M/month at 95% gross margin.
This is the hidden upside that incumbents don't have because they don't have consumer scale.
```

**Narrative note**: "The three-tier model is the Uber insight: don't just sell to enterprise. The consumer tier gives us the agent density that makes the enterprise tier work. The agent density gives us the training data flywheel. Each tier enables the others. And the training data at scale becomes a revenue stream that investors are currently undervaluing — at Month 36, it's $29M ARR at 95% margin."

**Design note**: Three column layout with each tier. Key numbers (prices, margins) in accent color. Bottom section: a simple cash flow diagram showing task price → 40% to agent → 60% to platform → infrastructure costs → net. Training data as a fourth column with upside annotation.

---

## Slide 8: Traction

**Headline**: [PLACEHOLDER — fill in with actual metrics at time of raise]

**Body template**:
```
AGENTS                    TASKS COMPLETED          CUSTOMERS
[X] verified              [X] completed            [X] paying
in [# cities]             in [# weeks]             [X pilots active]

ENTERPRISE                SMB                      CONSUMER
[X] customers             [X] subscribers          [X] active users
[$ MRR]                   [$ MRR]                  [$ MRR]

KEY PROOF POINTS:
✓ [First customer name or type] signed at $[X]/month
✓ [Fulfillment rate]% task fulfillment rate in first [X] weeks
✓ [Agent retention]% agent retention after first month
✓ [NPS score] agent NPS / customer NPS

INVESTOR VALIDATION / WARM SIGNALS:
[Specific VC or operator who has expressed strong interest]

WHAT WE BUILT WITH 2 PEOPLE IN 8 WEEKS:
→ Agent app (iOS + Android) — Expo/React Native
→ Customer portal — Next.js + Supabase
→ AI extraction pipeline — GPT-4V + custom validation
→ Route-matching algorithm — geospatial corridor matching
→ 3-tier pricing engine
```

**Narrative note**: "Before I show you the model, I want to show you what two people and an AI toolstack built in 8 weeks. [Walk through the traction metrics]. The most important number on this slide isn't the revenue — it's that we built all of this for a $30K/month burn rate. That's the AI-native advantage in action."

**Design note**: Large callout boxes for the key metrics — agents, tasks, customers — in the accent gradient. Below them, a timeline showing what was shipped when (build velocity story). This is the slide where confidence needs to radiate — if traction is strong, the design should amplify it with large numbers and green/positive color signals.

---

## Slide 9: Go-to-Market

**Headline**: Beachhead → expansion → the physical world intelligence default

**Body**:
```
PHASE 1 (NOW → MONTH 6): BEACHHEAD
CPG shelf audits in 2 US cities + London
Target: 10 enterprise customers + 500 agents per city
Signal: Field Agent charges $30–175/task with 2-week turnaround
Mosaic delivers in 4 hours for $8–25

PHASE 2 (MONTH 6 → 18): MULTI-CITY EXPANSION
8 US cities + 5 EU cities
SMB self-serve product launches → content + PLG growth
Agent count: 15,000 active by Month 18

PHASE 3 (MONTH 18+): CATEGORY CREATION
Consumer brand ("the app you use to check a place")
Data network effects: more tasks → more training data → better AI → more customers
Training data licensing → $2M+/month at scale

AGENT ACQUISITION FLYWHEEL:
Campus ambassadors [40%] → Agent referral [30%] → Paid social [20%] → Organic [10%]
First city: $5K ad spend → 500 verified agents
Each agent earns avg $200/month → LTV:CAC = 90:1 (commute-mode agents)

CUSTOMER ACQUISITION BY TIER:
Enterprise: Founder sales → warm intros → conference demos → AE
SMB: Shopify app + Faire partnership + content SEO + referral
Consumer: App store + agent earnings sharing (viral)
```

**Narrative note**: "The GTM is about sequence, not sprinkle. We go deep in 2 cities before expanding, because fulfillment rate above 80% is what unlocks enterprise contracts. London specifically is our EU proof point — if Unilever or Reckitt signs, we have a reference customer that opens every door in EU enterprise sales. That's worth more than 5 smaller customers."

**Design note**: Three-phase horizontal timeline, each phase with a key metric target. Below it, two simple diagrams: the agent flywheel (circular) and the customer funnel (top-down). Keep it clean — too many arrows kills comprehension.

---

## Slide 10: Competitive Landscape

**Headline**: We occupy white space no incumbent has ever entered

**Body**:
```
                HIGH AI QUALITY
                       |
                       | ← MOSAIC
                       |
ENTERPRISE-ONLY -------|------- CONSUMER + SMB
                       |
     Field Agent ●     |
     BeMyEye ●         |
                       |
     Trax ●            |
                       |
                LOW AI QUALITY

THE STRUCTURAL GAP: No company with strong AI capability has ever
built a consumer/SMB product. The consumer tier requires a
fundamentally different UX, pricing model, and agent acquisition
strategy — not just a "simplified enterprise" product.

DIRECT COMPETITORS:
| | Field Agent | BeMyEye | Trax | MOSAIC |
|---|---|---|---|---|
| Consumer tier | ✗ | ✗ | ✗ | ✓ |
| AI extraction | ✗ | ✗ | ✓ | ✓ |
| <4 hour SLA | ✗ | ✗ | ✗ | ✓ |
| Route matching | ✗ | ✗ | ✗ | ✓ |
| On-device GDPR | ✗ | Unknown | ✗ | ✓ |
| Self-serve | ✗ | ✗ | ✗ | ✓ |
```

**Narrative note**: "Every competitor has made the same bet: enterprise-only, sales-led, slow. BeMyEye reached $35M revenue in 15 years with that bet. We're building for the era where a brand manager can get shelf data in 4 hours for $50 without a sales call — and where the same platform serves a parent checking if the park is crowded. That's not a feature. That's a category."

**Design note**: The 2×2 matrix should be the hero visual — clean, axis labels clearly readable. Below it, a feature comparison table. Mosaic's column should be all checkmarks in the accent color; competitors should have a mix of ✗ and ✓ that makes the whitespace obvious.

---

## Slide 11: Team

**Headline**: The two people who can build this — and the AI team they've assembled

**Body**:
```
[CEO NAME] — Commercial Founder
→ [X] years at [CPG company] — personally managed [$X] competitive intelligence budget
→ Sold [$X] in enterprise SaaS; knows every procurement pattern at Tier 3 CPG
→ [Relevant exits/companies] [LinkedIn]

[CTO NAME] — Technical Founder
→ Shipped [consumer app with X million users] — knows mobile at scale
→ [AI/ML background, specific CV skills] — built real-time inference pipelines
→ [Relevant exits/companies] [GitHub]

THE AI TEAM:
Claude Code + Cursor + Devin → 4× engineering velocity
v0 + Figma AI → design without design headcount
Pilot.ai + Stripe → finance without finance headcount
Intercom AI → customer success without CS headcount

COMBINED: The output of a 12-person team at a $30K/month burn rate.

ADVISORS:
[Name] — ex-[major CPG company], [relevant role]
[Name] — [GDPR/privacy attorney]
[Name] — [marketplace operator, ex-[company]]
```

**Narrative note**: "The team slide is where I want to be honest with you about something unconventional. We're a 2-person team. By choice. We believe the AI tools available in 2026 make a 2-person founding team + AI stack more effective than a 10-person team from 3 years ago — and dramatically better on burn rate. Here's what we built in our first 8 weeks [reference Traction slide numbers]. That's the proof."

**Design note**: Two founder photos, professional but human. Clean bios with the 3 most relevant bullets each. Below them, the "AI Team" section formatted as a grid of tool logos with brief descriptions. Visually, this should communicate "lean and powerful" not "small and underfunded."

---

## Slide 12: Financial Projections

**Headline**: $10M ARR in 18 months — three tiers building compounding revenue

**Body**:
```
MONTHLY REVENUE PROJECTIONS (3-TIER MODEL):

Month    | T1 Consumer | T2 SMB    | T3 Enterprise | Total MRR
---------|-------------|-----------|---------------|----------
Month 3  | $6,600      | $6,225    | $22,000       | $34,825
Month 6  | $24,200     | $24,900   | $49,500       | $98,600
Month 12 | $88,000     | $107,070  | $137,500      | $354,570
Month 18 | $220,000    | $242,100  | $275,000      | $822,100
Month 24 | $550,000    | $398,800  | $467,500      | $1,626,300

                    + TRAINING DATA REVENUE (Month 12+)
Month 12: $22,000 | Month 18: $85,000 | Month 24: $210,000

Month 18 ARR run rate: $9.87M → Series A trigger ✓

KEY ASSUMPTIONS:
• Agent payout: 40% of task price (fixed)
• Blended gross margin: 55% early → 65%+ at scale
• Enterprise: $5,500/month avg, 2.5% monthly churn
• SMB: $249/month avg, 5% monthly churn
• Consumer: $22/month avg, 15% monthly churn
• 3-city launch by Month 4; 8 cities by Month 12

BURN vs REVENUE:
Pre-seed: $30K/month burn
Seed: $120K/month burn (team expands to 8)
Break-even: Month 20 on seed capital
```

**Narrative note**: "These numbers are built bottom-up from task economics, not top-down from market size. Every enterprise customer is modeled as a real company with a real contract value. The consumer and SMB tiers are modeled on comparables from Field Agent, Shopify app stores, and beachhead launch data from comparable two-sided marketplaces. The Series A trigger — $10M ARR — is achievable at Month 18 because three tiers means three engines growing simultaneously."

**Design note**: A clean line chart showing three revenue lines (T1, T2, T3) plus total, with a horizontal dashed line at $822K (Series A trigger). Below it, a burn vs. revenue chart showing the crossover to break-even. Projection chart uses gradient fill under the total revenue line.

---

## Slide 13: The Ask

**Headline**: We're raising $5M to prove three cities and three tiers

**Body**:
```
RAISING: $5,000,000 seed round
STRUCTURE: Priced round, Series Seed preferred
PRE-MONEY VALUATION: $20–25M
RUNWAY: 18 months to Series A metrics

USE OF FUNDS:
Engineering team (3 hires)         $1,500,000   30%
Agent acquisition (4 cities)       $1,000,000   20%
ML/AI model development            $500,000     10%
Enterprise sales (1 AE)            $500,000     10%
Marketing (SMB + consumer)         $500,000     10%
Legal/compliance (GDPR, SOC 2)     $300,000      6%
Operations (city launches)         $400,000      8%
Buffer                             $300,000      6%

MILESTONES THIS CAPITAL BUYS:
✓ 4 cities live (Atlanta, Dallas, London, Amsterdam)
✓ 15,000 active agents
✓ 50 enterprise customers + 600 SMB subscribers
✓ $10M ARR run rate by Month 18
✓ GDPR compliance architecture completed
✓ Series A raise begins Month 16

WHAT SUCCESS LOOKS LIKE AT SERIES A:
10× revenue multiple → $100M valuation
3× YoY growth rate
115% Net Revenue Retention
"The Field Agent for the AI era"
```

**Narrative note**: "We're raising $5M to close the loop on three things: prove the model works in multiple cities simultaneously, prove all three tiers grow together, and sign at least one European enterprise customer to validate the global thesis. If we hit those three things at Month 18, this is a straightforward $50–100M Series A story. The ask today is not just capital — it's a partner who understands marketplaces, has relevant portfolio companies we can learn from, and believes that physical world intelligence is a $35B market that's never had a great consumer product."

**Design note**: Clean use-of-funds donut chart with percentages. Milestone list formatted as a checklist with bold completion dates. Bottom section: Series A target in large gradient text. This slide should feel like the beginning of something, not the end of a pitch — confident forward-looking energy.

---

## Appendix Slides

### A1: Unit Economics Deep Dive

```
PER TASK ECONOMICS (BLENDED):
Customer revenue:          $14.00
Agent payout (40%):       ($5.60)
AI processing:            ($0.20)
Infrastructure:           ($0.36)
Payment processing:       ($0.70)
Gross profit:              $7.14
Gross margin:               51%

AT SCALE (500K tasks/month):
AI drops to $0.05/task
Infrastructure drops to $0.20/task
Target gross margin: 65%+

AGENT LTV/CAC (COMMUTE MODE):
CAC: $20 | Monthly earn: $240 | Tasks/month: 60
Platform contribution/task: $2.50
Monthly contribution: $150
Annual LTV: $1,800 | LTV:CAC: 90:1
```

### A2: Technology Architecture

```
AGENT APP (iOS/Android)
→ React Native via Expo
→ On-device AI: MediaPipe + custom TFLite
→ Face redaction: runs pre-upload, never server-side
→ GPS: ephemeral, task-time only
→ Route matching: client-side corridor computation

BACKEND API
→ Node.js + Next.js on Vercel
→ Supabase (PostgreSQL + Realtime)
→ AWS S3 for image storage
→ Redis (Upstash) for task queue + geospatial index

AI EXTRACTION PIPELINE
→ GPT-4V for structured data extraction
→ Custom fine-tuned models for repeat task types (CPG shelves)
→ Confidence scoring + human fallback queue
→ Output: JSON + natural language summary

PROOF OF COMPLETION
→ Cryptographic hash of image + GPS + timestamp + agent ID
→ Stored on task record; customer can verify independently
→ Tamper-evident audit trail
```

### A3: GDPR Compliance Architecture

```
PRIVACY BY DESIGN (ARTICLE 25):
✓ On-device face redaction before any image upload
✓ Ephemeral GPS (active only during task completion)
✓ No behavioral profiling of agents
✓ No unredacted images ever stored on servers

LAWFUL BASIS BY DATA TYPE:
• Agent data: Contract (Art. 6(1)(b))
• Customer data: Contract (Art. 6(1)(b))
• Task images (post-redaction): Not personal data (Recital 26)
• Task location: Legitimate interests (Art. 6(1)(f))

REQUIRED DOCUMENTATION:
✓ DPIA completed for each EU country before launch
✓ ROPA (Record of Processing Activities) maintained
✓ Data Processing Agreements with all sub-processors
✓ EU Representative appointed (Art. 27)
✓ Privacy notices (Arts. 13/14) in agent and customer apps

GDPR vs BIPA:
GDPR: More paperwork. No class action risk.
BIPA: Less paperwork. Class action risk = existential.
On-device redaction eliminates BIPA entirely.
GDPR compliance is operational. BIPA avoidance is mandatory.
```

### A4: European Strategy Summary

```
YEAR 1 EU LAUNCHES:
Month 2: London — Unilever/Reckitt territory, English-native, ICO pragmatic
Month 3: Amsterdam — Heineken HQ, 95% English proficiency, Dutch startup ecosystem
Month 5: Berlin — German CPG market, Henkel/Beiersdorf accessible
Month 7: Barcelona — Nestlé Iberia, Spain gig economy density, Riders Law manageable
Month 9: Paris — L'Oréal/Danone, CNIL requires full DPIA, highest CPG density

EUROPEAN COMPETITOR:
BeMyEye: $35M revenue, 3M+ contributors, enterprise-only
MOSAIC ADVANTAGE: AI quality + consumer/SMB tier + faster delivery
BEACHHEAD CUSTOMER: One of {Unilever, Reckitt, Heineken} by Month 8

EU VALIDATION → US FUNDRAISING:
"We have $X ARR in the US AND Unilever/Heineken in Europe.
We are building the global physical world intelligence layer."
This arc justifies $50–100M Series A valuation.
```
