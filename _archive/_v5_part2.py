content = open(r'C:/Users/user/projects/PR-001_agentic-ventures/projects/pixie/MOSAIC_V5.html', 'r', encoding='utf-8').read()

section2 = """
<!-- USE CASES -->
<section class="section" id="usecases">
  <div class="section-label">The Beachhead</div>
  <h2 class="section-h"><span class="grad">Three Problems.</span> One Platform.</h2>
  <p class="section-sub">We don't have 72 use cases. We have three, and they all sell to the same buyer with the same budget. This is how we win the CPG field intelligence market.</p>

  <div class="big-callout">
    <div class="bq">Mosaic gives CPG brand managers what they have never had &mdash; <em>real-time eyes on their shelves, their out-of-stocks, and their competitors' prices</em> &mdash; at $12&ndash;$45 per store check versus $150&ndash;$300 from current providers. In 4 hours instead of 2 weeks.</div>
    <div class="bsrc">The 10-second pitch. Everything below is the proof.</div>
  </div>

  <!-- UC 1 -->
  <div class="uc-card uc1">
    <div class="uc-card-header">
      <div class="uc-card-num">Use Case 01 &middot; CPG Shelf Intelligence</div>
      <div class="uc-card-title">Shelf Compliance Audits</div>
      <div class="uc-card-tagline">You paid for that end-cap. Is it actually there? A brand with 4,200 stores and 12 field reps has 19% coverage. Mosaic gives them 100%.</div>
      <div class="tag-row" style="margin-top:14px;margin-bottom:0">
        <span class="pill pill-p">$60K ACV</span><span class="pill pill-t">4-Hour SLA</span><span class="pill pill-g">60% Pilot-to-Annual</span><span class="pill pill-y">$12-25/store</span>
      </div>
    </div>
    <div class="uc-card-body">
      <div class="uc-col">
        <h4>The Buyer</h4>
        <div class="persona-inline">
          <div class="persona-avatar">D</div>
          <div class="persona-info">
            <div class="persona-name">Daniela Santos</div>
            <div class="persona-role">National Field Sales Manager &middot; $500M CPG Brand</div>
            <div class="persona-quote">"I can't see my shelves. I have 4,200 stores and 12 people. The math doesn't work."</div>
          </div>
        </div>
        <p>Daniela controls a field intelligence budget of <strong>$200K&ndash;$2M/year</strong>. She paid $85K for an end-cap during the Super Bowl window. 60 of 300 stores placed product two aisles from the agreed position. She found out three weeks later from scan data. <strong>$170K in promotional lift, gone.</strong></p>
        <p>Distributor-submitted compliance photos: 4&ndash;6 weeks old, often staged. Industry estimates put the discrepancy rate at <strong>30&ndash;40% versus actual shelf conditions</strong>.</p>
        <p>Decision trigger: a missed end-cap, a distributor dispute, a retailer deduction claim. Sales cycle: <strong>30&ndash;60 days for pilot</strong>. Annual contract follows successful pilot.</p>
      </div>
      <div class="uc-col">
        <h4>The Workflow</h4>
        <div class="workflow">
          <div class="wf-step"><div class="wf-num wn1">1</div><div class="wf-text"><strong>Upload</strong> planogram + SKU list. Define compliance criteria. Select 50 stores. Post with 4-hour SLA.</div></div>
          <div class="wf-step"><div class="wf-num wn2">2</div><div class="wf-text"><strong>Route-match</strong>: algorithm assigns each store to 1&ndash;2 collectors already on their morning commute near that location.</div></div>
          <div class="wf-step"><div class="wf-num wn1">3</div><div class="wf-text"><strong>Capture</strong>: 45&ndash;90 seconds in-store, 3 photos. On-device AI validates quality before upload. No faces captured.</div></div>
          <div class="wf-step"><div class="wf-num wn2">4</div><div class="wf-text"><strong>Deliver</strong>: Within 4 hours &mdash; compliance score per store (0&ndash;100%), AI-extracted JSON, photos sorted worst-first.</div></div>
        </div>
        <div class="highlight" style="margin-top:20px">
          <p><strong>Pilot ROI:</strong> 50 stores, 4 weeks. Cost $1,500&ndash;$3,000. If 8 stores (16%) are non-compliant at $400/week missed promotional lift, that is <strong>$12,800 in recovered value. 8x ROI in 30 days.</strong></p>
        </div>
      </div>
    </div>
    <div class="uc-card-footer">
      <div class="uc-foot-stat"><div class="ufn">$60K</div><div class="ufl">Annual Contract Value</div></div>
      <div class="uc-foot-stat"><div class="ufn">$25/store</div><div class="ufl">Blended Task Price</div></div>
      <div class="uc-foot-stat"><div class="ufn">60%</div><div class="ufl">Pilot-to-Annual</div></div>
      <div class="uc-foot-stat"><div class="ufn">$1.5M ARR</div><div class="ufl">Year 1 Potential</div></div>
    </div>
  </div>

  <!-- UC 2 -->
  <div class="uc-card uc2">
    <div class="uc-card-header">
      <div class="uc-card-num">Use Case 02 &middot; Inventory Intelligence</div>
      <div class="uc-card-title">Out-of-Stock Detection</div>
      <div class="uc-card-tagline">4&ndash;8% of CPG retail revenue evaporates to OOS events annually. Brands find out 5&ndash;10 days later. Mosaic detects it the same week it starts.</div>
      <div class="tag-row" style="margin-top:14px;margin-bottom:0">
        <span class="pill pill-y">$70K ACV</span><span class="pill pill-t">Same-Day Detection</span><span class="pill pill-r">70% Pilot-to-Annual</span><span class="pill pill-g">$18/check</span>
      </div>
    </div>
    <div class="uc-card-body">
      <div class="uc-col">
        <h4>The Buyer</h4>
        <div class="persona-inline">
          <div class="persona-avatar">M</div>
          <div class="persona-info">
            <div class="persona-name">Marcus Chen</div>
            <div class="persona-role">Category Manager &middot; $1B Ambient Grocery Brand</div>
            <div class="persona-quote">"I find out about OOS events after the damage is done. I need to see my shelves like I can see my website traffic &mdash; in near real time."</div>
          </div>
        </div>
        <p>Marcus owns performance across 2,300 Kroger locations. POS data: <strong>5 days old</strong>. Distributor reports: weekly and cherry-picked. Field reps cover 15% of locations on a 3&ndash;6 week cycle.</p>
        <p>A single OOS event &mdash; 200 stores, 10 days, $40/store/day velocity &mdash; is <strong>$800K in lost revenue</strong>. Research shows <strong>30&ndash;40% of shoppers switch brands permanently</strong> after failing to find their product twice.</p>
      </div>
      <div class="uc-col">
        <h4>The Workflow</h4>
        <div class="workflow">
          <div class="wf-step"><div class="wf-num wn1">1</div><div class="wf-text"><strong>Set up monitoring:</strong> 500 Kroger locations, 3 SKUs. Weekly automated sample of 80 stores via stratified algorithm.</div></div>
          <div class="wf-step"><div class="wf-num wn2">2</div><div class="wf-text"><strong>Monday 7am:</strong> 80 store tasks deployed. By 11am all 80 checked. Shelf status report on Marcus's desk by noon.</div></div>
          <div class="wf-step"><div class="wf-num wn1">3</div><div class="wf-text"><strong>Triggered surge:</strong> velocity decline 15%+ in a region triggers an emergency 50-store audit with 4-hour SLA. Same day. No phone calls needed.</div></div>
          <div class="wf-step"><div class="wf-num wn2">4</div><div class="wf-text"><strong>Output:</strong> "14/80 stores show OOS on SKU #3842. 9 of 14 are Dallas-Fort Worth. Suspected distributor issue." Data in hand for the distributor call.</div></div>
        </div>
        <div class="highlight" style="margin-top:20px">
          <p><strong>The killer demo:</strong> Ask Marcus which stores he thinks are in-stock. Run a same-day check on 20 of those stores. Call back in 4 hours. Typical result: <strong>15&ndash;25% discrepancy</strong>. That is the close. 70% pilot-to-contract &mdash; highest of the three use cases.</p>
        </div>
      </div>
    </div>
    <div class="uc-card-footer">
      <div class="uc-foot-stat"><div class="ufn">$70K</div><div class="ufl">Annual Contract Value</div></div>
      <div class="uc-foot-stat"><div class="ufn">$18/check</div><div class="ufl">Blended Task Price</div></div>
      <div class="uc-foot-stat"><div class="ufn">70%</div><div class="ufl">Pilot-to-Annual</div></div>
      <div class="uc-foot-stat"><div class="ufn">$2.8M ARR</div><div class="ufl">Year 2 from 40 Customers</div></div>
    </div>
  </div>

  <!-- UC 3 -->
  <div class="uc-card uc3">
    <div class="uc-card-header">
      <div class="uc-card-num">Use Case 03 &middot; Competitive Intelligence</div>
      <div class="uc-card-title">Competitive Pricing Scans</div>
      <div class="uc-card-tagline">Sophie's competitor ran a 20% discount at CVS Southeast for two weeks. She found out when it was over. Mosaic gives her that intelligence the day it launches.</div>
      <div class="tag-row" style="margin-top:14px;margin-bottom:0">
        <span class="pill pill-g">$250-300K ACV</span><span class="pill pill-t">Weekly Cadence</span><span class="pill pill-p">65% Pilot-to-Annual</span><span class="pill pill-y">$35/check</span>
      </div>
    </div>
    <div class="uc-card-body">
      <div class="uc-col">
        <h4>The Buyer</h4>
        <div class="persona-inline">
          <div class="persona-avatar">S</div>
          <div class="persona-info">
            <div class="persona-name">Sophie Lindqvist</div>
            <div class="persona-role">Director of Revenue Management &middot; $400M Premium Personal Care Brand</div>
            <div class="persona-quote">"I'm managing a live pricing market with data that's three weeks old. My competitor can react to my promotions in 48 hours. I can't react to theirs in 14 days."</div>
          </div>
        </div>
        <p>Sophie manages pricing across 6,200 retail points of distribution. Her quarterly competitive pricing audit returns data in <strong>10&ndash;14 days in Excel</strong>. Three things happened in that window: a competitor ran an undetected regional discount, a retailer violated her MAP policy, and Target repriced a competitor $2 below hers.</p>
        <p>Three distinct needs: <strong>competitive price monitoring, MAP violation detection, and promotional lift verification</strong> &mdash; all at premium extraction pricing ($35/check vs $150&ndash;$300 from current providers).</p>
      </div>
      <div class="uc-col">
        <h4>The Workflow</h4>
        <div class="workflow">
          <div class="wf-step"><div class="wf-num wn1">1</div><div class="wf-text"><strong>Upload brief:</strong> 5 Sophie's hero SKUs + 8 competitor SKUs. Target, Ulta, CVS. 150-store weekly sample. Tuesday 7am auto-deploy.</div></div>
          <div class="wf-step"><div class="wf-num wn2">2</div><div class="wf-text"><strong>Every Tuesday by 2pm:</strong> pricing dashboard updates &mdash; her prices vs. competitors by SKU, by retailer, by region. Competitor promotions flagged automatically.</div></div>
          <div class="wf-step"><div class="wf-num wn1">3</div><div class="wf-text"><strong>MAP enforcement:</strong> any shelf tag below MAP threshold triggers an automatic violation report with timestamped, geolocated, cryptographically-verified photo. Legal-grade documentation, instantly.</div></div>
          <div class="wf-step"><div class="wf-num wn2">4</div><div class="wf-text"><strong>Promo verification sweep:</strong> within 48 hours of a trade promo launch, 200-store check confirms the promotional price is live at shelf. Catch non-compliance before the promo window closes.</div></div>
        </div>
        <div class="highlight" style="margin-top:20px">
          <p><strong>Highest-ACV use case:</strong> Brands historically pay $150&ndash;$300/store visit for manual competitive pricing audits. Mosaic is <strong>4&ndash;8x cheaper and 40x faster</strong>. A brand using all three products reaches <strong>$200&ndash;$400K combined ACV.</strong></p>
        </div>
      </div>
    </div>
    <div class="uc-card-footer">
      <div class="uc-foot-stat"><div class="ufn">$280K</div><div class="ufl">Average Contract Value</div></div>
      <div class="uc-foot-stat"><div class="ufn">$35/check</div><div class="ufl">Premium AI Extraction</div></div>
      <div class="uc-foot-stat"><div class="ufn">$8.4M ARR</div><div class="ufl">30 Customers x $280K</div></div>
      <div class="uc-foot-stat"><div class="ufn">$400K</div><div class="ufl">Max ACV (All 3 Products)</div></div>
    </div>
  </div>

  <div class="highlight">
    <p><strong>The enterprise motion:</strong> Lead with shelf compliance (easiest pilot). Upsell OOS monitoring at Month 3 QBR. Introduce competitive pricing at Month 6 renewal. Three products. One account. <strong>$100K&ndash;$400K ACV by Year 2.</strong></p>
  </div>
</section>

<div class="divider"></div>
"""

with open(r'C:/Users/user/projects/PR-001_agentic-ventures/projects/pixie/MOSAIC_V5.html', 'a', encoding='utf-8') as f:
    f.write(section2)
print("Done section 2, length:", len(open(r'C:/Users/user/projects/PR-001_agentic-ventures/projects/pixie/MOSAIC_V5.html', encoding='utf-8').read()))
