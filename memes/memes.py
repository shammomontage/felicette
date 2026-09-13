import asyncio, os, html
from playwright.async_api import async_playwright

MASCOT = open('/home/claude/mascots/felicette_nobg.svg').read().replace('class="mascot"','')
OUT = '/home/claude/mascots/memes'
os.makedirs(OUT, exist_ok=True)

CSS = """
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1080px;overflow:hidden;font-family:'DejaVu Sans Condensed','DejaVu Sans',sans-serif;color:#EEF1F8;
  background:#0B1233 radial-gradient(900px 600px at 50% 0%,#1B2A5E 0%,rgba(27,42,94,0) 70%)}
.stars{position:absolute;inset:0;background-image:
  radial-gradient(2px 2px at 120px 90px,#fff 60%,transparent 61%),radial-gradient(1.5px 1.5px at 400px 40px,#fff 60%,transparent 61%),
  radial-gradient(2px 2px at 760px 120px,#fff 60%,transparent 61%),radial-gradient(1.5px 1.5px at 980px 260px,#fff 60%,transparent 61%),
  radial-gradient(2px 2px at 60px 420px,#fff 60%,transparent 61%),radial-gradient(1.5px 1.5px at 1020px 640px,#fff 60%,transparent 61%),
  radial-gradient(2px 2px at 300px 700px,#fff 60%,transparent 61%),radial-gradient(1.5px 1.5px at 900px 900px,#fff 60%,transparent 61%),
  radial-gradient(2px 2px at 560px 240px,#fff 60%,transparent 61%),radial-gradient(1.5px 1.5px at 200px 980px,#fff 60%,transparent 61%);opacity:.9}
.frame{position:absolute;inset:0;padding:64px;display:flex;flex-direction:column;justify-content:space-between}
.mascot{position:absolute;width:640px;height:640px;right:-30px;bottom:0;z-index:0}
.frame{z-index:2}
.mascot.left{right:auto;left:-40px}
.mascot.small{width:520px;height:520px}
.mascot.center{left:50%;transform:translateX(-50%);right:auto}
.big{font-weight:700;text-transform:uppercase;line-height:.98;letter-spacing:.01em;font-size:96px;text-shadow:0 4px 0 #05081C,0 0 24px rgba(0,0,0,.6)}
.big.xl{font-size:118px}
.big.md{font-size:72px}
.red{color:#E5462A}
.tag{font-family:'DejaVu Sans Mono',monospace;font-size:26px;letter-spacing:.18em;text-transform:uppercase;color:#9AA6C4}
.tag b{color:#E5462A}
.foot{display:flex;justify-content:space-between;align-items:flex-end;font-family:'DejaVu Sans Mono',monospace;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:#C9D1DC}
.foot .ticker{background:#E5462A;color:#fff;padding:10px 18px;font-weight:700}
.panel{background:rgba(5,8,28,.7);border:3px solid #C9D1DC;padding:28px 32px}
.list{display:flex;flex-direction:column;gap:18px;font-size:44px;font-weight:700;text-transform:uppercase}
.list div{display:flex;align-items:center;gap:22px}
.box{width:52px;height:52px;border:5px solid #C9D1DC;display:grid;place-items:center;font-size:40px;color:#7bc043;flex:none}
.box.empty{color:transparent}
.box.hot{border-color:#E5462A;color:#E5462A}
.mono{font-family:'DejaVu Sans Mono',monospace}
"""

def page(body, extra_css=''):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra_css}</style></head><body><div class='stars'></div>{body}</body></html>"

M = lambda cls='': f"<div class='mascot {cls}'>{MASCOT}</div>"

memes = {}

memes['01_chimps_dogs_cat'] = page(f"""
{M('')}
<div class='frame'>
  <div>
    <div class='tag'>Space race scoreboard · 1960–1963</div>
    <div class='big xl' style='margin-top:18px'>Chimps.<br>Dogs.<br><span class='red'>Cat.</span></div>
    <div class='tag' style='margin-top:26px;max-width:520px;line-height:1.5'>USA sent a chimp. USSR sent dogs. France sent a cat and got her back.<br><b>Only one of them has a token.</b></div>
  </div>
  <div class='foot'><span>First cat in space · 1963</span><span class='ticker'>$FELICETTE</span></div>
</div>""")

memes['02_157km'] = page(f"""
{M('left')}
<div class='frame' style='align-items:flex-end;text-align:right'>
  <div>
    <div class='tag'>Flight telemetry · Véronique AG1</div>
    <div class='big xl' style='margin-top:18px'>157 km up.</div>
    <div class='big xl red'>0 km of<br>roadmap.</div>
  </div>
  <div class='panel mono' style='font-size:26px;line-height:1.7;text-align:left;letter-spacing:.08em'>
    KÁRMÁN LINE ........ 100 KM<br>
    <span class='red'>FÉLICETTE ........... 157 KM</span><br>
    YOUR ROADMAP ......... 0 KM
  </div>
  <div class='foot' style='width:100%'><span class='ticker'>$FELICETTE</span><span>Hold the cat, collect SpaceX</span></div>
</div>""")

memes['03_elon_france'] = page(f"""
{M('')}
<div class='frame'>
  <div>
    <div class='big xl'>Elon sends<br>rockets.</div>
    <div class='big xl red' style='margin-top:14px'>France<br>sent a cat.</div>
    <div class='tag' style='margin-top:30px'>18 October 1963 · Hammaguir · 157 km</div>
  </div>
  <div class='foot'><span>Paired with SPCXX on StonkFun</span><span class='ticker'>$FELICETTE</span></div>
</div>""")

memes['04_hold_collect'] = page(f"""
{M('left small')}
<div class='frame' style='align-items:flex-end;text-align:right'>
  <div>
    <div class='big xl'>Hold the cat.</div>
    <div class='big xl red'>Collect SpaceX.</div>
  </div>
  <div class='panel' style='text-align:left;width:600px;border-color:#7bc043'>
    <div class='tag' style='color:#7bc043'>Wallet · incoming</div>
    <div class='mono' style='font-size:40px;font-weight:700;margin-top:10px'>+0.0042 SPCXX</div>
    <div class='mono' style='font-size:22px;color:#9AA6C4;margin-top:6px;letter-spacing:.1em'>HOLDER REWARD · NOTHING TO CLAIM</div>
  </div>
  <div class='foot' style='width:100%'><span class='ticker'>$FELICETTE</span><span>3% of every trade → holders, in SPCXX</span></div>
</div>""")

memes['05_day_22974'] = page(f"""
{M('center')}
<div class='frame' style='text-align:center;align-items:center'>
  <div>
    <div class='tag'>Mission log</div>
    <div class='big xl' style='margin-top:14px'>Day <span class='red'>22,974</span><br>of waiting<br>to get paid.</div>
  </div>
  <div class='foot' style='width:100%'><span>Launched 1963 · Paid 2026</span><span class='ticker'>$FELICETTE</span></div>
</div>""")

memes['06_eeg'] = page(f"""
{M('left')}
<div class='frame' style='align-items:flex-end;text-align:right'>
  <div>
    <div class='tag'>Cranial electrodes · live feed</div>
    <div class='big' style='margin-top:14px'>The electrodes<br>read the chart<br><span class='red'>directly.</span></div>
  </div>
  <svg width='620' height='260' viewBox='0 0 620 260' style='margin-bottom:10px'>
    <rect width='620' height='260' fill='rgba(5,8,28,.7)' stroke='#C9D1DC' stroke-width='3'/>
    <polyline fill='none' stroke='#E5462A' stroke-width='5' stroke-linejoin='round' points='20,140 60,140 80,60 100,220 120,140 170,140 190,90 210,200 230,140 280,140'/>
    <g fill='#7bc043'><rect x='330' y='150' width='26' height='60'/><rect x='372' y='120' width='26' height='90'/><rect x='414' y='130' width='26' height='70'/><rect x='456' y='90' width='26' height='110'/><rect x='498' y='60' width='26' height='120'/><rect x='540' y='30' width='26' height='130'/></g>
    <g stroke='#7bc043' stroke-width='4'><line x1='343' y1='135' x2='343' y2='225'/><line x1='385' y1='105' x2='385' y2='225'/><line x1='427' y1='115' x2='427' y2='215'/><line x1='469' y1='75' x2='469' y2='215'/><line x1='511' y1='45' x2='511' y2='195'/><line x1='553' y1='15' x2='553' y2='175'/></g>
    <text x='30' y='40' fill='#9AA6C4' font-family='DejaVu Sans Mono' font-size='20' letter-spacing='3'>EEG</text>
    <text x='590' y='40' fill='#7bc043' font-family='DejaVu Sans Mono' font-size='20' letter-spacing='3' text-anchor='end'>BULLISH</text>
  </svg>
  <div class='foot' style='width:100%'><span class='ticker'>$FELICETTE</span><span>Diagnosis: up</span></div>
</div>""")

memes['07_ham_vs_felicette'] = page(f"""
{M('')}
<div class='frame'>
  <div style='max-width:640px'>
    <div class='tag'>Lesson from 1961–1963</div>
    <div class='big md' style='margin-top:18px'>Ham the chimp pulled levers for banana pellets.</div>
    <div class='big md red' style='margin-top:22px'>Félicette did nothing for 15 minutes and made history.</div>
    <div class='big md' style='margin-top:22px'>Be like Félicette.<br>Hold.</div>
  </div>
  <div class='foot'><span>Hold the cat, collect SpaceX</span><span class='ticker'>$FELICETTE</span></div>
</div>""")

memes['08_every_launch'] = page(f"""
{M('center')}
<div class='frame' style='text-align:center;align-items:center'>
  <div>
    <div class='tag'>Launch day protocol</div>
    <div class='big xl' style='margin-top:14px'>Every SpaceX launch<br>is a <span class='red'>Félicette</span><br>launch.</div>
  </div>
  <div class='foot' style='width:100%'><span class='mono' style='font-size:40px;font-weight:700;color:#fff'>T-00:00:00</span><span class='ticker'>$FELICETTE</span></div>
</div>""")

memes['09_checklist'] = page(f"""
{M('')}
<div class='frame'>
  <div>
    <div class='tag'>Mission checklist · C 341</div>
    <div class='big' style='margin-top:12px;margin-bottom:28px'>Status</div>
    <div class='panel list' style='width:600px'>
      <div><span class='box'>✓</span>Launch</div>
      <div><span class='box'>✓</span>Reach 157 km</div>
      <div><span class='box'>✓</span>Come back alive</div>
      <div><span class='box'>✓</span>Statue (56 yrs later)</div>
      <div><span class='box hot'>✕</span><span class='red'>Get paid</span></div>
    </div>
  </div>
  <div class='foot'><span>Fixing the last one</span><span class='ticker'>$FELICETTE</span></div>
</div>""")

memes['10_calmest_cat'] = page(f"""
{M('left small')}
<div class='frame' style='align-items:flex-end;text-align:right'>
  <div style='max-width:640px'>
    <div class='tag'>Selection report · 1963</div>
    <div class='big md' style='margin-top:18px'>She was picked out of 14 cats because she stayed the calmest.</div>
    <div class='big md red' style='margin-top:22px'>Be the calmest cat in the trenches.</div>
  </div>
  <div class='foot' style='width:100%'><span class='ticker'>$FELICETTE</span><span>No staking · no claiming · no panic</span></div>
</div>""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1080})
        for name, html_ in memes.items():
            path = f'{OUT}/{name}.html'
            open(path,'w').write(html_)
            await pg.goto('file://'+path); await pg.wait_for_timeout(200)
            await pg.screenshot(path=f'{OUT}/{name}.png')
            print('ok', name)
        await b.close()
asyncio.run(main())
