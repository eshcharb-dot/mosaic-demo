# Mosaic — Next Stage Improvement Review V2
*Compiled: April 2, 2026*

Five-person team review covering CEO, UX/Design, CTO/Technical, GTM/Growth, and VC Analyst perspectives.
25 total improvement items. Each rated HIGH / MEDIUM / LOW impact.

---

## PRIORITY MATRIX

| # | Reviewer | Item | Impact |
|---|----------|------|--------|
| 1 | CEO | Founder names are placeholders — fatal before any VC meeting | HIGH |
| 2 | CEO | Traction slide has zero market-validated metrics | HIGH |
| 3 | CEO | 6-vertical expansion grid undercuts beachhead focus | HIGH |
| 4 | CEO | Collector cold-start problem is not addressed | HIGH |
| 5 | CEO | $20M pre-money cap is undefended at this stage | MEDIUM |
| 6 | UX | Token system fragmentation between demo and pitch | HIGH |
| 7 | UX | Camera screen uses CSS simulation at the most critical demo moment | HIGH |
| 8 | UX | Pitch deck has no slide transitions — hard cuts on large screens | HIGH |
| 9 | UX | Cover slide "View Demo" and "Download PDF" buttons are dead | HIGH |
| 10 | UX | C8 Earnings dashboard has duplicate transaction list | MEDIUM |
| 11 | CTO | "On-Device AI" claim is technically vague and partially contradictory | HIGH |
| 12 | CTO | AI extraction accuracy claims have no methodology or benchmarks | HIGH |
| 13 | CTO | Demo is simulated — no "Demo Mode" banner — credibility risk | HIGH |
| 14 | CTO | Team slide tech credentials are unverifiable placeholders | HIGH |
| 15 | CTO | Route-matching "moat" is a well-known algorithm, not novel IP | MEDIUM |
| 16 | GTM | Collector flywheel has no ignition plan for cold-start supply | HIGH |
| 17 | GTM | Enterprise sales motion is described but not operationalized | HIGH |
| 18 | GTM | Six-vertical messaging fragments the investor hook | HIGH |
| 19 | GTM | 90:1 LTV:CAC is buried — should be on the cover | HIGH |
| 20 | GTM | EU expansion story undercuts seed pitch urgency | MEDIUM |
| 21 | VC | Traction slide is a construction site — zero validated demand | HIGH |
| 22 | VC | Founding team slide has no founders in it | HIGH |
| 23 | VC | 4-hour SLA has no supply-side proof or density model | HIGH |
| 24 | VC | Three-tier simultaneity: no two-sided marketplace launches 3 tiers at once | MEDIUM |
| 25 | VC | "Why won't Uber/DoorDash do this?" objection goes unanswered | MEDIUM |

---

## 👔 CEO REVIEW

### 1. The Founders Are Ghosts — This Is a Fatal Signal

**Gap:** Both decks show `[CEO Name]` and `[CTO Name]` as literal placeholders. Every team credential is written in aspirational language — "has personally closed $100K+ SaaS contracts," "has shipped a consumer app with meaningful download numbers," "warm intro network." This isn't a team slide — it's a job description. No VC writing a $5M check will do so for a placeholder. This is the single biggest credibility hole in the entire deck, and it sits on the slide investors scrutinize hardest.

**Fix:** Put in real names, real companies, real numbers. If the CTO is not yet recruited, say "Seeking AI/ML CTO co-founder — technical lead currently contracted during search." That's honest and far less damaging than empty brackets. One real reference customer or pilot contact quoted by name changes everything. The deck must not be sent to a VC with placeholder text anywhere.

**Impact: HIGH**

---

### 2. Zero Revenue = Zero Traction, But the Deck Pretends Otherwise

**Gap:** The traction slide is entirely about what was built, not what was validated by the market. "3 enterprise pilots actively running" appears in the vision doc but is ambiguous — are these paid? LOI-signed? Free? The ARR trajectory starts at Month 3 with no Month 0 anchor. "First beta collectors onboarded" is the only real validation signal, and it's buried. The deck jumps to projections with no real baseline.

**Fix:** Add a "Validation to Date" section with specifics: pilot customer industry (e.g., "UK CPG brand, undisclosed"), whether paid or free, actual feedback, data collected. Even one paying pilot at $500 beats a thousand unpaid ones. Quantify the collector beta: how many onboarded, completed tasks, fulfillment rate. If pre-revenue, be explicit about it and reframe traction as "What We Know Is True."

**Impact: HIGH**

---

### 3. The "6 Markets, 1 Platform" Story Kills Beachhead Focus

**Gap:** The deck simultaneously argues "CPG is the wedge, laser-focused" and shows a 6-vertical grid with Insurance, Real Estate, Logistics, Alt Data, and Consumer. Seed investors reject unfocused founders. The "Year 1 Beachhead" label on CPG doesn't rescue this — the grid is right there, aspirational and detailed.

**Fix:** Remove the 6-vertical grid from the pitch deck entirely. Replace with: "CPG is the only market we're building for in the next 18 months, and here's why winning CPG creates the infrastructure that unlocks everything else." One sentence at the bottom: "The same API layer unlocks Insurance, Real Estate, and Alt Data post-Series A." The broader TAM stays in market sizing — but don't detail other verticals. This sharpens the story dramatically.

**Impact: HIGH**

---

### 4. The Collector Cold-Start Problem Is the Biggest Operational Risk and the Deck Buries It

**Gap:** The entire 4-hour SLA depends on having collectors in a city before the enterprise customer signs. This is the classic two-sided marketplace cold-start problem — zero coverage until addressed. The deck presents the flywheel as if it's already spinning. At zero: no collectors → can't deliver SLA → can't close enterprise → no tasks → can't attract collectors. Investors ask this on every marketplace pitch, and the deck gives them nothing.

**Fix:** Add a "Launch Playbook" section that addresses cold-start directly: (1) collector acquisition starts 60 days before enterprise sales opens in each city, seeded with referral bonuses; (2) "simulated demand" — run free pilots for beta enterprise customers to generate real tasks for collectors before paid contracts; (3) target cities with highest commuter density (London, NYC, Chicago). The route-matching insight — someone already commuting past Tesco doesn't need an SLA guarantee — is genuinely strong. Make it explicit.

**Impact: HIGH**

---

### 5. The $20M Pre-Money Cap Is Aggressive and Undefended

**Gap:** A $20M pre-money cap with zero revenue, placeholder founders, and a concept-stage product is top-quartile pre-seed. The deck never addresses this. Investors see "$20M cap" next to "[CEO Name]" and the math breaks. No comparable exits or return analysis is shown.

**Fix:** Either justify the cap explicitly with comparables (BeMyEye raised at X post-money with Y revenue) or lower to $12–15M and raise it at Series A when traction supports it. Alternatively, add a returns analysis slide: at $20M cap, $5M invested, $200M Series A = 10x. Show you understand the investor's return equation.

**Impact: MEDIUM**

---

## 🎨 UX / DESIGN REVIEW

### 1. Token System Fragmentation Undermines Brand Cohesion

**Gap:** The demo uses `--purple: #7c3aed`, the pitch uses `--purple: #7c6df5` — noticeably different violets. The pitch introduces pink, yellow, and orange accents that appear nowhere in the demo. Background colors differ (`#080b12` vs `#030305`). Gradient endpoints diverge. An investor who opens the demo after the pitch deck will notice the color shift immediately.

**Fix:** Unify on a single token file. Adopt the pitch's purple (`#7c6df5`) across both — it reads better at large display scale. Consolidate to two gradients: `--g1` (purple → cyan, primary) and `--g2` (warm accent for earnings only). A shared 6-line CSS `:root` block, copy-pasted identically into both files, is the minimum viable fix.

**Impact: HIGH**

---

### 2. The Camera Screen Is CSS Simulation at the Most Critical Demo Moment

**Gap:** Screen C5 (Camera) — the screen that proves the core product promise — uses a CSS shelf simulation (colored divs) instead of a real photo. The camera viewfinder shows an abstract colored grid over a dark gradient background. This is the screen investors stare at when you say "45-second capture, AI quality check live." Every other demo screen has real-world data (Sainsbury's Borough, real GBP amounts) — but the camera moment, where believability is most load-bearing, is the most obviously fabricated.

**Fix:** Replace the camera background with a real shelf photo (even a stock image from Unsplash) set as a `background-image` inside `.camera-bg` at opacity 0.9. The AI bounding-box corners and scan-line overlay will land on top and suddenly look like real AR, not decoration. The `deck-assets/` folder already exists — add one supermarket aisle photo there.

**Impact: HIGH**

---

### 3. The Pitch Deck Has No Slide Transitions — Hard Cuts on Big Screens

**Gap:** The pitch's `goTo()` function swaps slides via `display:none → display:flex` with zero transition. On a large screen or TV this is jarring for every advance. The demo, by contrast, has a well-executed `opacity + translateX(30px)` cubic-bezier fade-slide. The pitch plays in VC boardrooms on large screens — yet it has cruder interaction quality than the demo.

**Fix:** Change all slides to `position:absolute; opacity:0; pointer-events:none` and transition to `opacity:1; pointer-events:all` on `.active`. Optionally add `transform: translateY(12px)` enter animation. The `goTo()` function already removes/adds `.active` — just move display logic to CSS opacity/pointer-events. ~20 lines of CSS + remove the `display` toggle from JS. Elevates perceived production quality by a full tier.

**Impact: HIGH**

---

### 4. Cover Slide Buttons Are Dead — Instant Credibility Loss

**Gap:** Slide 3 (cover/intro) renders "View Demo" (gradient, high visual weight) and "Download PDF" (ghost) buttons. Both are `<button>` elements with no `onclick`. They do nothing. The founder who says "click View Demo" will watch the investor click the most obvious button and see nothing happen. The PDF button implies an asset that doesn't exist.

**Fix:** Wire "View Demo" to `onclick="window.open('MOSAIC_DEMO_V2.html', '_blank')"`. Rename "Download PDF" to "Contact Us" and wire to `mailto:` with pre-filled subject, or remove it entirely until a PDF export exists. A missing feature shown as present is worse than not mentioning it.

**Impact: HIGH**

---

### 5. C8 Earnings Dashboard Has a Duplicate Transaction List

**Gap:** Screen C8 renders two visually distinct but content-identical transaction lists stacked one after the other — "Recent Tasks" card followed by "Recent Transactions" card. Task names differ slightly but payouts are from the same session. An investor scrolling this screen will correctly infer it was assembled additively, not designed holistically.

**Fix:** Remove "Recent Tasks" and keep only "Recent Transactions." Use the recovered space for a prominent "Withdraw Earnings" CTA button. Reorder: header → big earnings number + progress bar → bar chart → badges → recent transactions → CTA. This transforms the screen from a data pile into a clear user journey.

**Impact: MEDIUM**

---

## 🔧 CTO / TECHNICAL REVIEW

### 1. The "On-Device AI" Privacy Claim Is Technically Contradictory

**Gap:** The pitch claims "on-device face redaction, GDPR-native, no biometric data ever leaves the device" while also describing corridor-based route-matching that requires knowing where the agent is going — information that must be communicated to the matching server. The architecture is contradictory. Additionally, MediaPipe Face Detection on low-end Android runs at 15–25fps with significant battery draw — never acknowledged. And "BIPA eliminated" because faces are redacted on-device is legally aggressive; Illinois BIPA case law is nuanced.

**Fix:** Add a "Privacy Architecture" diagram showing exactly what data flows where — what stays on device (redacted photo + GPS geofence confirmation), what goes to server (route corridor computed from declared commute endpoints, not real-time GPS streams). Replace "BIPA eliminated" with "BIPA risk substantially reduced." This turns a suspicious overclaim into a credible technical differentiator.

**Impact: HIGH**

---

### 2. AI Extraction Accuracy Claims Have No Methodology

**Gap:** ">90% extraction accuracy on CPG shelf tasks" — no methodology given. Is that SKU identification? Planogram compliance? Price tag reading? These have very different difficulty profiles. The "0.3% accuracy improvement per 1,000 tasks" claim has no citation or derivation — it reads as a marketing approximation masquerading as a technical measurement.

**Fix:** Replace the single accuracy stat with a task-type breakdown: binary compliance check vs. SKU count accuracy vs. price reading accuracy — with sample sizes. Drop the "0.3% per 1,000 tasks" claim or replace it with a reference to published literature on vision model fine-tuning data efficiency curves. Add one sentence on the human fallback confidence threshold.

**Impact: HIGH**

---

### 3. The Demo Is Simulated — No Disclaimer Banner Is a Credibility Risk

**Gap:** The demo is a fully rendered HTML/CSS/JS prototype with no live backend. Screenshots referenced in the pitch render as empty placeholders. Enterprise screens reference "3 enterprise pilots actively running" and "live compliance view" — but show no live data. A technical VC who opens DevTools will discover this immediately. The disconnect between pitch language ("Live in TestFlight," "3 pilots testing now") and the prototype creates a material trust gap.

**Fix:** Add a visible "Demo Mode — Simulated Data" banner at the top of MOSAIC_DEMO_V2.html. Add a note in pitch materials distinguishing live assets (TestFlight build, enterprise portal URL, pilot data) from illustrated ones (the interactive demo). Replace broken image placeholders with actual screenshots or designed SVG mockups — empty gray boxes read as unfinished.

**Impact: HIGH**

---

### 4. Team Slide Tech Credentials Are Unverifiable — Biggest Seed Red Flag

**Gap:** The CTO is described generically: "shipped consumer apps at scale," "vision model fine-tuning," "marketplace systems." None attributed to a real person, company, or verifiable track record. For a seed deal where the technical thesis depends entirely on one CTO building a GPT-4V extraction pipeline + route-matching algorithm + React Native app + Next.js portal + Supabase backend — all in 8 weeks — the absence of a named, verifiable technical founder is the single biggest red flag.

**Fix:** Fill in founder names with verifiable profiles (LinkedIn, GitHub, prior company). The CTO section specifically needs one concrete proof point: a shipped app with download numbers, an open-source repo, or a prior company with a technical outcome. If founders are anonymous for confidentiality, add "founders available for NDA call" — but placeholder brackets in investor materials signal unreadiness.

**Impact: HIGH**

---

### 5. Route-Matching "Moat" Is a Well-Known Algorithm

**Gap:** Route-matching is listed as a compounding moat with "patent-pending architecture." The description is: "corridor-based, 300–500m buffer, rank by payout/(1+detour), on-device computation." This is a one-sentence description of a well-understood geospatial problem — the same approach used by DoorDash batching and Uber pool, described in published papers from 2019. A technical VC will recognize this immediately. "Patent-pending" on a corridor buffer with a payout-over-detour objective is unlikely to survive USPTO review.

**Fix:** Either go deeper on what is genuinely novel (the pre-commit before departure, polyline computation from declared route rather than GPS tracking, multi-task batching optimization across a corridor) or deprioritize it as a moat and fold into "product execution." If the real moat is behavioral (pre-commit reduces cancellation 80%), lead with that — it's more defensible and harder to copy.

**Impact: MEDIUM**

---

## 🚀 GTM / GROWTH REVIEW

### 1. The Collector Flywheel Has No Ignition Plan

**Gap:** The materials articulate the flywheel elegantly but say nothing about how the first 500 collectors per city actually get acquired before there are tasks to earn from. Collector acquisition is one bullet: "Instagram ad / Facebook groups / Gumtree." For a marketplace, the cold-start supply side is the entire GTM risk. No channel mix with CPCs, no budget allocation, no sequenced seeding plan, no answer to "why would a commuter install an app with zero tasks near her yet?"

**Fix:** Add a "Collector Ignition Playbook": partner with one or two large employers (hospital, university) to recruit their commuting workforce as a founding cohort with a guaranteed first-week earning bonus; state city-by-city collector targets with timeline; clarify that first 2–4 enterprise pilots are pre-sold before collectors go live, so first task batches have guaranteed demand. The "£14.50 per commute" promise can't be on the cover if the reader doesn't believe it can be delivered day one.

**Impact: HIGH**

---

### 2. Enterprise Sales Motion Is Described, Not Operationalized

**Gap:** The pitch gives excellent buyer personas and a sharp 8x ROI proof point, but no actual sales motion: who closes the first 10 accounts, how, and when. "Founder sales → AE → Reference logos" is a three-word line. "Warm intros to first 10 enterprise accounts" appears without a named target list, outreach sequence, or timeline. The killer demo mechanic — "run 20 stores they think are compliant, return results in 4 hours, convert on the discrepancy" — is never named as the GTM mechanism.

**Fix:** Add a "First 10 Deals" section: exact target companies, intro path for each, timeline to LOI. Show the demo-close explicitly as the GTM mechanism. State the pilot price ($1,500–3,000) as a deliberate loss leader designed to generate a reference logo, not a revenue target. This turns a vague strategy into an operational playbook a VC can believe in.

**Impact: HIGH**

---

### 3. Six-Vertical Messaging Fragments the Investor Hook

**Gap:** Both documents open with CPG as the wedge, then immediately pivot to a 6-vertical grid. The multimillion-dollar CPG enterprise buyer and the "is the park crowded?" consumer buyer cannot be in the same paragraph and both feel primary. This signals optionality over conviction.

**Fix:** Treat the 6 verticals as an appendix or "year 3+ expansion" callout. The hook: "We are the Stripe for physical world intelligence — CPG is our first API use case, the platform is the infrastructure play." Anchor to the $4.2B CPG SAM as the credible near-term number, then reveal $35B as the infrastructure opportunity — rather than opening with $35B and making investors do the work.

**Impact: HIGH**

---

### 4. 90:1 LTV:CAC Is Buried — It's the Best Number in the Deck

**Gap:** The LTV:CAC of 90:1 at $20 CAC is buried in a supporting document rather than front and center in the pitch. A 90:1 LTV:CAC is better than most SaaS companies can claim — it should be screaming from the cover. The agent acquisition section also lists only paid channels. No referral mechanic, no "earnings badge" share feature, no community flywheel.

**Fix:** Surface 90:1 LTV:CAC prominently on the business model slide. Then add a "viral referral loop": "Maya refers 3 friends → each earns £10 joining bonus → Maya earns £15 → platform acquires 3 agents at effective CAC of £5." Design the collector app to generate a shareable end-of-month earnings card — native shareability. Uber's earliest growth was driver referrals, not advertising — say so.

**Impact: HIGH**

---

### 5. European Expansion Story Undercuts Seed Pitch Urgency

**Gap:** The EUROPE_STRATEGY.md is thorough but its presence as an elaborated parallel document creates a GTM message problem: pre-revenue and raising $5M while laying out a 7-city EU expansion plan signals premature geographic ambition. The pitch uses London examples but is silent on US launch cities. VCs will ask "US or EU first?" and the answer isn't crisp.

**Fix:** Make geographic sequencing explicit in the pitch: "Month 1: Atlanta + Dallas. Month 3: London soft launch — 1 paid pilot with a UK CPG brand. Month 9–12: EU contracts become Series A proof points." This gives US-focused VCs a US-first story and positions Europe as a designed milestone rather than an unanswered question.

**Impact: MEDIUM**

---

## 💼 VC ANALYST REVIEW

### 1. The Traction Slide Is a Construction Site

**Gap:** The traction slide contains zero paying customers, zero agents onboarded, zero tasks completed, zero revenue — only a list of products shipped. The deck template explicitly labels the traction section `[PLACEHOLDER — fill in with actual metrics at time of raise]`, which means it's being circulated before the metrics exist to fill it in. Partners will say: "You're asking for $5M on $20M pre-money with no customers and no agents."

**Fix:** Do not approach seed VCs until you have at minimum: (a) 50–100 verified agents in one city, (b) 3–5 completed tasks with real customer payment, and (c) one enterprise pilot — even if discounted. Any one converts the traction slide from a promise to a proof. Alternatively, reframe explicitly as a pre-seed raise at $400–500K which resets valuation expectations appropriately.

**Impact: HIGH**

---

### 2. The Founding Team Slide Has No Founders In It

**Gap:** Every version of the materials presents the team slide with literal `[CEO NAME]`, `[CTO NAME]`, `[LinkedIn]` placeholder text. The team section acknowledges "two founders" but names neither, lists none of their actual credentials, and cites no prior exits or domain authority. The advisor section is entirely placeholder. A partner will not proceed past the team slide without identities — team is the entire thesis at pre-revenue stage.

**Fix:** Replace all placeholder text with real names, photos, and verifiable credentials before any deck is sent. The AI-native team narrative — "2 people doing the work of 12" — is genuinely compelling, but only if the audience can verify the 2 people are credible. Specify prior companies, revenue generated, apps shipped, relevant AI or CPG domain experience.

**Impact: HIGH**

---

### 3. The 4-Hour SLA Has No Supply-Side Proof or Density Model

**Gap:** The 4-hour SLA is the central product promise — on the cover, in the product flow, in the competitive comparison. But there is no evidence it's achievable. No agents. No city density data. No fulfillment rate. The route-matching algorithm is only as good as the supply in the corridor. BeMyEye took 3+ years to hit 80% fulfillment — the deck never addresses why Mosaic will hit it in 4 months.

**Fix:** Add a minimum viable density model: how many agents per city radius are required to hit 80%+ fulfillment on a 50-store task within 4 hours? State your agent recruitment pace assumption. Include in the Appendix as a "supply-side sensitivity analysis." Even "We need 300 active agents per 15-mile radius to hit 4-hour SLA at 95% fulfillment" demonstrates you've stress-tested the claim.

**Impact: HIGH**

---

### 4. Three-Tier Simultaneity: No Marketplace Launches 3 Customer Segments at Once

**Gap:** The GTM plan launches consumer, SMB, and enterprise effectively simultaneously. Projections assume all three tiers are growing by Month 3. No two-sided marketplace has successfully launched three customer segments simultaneously with two founders and a $30K/month burn. The deck doesn't explain which tier is the actual beachhead or how founders divide time between high-touch enterprise sales, PLG SMB, and consumer brand-building.

**Fix:** Define a single beachhead tier and sequencing logic. Strongest version: "Enterprise is the only revenue tier that matters in the first 6 months. Consumer and SMB exist to build agent density, not generate meaningful revenue." Show revised projections depicting conservative enterprise-first growth through Month 12, with consumer/SMB as lagging contributors.

**Impact: MEDIUM**

---

### 5. "Why Won't Uber or DoorDash Do This?" Goes Unanswered

**Gap:** The competitive landscape positions Mosaic against BeMyEye and Field Agent — legacy incumbents — but completely ignores the most obvious threat: platform risk from Uber, DoorDash, Google Maps, or Amazon. DoorDash has millions of drivers with smartphones, GPS, store location graphs, and existing CPG partnerships. The "Why Now" slide argues the gig infrastructure is already built — but that same argument works against Mosaic. The materials never address this, even in an appendix.

**Fix:** Add a direct "Why Not Uber/DoorDash?" section. The honest answer has merit: platform companies don't build data intelligence products — they build delivery products. CPG shelf audit is low-volume, specialized, and conflicts with driver utilization optimization. The API/data business model requires GDPR compliance infrastructure that DoorDash has no incentive to build. Make this argument explicitly, not as a diligence landmine.

**Impact: MEDIUM**

---

## CONSOLIDATED ACTION LIST — DO BEFORE FIRST VC MEETING

### Non-Negotiable (do these first):
1. **Fill in real founder names and credentials** — everywhere, no exceptions
2. **Add "Demo Mode — Simulated Data" banner** to MOSAIC_DEMO_V2.html
3. **Wire up the "View Demo" button** on the pitch cover slide
4. **Remove the 6-vertical expansion grid** from the pitch (keep in vision doc only)
5. **Add a cold-start / collector ignition slide** explaining how you get agents before enterprise

### High Value Before VC Meetings:
6. Unify color tokens across pitch and demo (`--purple: #7c6df5` everywhere)
7. Replace CSS camera simulation with a real shelf photo
8. Add slide transitions to the pitch deck
9. Surface 90:1 LTV:CAC on the business model slide
10. Add explicit geographic sequencing (US-first, then EU at Series A)

### Requires Real-World Validation:
11. Get at least one paying enterprise pilot on record
12. Onboard 50+ verified collectors in one city with real task completion data
13. Run a real 20-store pilot and document the results

---

*See MOSAIC_IMPROVEMENTS_V1.md for bug-level fixes and demo interaction improvements.*
