"""GoatCounter visitor stats for noorslist.org (dashboard: https://noorslist.goatcounter.com).

Every public page (homepage + every event page) must carry SNIPPET just before </body>.
- home_live.py adds it to index.html automatically.
- Event pages: run  python3 _tools/analytics.py  from the repo root after building pages;
  it adds the snippet to any yyyy-mm-dd-*/index.html that lacks it (safe to re-run).
- NOT for the WhatsApp images (build.py img_page / shot.py): those are screenshots, not visits.
  (count.js also ignores localhost, so local Playwright checks are not counted.)

Besides page views, the small inline script counts link clicks as GoatCounter "events",
named "<kind>: <page path>", e.g. "maps: /2026-11-07-iscf-muslim-matrimonial/".
Kinds: maps (Open in Maps), flyer (full-size flyer), call (tel:), email (mailto:),
link (any other outside link: Register, Zeffy, Instagram, Google Sites event pages ...).
Links to other noorslist.org pages are not events (they show up as page views).
"""
import sys
from pathlib import Path

CODE = "noorslist"   # GoatCounter site code -> https://noorslist.goatcounter.com
MARK = "<!-- GoatCounter -->"

CLICKS = r"""<script>document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a||!window.goatcounter||!window.goatcounter.count)return;var h=a.getAttribute('href'),u=new URL(a.href,location.href),k;if(/^tel:/i.test(h))k='call';else if(/^mailto:/i.test(h))k='email';else if(/(^|\/)flyer\.jpg$/.test(u.pathname)&&u.host==location.host)k='flyer';else if(/google\.[a-z.]+\/maps|maps\.app\.goo\.gl|maps\.apple\.com/i.test(u.href))k='maps';else if(u.host&&u.host!=location.host)k='link';if(!k)return;window.goatcounter.count({path:k+': '+location.pathname,title:((a.textContent||'').trim()||(a.querySelector('img')||{}).alt||'').slice(0,80)+' → '+u.href.slice(0,200),event:true})})</script>"""

SNIPPET = (MARK + CLICKS +
           '<script data-goatcounter="https://%s.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>'
           "<!-- End GoatCounter -->") % CODE


def add(html: str) -> str:
    """Insert the snippet before the last </body> (no-op if already there)."""
    if MARK in html:
        return html
    i = html.rfind("</body>")
    if i < 0:
        raise ValueError("no </body> in page")
    return html[:i] + SNIPPET + "\n" + html[i:]


def stamp_event_pages(root: Path) -> int:
    n = 0
    for p in sorted(root.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*/index.html")):
        old = p.read_text(encoding="utf-8")
        new = add(old)
        if new != old:
            p.write_text(new, encoding="utf-8"); n += 1
    return n


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    print("added GoatCounter to", stamp_event_pages(root), "event pages")
