"""Build the live noorslist homepage (index.html) from the Events sheet rows.
Sections are computed in the visitor's browser from today's date, so the page stays right all week.
Look = approved theme v1 (CSS taken from the approved mockup in build.py)."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import build
from sheet_rows import ROWS

GH_HOSTS = ("https://noorslist.github.io", "https://noorslist.org")

def split(s): return [x.strip() for x in s.split(",") if x.strip()]

events = []
for (typ, d, e, t, w, title, v, orgs, aud, url) in ROWS:
    for h in GH_HOSTS:
        if url.startswith(h): url = url[len(h):]          # same-site link -> relative
    events.append({"k": typ, "d": d, "e": e, "t": t.replace(" - ", "–"), "w": w,
                   "n": title, "v": v, "o": split(orgs), "a": split(aud), "u": url})

mock = build.home()
css = re.search(r"<style>(.*?)</style>", mock, re.S).group(1)
fonts = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Figtree:wght@400;500;600;700&display=swap">'

JS = r"""
const EV = __DATA__;
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const iso = d => d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const parse = s => { const [y,m,d] = s.split('-').map(Number); return new Date(y, m-1, d); };
const add = (d, n) => { const x = new Date(d); x.setDate(x.getDate()+n); return x; };
const MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const DAY = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
const span = (a, b) => iso(a)===iso(b) ? `${MON[a.getMonth()]} ${a.getDate()}` : a.getMonth()===b.getMonth() ? `${MON[a.getMonth()]} ${a.getDate()} – ${b.getDate()}` : `${MON[a.getMonth()]} ${a.getDate()} – ${MON[b.getMonth()]} ${b.getDate()}`;
const PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>';

function chips(e){
  const c = [];
  if (e.v) c.push(`<span class="chip place">${PIN}${esc(e.v)}</span>`);
  e.o.filter(o => o !== e.v).forEach(o => c.push(`<span class="chip org">${esc(o)}</span>`));
  e.a.forEach(a => c.push(`<span class="chip aud a-${a.toLowerCase()}">${esc(a)}</span>`));
  return c.length ? `<div class="chips">${c.join('')}</div>` : '';
}
function card(time, e){
  const inner = `<div class="time">${esc(time) || '&nbsp;'}</div><div class="body"><div class="title">${esc(e.n)}</div>${chips(e)}</div>`;
  return e.u ? `<a class="card" href="${esc(e.u)}">${inner}<span class="go" aria-hidden="true">›</span></a>` : `<div class="card">${inner}<span></span></div>`;
}
function days(list){
  const by = {};
  list.forEach(x => (by[x.day] = by[x.day] || []).push(x.e));
  return Object.keys(by).sort().map(k => {
    const d = parse(k);
    return `<h3 class="day"><span>${DAY[d.getDay()]}</span> ${MON[d.getMonth()]} ${d.getDate()}</h3>` + by[k].map(e => card(e.t, e)).join('');
  }).join('');
}
function render(){
  const today = parse(iso(new Date())), t = iso(today), dow = today.getDay();
  // Weekend = Fri-Sun. Mon-Thu: "This Week" runs to Thursday.
  let wkStart, wkEnd;
  if (dow === 0) { wkStart = today; wkEnd = today; }
  else if (dow >= 5) { wkStart = today; wkEnd = add(today, 7 - dow); }
  else { wkStart = add(today, 5 - dow); wkEnd = add(wkStart, 2); }
  const nxStart = add(wkEnd, 1), nxEnd = add(nxStart, 6);
  const S = { week: [], weekend: [], next: [], later: [] };
  EV.filter(e => e.k !== 'Program').forEach(e => {
    const last = e.e || e.d; if (last < t) return;
    const day = e.d < t ? t : e.d;            // multi-day event already running: show today
    const sec = day < iso(wkStart) ? 'week' : day <= iso(wkEnd) ? 'weekend' : day <= iso(nxEnd) ? 'next' : 'later';
    S[sec].push({ day, e });
  });
  const progs = EV.filter(e => e.k === 'Program' && (!e.e || e.e >= t));
  const secs = [
    ['week', 'This Week', span(today, add(wkStart, -1)), days(S.week)],
    ['weekend', 'This Weekend', span(wkStart, wkEnd), days(S.weekend)],
    ['next', 'Next Week', span(nxStart, nxEnd), days(S.next)],
    ['later', 'Coming Later', '', days(S.later)],
    ['programs', 'Weekly Programs', '', progs.length ? `<div class="progs">${progs.map(e => card(e.w, e)).join('')}</div>` : ''],
  ].filter(s => s[3]);
  $('nav').innerHTML = secs.map(s => `<a href="#${s[0]}">${s[1]}</a>`).join('');
  $('#list').innerHTML = secs.map(s => `<section id="${s[0]}"><h2>${s[1]}${s[2] ? ` <small>${s[2]}</small>` : ''}</h2>${s[3]}</section>`).join('')
    || '<p>No upcoming events listed right now. Check back Thursday.</p>';
}
render();
"""

page = f"""<!DOCTYPE html>
<html lang="en" class="q-lines q-glow"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Noor's List — Muslim community events in Central Florida</title>
<meta name="description" content="Weekly list of Muslim community events in Central Florida. Updated every Thursday.">
<meta property="og:title" content="Noor's List">
<meta property="og:description" content="Muslim community events in Central Florida. Updated every Thursday.">
<meta property="og:url" content="https://noorslist.org/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Noor's List">
<meta property="og:image" content="https://noorslist.org/assets/icon-512.png">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png">
{fonts}
<style>{css}
header .mark a {{ color:inherit; text-decoration:none }}
</style></head><body><div class="wrap">
<header><div class="mark"><a href="/">Noor's List</a><i class="dot"></i></div>
<p>Muslim community events in Central Florida · updated every Thursday</p></header>
<nav></nav>
<main id="list"><noscript><p>Please turn on JavaScript to see the events list.</p></noscript></main>
<footer>Send an event: text or WhatsApp <a href="tel:+14077740332">407-774-0332</a> ·
<a href="mailto:info@noorslist.org">info@noorslist.org</a><br>Want to sponsor Noor's List? Get in touch.</footer>
</div><script>{JS.replace("__DATA__", json.dumps(events, ensure_ascii=False))}</script></body></html>"""

out = Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
out.write_text(page, encoding="utf-8")
print("wrote", out, len(events), "rows")
