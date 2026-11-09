# Downloading & Sharing

There are three ways to get this portal in front of someone. Pick based on whether you want a
link, a file, or an editable project.

---

## 1. Send it as one file (easiest to share)

`maison-hyderabad-portal.html` — a single 2.4 MB file with the images, styles, data and logic
embedded. No folder, no server, no internet needed.

- **Email / WhatsApp / Telegram / Drive:** attach the file. It opens in any browser on phone or
  desktop. WhatsApp supports it up to 2 GB, Gmail up to 25 MB.
- **Dropbox / Google Drive:** upload and share the link — but note the recipient will get a
  *download* link, not a live site (Drive no longer renders HTML).
- **Verified:** opens correctly from `file://` with all six projects, dossiers, filters and the
  shortlist working. Weights: 2.4 MB total.

Best for: clients, family, a portfolio reviewer who should just double-click and see it.

---

## 2. Host it as a real link (best for a portfolio)

Any static host will do — there is no build step and no backend.

### Netlify Drop (fastest, ~30 seconds, free)
1. Unzip `hyderabad-buyer-portal.zip` so you have the `hyderabad-buyer-portal` folder.
2. Go to **app.netlify.com/drop** and drag the folder onto the page.
3. You get a live URL immediately (e.g. `https://maison-hyderabad.netlify.app`). Claim the site
   to keep it permanently and rename it.

### GitHub Pages (free, versioned)
```bash
# from a clone of this repo
git checkout -b gh-pages
git subtree push --prefix hyderabad-buyer-portal origin gh-pages
```
Then Settings → Pages → source `gh-pages` → root. URL becomes
`https://<username>.github.io/<repo>/`. Deep links such as `/index.html#/project/skyline` work
because routing is hash-based.

### Vercel or Cloudflare Pages
Import the repo, set the output/root directory to `hyderabad-buyer-portal`, framework preset
**None**. Deploy.

> Since this repo is a fork of `public-apis`, prefer Netlify Drop or a fresh repo for a portfolio
> link rather than publishing from this fork.

---

## 3. Hand over the editable project

`hyderabad-buyer-portal.zip` (666 KB) — the full folder: `index.html`, `README.md`,
`AUDIT_REPORT.md` and `assets/`. This is what to send a developer or a designer who needs to
edit content, swap images or wire the form to a CRM.

To work on it:
```bash
unzip hyderabad-buyer-portal.zip
cd public-apis/hyderabad-buyer-portal
python3 -m http.server 8099   # then open http://localhost:8099
```

---

## A QR code for show-and-tell

Once hosted, generate a QR at `api.qrserver.com/v1/create-qr-code/?size=300x300&data=<your-url>`
and drop it into a deck or a WhatsApp message. Useful for site-visit desks and print handouts.

---

## Before you share publicly — three edits

All of these are in `index.html`:

1. **Phone and WhatsApp** — replace every `919999999999` (currently 11 occurrences) with the real
   number, including the `wa.me` links in the header, footer, floating button and dossiers.
2. **The demo disclaimer** — the footer says all data is illustrative. Keep that until the prices,
   TSRERA numbers and builder scores are replaced with verified figures (see `README.md` →
   "Editing content"; the data arrays are at the top of the second `<script>`).
3. **The visit form** — it validates and confirms but deliberately transmits nothing. Wire it to
   your CRM or a form endpoint before using it to collect real enquiries.

## Privacy note

The shortlist and comparison are stored only in the visitor's own browser (`localStorage`).
Nothing is sent to a server, and there are no analytics or tracking scripts — the only external
requests are the two Google Fonts. If you need the portal to work fully offline (for example on
a laptop at a site office with no signal), say so and the fonts can be embedded locally instead.
