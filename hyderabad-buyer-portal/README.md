# Maison Hyderabad — Buyer Intelligence Portal

A single-file, premium residential buyer portal for Hyderabad flats, villas and plots.
It is an upgraded redesign of the original `index.html`: same subject and buyer-first positioning,
rebuilt around a warm editorial design system, motion, and full project and builder dossier pages.

> **Demo content.** Every project, TSRERA number, price and builder score is illustrative content
> created for a portfolio project. Nothing here is an offer, a valuation or legal advice.

---

## What it does

| Area | Behaviour |
| --- | --- |
| **Hero + search** | Corridor, property type and budget filters that actually filter the project grid |
| **Market ticker** | Scrolling corridor-by-corridor price snapshot (pure CSS marquee, pauses on hover) |
| **Locality notes** | 8 micro-markets with price bands, 5-year trend bars, pros/cons and a written verdict; filter by west/north/south |
| **Builder directory** | 6 builders scored on compliance, delivery, legal record and service, with a delivery-confidence bar |
| **Project discovery** | 6 fully annotated projects; type tabs, budget band, "ready to move" and corridor filtering |
| **Project dossier** | Routed detail view: our read, gallery, unit mix, payment plan, construction progress, amenities, connectivity, objections we would raise, true all-in cost, builder card, similar projects |
| **Builder dossier** | Routed detail view: who they are, scorecard, delivery record vs committed dates, live projects, risk notes, verification trail |
| **Comparison** | Shortlist up to 4 projects (persisted to `localStorage`), then compare 13 parameters side by side |
| **Affordability model** | Sliders for income, savings, rate and tenure → affordable price after stamp duty + corpus, EMI, interest, cash buffer, and the corridors that still fit |
| **Guided visit** | Validated request form with generated date chips, slot selection and a personalised confirmation |
| **Trust** | Commission transparency statement, scoring rationale, FAQ accordion |

## Files

```
hyderabad-buyer-portal/
├── index.html                         # the entire portal: markup, design system, data, app logic
├── README.md                          # this file
├── AUDIT_REPORT.md                    # what was wrong with the original and what changed
├── DEPLOY.md                          # how to download, host and share it
└── assets/
    ├── hero-financial-district.jpg    # hero skyline (blue-hour, Financial District feel)
    ├── villa-community.jpg            # gated villa community
    └── interior-lobby.jpg             # tower lobby interior
```

## Run it

No build step, no dependencies, no network calls at runtime.

```bash
# from the repository root
cd hyderabad-buyer-portal
python3 -m http.server 8099
# open http://localhost:8099
```

Opening `index.html` directly with `file://` also works. Deep links are hash-based
(`#/project/skyline`, `#/builder/aparna`), so they work on any static host.

## How it is built

`index.html` contains four layers, in order:

1. **Design system** — CSS custom properties for colour, type, radius, shadow, easing; one
   token change re-themes the whole page.
2. **Layout + components** — sections, cards, buttons, chips, modals, detail-page shell.
3. **Data layer** — three plain arrays (`LOCALITIES`, `BUILDERS`, `PROJECTS`) plus `INSIGHTS`,
   `FAQS`, `TICKS`. The grids, the detail pages, the comparison table and the visit form's
   project list are all rendered from these. Edit the data, not the markup.
4. **App logic** — one IIFE: renderers, filters, hash router for dossiers, shortlist with
   `localStorage`, affordability model, form validation, reveal/counter observers.

### Editing content

Everything is at the top of the second `<script>`:

```js
const PROJECTS = [ { id:'skyline', name:'Skyline Residency', builder:'prestige',
                     locality:'gachibowli', units:[…], plan:[…], objections:[…] } ];
```

Add an object to `PROJECTS` and it appears in the grid, the comparison table, the visit form
and its own `#/project/<id>` page automatically. Same for `BUILDERS` and `LOCALITIES`.
`similar: ['vista','heritage']` picks the cross-links at the bottom of a dossier.
To add photography, drop a file in `assets/` and reference it from the project's `images` array.

### Design decisions worth knowing

- **Palette** — deep forest ink (`#0A1411`) with warm gold (`#C9A45C`) and ivory (`#F8F5EE`).
  Deliberately not the default blue/white property-portal look; the gold is used sparingly as an
  accent and never as text on light backgrounds (contrast).
- **Type** — Fraunces (display serif) for headlines and figures, Manrope for UI and body.
  Loaded from Google Fonts with a serif/sans fallback stack.
- **Motion** — one easing family (`--ease`, `--ease-out`), scroll reveals via
  `IntersectionObserver`, hero line-reveal, animated counters, progress bars that fill on open.
  Everything is disabled under `prefers-reduced-motion: reduce`.
- **Depth** — layered shadows and hairline borders instead of heavy drop shadows; a faint SVG
  grain overlay on the dark sections so large flat areas do not band.

### Accessibility

- Single visible `h1`; dossiers are `role="dialog"` overlays with `aria-modal` and labelled headings.
- Skip link, visible focus rings, keyboard-operable locality and builder cards (`tabindex` + Enter/Space).
- Tabs expose `aria-selected`; the FAQ uses buttons with `aria-expanded`/`aria-controls`.
- All form fields are labelled; validation errors are announced through `role="alert"`.
- Escape closes modals, the dossier and the mobile drawer; focus is moved into dialogs on open.

### Performance

- No frameworks, no build, no runtime requests except the two webfonts and the three local images.
- Images are resized and re-encoded (~190–220 KB each) with explicit `width`/`height` to avoid
  layout shift; non-hero images use `loading="lazy"`; the hero uses `fetchpriority="high"`.
- Animation work is limited to `transform`/`opacity`.

## Known limitations

- The visit form is a demo: it validates, then shows a confirmation and deliberately transmits
  nothing. Wire it to your CRM or a form endpoint before use.
- Comparison and the shortlist persist per device (`localStorage`); there is no backend.
- Prices, registration numbers and builder scores are fictional and must be replaced with
  verified data before any real use.
- The enquiry number (`+91 99999 99999`) and WhatsApp links are placeholders.
