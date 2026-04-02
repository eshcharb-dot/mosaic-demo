# Mosaic — Location-Aware "Already Going There" Model
*Cycles 126–128: Product design, business model implications, technical architecture, Daily Commuter persona*

---

## The Core Insight

Every gig economy platform treats location as reactive: you finish a delivery, then look for the next one nearby. The whole model is built around dispatching people to places. Mosaic's opportunity is fundamentally different: **the most valuable agent is someone who is already going where the task is.** A commuter passing the Whole Foods every morning at 8:47am is worth infinitely more than a driver who has to detour 12 minutes to get there.

This reframe changes everything. It changes pricing (no travel = lower floor price = more tasks = more agents = more customers). It changes agent retention (higher earnings density = stickier). It changes fulfillment economics (cost-per-completed-task drops dramatically when agents aren't compensated for travel). And it creates a product experience that no competitor has built — because no competitor has thought about it this way.

---

## Part 1: Product Design — The Four Modes

### Mode 1: Trip Intent ("I'm heading somewhere")

**The problem it solves**: Current gig apps show you tasks near your *current* location. But by the time you see a task near your destination, you're already there and may have already passed the optimal task locations on your route. The window for earnings maximization is *before* you leave.

**How it works**:

1. Agent opens Mosaic app before leaving home (triggered by morning notification: "You have 3 tasks along your usual commute. Review before you leave →")
2. Agent enters or confirms destination: [Work] [Gym] [Specific address] [Store name]
3. App renders a route corridor (not just a radius) showing all active tasks within 500 meters of the inferred fastest route
4. Tasks are ranked by: payout × (1 - detour cost) — tasks that require zero detour rank highest; tasks requiring a 2-minute detour rank lower but still show
5. Agent taps to accept 1–5 tasks before leaving home
6. At each task location, app sends a notification: "You're near the Whole Foods on Main St — your task is ready. Tap to start (90 seconds)"
7. After completion, app queues next task on the remaining route

**Data the app uses**:
- Stated destination (entered by agent)
- Historical routes (learned over time from task completion patterns — not continuous GPS tracking)
- Current active tasks with location coordinates
- Estimated walking/transit route between agent's origin and destination

**What makes this differentiated**: No other gig platform pre-stages tasks for a journey *before the journey starts*. DoorDash, TaskRabbit, Fiverr — all reactive. Mosaic's trip intent model is proactive and route-aware.

---

### Mode 2: Commute Mode

**Trigger**: Agent turns on "Commute Mode" by tapping a persistent button on the app home screen. Can also auto-trigger if agent opens the app within their typical commute window (learned from usage patterns after 10+ commutes).

**Design flow**:

```
HOME SCREEN — COMMUTE MODE ON
┌─────────────────────────────────────────────┐
│  ⚡ Commute Mode Active                     │
│  📍 3 tasks along your route                │
│                                             │
│  [TASK 1] Sainsbury's Camden              │
│  Shelf check — Oat milk section            │
│  💰 £6.00  ⏱ 90 sec  📍 On your route    │
│  [Accept]                                   │
│                                             │
│  [TASK 2] Costa Coffee Euston Rd          │
│  Crowd level — interior                    │
│  💰 £3.50  ⏱ 45 sec  📍 2 min detour     │
│  [Accept]                                   │
│                                             │
│  [TASK 3] Boots Pharmacy Kings Cross      │
│  Product in-stock check                    │
│  💰 £4.20  ⏱ 60 sec  📍 On your route    │
│  [Accept]                                   │
│                                             │
│  Potential earnings: £13.70               │
│  ─────────────────────────────────────────  │
│  [Accept All 3]  [Review individually]     │
└─────────────────────────────────────────────┘
```

**The "accept all" button** is key. An agent who accepts 3 tasks with one tap and earns £13.70 in their morning commute with zero detour is a retained agent. That single UX decision drives LTV.

**Commute profile learning**: After 5 commutes, the app knows the agent's route corridor, typical departure time, and commute duration. It pre-loads the task feed overnight so it's ready when they wake up. No waiting for the algorithm — tasks are staged before the agent even thinks to open the app.

---

### Mode 3: Shopping Run Mode

**Trigger**: Agent indicates they're heading to a specific store or shopping area.

**Design flow**:

1. Agent taps "I'm going shopping" → selects store (Tesco, Whole Foods, Target, etc.) or types address
2. App shows all tasks available at that store AND at stores within 500m
3. Tasks are organized by: "Do while you shop at [Store]" and "Quick stop nearby (2 min)"
4. Agent pre-accepts tasks — they become the agent's "shopping list" alongside their own shopping
5. At the store, app guides them through tasks interleaved with their own shopping: "While you're in the cereal aisle, there's a task here. [Start]"

**The insight**: A shopper at Whole Foods is already walking every aisle. A 90-second shelf check while they're in the snack aisle costs them nothing. Mosaic is monetizing dead time they were spending anyway.

**Task bundling at one location**: Multiple customers may have tasks at the same store. A shopping run agent at Whole Foods might complete:
- Customer A: Oat milk shelf check (30 sec)
- Customer B: Competitor price scan for protein bars (90 sec)
- Customer C: Crowd level and checkout queue time (60 sec)
- Total: 3 minutes, 3 tasks, £12.50 earned while buying groceries

This is the highest earnings density possible on the platform.

---

### Mode 4: Already Here ("I'm at a location")

**Trigger**: Agent is already at a location and opens the app opportunistically.

**Design flow**: Simple proximity-based task feed, ranked by distance and payout. No journey planning required. This is the existing geo-radial model, which remains for opportunistic use. The innovation is that modes 1–3 make this mode less necessary because tasks are pre-accepted before arrival.

**Differentiation for "already here"**: Push notifications with geofencing. When an agent enters a 200m radius of a task location, app sends: "You're near a task. 60 seconds, £4.00. Accept?" — low friction, high conversion.

---

## Part 2: Business Model Implications

### The Micro-Task Tier

The "already going there" insight enables a new pricing tier that doesn't exist in dispatched gig models.

**The problem with dispatched gig economics**: If an agent needs 15 minutes to get to a task, the task needs to pay at least £5–8 to justify the travel. Below that, agents reject the task. This creates a price floor.

**Mosaic's "already going there" price floor**: If the agent is already at the location, there's no travel cost. The floor is determined by the effort of the task alone. A 45-second shelf check that requires zero detour needs to pay only enough to cover 45 seconds of the agent's attention — not 15 minutes of their transit time.

**The Micro-Task Tier Design**:

| Task | Duration | Agent Payout | Customer Price | Conditions |
|------|----------|--------------|----------------|------------|
| Crowd level check | 30 sec | £1.50 | £3.75 | On-route only, commute mode |
| Single product in-stock | 45 sec | £2.00 | £5.00 | Already at store |
| Price scan (1 item) | 30 sec | £1.50 | £3.75 | Already at store |
| Queue time check | 20 sec | £1.00 | £2.50 | Commute mode |
| Exterior photo | 45 sec | £2.00 | £5.00 | On-route only |

**Key constraint**: Micro-tasks are only available to agents in commute mode or shopping run mode. They don't appear for agents in "already here" mode without route context. This prevents gaming (agents can't just stand at one location completing £2 tasks endlessly). The platform assigns micro-tasks only where the agent's stated route passes through the location.

**Customer economics for micro-tasks**: A customer who wants crowd-level checks at 20 London Starbucks every Monday morning can do this for £50/week (20 × £2.50). Previously, this would have cost £100+ via BeMyEye with a 48-hour turnaround. Mosaic delivers it in real-time at half the price because agents are already passing these Starbucks on their morning commutes.

---

### Route-Matching and Agent Retention

**The earnings density equation**:

Standard dispatched gig task: Agent earns £6 in 20 minutes (including 15 min travel) = £18/hour effective rate
Route-matched task: Agent earns £6 in 5 minutes (90 sec task + 3.5 min walking detour) = £72/hour effective rate

The agent who does 3 route-matched tasks during their 30-minute commute earns £15 with zero dedicated travel time. The same agent doing dispatched tasks earns £4–6 for the same time investment. **Route matching increases effective hourly earnings 4–5x without any increase in platform cost.**

Higher effective earnings = dramatically better agent retention. Mosaic's monthly agent retention target improves from 45% (dispatched gig baseline) to **65%+ for commute-mode agents**. This is the key lever.

**The passive task feed** — agent home screen shows upcoming route tasks before they leave, creating a habit loop: "Check Mosaic before commute" becomes a morning ritual because it consistently puts £10–15 in the agent's pocket with zero additional effort.

---

### Cost-Per-Fulfilled-Task Economics

| Model | Agent Payout | Surge Required? | Fulfillment Rate | Effective Platform Cost/Task |
|-------|-------------|-----------------|-----------------|------------------------------|
| Dispatched gig (competitor) | $8–12 + 1.5× surge for rush | Often | 70% | $15–18 effective |
| Mosaic standard (nearby) | $4–8 | Occasionally | 78% | $7–10 effective |
| Mosaic commute-match | $2–6 | Rarely | 92% | $4–7 effective |

**Why fulfillment rate is higher for commute-match**: The agent has pre-accepted the task at home, before commuting. Acceptance = commitment. Cancellation rates for pre-accepted tasks are dramatically lower than for real-time notifications (estimated 80% lower based on analogous patterns from pre-scheduled delivery platforms). Higher fulfillment rate = less wasted platform infrastructure = lower effective cost.

**The platform flywheel**:
- More commute-mode agents → better fulfillment rates → better SLAs for customers → more customers → more tasks → better earnings for agents → more agents choose commute mode

---

## Part 3: Technical Architecture

### Data Requirements for Trip Intent

**What the app needs to know**:
1. **Stated destination** — entered by agent (no inference required, no passive tracking)
2. **Origin** — agent's current GPS location at time of trip intent declaration (one-time permission prompt)
3. **Active tasks** — list of all tasks with coordinates, from the backend task database
4. **Route corridor** — computed route between origin and destination, with 500m buffer on each side

**What the app does NOT need**:
- Continuous GPS tracking
- Calendar integration (optional enhancement, not required)
- Historical location data (optional, for route learning — privacy-preserving implementation below)
- Cell tower triangulation or WiFi mapping

**Minimum data footprint**: Origin → Destination → Route computed on-device → Tasks within route corridor surfaced → Destination reached or mode disabled → Location data discarded.

---

### Geo-Matching Algorithm

**Not radius-based — corridor-based**:

Standard geo-matching: "Show tasks within 500m of agent's current location" → misses tasks that are on the agent's path but 600m away; shows tasks that are 300m away but require a 10-minute detour.

**Corridor matching**:
1. Compute fastest walking/transit route from origin to destination (Google Maps Directions API or Apple Maps API)
2. Buffer the route polyline by 300–500m on each side (configurable) → creates a corridor
3. Find all task coordinates within the corridor polygon
4. For each task in corridor, compute "detour cost": additional distance/time the agent would need to walk to the task vs. staying on the direct route
5. Rank tasks: Payout / (1 + detour_coefficient) — tasks on the direct route rank highest; tasks requiring detours are discounted proportionally
6. Surface top 5 ranked tasks to the agent

**Example**: Agent walking from Hackney to Kings Cross.
- Task A: Sainsbury's Caledonian Road — directly on route, 0% detour. Rank: £5.00 / 1.0 = 5.0
- Task B: Waitrose Islington — 3 minutes off route. Rank: £8.00 / 1.3 = 6.15 (higher payout compensates for detour)
- Task C: Co-op Farringdon — 8 minutes off route. Rank: £6.00 / 1.8 = 3.33 (not worth it unless agent has time)

---

### Privacy-Preserving Route History

**The risk**: Storing agent route histories creates persistent location profiles that could be sensitive (revealing home address, daily patterns, medical facility visits).

**Privacy-preserving design**:
1. **On-device route computation**: Route computation happens on-device using the phone's maps APIs. The full route polyline is never sent to Mosaic's servers — only the list of task IDs that match the route.
2. **Ephemeral route data**: The route is stored in app memory only, cleared when the trip ends (destination reached or user closes commute mode).
3. **Frequent location data**: The app uses GPS only at the moment of declaring a trip (origin) and at task completion points (geofenced trigger). Between these moments, GPS is not accessed.
4. **Historical pattern learning (opt-in)**: After 5+ commutes, the app offers to "remember your routes" to pre-stage tasks. This is explicitly opt-in, stored locally on device only (not synced to servers), and deletable at any time.
5. **No server-side behavioral profiles**: Mosaic's backend knows which tasks were completed at which locations and times — not the agent's full daily movement pattern.

**GDPR compliance for route data**: This design satisfies the data minimization principle (Article 5(1)(c)) — only the minimum location data necessary for task matching is processed. The on-device computation means personal route data never leaves the device.

---

### Battery and Data Cost

**The concern**: Any location-aware app risks excessive battery drain and data usage, which causes users to uninstall.

**Mosaic's low-impact design**:
- GPS active only during: (a) trip declaration (1 second), (b) geofence crossing (0.5 seconds), (c) task completion verification (2 seconds)
- Total daily GPS active time for a commute-mode agent: < 10 seconds
- Background location mode: uses "significant location change" API (iOS/Android), which wakes the app only when the phone moves 500+ meters — battery cost ≈ 0
- Geofencing: uses native iOS/Android geofence APIs (1–5 regions maximum), which are extremely battery-efficient (vendor-tested: <0.1% additional battery drain per monitored region)
- Data usage: route corridor computation = 1 API call ≈ 2–5KB. Total data per commute session: <20KB. Negligible.

**Comparison**: Uber driver app in active mode uses 30–50MB data/hour and 15–20% battery/hour. Mosaic's commute mode uses <1MB data/day and <1% battery/day.

---

### Integration with Existing Task Assignment System

**Current system (assumed)**: Task posted by customer → stored in database with coordinates, deadline, requirements → assigned to best available nearby agent via push notification.

**Commute mode integration**:
- New API endpoint: `GET /tasks/route-corridor?origin=[lat,lon]&destination=[lat,lon]&buffer=500`
- Returns: ranked list of tasks within route corridor, with detour cost
- New task state: `pre-accepted` — agent has accepted before traveling; task is reserved for them; removed from general pool
- Pre-acceptance window: 12 hours (tasks can be pre-accepted the night before for morning commute)
- Fallback: if pre-accepted agent doesn't complete within 30-minute window of task location, task re-enters pool

**Database schema addition**: Task table gains `pre_accepted_by`, `pre_accepted_at`, `expected_completion_window` fields.

---

## Part 4: The Daily Commuter Agent Persona

### Profile: Maya, 28, London

**Background**: Maya is a junior marketing coordinator at a media agency in Shoreditch. She earns £32,000/year and lives in Hackney. She commutes by tube and walking — 35 minutes each way. She has Deliveroo and TaskRabbit on her phone but uses them inconsistently. She found Mosaic through an Instagram ad: "Earn £15 during your morning commute."

**Commute**: Hackney Central station → tube (Overground) → Old Street → 8-minute walk to Shoreditch office.

**Her Mosaic morning routine**:
- 7:52am — wakes up, phone notification: "3 tasks along your commute. Est. earnings: £14.50. Accept before 8:30am."
- 7:54am — opens Mosaic, reviews tasks: Sainsbury's on Kingsland Road (2 min walk, on her route), Boots Pharmacy near Old Street Station (on route), Pret on Shoreditch High St (30 sec, 20m off route)
- 7:55am — accepts all 3 with one tap. Total: £14.50. Goes back to getting ready.
- 8:31am — passes Sainsbury's. App pings: "Task ready. Start?" Opens Mosaic, enters store, takes 4 photos of the oat milk section per instructions. 75 seconds. AI validates photos. Task complete. £6.00 earned.
- 8:42am — exits Old Street station. App pings: "Boots task. Start?" Checks product availability for Dettol hand soap in pharmacy. 50 seconds. Task complete. £4.50 earned.
- 8:51am — walks past Pret. App pings: "Crowd level check. 20 seconds." Takes a 360 video pan of the cafe interior. Done. £4.00 earned.
- 9:01am — arrives at office. Total earned: £14.50. Time spent on tasks: ~4 minutes.

**End-of-week view**: Maya does this 4–5 days/week. She earns £55–75/week, £220–300/month, with zero dedicated time beyond what her commute already required. She's one of Mosaic's highest-retention agents because the app delivers on its promise consistently.

---

### Maya's LTV Calculation

Monthly earnings: £240 (blended, some months higher)
Monthly tasks completed: 60 (3 tasks/day × 5 days/week × 4 weeks)
Platform contribution per task: £2.50 (above direct payout cost)
Monthly platform contribution from Maya: £150

Annual platform contribution: £1,800
CAC to acquire Maya: £20 (Instagram ad + welcome bonus)
**Maya's LTV:CAC = 90:1**

Maya stays because the product works perfectly for her lifestyle. She doesn't think of herself as a "gig worker" — she thinks of herself as someone who "earns money on her commute." This identity is sticky in a way that "gig worker" identity is not.

---

### The Daily Commuter Cohort

Agents like Maya are Mosaic's highest-value segment:
- **Retention**: 75%+ monthly retention (vs 45% platform average) because earnings are tied to existing behavior, not additional effort
- **Earnings density**: Complete 3–5 tasks/day vs 0.5 tasks/day for opportunistic agents
- **Task quality**: Pre-planned tasks result in better photo quality (agent is mentally prepared, not rushing)
- **Word of mouth**: "I earn £200/month on my commute" is a story Maya tells her friends — unlike "I occasionally complete random photo tasks"

**Acquiring commuter agents**: Target Facebook/Instagram ads at "London commuters," "people who commute by train/tube," commuter-focused communities. Message: "Turn your morning commute into £50/week."

**Commuter onboarding flow**: New agent → select "I have a regular commute" → enter commute route → see estimated monthly earnings → complete first commute-mode task → retain.

---

## Part 5: Commute Mode Economics Model

### Platform Cost Reduction vs Dispatched Model

| Metric | Dispatched Model (competitor) | Mosaic Commute-Match | Improvement |
|--------|------------------------------|---------------------|-------------|
| Agent travel cost (implicit) | $8–15/trip | $0 | 100% savings |
| Surge pricing frequency | 30% of tasks | 8% of tasks | 73% reduction |
| Fulfillment rate | 72% | 91% | +26 points |
| Tasks/agent/day | 1.2 | 3.8 | +217% |
| Effective cost/fulfilled task | $18 | $8 | -56% |
| Agent monthly retention | 38% | 67% | +76% |

**The bottom line**: Route-matched commute tasks cost Mosaic 56% less per fulfilled task than dispatched gig tasks. This is the efficiency advantage that enables micro-task pricing and still maintains 55%+ gross margin.

### Why Competitors Can't Copy This Quickly

The "already going there" model requires:
1. **Trip intent UX** — a fundamentally different app design from task-reactive interfaces
2. **Route corridor matching** — geospatial algorithm that's different from radius matching
3. **Pre-acceptance infrastructure** — changes task state machine throughout the backend
4. **Consumer trust** — agents must trust that pre-accepting tasks will yield results (requires consistent fulfillment of pre-staged tasks)
5. **Task density** — only works when there are enough tasks in a metro area to fill route corridors (requires critical mass)

Field Agent and BeMyEye are enterprise-focused dispatch platforms. They don't have the consumer product to build this. DoorDash/Uber could build it, but they haven't — and Mosaic will have first-mover advantage with consumer agents before they notice.
