# Noor's List website

The website of [Noor's List](https://noorslist.org), the weekly schedule of Muslim community events in Central Florida. Served by GitHub Pages at **https://noorslist.org** (`CNAME` — never delete it).

**This repo is public and everything in it is served on the site — it holds only the website itself:**
- `index.html` — homepage, built from the "Noor's List Events" Google Sheet
- `<yyyy-mm-dd-slug>/` — one page per event (`index.html` + `flyer.jpg`); kept forever so old WhatsApp links keep working
- `assets/` — shared stylesheet, icons, brand files; favicons at the root

The builders (homepage, event pages, WhatsApp images, visitor stats snippet, quality check) and all running state live in the **private** repo `noorslist/noorslist-private` (moved there Nov 5, 2026). Don't add scripts, data files or anything from WhatsApp here.

Every page carries the GoatCounter snippet (https://noorslist.goatcounter.com); new pages also a canonical link.
