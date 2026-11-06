"""Build Noor's List mockups: homepage (home.html) and two WhatsApp images (weekend/coming .html -> .png)."""
import sys, html, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from data import EVENTS, PROGRAMS, GH

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)
E = html.escape
ISSUE = dt.date(2026, 10, 29)               # Thursday publish date for this mock
WKND = (dt.date(2026, 10, 30), dt.date(2026, 11, 1))
NEXT = (dt.date(2026, 11, 2), dt.date(2026, 11, 8))

def d(s): return dt.date.fromisoformat(s)
def evs(lo, hi): return [e for e in EVENTS if lo <= d(e[0]) <= hi]
def mon(x): return x.strftime("%b")
def span(a, b):
    return f"{mon(a)} {a.day} – {b.day}" if a.month == b.month else f"{mon(a)} {a.day} – {mon(b)} {b.day}"
def by_day(rows):
    out = {}
    for e in rows: out.setdefault(e[0], []).append(e)
    return out

AUD = ["Brothers", "Sisters", "Youth", "Seniors"]

# ---------------------------------------------------------------- homepage
def chips(place, orgs, aud):
    c = []
    if place: c.append(f'<span class="chip place"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>{E(place)}</span>')
    c += [f'<span class="chip org">{E(o)}</span>' for o in orgs if o != place]
    c += [f'<span class="chip aud a-{a.lower()}">{E(a)}</span>' for a in aud]
    return f'<div class="chips">{"".join(c)}</div>' if c else ""

def card(time, title, place, orgs, aud, slug):
    inner = (f'<div class="time">{E(time.replace(" - ", "\u2013")) or "&nbsp;"}</div>'
             f'<div class="body"><div class="title">{E(title)}</div>{chips(place, orgs, aud)}</div>')
    if slug:
        return f'<a class="card" href="{GH}{slug}/">{inner}<span class="go" aria-hidden="true">›</span></a>'
    return f'<div class="card">{inner}</div>'

def day_groups(rows):
    h = []
    for day, items in by_day(rows).items():
        x = d(day)
        h.append(f'<h3 class="day"><span>{x.strftime("%A")}</span> {mon(x)} {x.day}</h3>')
        h += [card(e[1], e[2], e[3], e[4], e[5], e[6]) for e in items]
    return "\n".join(h)

def home():
    later = [e for e in EVENTS if d(e[0]) > NEXT[1]]
    progs = "\n".join(card(p[0], p[1], p[2], p[3], p[4], p[5]) for p in PROGRAMS)
    sections = [
        ("weekend", "This Weekend", span(*WKND), day_groups(evs(*WKND))),
        ("next", "Next Week", span(*NEXT), day_groups(evs(*NEXT))),
        ("later", "Coming Later", "", day_groups(later)),
        ("programs", "Weekly Programs", "", f'<div class="progs">{progs}</div>'),
    ]
    nav = "".join(f'<a href="#{k}">{t}</a>' for k, t, _, _ in sections)
    body = "\n".join(f'<section id="{k}"><h2>{t}{f" <small>{s}</small>" if s else ""}</h2>{c}</section>'
                     for k, t, s, c in sections)
    return f"""<!DOCTYPE html>
<html lang="en" class="q-lines q-glow"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Noor's List — Muslim community events in Central Florida</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Figtree:wght@400;500;600;700&display=swap">
<style>
:root {{
  --bg:#f6f7f4; --surface:#fff; --ink:#18233a; --muted:#5b6577; --line:#dfe3e2; --lamp:#b77712;
  --display:"Bricolage Grotesque","Avenir Next","Segoe UI",system-ui,sans-serif;
  --body:"Figtree","Segoe UI",system-ui,-apple-system,sans-serif;
  --bro:#dbe8f6; --bro-ink:#1d4f80; --sis:#f7e0e6; --sis-ink:#8a2a47;
  --you:#dcefe2; --you-ink:#21653a; --sen:#ece4f5; --sen-ink:#57358a;
  color-scheme: light dark;
}}
@media (prefers-color-scheme: dark) {{ :root {{
  --bg:#10161f; --surface:#172030; --ink:#e8ecf2; --muted:#9aa5b6; --line:#2a3546; --lamp:#e3a843;
  --bro:#1d3550; --bro-ink:#a9cdf2; --sis:#47222f; --sis-ink:#f2b3c6;
  --you:#1c3a27; --you-ink:#a5dcb5; --sen:#33284a; --sen-ink:#cfb8f0; }} }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:16px/1.45 var(--body);
  padding:0 max(14px, env(safe-area-inset-left)) }}
.wrap {{ max-width:680px; margin:0 auto; padding:18px 0 48px }}
header .mark {{ font:700 1.9rem/1 var(--display); letter-spacing:-.02em; margin:6px 0 4px }}
header .mark .dot {{ display:inline-block; width:.42em; height:.42em; border-radius:50%; background:var(--lamp); margin-left:.18em; box-shadow:0 0 10px var(--lamp) }}
header p {{ margin:0; color:var(--muted) }}
nav {{ position:sticky; top:0; z-index:5; background:var(--bg); display:flex; gap:8px; overflow-x:auto;
  padding:14px 0 10px; margin-bottom:4px; border-bottom:1px solid var(--line); scrollbar-width:none }}
nav a {{ flex:none; text-decoration:none; color:var(--ink); font-weight:600; font-size:.92rem;
  border:1px solid var(--line); background:var(--surface); padding:6px 12px; border-radius:999px }}
section {{ scroll-margin-top:60px }}
h2 {{ font:700 1.45rem/1.2 var(--display); margin:26px 0 4px; letter-spacing:-.01em }}
h2 small {{ font:500 .95rem var(--body); color:var(--muted); margin-left:6px }}
h3.day {{ font:600 .82rem/1 var(--body); text-transform:uppercase; letter-spacing:.08em; color:var(--muted);
  margin:18px 0 8px; display:flex; gap:6px; align-items:center }}
h3.day span {{ color:var(--lamp) }}
h3.day::after {{ content:""; flex:1; height:1px; background:var(--line); margin-left:6px }}
.card {{ display:grid; grid-template-columns:92px 1fr 14px; gap:12px; align-items:start; background:var(--surface);
  border:1px solid var(--line); border-radius:12px; padding:10px 10px 10px 12px; margin-bottom:6px;
  color:inherit; text-decoration:none }}
a.card:hover {{ border-color:var(--lamp) }}
.time {{ font-weight:700; font-size:.9rem; padding-top:2px; font-variant-numeric:tabular-nums }}
.title {{ font-weight:600; font-size:1rem; line-height:1.28 }}
.go {{ color:var(--muted); font-size:1.4rem; line-height:1 }}
.progs .card {{ grid-template-columns:120px 1fr 14px }}
.chips {{ display:flex; flex-wrap:wrap; gap:5px; margin-top:5px }}
.chip {{ font-size:.78rem; font-weight:600; padding:2px 8px; border-radius:999px; line-height:1.5;
  display:inline-flex; align-items:center; gap:3px }}
.chip.place {{ color:var(--muted); padding-left:4px }}
.chip.place svg {{ width:13px; height:13px; fill:currentColor; opacity:.8 }}
.chip.org {{ border:1px solid var(--line); color:var(--ink) }}
.a-brothers {{ background:var(--bro); color:var(--bro-ink) }} .a-sisters {{ background:var(--sis); color:var(--sis-ink) }}
.a-youth {{ background:var(--you); color:var(--you-ink) }} .a-seniors {{ background:var(--sen); color:var(--sen-ink) }}
footer {{ margin-top:36px; padding-top:16px; border-top:1px solid var(--line); color:var(--muted); font-size:.92rem }}
footer a {{ color:inherit }}
@media (max-width:420px) {{ .card {{ grid-template-columns:66px 1fr 10px; gap:10px }} .time {{ font-size:.8rem }}
  .progs .card {{ grid-template-columns:1fr 10px }} .progs .time {{ grid-column:1; }} }}
html.q-chips .chip.aud {{ background:var(--line) !important; color:var(--ink) !important }}
html.q-glow header .mark .dot {{ box-shadow:none }}
html.q-lines .card {{ background:transparent; border:0; border-bottom:1px solid var(--line); border-radius:0; padding:12px 2px; margin:0 }}
html.q-lines h3.day::after {{ display:none }}
</style><script>addEventListener('message',e=>{{if(e.data&&e.data.nl)document.documentElement.className=e.data.nl}})</script></head><body><div class="wrap">
<header><div class="mark">Noor's List<i class="dot"></i></div>
<p>Muslim community events in Central Florida · updated every Thursday</p></header>
<nav>{nav}</nav>
{body}
<footer>Send an event: text or WhatsApp <a href="tel:+14077740332">407-774-0332</a> ·
<a href="mailto:info@noorslist.org">info@noorslist.org</a><br>Want to sponsor Noor's List? Get in touch.</footer>
</div></body></html>"""

# ---------------------------------------------------------------- WhatsApp images
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&display=swap">'
LISTEN = """<script>addEventListener('message',e=>{if(e.data&&e.data.nl)document.documentElement.className=e.data.nl})</script>"""
IMG_QUIET = """
html.q-chips .a{background:#ebe8e1 !important;color:#3d4659 !important}
html.q-glow .dot{box-shadow:none}
html.q-lines .ev{border-bottom:0;padding:14px 0}
html.q-lines .day::after{background:#ebe5d8;height:2px}
html.q-header body{background:#f6f3ec}
html.q-header .top{background:transparent;color:#18233a;padding:56px 60px 6px}
html.q-header .sub{color:#5b6577}
html.q-header .sub b{color:#b77712}
html.q-header .foot{background:transparent;color:#18233a;border-top:2px solid #e2dccd;margin:0 60px;padding:30px 0 40px}
html.q-header .foot .p{color:#5b6577}
html.q-header .foot .u b{color:#b77712}
html.q-header .dot{background:#b77712}
"""
IMG_FOOT = """
html.f-light .foot{background:transparent;color:#18233a;border-top:2px solid #e2dccd;margin:0 60px;padding:30px 0 40px}
html.f-light .foot .p{color:#5b6577}
html.f-light .foot .u b{color:#b77712}
html.f-strip .foot{padding:16px 60px}
html.f-strip .foot .u{font-size:34px}
html.f-strip .foot .p{font-size:24px}
"""
IMG_CSS = """
*{box-sizing:border-box} body{margin:0;width:1080px;background:#f6f3ec;color:#18233a;font-family:Figtree,sans-serif}
.top{background:#18233a;color:#fff;padding:44px 60px 36px}
.mark{font:700 38px/1 'Bricolage Grotesque';letter-spacing:-.01em}.dot{display:inline-block;width:.42em;height:.42em;border-radius:50%;background:#e3a843;margin-left:.18em;box-shadow:0 0 14px #e3a843}
h1{font:800 84px/1 'Bricolage Grotesque';margin:20px 0 8px;letter-spacing:-.025em}
.sub{font-size:34px;color:#c9d2e0}.sub b{color:#e3a843;font-weight:700}
.main{padding:6px 60px 22px}
.day{display:flex;align-items:center;gap:16px;margin:26px 0 4px;font:700 26px/1 Figtree;letter-spacing:.12em;
 text-transform:uppercase;color:#b77712}.day::after{content:"";flex:1;height:3px;background:#e7dcc6}
.ev{display:grid;grid-template-columns:180px 1fr;gap:16px;padding:11px 0;border-bottom:2px solid #ebe5d8}
.ev:last-child{border-bottom:0}
.t{font:700 27px/1.3 Figtree;font-variant-numeric:tabular-nums;padding-top:3px}
.n{font:600 35px/1.17 Figtree;letter-spacing:-.005em}
.m{margin-top:5px;font-size:26px;color:#5b6577;display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center}
.a{font-size:23px;font-weight:700;padding:3px 14px;border-radius:99px}
.a-brothers{background:#dbe8f6;color:#1d4f80}.a-sisters{background:#f7e0e6;color:#8a2a47}
.a-youth{background:#dcefe2;color:#21653a}.a-seniors{background:#ece4f5;color:#57358a}
.more{margin-top:22px;font-size:30px;color:#5b6577}
.foot{background:#18233a;color:#fff;padding:28px 60px;display:flex;justify-content:space-between;align-items:center}
.foot .u{font:700 44px 'Bricolage Grotesque'}.foot .u b{color:#e3a843}.foot .p{font-size:28px;color:#c9d2e0;text-align:right;line-height:1.35}
"""

def short_time(t):
    return t.replace(" - ", "–")

CLS = "q-glow"
def img_page(title, sub, rows, cap=None):
    shown = rows if cap is None else rows[:cap]
    h = []
    for day, items in by_day(shown).items():
        x = d(day)
        h.append(f'<div class="day">{x.strftime("%A")} · {mon(x)} {x.day}</div>')
        for e in items:
            meta = []
            if e[3]: meta.append(f'<span>{E(e[3])}</span>')
            orgs=[o for o in e[4] if o!=e[3]]
            if orgs: meta.append(f'<span>{E(" x ".join(orgs))}</span>')
            meta = " <span>·</span> ".join(meta)
            aud = "".join(f'<span class="a a-{a.lower()}">{a}</span>' for a in e[5])
            m = f'<div class="m">{meta}{aud}</div>' if (meta or aud) else ""
            h.append(f'<div class="ev"><div class="t">{E(short_time(e[1]))}</div><div><div class="n">{E(e[2])}</div>{m}</div></div>')
    if cap is not None and len(rows) > cap:
        h.append(f'<div class="more">+ {len(rows)-cap} more at noorslist.org</div>')
    return f"""<!DOCTYPE html><html class="{CLS}"><head><meta charset="utf-8">{FONTS}<style>{IMG_CSS}{IMG_QUIET}{IMG_FOOT}</style>{LISTEN}</head><body>
<div class="top"><div class="mark">Noor's List<i class="dot"></i></div><h1>{title}</h1><div class="sub">{sub}</div></div>
<div class="main">{''.join(h)}</div>
<div class="foot"><div class="u">noorslist<b>.</b>org</div><div class="p">Full list & details<br>Text/WhatsApp 407-774-0332</div></div>
</body></html>"""

if __name__ == "__main__":
    (OUT / "home.html").write_text(home(), encoding="utf-8")
    (OUT / "weekend.html").write_text(img_page("This Weekend", f"<b>{span(*WKND)}</b> · Central Florida", evs(*WKND)), encoding="utf-8")
    (OUT / "coming.html").write_text(img_page("Coming Up", f"<b>Next week, {span(*NEXT)}</b>", evs(*NEXT)), encoding="utf-8")
    print("built", [p.name for p in OUT.iterdir()])
