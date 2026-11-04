"""Side-by-side compare page: current (left, fixed) vs quiet (right, toggles)."""
import json
from pathlib import Path
OUT = Path(__file__).parent / "out"
img = (OUT / "weekend.html").read_text(encoding="utf-8")
home = (OUT / "home.html").read_text(encoding="utf-8")

TOGGLES = [
  ("q-header", "Light header", "Image: no navy band top and bottom — wordmark and title in navy on the cream background, thin rule above the footer."),
  ("q-chips", "Plain audience tags", "Brothers / Sisters / Youth / Seniors all in one soft gray instead of four colors."),
  ("q-lines", "No boxes or lines", "Image: no line between events, just space. Website: events as plain rows instead of white cards."),
  ("q-glow", "Flat gold dot", "No glow around the dot after “Noor's List”."),
]

page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Noor's List — compare styles</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700&family=Figtree:wght@400;600;700&display=swap">
<style>
*{box-sizing:border-box} body{margin:0;background:#eeece6;color:#18233a;font:15px/1.45 Figtree,system-ui,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:22px 16px 60px}
h1{font:700 1.6rem/1.2 'Bricolage Grotesque',sans-serif;margin:0 0 4px}
.lead{color:#5b6577;margin:0 0 18px}
.panel{background:#fff;border:1px solid #dfdbd0;border-radius:14px;padding:14px 16px;margin-bottom:22px}
.panel h2{font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:#5b6577;margin:0 0 10px}
.tg{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px}
label.t{display:flex;gap:10px;align-items:flex-start;padding:10px;border:1px solid #e6e2d8;border-radius:10px;cursor:pointer}
label.t input{margin-top:3px;width:18px;height:18px;accent-color:#18233a;flex:none}
label.t b{display:block} label.t span{color:#5b6577;font-size:.86rem}
.presets{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.presets button{font:600 .88rem Figtree,sans-serif;border:1px solid #18233a;background:#fff;color:#18233a;border-radius:999px;padding:6px 14px;cursor:pointer}
.presets button:hover{background:#18233a;color:#fff}
.sec{font:700 1.15rem/1.2 'Bricolage Grotesque',sans-serif;margin:28px 0 10px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.col h3{font-size:.85rem;margin:0 0 8px;color:#5b6577;font-weight:600}
.col h3 b{color:#18233a}
.frame{background:#fff;border:1px solid #dfdbd0;border-radius:10px;overflow:hidden;position:relative}
.col{min-width:0} .frame iframe{border:0;display:block;transform-origin:0 0;position:absolute;top:0;left:0}
.phone{width:100%;max-width:390px;height:760px;border:1px solid #dfdbd0;border-radius:22px;overflow:hidden;background:#f6f7f4}
.phone iframe{width:100%;height:100%;border:0;display:block}
@media (max-width:640px){.cols{gap:8px}.phone{height:620px;border-radius:14px}}
</style></head><body><div class="wrap">
<h1>Compare styles</h1>
<p class="lead">Left is the current design and doesn’t change. Right starts fully quiet — switch any element on or off to mix and match. Nothing here is live.</p>
<div class="panel"><h2>Quiet elements (right side)</h2><div class="tg" id="tg"></div>
<div class="presets"><button data-p="all">All quiet</button><button data-p="none">Same as current</button></div></div>

<div class="sec">WhatsApp image — This Weekend</div>
<div class="cols">
 <div class="col"><h3><b>A</b> · Current</h3><div class="frame" data-h="2420"><iframe id="imgA"></iframe></div></div>
 <div class="col"><h3><b>B</b> · Quiet</h3><div class="frame" data-h="2420"><iframe id="imgB"></iframe></div></div>
</div>

<div class="sec">Website — phone view (scrolls)</div>
<div class="cols">
 <div class="col"><h3><b>A</b> · Current</h3><div class="phone"><iframe id="homeA"></iframe></div></div>
 <div class="col"><h3><b>B</b> · Quiet</h3><div class="phone"><iframe id="homeB"></iframe></div></div>
</div>
</div>
<script>
const IMG = __IMG__, HOME = __HOME__, TOGGLES = __TOGGLES__;
const $ = s => document.querySelector(s);
const tg = $('#tg');
TOGGLES.forEach(([k,t,d]) => {
  tg.insertAdjacentHTML('beforeend', `<label class="t"><input type="checkbox" value="${k}" checked><div><b>${t}</b><span>${d}</span></div></label>`);
});
['imgA','imgB'].forEach(id => $('#'+id).srcdoc = IMG);
['homeA','homeB'].forEach(id => $('#'+id).srcdoc = HOME);
function classes(){ return [...tg.querySelectorAll('input:checked')].map(i=>i.value).join(' ') || 'none'; }
function apply(){ ['imgB','homeB'].forEach(id => { try { $('#'+id).contentWindow.postMessage({nl:classes()}, '*'); } catch(e){} }); setTimeout(fit, 150); setTimeout(fit, 800); }
tg.addEventListener('change', apply);
document.querySelectorAll('.presets button').forEach(b => b.onclick = () => {
  tg.querySelectorAll('input').forEach(i => i.checked = b.dataset.p === 'all'); apply();
});
['imgB','homeB'].forEach(id => $('#'+id).addEventListener('load', apply));
function fit(){
  document.querySelectorAll('.frame').forEach(f => {
    const ifr = f.querySelector('iframe'), w = f.clientWidth, s = w/1080; let h = +f.dataset.h;
    try { const d = ifr.contentDocument; if (d && d.body && d.body.scrollHeight > 400) h = d.body.scrollHeight; } catch(e){}
    ifr.style.width = '1080px'; ifr.style.height = h+'px'; ifr.style.transform = `scale(${s})`;
    f.style.height = (h*s)+'px';
  });
}
addEventListener('resize', fit); fit(); ['imgA','imgB'].forEach(id => $('#'+id).addEventListener('load', () => { fit(); setTimeout(fit, 800); }));
</script></body></html>"""
page = (page.replace("__IMG__", json.dumps(img).replace("</", "<\\/"))
            .replace("__HOME__", json.dumps(home).replace("</", "<\\/"))
            .replace("__TOGGLES__", json.dumps(TOGGLES)))
(OUT / "compare.html").write_text(page, encoding="utf-8")
print("ok", len(page))
