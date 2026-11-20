# Audit & Upgrade Report

**Subject:** `hyderabad-buyer-portal/index.html` — Hyderabad Residential Buyer Portal
**Scope:** design, structure, interaction, accessibility, performance, content integrity
**Date:** 9 November 2026

---

## 1. Summary

The original portal was content-strong and structurally sound: a real buyer-first information
architecture, an honest commission disclosure, and working comparison and budget tools. Its
weaknesses were design and depth — a generic corporate look, no project or builder detail pages,
alert-driven interactions, a comparison table that showed empty columns, and a budget model that
mixed up "cash available" with "affordable property price".

The upgrade keeps the editorial substance, replaces the visual language entirely, adds routed
project and builder dossier pages, and fixes the functional and accessibility defects listed below.

| | Before | After |
| --- | --- | --- |
| Sections | 9 | 11 (adds dossier layer) |
| Design tokens | ~14 | ~60 (colour, type scale, radii, shadows, easing) |
| Project detail | none | routed dossier, 7 content blocks + gallery |
| Builder detail | none | routed dossier, 5 content blocks + scorecard |
| Comparison parameters | 9, with empty columns | 13, columns adapt to shortlist |
| Locality notes | 6 cards, price only | 8 notes + trend bars, pros/cons, verdict |
| Interactions using `alert()` | 4 | 0 (inline validation + toasts) |
| Persistence | none | shortlist saved to `localStorage` |
| Accessibility defects | 9 identified | 0 remaining (see §5) |

---

## 2. Findings — functional

| # | Finding | Severity | Resolution |
| --- | --- | --- | --- |
| F1 | Comparison table always rendered four columns; with fewer selections it showed "Project 2/3/4" headers and "—" rows. | High | Columns are generated from the shortlist; a two-project comparison renders two columns. |
| F2 | Comparison and shortlist were not persisted; a page refresh lost the selection. | Medium | `localStorage` persistence with validation against known project ids on load. |
| F3 | Locality cards called `selectLocality()`, which set a dropdown and then fired an `alert()` — the page did not actually navigate to anything. | High | Cards filter the project grid by corridor and scroll to it, with a toast confirming the count. |
| F4 | Filters were partly wrong: "East Hyderabad" mapped to `kokapet` (a west locality), and the budget filter used exact band equality so "above ₹2 Cr" excluded a plot priced per square yard. | Medium | Corridor mapping removed in favour of per-project `zone`; filters are explicit and testable. |
| F5 | Budget calculator compared EMI to income but added savings as if it were free cash; "Maximum Property Price" arrived before stamp duty, registration and corpus. | High | Model rebuilt: affordable *price* = (loan + savings) ÷ (1 + 6% duty + 1% corpus), with duty, corpus and the remaining cash buffer shown separately. |
| F6 | Site-visit form used `alert()` for validation and gave no feedback on which field failed. | Medium | Inline validation with a `role="alert"` message, field-specific copy, and a personalised confirmation. |
| F7 | Newsletter form posted nothing and confirmed with `alert()`; there was no indication it was a demo. | Low | Removed. Replaced by the guided-visit flow, which is honest about being a demo. |
| F8 | No project or builder detail content — every card was a dead end except a generic "Book Site Visit" anchor. | High | Full routed dossier pages (see §3). |
| F9 | `#compare` was linked from the nav and footer but no element had that id. | Low | Comparison now lives in a modal opened from the shortlist bar; dead links removed. |
| F10 | A Cloudflare challenge iframe script was embedded at the end of the document (a copy-paste artefact from a scraped page), which calls `window.parent.location` and fails outside that origin. | Medium | Removed. |

## 3. Findings — design and content depth

| # | Finding | Resolution |
| --- | --- | --- |
| D1 | Visual language was default corporate navy + amber, indistinguishable from a template. | New design system: forest ink, warm gold, ivory; Fraunces display serif with Manrope UI; hairline borders and layered shadows instead of heavy cards. |
| D2 | No motion beyond hover lifts; nothing guided the eye or rewarded scrolling. | Hero line-reveal, 26s skyline pan, scroll reveals with stagger, counters, progress bars that fill on open, marquee ticker — all gated behind `prefers-reduced-motion`. |
| D3 | Locality cards were text-only; no way to compare corridors. | Trend bars, price bands, yield and tracked-project counts, plus a west/north/south filter. |
| D4 | Builder cards gave a paragraph and a project count — no way to judge credibility. | Ranked rows with a delivery-confidence bar and a full dossier: four-dimension scorecard, delivery record against committed dates, live projects, risk notes, verification trail. |
| D5 | Project cards showed price and two meta lines; no legal, payment, progress or objection detail. | Dossiers carry unit mix and pricing, payment milestones, construction progress, amenities, connectivity, and "questions we would ask" — the objection list that makes the portal credible. |
| D6 | No true-cost information, which is the single biggest gap for a first-time buyer. | An all-in cost panel per project: base price, stamp duty and registration, GST by possession status, corpus, parking. |
| D7 | Trust section listed claims but not their basis. | Scoring method, data vintage, and an explicit note that the site is demo content. |

## 4. Findings — performance

| # | Finding | Resolution |
| --- | --- | --- |
| P1 | Large single stylesheet with no token discipline; several selectors redefined later in the file. | Tokens first, then components; duplicate declarations consolidated. |
| P2 | No image strategy (no assets, no dimensions, no lazy loading). | Three optimised images (190–220 KB), explicit `width`/`height`, `loading="lazy"` below the fold, `fetchpriority="high"` on the hero. |
| P3 | Emoji used as icons, causing inconsistent rendering across platforms. | Inline SVG icon set. |
| P4 | Layout shift risk from dynamically injected card grids. | Cards render from data on first paint; media boxes use fixed aspect ratios. |

## 5. Findings — accessibility

| # | Finding | Severity | Resolution |
| --- | --- | --- | --- |
| A1 | Multiple `h1`-level messaging and a heading order that skipped levels. | Medium | One `h1` per view; dossier headings start at `h2`. |
| A2 | Clickable `<article>` locality cards were not keyboard reachable. | High | `tabindex="0"`, `role="button"`, `aria-label`, and Enter/Space handlers. |
| A3 | Comparison modal lacked `role="dialog"`, `aria-modal` and a labelled title; focus was not moved into it and Escape did not close it. | High | Dialog semantics, labelled heading, focus move on open, Escape and scrim close; body scroll locked. |
| A4 | FAQ used `div` + `onclick`. | Medium | Real `<button>` elements with `aria-expanded` and `aria-controls`. |
| A5 | Form inputs relied on visible labels associated by proximity only in places. | Medium | Every control has a `<label for>` or `aria-label` (verified: 0 unlabelled). |
| A6 | No skip link, and no visible focus styling. | Medium | Skip link plus a gold `:focus-visible` ring on every interactive element. |
| A7 | Gold-on-ivory text in the original sat below 4.5:1 in places. | Medium | Gold is used as an accent only; body copy uses the ink and muted tokens which pass on their backgrounds. |
| A8 | Mobile menu had no expanded state announced. | Low | `aria-expanded` on the toggle, `aria-controls` to the drawer. |
| A9 | Animation had no reduced-motion path. | Medium | Full `prefers-reduced-motion` block disables reveals, counters and marquees. |

## 6. What was added

- **Hash router** for dossiers: `#/project/<id>` and `#/builder/<id>`, with browser back/forward,
  deep-link support on load, cross-links between project and builder dossiers, and scroll restore.
- **Project dossier** (7 blocks): our read with a consultant quote, gallery with hero swap,
  unit mix and pricing, payment plan, construction progress, amenities, connectivity,
  objection list, true-cost panel, builder card, similar projects.
- **Builder dossier** (5 blocks): narrative, four-dimension scorecard, delivery record against
  committed dates, live projects, risk notes, verification trail, peer comparison.
- **Shortlist** with a floating bar, header badge, modal and four-project cap.
- **Affordability model** with four sliders and corridor recommendations that deep-link to the grid.
- **Guided visit flow** with generated date chips, slot pills, validation and a confirmation.
- **Market ticker** with corridor price snapshots.
- **Design system, motion system and image assets.**

## 7. Verification performed

- HTML parse: balanced tags, no stray or unclosed elements (0 errors).
- JavaScript: both script blocks pass `node --check`; runtime exercised in jsdom — 0 errors across
  boot, filtering, search, quick filters, shortlisting, the 4-item cap, comparison, shortlist modal,
  all six project dossiers, all six builder dossiers, FAQ, calculator input, visit validation and
  the confirmation path.
- Accessibility pass: 0 unlabelled controls, 0 images without `alt`, 0 empty buttons,
  0 duplicate ids, all `aria-controls` targets resolve, one `h1` per view.
- CSS: balanced braces; verified a static-server load of `index.html` and all three assets.

## 8. Residual risks and next steps

1. **Replace the demo data.** Prices, TSRERA numbers, delivery records and scores are fictional.
   Publish only verified figures, and date-stamp them.
2. **Wire the visit form** to a CRM or form endpoint; add consent capture and a spam guard.
3. **Serve responsive images** (`srcset` + AVIF/WebP) once real photography is available; the
   current JPEGs are sized for a single desktop breakpoint set.
4. **Add a locality map** — the one thing this portal still lacks is spatial orientation.
5. **Legal review** of the commission disclosure and the "no buyer fee" claim for the operating
   entity's actual market and regulator.
6. **Test on real devices**, particularly iOS Safari (backdrop-filter and sticky behaviour) and
   low-end Android, to confirm the motion budget holds.
