# Mosaic — Top 3 Use Cases
*Focus document: the three use cases to lead with, presented in full investor-facing narrative*

---

## Why Three, Not Seventy-Two

The current use case inventory spans 72 applications. This is a product thinking artifact, not a go-to-market strategy. When a VC partner hears 72 use cases, they hear: "we don't know what we are."

The best marketplace companies at seed stage have one answer to "who is your customer and what is their problem?" Uber was "businesspeople who can't get a reliable cab." DoorDash was "restaurants that couldn't afford delivery." The breadth came after.

Our three use cases share three properties that make them the right beachhead:

1. **The buyer already has budget.** They're not being asked to create a new line item. They have a field intelligence or retail execution budget that's currently going to slower, more expensive methods.
2. **The pain is measurable in dollars.** We can show a brand manager the exact revenue impact of an out-of-stock event. The ROI case writes itself.
3. **The proof of concept is a single pilot.** We can show value in 30 days with one city and ten stores. No 6-month implementation. No API integration required to see the first result.

---

## Use Case 1: CPG Shelf Compliance Audits

### The Problem

It's 9:14am on a Tuesday in October, two weeks before the holiday promotional cycle kicks in for a mid-size snack brand — let's call them Ridge Valley Chips. Ridge Valley's National Field Sales Manager, Daniela, is sitting in a planning meeting with the VP of Sales and the VP of Marketing. The question on the table: "Are all 4,200 Walmart locations actually carrying our new jalapeño SKU at the end-cap position we paid for?"

Nobody in that room knows the answer. And that's the problem.

Daniela's team of 12 field reps covers approximately 800 Walmart locations per quarter. That's 19% coverage. For the other 81%, Daniela is working from photosets submitted by the distributor reps — photos that are four to six weeks old, often staged to look compliant, and not machine-verified against the planogram.

She's not unusual. This is the universal condition of CPG field intelligence:

- The average CPG brand covers fewer than 20% of their retail distribution network with any field verification per quarter
- Distributor-submitted compliance photos have an estimated 30–40% discrepancy rate versus actual shelf conditions (source: industry estimates from shopper marketing consultants)
- A single missed end-cap placement in 1,000 stores costs a brand $400,000–$1.2M in lost promotional lift during a peak period (assuming $400–$1,200 incremental revenue per store per promotional week)
- The average Field Agent or mystery shopping firm charges $30–$175 per store visit with a 2–3 week turnaround

The brands know this is a problem. They've built entire teams around it. But they've never had a tool that was fast, cheap, and comprehensive enough to make real-time shelf compliance a routine operation.

### The Buyer Persona

**Name**: Daniela Santos (composite)
**Title**: National Field Sales Manager or VP of Shopper Marketing
**Company size**: $100M–$2B revenue CPG brand
**Budget authority**: Controls field intelligence / retail execution budget, typically $200K–$2M/year
**Current spend**: Mystery shopping firms ($50K–$400K/year), distributor relationship management, internal field rep headcount ($800K–$3M/year fully loaded for 8–25 reps)
**Core frustration**: "I can't see my shelves. I have 4,200 stores and 12 people. The math doesn't work."
**Decision trigger**: A specific incident — a missed promotional placement, a distributor dispute, a retailer deduction claim, or a competitive launch that went undetected until too late
**Sales cycle**: 30–60 days for initial pilot. Annual contract conversion follows successful pilot.
**Champion vs. economic buyer**: Daniela is the champion. The economic buyer is the VP of Sales or CFO. Daniela needs the ROI case to take upstairs — and we give it to her.

### The Exact Pain Point

The pain crystallizes around three specific scenarios, each of which Daniela can point to from the last 12 months:

**Scenario A — The Missed End-Cap**: Ridge Valley paid a regional grocery chain $85,000 for end-cap placement across 300 stores during the Super Bowl window. The merchandising team did the setup. But 60 of those 300 stores had the product placed two aisles away from the agreed end-cap position — either because the store manager ran out of space, or the distributor rep didn't confirm placement. Ridge Valley didn't find out until they pulled post-event scan data three weeks later. $170,000 in expected promotional lift, gone.

**Scenario B — The Planogram Deviation**: A large national retailer "optimized" their snack aisle planogram mid-quarter, shifting Ridge Valley's primary SKU from eye-level to knee-level in roughly 400 stores. The distributor didn't flag it. Field reps didn't see it. It showed up as a 12% velocity decline in that chain that the VP of Sales initially attributed to competitive pressure. It was shelf placement.

**Scenario C — The OOS Event That Lasted Three Weeks**: A supply chain hiccup left a Ridge Valley SKU out of stock in approximately 600 stores for 21 days. Nobody in the field caught it systematically. The brand found out because a category manager at the retailer called. By the time they reacted, three weeks of sales were gone.

In each scenario, the brand had no real-time visibility. Mosaic gives them that visibility for the first time.

### How Mosaic Solves It

**The Mosaic workflow for shelf compliance:**

1. Daniela uploads the planogram and SKU list to the Mosaic enterprise dashboard. She defines the compliance criteria: product at eye-level shelf, price tag correct, facing count ≥3, no competitive products in her allocated space.

2. She selects 50 stores across three metro areas. She posts the task with a 4-hour SLA.

3. Within 90 minutes, Mosaic's routing algorithm has matched each store to 1–2 collectors who are already near that location on their morning commute or routine. Collectors receive a task brief with photos of the planogram, instructions on what to photograph, and location confirmation.

4. Collectors spend 45–90 seconds in each store. They photograph the shelf from three angles. The on-device AI validates image quality before upload. No faces are captured.

5. Within 4 hours of task posting, Daniela's dashboard shows:
   - A store-by-store compliance score (0–100%)
   - Flagged deviations: wrong shelf position, out-of-stock, wrong facings, competitive intrusion
   - AI-extracted structured data: "Eye level: Yes. Facing count: 2 (target: 3). Price tag: Present. SKU in correct section: Yes."
   - Photos sortable by compliance score — worst stores first

6. Daniela sends the report to the regional distributor: "Stores 14, 22, and 31 are non-compliant. Please address by Thursday." She has photos. She has AI-verified data. The conversation is settled in minutes instead of weeks.

**The key product difference from existing solutions:**
- Field Agent: $30–175/store, 2-week turnaround, no AI extraction, no dashboard
- Mosaic: $12–25/store, 4-hour turnaround, AI extraction, structured JSON output, dashboard with drill-down

### What a Pilot Looks Like

**Pilot structure**: 50 stores, 1 metro area, 1 promotional cycle (4 weeks)
**Cost to customer**: $1,500–$3,000 (50 stores × $30–60/store including platform fee)
**Mosaic cost to deliver**: $750–$1,500 (50% gross margin)
**Time to deliver first results**: 4–8 hours after task posting
**Success criteria**: >80% fulfillment rate, AI-extracted compliance report within SLA, customer can see measurable ROI

**The ROI case for the pilot**: If the pilot reveals 8 stores (16%) are non-compliant with promotional placement, and each store represents $400 in missed weekly lift during a 4-week promotion, that's $12,800 in recovered promotional value from a $1,500–$3,000 pilot investment. The ROI is 4–8× in a single pilot. That closes the annual contract.

**Pilot to contract conversion target**: 60%. Our assumption is that 6 out of 10 companies who complete a pilot will sign an annual contract. This is consistent with enterprise software pilots where the product works and the ROI is clear.

### Revenue Potential

**Single customer economics** (mid-size CPG brand):
- Monthly audit cadence: 200 stores/month
- Blended task price: $25/store (4-hour SLA, AI extraction included)
- Monthly revenue: $5,000
- Annual contract value: $60,000

**Customer segment sizing:**
- Addressable mid-size CPG brands in the US with $100M–$2B revenue: ~800
- Brands that currently spend >$100K/year on field intelligence: ~400 (conservative)
- Mosaic-convertible (have existing budget, pain is measurable, SLA is compelling): ~200
- Realistic Year 1 penetration (founder-led sales): 15–25 customers
- Year 1 revenue from this use case alone: $900K–$1.5M ARR

**At 50 enterprise customers at $60K ACV (Year 2)**: $3M ARR from one use case.

This is the beachhead. Not the ceiling.

---

## Use Case 2: Out-of-Stock Detection for Brands

### The Problem

There is a number that haunts every CPG brand manager: 4–8%.

That's the percentage of retail revenue lost to out-of-stock (OOS) events across the industry. It's not a fringe number — it's well-documented by the Food Marketing Institute, ECR Europe, and Kantar. For a brand doing $500M in retail revenue, that's $20–40M lost every year to empty shelves.

The frustrating part: many OOS events are preventable if caught within 24–48 hours. Replenishment cycles exist. Distributor relationships exist. But the brand only finds out about an OOS event when it shows up as a velocity decline in weekly scan data — by which point the event has already lasted 5–10 days.

Marcus Chen is a Category Manager for an ambient grocery brand. His job is to own the performance of his category across 2,300 Kroger locations. Every Monday morning, he pulls POS data from Kroger's retailer portal. The data is 5 days old. If a SKU went OOS on Wednesday and stayed OOS through Sunday, Marcus sees the velocity drop on Monday. By Tuesday, he might get his distributor on the phone. By Thursday, shelves might start getting restocked.

Ten days of OOS. Times 200 stores. Times an average daily velocity of $40/store/day. That's $800,000 in lost revenue from a single OOS event that nobody caught in real time.

Marcus knows this is happening. He doesn't have a tool to see it as it happens.

### The Buyer Persona

**Name**: Marcus Chen (composite)
**Title**: Category Manager, Senior Brand Manager, or Director of Sales Operations
**Company size**: $200M–$5B revenue CPG brand (includes large brands with narrow-category focus)
**Budget authority**: Shares budget with VP of Category Management or VP of Sales. Has direct authority over $100K–$500K in field intelligence spend.
**Current tools**: Retailer POS portals (5–7 day lag), Nielsen/IRI scan data (weekly lag), distributor reports (unreliable, incentive to underreport), internal field rep network (covers <20% of locations)
**Core frustration**: "I find out about OOS events after the damage is done. I need to see my shelves like I can see my website traffic — in near real time."
**Decision trigger**: One large OOS event, quantified. Most brand managers can point to a specific incident in the last 12 months that cost them $500K–$2M. That incident is our opening.
**Differentiation from Use Case 1**: Shelf compliance is about promotional placement quality. OOS detection is about inventory availability. Different trigger, same platform, often the same buyer.

### The Exact Pain Point

Marcus's world is a game of managing lag. Every data source he has is stale:

- **POS data**: 3–7 day lag from most retailers
- **Distributor reports**: Weekly, often Monday for last week's data, and known to be cherry-picked
- **Field rep reports**: Cover 15% of locations, submitted on a 3–6 week cycle
- **IRI/Nielsen scan data**: Weekly industry data, no store-level granularity for OOS detection
- **Retailer OSA (On-Shelf Availability) programs**: Only Walmart and a handful of tier-1 retailers have these. They're expensive to access. They don't cover Marcus's full distribution network.

The result: the average CPG brand detects an OOS event 5–10 days after it begins. By that point:
- The shopper who wanted the product bought a competitor
- 2–3 replenishment cycles may have already been missed
- The retailer may have reset the planogram to fill the gap with a competitor's product

**The conversion cost is permanent.** When a shopper can't find their usual brand twice, research shows 30–40% switch brands permanently. Each undetected OOS event isn't just lost revenue — it's a customer acquisition problem that now requires marketing spend to fix.

### How Mosaic Solves It

**The Mosaic OOS detection workflow:**

1. Marcus sets up a "monitoring program" for his top 500 Kroger locations. He specifies 3 SKUs to track. He sets a cadence: weekly random sample of 80 stores (16% weekly coverage), or a triggered deployment when scan data shows velocity anomalies.

2. The weekly automated scan: every Monday at 7am, Mosaic deploys tasks to 80 stores selected by a stratified algorithm (geographic distribution, historical OOS risk score, store volume tier). By 11am, all 80 stores are checked. Marcus has a "shelf status report" on his desk by noon — before lunch.

3. The triggered deployment: if IRI/Nielsen data or Kroger's portal shows a velocity decline >15% in a specific region, Marcus can post an emergency audit of 50 stores in that region with a 4-hour SLA. Same day. No phone calls to distributor reps. No waiting.

4. The AI extraction output for OOS detection:
   - Stock status: In-stock / Low stock (<3 facings) / Out-of-stock
   - Shelf location: Correct position / Moved / Missing from set
   - Price tag status: Present / Missing / Wrong price
   - Competitive context: What's filling the space if OOS

5. Marcus gets a structured report: "14 of 80 stores checked show OOS on SKU #3842. 9 of those 14 are in the Dallas-Fort Worth region. Suspected distributor issue." He calls the Dallas distributor with data in hand. Restock is prioritized by end of week.

**The before/after:**
- Before Mosaic: OOS event starts Wednesday. Marcus sees velocity drop Monday. Calls distributor Tuesday. Shelves restocked Thursday–Friday. **10 days of OOS.**
- After Mosaic: OOS event starts Wednesday. Mosaic monitoring catches it in the next Monday scan. Distributor call Monday morning. Shelves restocked Wednesday. **7 days of OOS, 30% reduction.** For a $500M brand, that's $10–15M in recovered annual revenue.

### What a Pilot Looks Like

**Pilot structure**: 80-store weekly sample, 3 SKUs, 4 weeks
**Cost to customer**: $2,000–$4,000/month (80 stores × $12–25/check × 4 weeks spread across monthly billing)
**Contract trigger**: If the pilot catches one OOS event that the customer's existing tools missed, the contract is closed. This happens in nearly every pilot — because the tools they have are blind.

**The killer demo moment**: In the pilot kickoff call, we ask Marcus to pull up his current POS data and tell us which stores he thinks are in-stock on his top SKU. We run a same-day Mosaic check on 20 of those stores. We call him back in 4 hours. There's typically a 15–25% discrepancy. That is the close.

**Pilot to contract conversion target**: 70%. OOS detection has higher conversion than compliance because the ROI is simpler to calculate and the pain is sharper.

### Revenue Potential

**Single customer economics** (mid-size CPG brand, OOS monitoring program):
- Monthly task volume: 320 store checks (80 stores × 4 weekly scans)
- Blended task price: $18/check
- Monthly revenue: $5,760
- Annual contract value: $69,120 (rounded to $70K ACV)

**Scale potential:**
- 50 enterprise OOS monitoring customers at $70K ACV = $3.5M ARR
- This is separate from compliance audit revenue — the same brand often buys both products
- Brands with $500M+ in retail revenue: ~150 in the US alone
- Realistic Year 2 penetration: 30–40 OOS monitoring customers → $2.1–$2.8M ARR

**Cross-sell insight**: 60–70% of compliance audit customers (Use Case 1) will also buy OOS monitoring. These are complementary products with the same buyer and the same ROI story. Combined ACV for a mid-size CPG brand using both products: $100K–$130K/year.

---

## Use Case 3: Competitive Pricing Scans for Brand Managers

### The Problem

Sophie Lindqvist manages the North American pricing strategy for a premium personal care brand. Her products retail between $18 and $45. She has 6,200 active retail points of distribution across Target, Ulta, Walgreens, CVS, and regional beauty retailers.

Her problem is not knowing her own prices — her problem is not knowing her competitors' prices.

Every quarter, Sophie's brand does a "competitive pricing audit." They send field reps and interns to visit ~300 stores across 8 markets. They transcribe prices by hand from shelf tags. The data comes back in Excel spreadsheets. By the time the analysis is done, 10–14 days have passed. Sophie is looking at pricing data that is 2 weeks old before she can even begin to respond to it.

In the intervening two weeks:
- Her main competitor ran a 20% promotional discount at CVS in the Southeast that Sophie didn't see until it was over
- A regional beauty chain dropped her top SKU to a clearance price — below her MAP (Minimum Advertised Price) policy — that she's still trying to get retroactively documented for enforcement
- Target repriced a competitor's entry-level product $2 below hers in a direct side-by-side shelf placement

Sophie could respond to every one of these if she knew about them faster. She can't.

This problem exists at every CPG brand in every category where retail pricing is dynamic. Beauty, snacks, beverages, household products, personal care — all of them are running competitive pricing programs today that are slow, manual, and expensive.

### The Buyer Persona

**Name**: Sophie Lindqvist (composite)
**Title**: Director of Revenue Management, VP of Pricing, or Senior Brand Manager
**Company size**: $150M–$3B revenue CPG brand (personal care, beauty, household, food & beverage)
**Budget authority**: Direct authority over pricing intelligence budget ($50K–$300K/year) and often shares the field intelligence budget with the broader sales team
**Current tools**: Manual field visits by reps and interns, syndicated pricing data from Nielsen/IRI (weekly, aggregate, no SKU-level real-time data), vendor portals where available (inconsistent), spot-check vendor programs ($150–$300/store visit, 3-week turnaround)
**Core frustration**: "I'm managing a live pricing market with data that's three weeks old. My competitor can react to my promotions in 48 hours. I can't react to theirs in 14 days."
**Decision trigger**: A specific pricing incident — a competitor promotion that ran undetected, a MAP violation that went undocumented, a pricing gap that cost market share in a specific retailer
**Urgency signal**: Brands that have recently hired a Revenue Management or Yield Management function are actively shopping for better pricing intelligence tools. This is a budgeted problem with a clear owner.

### The Exact Pain Point

Sophie has three distinct pricing intelligence needs, all of which Mosaic addresses:

**Need 1 — Competitive Price Monitoring**: "What is my competitor's shelf price at Ulta today, in each region, for each SKU I'm competing with?" This requires knowing not just the listed price but the actual shelf tag, including any in-store promotional pricing not reflected in online data. Online price scrapers get the website price. Sophie needs the physical shelf price.

**Need 2 — MAP Violation Detection**: Brands set MAP (Minimum Advertised Price) policies to prevent retailers from discounting products below a threshold. MAP violations are common — small retailers discount aggressively, and even large chains run unauthorized clearance events. Documenting MAP violations requires a photo of the shelf tag with date, location, and price visible. That's exactly what Mosaic produces. Without documentation, MAP enforcement is a negotiation; with documentation, it's a contract dispute with evidence.

**Need 3 — Promotional Lift Verification**: When Sophie runs a trade promotion (a temporary price reduction funded by the brand, executed at retail), she needs to verify that the promotional price was actually implemented correctly at the shelf level. Retailers are supposed to pass through the discount — but "promotional leakage" (where the brand pays for the promotion but the shelf price doesn't change) is estimated at 15–25% of trade spend. For a $300M brand spending $30M in trade promotion annually, that's $4.5–$7.5M of unverified, potentially leaking spend.

### How Mosaic Solves It

**The Mosaic competitive pricing workflow:**

1. Sophie's team uploads a competitive pricing brief to Mosaic's enterprise dashboard:
   - Target SKUs: her 5 hero products and 8 key competitor products
   - Target retailers: Target (national), Ulta (national), CVS (regional focus: Southeast, Midwest)
   - Task type: "Photograph shelf tag showing price and product UPC. Include shelf context (product facings visible)."
   - Cadence: Weekly sample (150 stores/week) with surge capability for promotional periods

2. Every Tuesday morning, 150 store tasks deploy automatically. By 2pm, Sophie's pricing dashboard updates with:
   - Her prices vs. competitor prices, by SKU, by retailer, by region
   - Price gap trend lines (week-over-week)
   - Flagged anomalies: competitor promotions detected, MAP violation alerts, pricing errors
   - AI-extracted price data from shelf tag photos (OCR + visual validation)

3. When Sophie sees a competitor running a 20% discount at CVS in the Southeast: "Launched Tuesday, 38 of 45 stores checked, average $3.60 discount. Appears to be a regional trade event." She calls her CVS buyer with a matching offer by Thursday. Without Mosaic, she'd see this in the next Nielsen pull — 10 days later.

4. MAP violation detection: Mosaic's AI flags any shelf tag showing a price below Sophie's MAP threshold. The photo — timestamped, geolocated, cryptographically verified — is automatically attached to a violation report. Sophie sends it to her legal/compliance team and to the retailer's buyer. Documented, defensible, actionable.

5. Promotional verification: During Sophie's Q4 trade promotion window, Mosaic deploys a "promotion verification sweep" — 200 stores in the first 48 hours of the promotion period. Sophie can confirm within 2 days whether the promotional price is live at shelf. If 30 stores aren't showing the promotional price, she calls the regional DSD managers before the promotion window is half over.

**The AI extraction requirements are higher here than for basic compliance checks.** The platform needs to:
- OCR the shelf tag price accurately (including promotional stickers overlaid on base price tags)
- Match the photographed product to the correct SKU from Sophie's SKU list
- Extract base price, promotional price if present, and price-per-unit where visible

This is a premium AI extraction task — priced accordingly ($25–45/store check vs $12–15 for basic stock checks).

### What a Pilot Looks Like

**Pilot structure**: 50 stores, 3 retailers, 10 SKUs tracked (5 Sophie's + 5 competitor), 4 weeks
**Cost to customer**: $5,000–$8,000 for the pilot (premium pricing for AI-intensive extraction)
**Pilot value demo**: In week 1, Sophie's team gets a competitive pricing snapshot across 50 stores. For most brands, this is better competitive pricing data than they've seen in a quarter of manually collected data. The "aha moment" happens in week 1, not week 4.

**What makes this pilot irresistible**: The pilot delivers two things simultaneously — current competitive pricing intelligence AND a baseline dataset that Sophie can start using immediately for decision-making. It's not "wait 4 weeks to see if it works" — it's "you get data in 4 hours, and you'll have a decision to make with it."

**Pilot to contract conversion target**: 65%. Slightly lower than OOS detection because the integration with pricing workflows requires a bit more setup. But the ROI case is even more compelling for brands actively spending on trade promotion.

### Revenue Potential

**Single customer economics** (premium CPG brand, competitive pricing program):
- Monthly task volume: 600–800 store checks (150 stores × 4 weekly scans, plus surge events)
- Blended task price: $35/check (premium AI extraction for pricing)
- Monthly revenue: $21,000–$28,000
- Annual contract value: $252,000–$336,000 → round to $250K–$300K ACV

This is the highest-ACV use case by far. Competitive pricing programs are expensive because the data is valuable. Brands have historically paid $150–$300/store visit for manual competitive pricing audits. At $35/check with 4-hour turnaround, Mosaic is 4–8× cheaper and 40× faster.

**Scale potential:**
- 30 enterprise pricing intelligence customers at $280K ACV = $8.4M ARR from this use case alone
- Total addressable brand managers with active competitive pricing programs: 3,000+ in the US (mid-to-large CPG)
- Year 2 realistic penetration: 15–20 pricing intelligence customers → $4.2–$5.6M ARR

**Cross-sell dynamics**: Pricing intelligence customers are the highest-value accounts. A brand using Mosaic for pricing intelligence is extremely likely to expand to compliance auditing and OOS detection. Combined ACV for a brand using all three products: $200K–$400K/year. This is the enterprise account we pitch to a major CPG at $50K/month and grow to $200K+/month over 18 months through expansion.

---

## The Combined GTM Narrative

These three use cases are not three separate products. They're one product with three entry points — and they sell to the same buyer.

The enterprise CPG brand manager has a field intelligence budget. Shelf compliance, OOS detection, and competitive pricing are three chapters of the same story. A brand that buys one will buy the others if the first one works.

**Sequencing for the first 6 months:**
1. Lead with shelf compliance audits — easiest pilot to scope, clearest ROI, fastest to close
2. Upsell to OOS monitoring at the Month 3 QBR — "you caught 6 compliance issues; want to know about OOS events in real time?"
3. Introduce competitive pricing intelligence at Month 6 renewal — "ready to upgrade the program to include competitor pricing?"

**Three products. One account. $100K–$400K ACV by Year 2 with expansion. This is the enterprise motion.**

---

## What This Means for the Deck

In the pitch, we do not show 72 use cases. We show the CPG retail intelligence story:

*"Mosaic gives CPG brand managers what they've never had — real-time eyes on their shelves, their out-of-stocks, and their competitors' prices. At $12–$45 per store check versus $150–$300 from current providers. Delivered in 4 hours instead of 2 weeks. Starting with a 50-store pilot that pays for itself the first time it catches a compliance failure."*

That's it. That's the lead.

The 72 use cases are the appendix. The enterprise CPG motion is the story.
