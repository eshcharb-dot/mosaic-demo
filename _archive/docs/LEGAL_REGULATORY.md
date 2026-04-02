# Pixie — Legal & Regulatory

## Executive Summary

Pixie operates in a legally complex space at the intersection of privacy law, gig economy regulation, and image capture rules. The platform's core legal strategy is: **build privacy protection into the technical architecture** so that legal compliance is a technical fact, not a policy claim. On-device face redaction before upload is the foundational legal decision — it means the platform never processes biometric data, never creates a database of face images, and operates within the legitimate interest basis of every major privacy regime.

---

## Privacy Law: EU/UK — GDPR + UK GDPR

### Applicability
GDPR applies to any business processing personal data of EU residents, regardless of where the business is incorporated. Personal data = information that identifies or could identify a natural person. Photographs of identifiable people = personal data. Photographs with faces blurred = not personal data in most interpretations.

### Key Provisions

**Article 6 — Lawful Basis**
Pixie requires a lawful basis for any residual data processing:
- Agent submissions: Contractual necessity (agent agreed to T&C) + legitimate interest
- Customer task data: Legitimate interest (business intelligence collection in public spaces)
- Face data: NOT processed — eliminated at capture (redaction)

**Article 9 — Special Categories (Biometric Data)**
Biometric data (data processed to uniquely identify a natural person) requires explicit consent. On-device face blurring before upload means Pixie never processes biometric data — there is no face data to process. This is the legal architecture's most important property.

**Article 17 — Right to Erasure**
Solution: 30-day automatic raw image deletion policy. Structural data (SKUs, prices, counts) retained but contains no personal data. Agent submissions retain only the cryptographic hash, not the underlying image, after deletion window.

**Article 28 — Controller-Processor Agreements**
All enterprise customers must sign a Data Processing Agreement (DPA) before accessing the platform. Template DPA developed with privacy counsel.

**Article 35 — Data Protection Impact Assessment (DPIA)**
Required before launch in EU. Document: what data processed, why, risks, mitigations. On-device redaction is the key risk mitigation — document it explicitly.

### GDPR Compliance Checklist
- [ ] Privacy attorney review of Terms of Service + Privacy Policy
- [ ] DPA template for all customers (required before EU launch; best practice from Day 1)
- [ ] Data Protection Officer (DPO) appointed (can be founder initially)
- [ ] DPIA completed and documented
- [ ] Agent consent flow: explicit, specific consent to each task type
- [ ] Cookie policy (if web dashboard uses tracking)
- [ ] 72-hour data breach notification procedure documented

### EU Launch Readiness
- UK: Year 2 (UK GDPR, similar to EU, more pragmatic enforcement)
- Netherlands/Nordics: Year 3
- France (CNIL pre-authorization risk) / Germany (strict BDSG): Year 4

---

## Privacy Law: United States

### CCPA (California Consumer Privacy Act)
**Applicability**: Applies if >$26.625M gross revenue OR processes >100,000 CA residents' data/year.

Key points:
- Photographs ≠ biometric data under CCPA **unless** used for facial recognition. On-device redaction prevents facial recognition use = CCPA biometric provisions do not apply.
- Applies to California residents' data. If Pixie has California agents, CCPA applies from launch.
- New regulations effective January 1, 2026 expand requirements — privacy counsel review required.
- **Action**: Privacy policy must list all data categories collected. Agent data: identifiers, geolocation, commercial information (earnings).

### BIPA — Illinois Biometric Information Privacy Act
**THE HIGHEST US LEGAL RISK**

BIPA prohibits collecting biometric identifiers (face geometry, retina scans, fingerprints) without written consent, notice, and a retention/destruction policy. Statutory damages: $1,000 per negligent violation, $5,000 per intentional violation. Class action exposure is enormous (Facebook paid $650M settlement).

**Pixie's position**: On-device face blurring means no biometric data is ever collected or transmitted. Technically, BIPA does not apply — no biometric data is created.

**Risk**: Litigation risk even if technically compliant. Plaintiffs' attorneys may argue that the on-device detection process itself (even if it outputs only a blur, not a faceprint) constitutes "collection."

**Mitigation strategy**:
1. Delay Illinois launch to Year 2 (after legal opinion obtained)
2. Obtain Illinois-specific legal opinion on on-device detection scope
3. In Illinois, add explicit in-app notice: "No biometric data is collected or stored by Pixie. Our privacy protection technology blurs faces on your device before any data is transmitted."
4. Explore: having Illinois agents opt into an additional consent specifically disclosing the on-device face detection step.

### Texas, Washington, Other State Biometric Laws
Texas CUBI (Capture or Use of Biometric Identifier): Similar to BIPA. On-device redaction mitigation applies.
Washington My Health MY Data Act: Biometrics covered. Same mitigation.

**Strategy**: Launch in states without biometric-specific laws (Georgia, Florida, Tennessee, Texas after legal review, Colorado, Arizona) before expanding to Illinois, Washington, Massachusetts.

---

## Photography in Public Spaces

### United States
**General rule**: Photography in public spaces is protected by First Amendment. Commercial photography of publicly visible subjects (storefronts, products on shelves, street scenes) is generally legal.

**Limitations**:
- Private property: Store owners can prohibit photography inside their stores. Agents operating without store permission are in a legal gray area — see "In-Store Access" section below.
- Expectation of privacy: Photographing in spaces where people have a reasonable expectation of privacy (bathrooms, changing rooms) is illegal. This never applies to Pixie's use cases.
- One-party consent for video/audio: Federal law allows recording conversations where one party consents. Most states match. All-party consent states (California, Illinois) — Pixie tasks should not capture audio.

### United Kingdom
No general right to prevent photography in public places. Commercial photography of public spaces (storefronts, street scenes) is legal. UK GDPR applies to identifiable images — face redaction resolves this.

### European Union
Varies by country. Key principle: photography of public spaces for legitimate commercial purposes is generally permitted under legitimate interest basis, subject to GDPR requirements for personal data.

---

## In-Store Access

### The Problem
Agents capturing shelf data inside private retail stores face a legal question: does the store owner's "no photography" policy or property rights give them grounds to ban/sue agents?

### Legal Analysis
US retail stores are generally open to the public. While stores can ask people to stop photographing, they typically cannot pursue legal action for a single-visit customer who photographs products (trade secret law protects confidential business information, not publicly displayed prices and products). Mystery shopping (taking notes, photos of publicly visible products) has been a standard, unchallenged practice for 50+ years.

### Risk Assessment
- **Competitor price checks** (photographing a competitor's shelf): Very low risk. You're photographing their competitor's products, displayed for public purchase.
- **Own-brand shelf audits** (photographing your own products in a store you didn't place them): Low risk. CPG brands have long visited their own products in stores.
- **Store operational data** (employee behavior, traffic patterns): Higher risk — store owners have more grounds to restrict this.

### Solutions

**Option 1 — Mystery Shopper Framework** (Year 1)
Agents register as "independent market researchers." They enter stores as regular customers, make a small purchase ($1–5 items), and capture task photos. This is identical to how Field Agent, mystery shopping agencies, and market research firms have operated for decades. Legal challenge: near-zero based on industry history.

**Option 2 — Retailer Partnership Program** (Year 2+)
Retailers become Pixie customers AND grant agent access permissions. Retailer pays Pixie to monitor their own store network; CPG brands access data through retailer authorization. This inverts the access problem — agents have explicit permission.

**Option 3 — Competitor-Only Mode** (always available)
Tasks only photograph competitor products, not the host store's own operations. Lowest sensitivity.

**Year 1 strategy**: Primarily Option 1 + Option 3. Begin Option 2 conversations in Month 6.

---

## Gig Worker Classification

### United States

**Federal law**: No federal classification law for gig workers. IRS test for independent contractor focuses on behavioral control, financial control, and relationship type.

**California AB5**:
- ABC test: (A) free from company control, (B) performs work outside company's usual course of business, (C) independently established trade
- Pixie position on each prong: (A) agents choose their own hours, locations, tasks — YES; (B) Pixie's business is the platform/AI, not photography itself — arguable; (C) agents can and do work for other platforms simultaneously — YES
- Prop 22 (app-based gig platforms exemption): Pixie should qualify if it meets the "app-based transportation or delivery network company" definition — legal review required.
- **Strategy**: Launch in non-California states first (Georgia, Texas, Florida). Obtain California-specific employment law opinion before California launch.

**Other states**: Most US states have more lenient independent contractor definitions than California. Texas, Florida, Georgia: low classification risk.

### European Union
EU Platform Work Directive (adopted 2024): Rebuttable presumption of employment for platform workers in EU. Pixie must demonstrate: agents set their own rates (no — platform sets rates), choose their own clients (no — platform routes tasks), not subject to exclusivity (yes — agents can use other platforms), not subject to disciplinary power (yes — Pixie can deactivate accounts but not fire "employees"). This is legally complex. **EU launch requires specific legal analysis per country**.

### UK
UK Supreme Court (Uber BV v Aslam, 2021) established that Uber drivers are "workers" (intermediate category). Pixie's model may face similar classification risk in UK. Legal review required before UK launch.

### Compliance Actions
- Clear Independent Contractor Agreement at agent sign-up
- No exclusivity requirements (agents can use competing platforms)
- Agents set their own availability (no scheduling requirements)
- Platform cannot "fire" agents — only deactivate accounts for policy violations
- 1099-NEC filing (US) for agents earning >$600/year
- No employee benefits, no minimum hours guarantee

---

## IRS / Tax Compliance

**1099-NEC requirement**: Any US agent earning >$600 in a calendar year must receive a Form 1099-NEC.
- Hyperwallet handles automated 1099 generation
- Agents must provide SSN or EIN at sign-up (IRS requirement for 1099 issuance)
- For foreign agents: W-8BEN form required

**AML/KYC**: Payment processors require Know Your Customer checks for payouts. Hyperwallet provides this as part of their platform.

---

## Data Retention Policy

| Data Type | Retention Period | Rationale |
|---|---|---|
| Raw images (original) | 30 days | GDPR Art. 5(1)(e) data minimization; configurable per customer |
| Redacted images | 90 days | Customer access window |
| AI extraction results (structured data) | Indefinite | No PII; core product data |
| Cryptographic proof chain | Indefinite | Audit + legal evidence purposes |
| Agent GPS records | 90 days | Task verification purposes only |
| Agent PII (name, address, SSN) | Duration of account + 7 years | Tax compliance (IRS requirement) |
| Customer PII | Duration of contract + 3 years | Contractual + tax |

---

## Pre-Launch Legal Checklist

### Must Be Complete Before Launch (Month 0)
- [ ] Privacy Policy drafted + reviewed by privacy attorney (US + GDPR compliant)
- [ ] Agent Terms of Service + Independent Contractor Agreement reviewed
- [ ] Customer Terms of Service + Data Processing Agreement template
- [ ] Agent consent flow: specific consent to task types, redaction disclosure, data use
- [ ] On-device redaction tested on 50+ device models (Samsung, Apple, Google, OnePlus)
- [ ] Stripe + Hyperwallet accounts active and tested
- [ ] IRS EIN obtained, 1099 process documented
- [ ] No-audio mode enabled by default (for all-party consent states)
- [ ] Incident response procedure documented

### Year 1 Compliance Goals
- [ ] SOC 2 Type I by Month 9
- [ ] SOC 2 Type II by Month 15
- [ ] BIPA legal opinion obtained before Chicago launch
- [ ] GDPR DPA template finalized (for EU-headquartered enterprise customers)
- [ ] Penetration test (external firm) by Month 6
- [ ] Quarterly privacy audit by Month 12

### Year 2 Goals
- [ ] UK launch: UK GDPR compliance audit
- [ ] FedRAMP process initiated (for government customers)
- [ ] EU GDPR full compliance documentation
- [ ] California AB5 / Prop 22 legal opinion for CA launch
