# Mosaic — Master Improvement Log V1
*Compiled: April 2, 2026*

This is the living document for all known bugs, missing features, quality gaps, and strategic improvements across all Mosaic deliverables. Prioritized by impact. Every item should be resolved before first VC meeting.

---

## STATUS DASHBOARD

| Asset | Version | Status | Quality |
|---|---|---|---|
| MOSAIC_DEMO.html | V6+ | Live (GitHub Pages) | 7/10 |
| MOSAIC_PITCH_V4.html | V4 | Local only | 7/10 |
| MOSAIC_PITCH_V4.pdf | V4 | Local only | 7/10 |
| deck-assets/ | Mixed | 35 images | 8/10 |

---

## PITCH DECK (MOSAIC_PITCH_V4.html)

### BUGS
- [ ] **Team slide placeholders**: `[CEO Name]` / `[CTO Name]` — must be filled before any VC meeting
- [ ] **Cover slide demo link** points to GitHub Pages — confirm the URL is correct and the page loads
- [ ] **Print CSS**: `✓` and `→` characters in PDF generation fail on Windows cp1252 encoding — use `generate_pitch_pdf.py` which already handles this via Playwright (no encoding issue)
- [ ] **Slide 3 tag div wrapping** — added `z-index:1` wrapper which may affect layout if tag div had original position:relative flow

### VISUAL IMPROVEMENTS (HIGH PRIORITY)
- [x] **All slides**: Every slide now has a subtle background image — s3-s13 all have deck-assets bg images at 3-7% opacity with gradient fade overlays
- [x] **Slide 5 Product**: Panel images at 230px + subtle shelf-scan-v2 bg at 3% opacity
- [ ] **Slide 6 Market**: The TAM/SAM/SOM circles are CSS-only — a proper market visualization graphic would be stronger
- [x] **Slide 10 Competition**: Brand-colored competitor chips + glow dots + moat callout added; London map bg at 3%
- [ ] **Slide 11 Team**: Both founders are placeholders with no photos — add headshots or abstract avatars once team is confirmed
- [x] **Slide 12 Financials**: SVG bar chart M3→M24 revenue trajectory added + data-flywheel bg

### CONTENT IMPROVEMENTS
- [ ] **GTM slide (s9) — customer names**: First Unilever/Reckitt conversation "by Month 3" is aspirational — ensure this is either replaced with confirmed LOIs or clearly flagged as pipeline
- [ ] **Traction slide (s8)**: "First enterprise pilots in active conversations" — be ready to name the companies or explain why you can't
- [ ] **Financials slide (s12)**: Needs a sanity check on the unit economics row — GPT-4V pricing has changed in 2026; verify $0.20/image is still accurate
- [ ] **Ask slide (s13)**: Term sheet details (valuation cap, pro-rata rights) are missing — add or explicitly note "terms TBD"
- [ ] **Slide 1 Cover**: Replace `mosaic-intel.com` with actual live domain once purchased/set up; currently the domain doesn't exist

### MISSING SLIDES
- [ ] **Product video/demo slide**: Consider inserting a "Live Demo" slide with QR code + screenshot linking to MOSAIC_DEMO.html after Slide 5
- [ ] **Customer quote slide**: Even a single attributed pilot customer quote changes investor perception dramatically
- [ ] **GDPR / Risk slide**: Investors will ask about privacy. Consider a brief "Risk Mitigation" appendix slide

---

## DEMO (MOSAIC_DEMO.html)

### BUGS
- [ ] **Gallery filter count**: When switching to 'Compliant' filter, count shows `5` correctly — verify 'Warning (2)' and 'Critical (2)' also count correctly after JS filter runs
- [ ] **E1 Dashboard mini-bars animation**: The `transform: scaleY(0) → scaleY(1)` animation only triggers on `e-screen.active`. If the user switches to Collector and back to Enterprise, the bars may not re-animate since the screen is already visited. Add animation reset on screen enter.
- [ ] **payout counter animation**: `payoutAnimated` flag is set `true` after first visit and never resets — so if user goes back to payout screen, no animation plays. Reset on screen enter.
- [ ] **Mobile: Enterprise desktop frame overflow** - On screens < 860px wide, the enterprise desktop frame (min 1060px) overflows. The existing mobile banner warns users but doesn't prevent the layout break.
- [ ] **Keyboard hint disappears after 4s** — fine for desktop demo, but on mobile the hint shows before user can read it. Consider longer timeout or touch-aware triggering.

### VISUAL IMPROVEMENTS (HIGH PRIORITY)
- [x] **C1 Onboarding — commute route visual**: Inline SVG route map with animated traveling light dot, Home + Office pins, and 3 task stops showing +£5 each added to Commute Mode card
- [x] **C5 Camera — scanning progress bar**: Progress bar fills to 100% over 2s when entering screen; badge updates from "Detecting" → "Shelf identified" → "3 products detected · 1 gap found"; shutter button activates with cyan glow
- [ ] **C6 AI Verify — results appear instantly**: In reality, AI takes a few seconds. Add a 2-second animated "Analysing…" state (spinner + partial results filling in) before showing the final results card for demo realism.
- [ ] **E2 Campaign Creator — Launch button does nothing**: The "Launch Campaign →" button has no feedback. Add a success toast / confirmation state when clicked.
- [ ] **E5 Alert Center — action buttons do nothing**: "Dispatch Rep" / "Auto-Replenish" buttons have no interaction. Add a "✓ Action taken" feedback state.
- [ ] **E6 Compliance Report — table is static**: The compliance table is static HTML. Make rows clickable (open store gallery detail).

### CONTENT IMPROVEMENTS
- [ ] **Collector name "Maya Chen"** in task feed — ensure this is consistent with gallery credits (currently "Maya C." in gallery, "Maya Chen" in task feed — consistent)
- [ ] **Task payout amounts** — currently showing USD ($14.50). UK market should show GBP (£14.50). Decide on currency and be consistent across the demo.
- [ ] **Enterprise sidebar shows "Meridian Foods Ltd."** — good fictional client. But the demo link from pitch deck says "Oat+" brand. Clarify whether Meridian Foods IS the brand or the manufacturer.
- [ ] **E3 Live Map** — the map shows London correctly but the dots are clustered in one area. Spread them across more of Greater London for a more impressive coverage visual.
- [ ] **Gallery: Two Sainsbury's use the same base image** (sainsburys-v1.png with different CSS filters) — ideally 2 different photos. Once more images are available, swap one.

### MISSING FEATURES
- [x] **Demo tour mode**: "▶ Demo Tour" button in header auto-advances all 14 screens (8 collector + 6 enterprise) every 7s; turns red to stop; stops on manual navigation
- [x] **"Back to top" on enterprise screens**: Floating ↑ button appears at bottom-right after 80px scroll; smooth scroll to top on click.
- [ ] **Share/export link for enterprise report**: The compliance report (E5) has no export or share button. Add a fake "Export PDF" button with a toast notification.
- [ ] **Payout history on C8**: The earnings dashboard shows $847.50 but no transaction history. Add a recent transactions list (last 5 tasks with time/location).
- [ ] **Deep link to specific screens**: No URL routing — demo always starts at C1. Consider adding `#enterprise-map` anchor support.
- [ ] **404 fallback for missing images**: Some images (mosaic-store-worker-v2.png etc) may not be accessible on GitHub Pages. The `onerror` fallbacks are good but the CSS shelf fallbacks aren't always styled well — audit all image fallback states.

---

## DECK ASSETS (deck-assets/)

### MISSING IMAGES (needed but not generated)
- [ ] **mosaic-team-ceo-v1.png** — CEO headshot / avatar for Team slide
- [ ] **mosaic-team-cto-v1.png** — CTO headshot / avatar for Team slide
- [ ] **mosaic-timeline-roadmap-v1.png** — Visual 24-month roadmap for GTM slide
- [ ] **mosaic-unit-economics-v1.png** — Visual unit economics breakdown for Business Model slide
- [ ] **mosaic-data-flywheel-visual-v1.png** — Proper flywheel diagram (currently text-only in slide 9)

### IMAGE QUALITY ISSUES
- [ ] **mosaic-shelf-scan-v2.png** — Check if this is different enough from v1. If they're near-identical, the gallery demo loses visual variety.
- [ ] **mosaic-store-worker-v2.png** — Verify the person is clearly a customer / shopper, not a store employee (Mosaic collectors blend in as shoppers)
- [ ] **mosaic-payout-screen-v1.png** — Check if the payout amount shows GBP or USD. Should match currency chosen for demo.
- [ ] **mosaic-app-ui-v1.png** — Check the UI shows a dark, professional task card consistent with demo design language.
- [ ] **mosaic-enterprise-dashboard-v1.png** — Used in slide 5. Check it reads clearly at 230px wide (the panel-img size).

### DESIRED NEW ASSETS
- [ ] **mosaic-commute-animation** — Animated GIF or video showing a person's commute path with tasks appearing along the route
- [ ] **mosaic-shelf-before-after-v1.png** — Side-by-side: empty shelf (red score) vs restocked shelf (green score). Very powerful for investor conversations.
- [ ] **mosaic-competitor-grid-v1.png** — Visual grid of competitor logos vs features. Currently text table in slide 10.

---

## DISTRIBUTION & DEPLOYMENT

### NOT YET DONE
- [ ] **Deploy MOSAIC_PITCH_V4.html to GitHub Pages**: Currently local only. Should be at `eshcharb-dot.github.io/mosaic-demo/MOSAIC_PITCH_V4.html`
- [ ] **Generate updated PDF** after visual improvements: `python generate_pitch_pdf.py` — run again after all pitch deck changes
- [ ] **Cover page link update**: Slide 1 shows `mosaic-intel.com` — either buy and forward this domain or update to the GitHub Pages demo URL
- [ ] **Password protection**: The demo and deck are publicly accessible. Before sending to VCs, consider adding a simple JS password gate or moving to a private link.

### INVESTOR SEND PACKAGE
- [ ] One-pager (500 words): Problem, Solution, Traction, Ask, Contact. Not yet written.
- [ ] Executive summary email template (2 paragraphs + deck link)
- [ ] CalendlyLink / Zoom link for follow-up meetings

---

## STRATEGIC GAPS (Big Picture)

### BEFORE FIRST VC CONVERSATION
- [ ] **Define the team clearly**: VCs will ask "who are you?" immediately. The deck has `[CEO Name]` and `[CTO Name]`. Even if using aliases for now, prepare a verbal answer.
- [ ] **One signed LOI or pilot agreement**: Even a non-binding letter of intent from one CPG brand transforms the deck from "idea" to "traction." BeMyEye's sales team can be targeted.
- [ ] **Agent waitlist**: Build and show a waitlist landing page. Even 200 signups with email addresses is early social proof.
- [ ] **Live product or testable prototype**: The demo is excellent but a live hosted demo URL (not just GitHub Pages) with a real task flow adds credibility.

### MONETIZATION VALIDATION
- [ ] Run a paid pilot: Post 5 real tasks to 5 agents and have them complete real shelf audits. Even if done manually, it validates the economic model.
- [ ] Price test: Get 3 CPG brand managers to respond to a cold outreach with pricing info. Any response at all is signal.

---

## COMPLETED (This Session)
- [x] Fixed enterprise dashboard blank at startup (setMode calls goScreen)
- [x] Fixed live map (removed conflicting layers, used London map image)
- [x] Built gallery with 9 unique items + modal detail
- [x] Built task detail (C4) with location card + mini-map
- [x] Built task feed (C2) with commute mode banner + address details
- [x] Fixed dev browser tab accumulation (closeOldTabs + explicit DELETE)
- [x] Made PITCH slide 2 (Problem) visual with shelf image split layout
- [x] Made PITCH cover bg-img more visible (0.07 → 0.18 opacity)
- [x] Made PITCH slide 5 product images bigger (120px → 230px)
- [x] Added London map to E1 dashboard map panel
- [x] Enhanced C1 onboarding with Commute Mode feature card
- [x] Added subtle background visuals to slides 3 and 8
