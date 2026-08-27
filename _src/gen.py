# -*- coding: utf-8 -*-
"""Renders the Cooldown App Store pages into the repo root.

    python3 _src/gen.py

One file, no dependencies. Every visual value below is taken from the app's own
design tokens (Cooldown/Core/DesignSystem/DesignTokens.swift in the app repo) so
the pages read as the same product: the same night-sky background, the same dusk
indigo, savings green reserved for realised saves, cooling amber for items still
on ice, and the same radii.
"""
import os, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)

BASE = "/cooldown-links"
SITE = "https://sohaibiii.github.io" + BASE
APP = "Cooldown"
COMPANY = "TOPSOL"
EMAIL = "topsol.org@gmail.com"
UPDATED = "27 August 2026"
YEAR = "2026"

# Set this once App Store Connect has assigned the Apple ID, e.g.
# "https://apps.apple.com/app/id1234567890". Until then every "App Store" button
# renders as a quiet "coming soon" label rather than a dead link.
APP_STORE_URL = None

NAV = [
    ("support", "Support", f"{BASE}/"),
    ("about", "About", f"{BASE}/about/"),
    ("privacy", "Privacy", f"{BASE}/privacy/"),
    ("terms", "Terms", f"{BASE}/terms/"),
    ("data", "Your data", f"{BASE}/delete-data/"),
]

E = lambda s: html.escape(s, quote=True)
CUR = ' aria-current="page"'

# ---------------------------------------------------------------------------
# Chrome
# ---------------------------------------------------------------------------

CSS = r"""
:root{
  --bg:#F5F6FA;--surface:#FFFFFF;--fill:#EAECF4;--ink:#12151B;--ink-2:#5A6070;--ink-3:#6B7180;
  --line:rgba(0,0,0,.06);--accent:#4A5AC4;--accent-strong:#3F4EB2;--accent-soft:rgba(74,90,196,.12);--on-accent:#FFFFFF;
  --glow:transparent;--card-shadow:0 10px 30px rgba(18,21,27,.07);--card-edge:transparent;
  --savings:#2E7D4F;--savings-soft:rgba(46,125,79,.13);--cooling:#8A5D0A;--cooling-soft:rgba(138,93,10,.13);
  --hero-top:#1D2347;--hero-bottom:#12152A;--hero-glow:rgba(123,140,222,.42);--hero-ink:#F2F4F7;--hero-ink-2:rgba(242,244,247,.74);--hero-stroke:rgba(255,255,255,.10);--hero-fill:rgba(255,255,255,.10);
  --moon-core:#D3DCFF;--moon-edge:#8FA0EA;--moon-glow:rgba(123,140,222,.70);
  --r-card:20px;--r-hero:28px;--r-control:14px;--r-chip:12px;--r-tile:10px;
  --max:760px;--wide:1080px;
  --display:"Nunito",ui-rounded,"SF Pro Rounded",-apple-system,system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){:root{
  --bg:#0F1214;--surface:#181D20;--fill:#222931;--ink:#F2F4F7;--ink-2:#9AA3AF;--ink-3:#7C8594;
  --line:rgba(255,255,255,.08);--accent:#8FA0EA;--accent-strong:#A3B2F2;--accent-soft:rgba(123,140,222,.16);--on-accent:#0F1214;
  --glow:rgba(123,140,222,.35);--card-shadow:none;--card-edge:rgba(255,255,255,.07);
  --savings:#7FC98F;--savings-soft:rgba(127,201,143,.16);--cooling:#E8C170;--cooling-soft:rgba(232,193,112,.16);
}}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{animation:none!important;transition:none!important}}
html,body{overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:var(--accent);text-decoration:underline;text-decoration-color:color-mix(in srgb,var(--accent) 40%,transparent);text-underline-offset:3px;overflow-wrap:anywhere}
a:hover{text-decoration-color:var(--accent)}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}
.skip{position:absolute;top:8px;left:8px;background:var(--surface);color:var(--ink);padding:8px 12px;z-index:20;border-radius:var(--r-chip);box-shadow:var(--card-shadow)}
.skip:not(:focus){clip:rect(0 0 0 0);clip-path:inset(50%);width:1px;height:1px;overflow:hidden;white-space:nowrap;padding:0;margin:-1px}
h1,h2,h3{margin:0;letter-spacing:-.022em;text-wrap:balance;font-family:var(--display);font-weight:800}
h1{font-size:clamp(32px,4.6vw,48px);line-height:1.06}
h2{font-size:25px;line-height:1.24}
h3{font-weight:700;font-size:18px;line-height:1.3}
p{margin:0 0 1em}
p:last-child{margin-bottom:0}
ul,ol{margin:0;padding-left:1.3em}
li{margin:.45em 0}
li::marker{color:var(--accent)}
strong{font-weight:600}
.muted{color:var(--ink-2)}
small,.small{font-size:14px;color:var(--ink-2)}
code{font:.92em ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:var(--fill);padding:.1em .4em;border-radius:6px}
kbd{font:inherit;background:var(--fill);border-radius:8px;padding:.05em .5em;white-space:nowrap}
.est{font-style:normal;color:var(--ink-2);font-size:.86em;font-weight:500}

/* top bar — the one glass surface, like the app's navigation layer */
.topbar{position:sticky;top:0;z-index:10;background:color-mix(in srgb,var(--bg) 82%,transparent);-webkit-backdrop-filter:saturate(1.4) blur(14px);backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--line)}
.topbar .in{max-width:var(--wide);margin:0 auto;padding:12px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.brand{display:inline-flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-family:var(--display);font-weight:800;font-size:20px;letter-spacing:-.02em}
.mark{width:26px;height:26px;border-radius:8px;flex:none;display:grid;place-items:center;background:linear-gradient(160deg,#252B52,#12152A);box-shadow:0 0 0 1px var(--hero-stroke),0 0 14px var(--moon-glow)}
.mark svg{width:15px;height:15px}
nav.pages{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
nav.pages a{text-decoration:none;color:var(--ink-2);font-size:15px;font-weight:500;padding:7px 12px;border-radius:999px}
nav.pages a[aria-current="page"]{color:var(--accent);background:var(--accent-soft)}
nav.pages a:hover{color:var(--ink)}
@media (max-width:640px){nav.pages{margin-left:0;width:100%;overflow-x:auto;flex-wrap:nowrap;scrollbar-width:none;padding-bottom:2px}nav.pages::-webkit-scrollbar{display:none}nav.pages a{flex:none}}

/* hero — the app's protection island, dark in both appearances */
.hero-wrap{max-width:var(--wide);margin:24px auto 0;padding:0 20px}
.hero{position:relative;overflow:hidden;border-radius:var(--r-hero);background:linear-gradient(135deg,var(--hero-top),var(--hero-bottom));color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke),0 24px 60px rgba(15,18,20,.20);padding:clamp(36px,6vw,64px) clamp(24px,5vw,56px)}
.hero::before{content:"";position:absolute;inset:-40% -18% auto auto;width:62%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--hero-glow) 0,transparent 62%);pointer-events:none}
.hero>*{position:relative}
.hero .eyebrow{display:inline-flex;align-items:center;gap:9px;font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--hero-ink-2);margin-bottom:18px;font-family:var(--display)}
.hero .eyebrow .dot{width:9px;height:9px;border-radius:50%;background:var(--moon-edge);box-shadow:0 0 10px var(--moon-glow)}
.hero h1{max-width:18ch}
.hero .sub{margin:16px 0 0;max-width:56ch;font-size:clamp(17px,2vw,20px);color:var(--hero-ink-2)}
.hero .ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px;align-items:center}
.hero .ctas a,.hero .ctas span{color:var(--hero-ink)}
.hero .ctas .btn.primary{background:linear-gradient(to bottom,#8FA0EA,#7B8CDE);color:#0F1214;box-shadow:0 8px 24px rgba(123,140,222,.34)}
.hero .ctas .btn.quiet{background:var(--hero-fill);color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke)}
.hero .meta{margin-top:22px;font-size:14px;color:var(--hero-ink-2)}
.hero .meta a{color:var(--hero-ink);text-decoration-color:rgba(255,255,255,.4)}

/* buttons */
.btn{display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:16px;line-height:1;padding:14px 20px;border-radius:var(--r-control);text-decoration:none;white-space:nowrap}
.btn.primary{background:var(--accent);color:var(--on-accent);box-shadow:0 8px 24px var(--glow)}
.btn.quiet{background:var(--fill);color:var(--ink)}
.btn svg{width:18px;height:18px;flex:none}
.soon{display:inline-flex;align-items:center;gap:8px;font-size:15px;color:var(--hero-ink-2);padding:12px 4px}
.soon svg{width:18px;height:18px;flex:none}

/* content */
main{max-width:var(--wide);margin:0 auto;padding:32px 20px 64px}
.grid{display:grid;grid-template-columns:minmax(0,1fr);gap:20px}
@media (min-width:900px){.grid.with-toc{grid-template-columns:240px minmax(0,1fr);align-items:start}}
.toc{position:sticky;top:76px;padding:20px 22px;border-radius:var(--r-card);background:var(--surface);box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge)}
.toc .lbl{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);margin-bottom:10px;font-family:var(--display)}
.toc ol{list-style:none;padding:0;margin:0}
.toc li{margin:0}
.toc a{display:block;padding:6px 0;font-size:15px;color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--line)}
.toc li:last-child a{border-bottom:0}
.toc a:hover{color:var(--accent)}
.stack{display:grid;gap:20px;max-width:var(--max)}
.grid.with-toc .stack{max-width:none}
.card{background:var(--surface);border-radius:var(--r-card);padding:clamp(22px,3.4vw,32px);box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge)}
.card h2{margin-bottom:12px;scroll-margin-top:84px}
.card h3{margin:20px 0 6px}
.card h3:first-of-type{margin-top:0}
.card p+h3{margin-top:18px}
.lead{font-size:clamp(18px,2vw,21px);line-height:1.5;color:var(--ink)}
.stamp{font-size:14px;color:var(--ink-2);margin:0 0 4px}
.callout{display:flex;gap:14px;align-items:flex-start;padding:16px 18px;border-radius:var(--r-control);background:var(--accent-soft)}
.callout .tile{flex:none;width:32px;height:32px;border-radius:var(--r-tile);display:grid;place-items:center;background:var(--accent);color:var(--on-accent)}
.callout .tile svg{width:18px;height:18px}
.callout.amber{background:var(--cooling-soft)}.callout.amber .tile{background:var(--cooling);color:var(--bg)}
.callout.green{background:var(--savings-soft)}.callout.green .tile{background:var(--savings);color:var(--bg)}
.rows{list-style:none;padding:0;margin:0;display:grid;gap:2px}
.rows li{display:grid;grid-template-columns:40px minmax(0,1fr);gap:14px;padding:12px 0;margin:0;border-bottom:1px solid var(--line);align-items:start}
.rows li:last-child{border-bottom:0}
.rows .tile{width:40px;height:40px;border-radius:var(--r-tile);display:grid;place-items:center;background:var(--accent-soft);color:var(--accent)}
.rows .tile.amber{background:var(--cooling-soft);color:var(--cooling)}
.rows .tile.green{background:var(--savings-soft);color:var(--savings)}
.rows .tile svg{width:20px;height:20px}
.rows b{display:block;font-weight:600}
.rows span{color:var(--ink-2);font-size:15.5px}
.features{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.features .card{display:flex;flex-direction:column;gap:10px}
.features .tile{width:44px;height:44px;border-radius:var(--r-chip);display:grid;place-items:center;background:var(--accent-soft);color:var(--accent);margin-bottom:6px}
.features .tile.amber{background:var(--cooling-soft);color:var(--cooling)}
.features .tile.green{background:var(--savings-soft);color:var(--savings)}
.features .tile svg{width:22px;height:22px}
.features .card h3{margin:0}
.features .card p{color:var(--ink-2);font-size:16px}
.tiers{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.tier{background:var(--surface);border-radius:var(--r-card);padding:24px;box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge);display:flex;flex-direction:column;gap:10px}
.tier .lbl{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);font-family:var(--display)}
.tier .price{font-family:var(--display);font-size:28px;font-weight:800;letter-spacing:-.02em}
.tier .price small{font-size:15px;font-weight:500;color:var(--ink-2)}
.tier ul{margin-top:4px;color:var(--ink-2);font-size:15.5px}
.tier.premium{background:linear-gradient(135deg,var(--hero-top),var(--hero-bottom));color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke)}
.tier.premium .lbl,.tier.premium ul{color:var(--hero-ink-2)}
.tier.premium li::marker{color:#8FA0EA}
.chip{display:inline-flex;align-items:center;gap:6px;background:var(--fill);color:var(--ink-2);border-radius:999px;padding:4px 10px;font-size:13.5px;font-weight:500}
dl.faq{margin:0}
dl.faq dt{font-weight:600;margin-top:18px}
dl.faq dt:first-child{margin-top:0}
dl.faq dd{margin:6px 0 0;color:var(--ink-2)}
table{width:100%;border-collapse:collapse;font-size:15.5px}
th,td{text-align:left;vertical-align:top;padding:10px 12px 10px 0;border-bottom:1px solid var(--line)}
th{font-weight:700;color:var(--ink-2);font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-family:var(--display)}
tr:last-child td{border-bottom:0}
.table-wrap{overflow-x:auto}
.steps{counter-reset:s;list-style:none;padding:0;margin:0;display:grid;gap:12px}
.steps li{display:grid;grid-template-columns:32px minmax(0,1fr);gap:14px;margin:0;align-items:start}
.steps li::before{counter-increment:s;content:counter(s);width:32px;height:32px;border-radius:50%;display:grid;place-items:center;background:var(--accent);color:var(--on-accent);font-weight:800;font-size:14px;font-family:var(--display)}

/* footer */
footer{border-top:1px solid var(--line);padding:28px 20px 44px;color:var(--ink-2);font-size:14.5px}
footer .in{max-width:var(--wide);margin:0 auto;display:flex;gap:10px 22px;flex-wrap:wrap;align-items:center;justify-content:space-between}
footer nav{display:flex;gap:6px 16px;flex-wrap:wrap}
footer a{color:var(--ink-2)}
footer a:hover{color:var(--accent)}
"""

MOON = '<svg viewBox="0 0 100 100" aria-hidden="true"><defs><radialGradient id="mg" cx="38%" cy="32%" r="72%"><stop offset="0" stop-color="#D3DCFF"/><stop offset="1" stop-color="#8FA0EA"/></radialGradient></defs><path d="M50 6a44 44 0 1 0 40 62A36 36 0 0 1 50 6Z" fill="url(#mg)"/></svg>'

ICONS = {
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/></svg>',
    "snow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 2v20M3.5 7l17 10M20.5 7l-17 10"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/></svg>',
    "note": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h11l4 4v12H5z"/><path d="M9 11h7M9 15h5"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.7 2.6 15.3 0 18M12 3c-2.6 2.7-2.6 15.3 0 18"/></svg>',
    "eye-off": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3l18 18M10.6 10.6a2 2 0 0 0 2.8 2.8M9.9 5.1A10 10 0 0 1 12 5c5 0 8.5 4 9.5 7-.4 1.1-1.1 2.3-2 3.3M6.6 6.6C4.6 8 3.3 10 2.5 12c1 3 4.5 7 9.5 7 1.6 0 3-.4 4.3-1"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "trash": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>',
    "info": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l4 4L19 6"/></svg>',
    "apple": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.3 1.2 9.7.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.2-.8s1.9.8 3.2.8 2.1-1.2 2.9-2.4c.9-1.4 1.3-2.7 1.3-2.8-.1 0-2.5-1-2.5-3.8zM14 5.5c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1.1.1 2.2-.6 2.8-1.4z"/></svg>',
    "widget": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/></svg>',
    "bell": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15L6 16z"/><path d="M10 21h4"/></svg>',
    "sparkle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M18 16l.8 2.2L21 19l-2.2.8L18 22l-.8-2.2L15 19l2.2-.8z"/></svg>',
    "coin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2.6" y="6" width="18.8" height="12" rx="2.6"/><circle cx="12" cy="12" r="2.7"/></svg>',
}


def store_button(hero=False):
    if APP_STORE_URL:
        return f'<a class="btn primary" href="{E(APP_STORE_URL)}">{ICONS["apple"]} Download on the App Store</a>'
    return f'<span class="soon">{ICONS["apple"]} Coming soon to the App Store</span>'


def page(key, title, description, hero, body, toc=None, canonical=""):
    nav = "".join(
        f'<a href="{E(href)}"{CUR if k == key else ""}>{E(label)}</a>'
        for k, label, href in NAV
    )
    footnav = " · ".join(f'<a href="{E(href)}">{E(label)}</a>' for k, label, href in NAV)
    toc_html = ""
    grid_cls = "grid"
    if toc:
        grid_cls = "grid with-toc"
        toc_html = '<aside class="toc" aria-label="On this page"><div class="lbl">On this page</div><ol>' + "".join(
            f'<li><a href="#{E(i)}">{E(t)}</a></li>' for i, t in toc
        ) + "</ol></aside>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{E(description)}">
<meta name="robots" content="index,follow">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#F5F6FA">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#0F1214">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{E(SITE + canonical)}">
<link rel="canonical" href="{E(SITE + canonical)}">
<link rel="icon" href="{BASE}/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png">
<title>{E(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="topbar"><div class="in">
  <a class="brand" href="{BASE}/"><span class="mark" aria-hidden="true">{MOON}</span>{APP}</a>
  <nav class="pages" aria-label="Pages">{nav}</nav>
</div></header>
<div class="hero-wrap"><section class="hero">{hero}</section></div>
<main id="content"><div class="{grid_cls}">{toc_html}<div class="stack">{body}</div></div></main>
<footer><div class="in">
  <div>© {YEAR} {APP} · {COMPANY} · All rights reserved.</div>
  <nav aria-label="Footer">{footnav} · <a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body>
</html>
"""


def hero(eyebrow, h1, sub, ctas="", meta=""):
    return (
        f'<div class="eyebrow"><span class="dot" aria-hidden="true"></span>{eyebrow}</div>'
        f"<h1>{h1}</h1><p class=\"sub\">{sub}</p>"
        + (f'<div class="ctas">{ctas}</div>' if ctas else "")
        + (f'<p class="meta">{meta}</p>' if meta else "")
    )


def card(id_, h2, inner):
    return f'<section class="card" id="{id_}"><h2 id="{id_}-h">{h2}</h2>{inner}</section>'


def callout(icon, text, tone=""):
    cls = f" {tone}" if tone else ""
    return f'<div class="callout{cls}"><span class="tile">{ICONS[icon]}</span><div>{text}</div></div>'


MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

# ---------------------------------------------------------------------------
# Support — the App Store "Support URL"
# ---------------------------------------------------------------------------

SUPPORT_TOC = [
    ("how", "How Cooldown works"),
    ("requirements", "Requirements"),
    ("start", "Getting started"),
    ("money", "About the savings number"),
    ("faq", "Frequently asked questions"),
    ("trouble", "Troubleshooting"),
    ("contact", "Contact"),
]

support_body = "".join([
    card("how", "How Cooldown works", f"""
<p class="lead">Cooldown puts one night between you and the buy button.</p>
<p>You choose the shopping apps and websites that get you. From then on, opening one does not take you straight to the checkout — Cooldown steps in first with a quiet screen that says <em>Sleep on it.</em> You can note the thing down, walk away, or open the shop anyway for a few minutes. Nothing is ever bought or cancelled on your behalf.</p>
<p>Anything you note down waits twenty-four hours. When the wait is over Cooldown asks one question: do you still want it? Most wants don't survive the night — and the ones that do were real.</p>
<ul class="rows">
  <li><span class="tile">{ICONS['shield']}</span><div><b>Protection</b><span>One switch. While it is on, the shops you chose show Cooldown's shield instead of opening — the app <em>and</em> the website, including in Safari.</span></div></li>
  <li><span class="tile">{ICONS['note']}</span><div><b>Capture</b><span>Name the thing, tap a price, tap how you feel — bored, stressed, celebrating, deal FOMO, or “I need it”. Fifteen seconds, one screen, no keyboard gymnastics.</span></div></li>
  <li><span class="tile amber">{ICONS['snow']}</span><div><b>On ice</b><span>Captured items wait under a slow twenty-four-hour ring. Nothing is bought while an item cools.</span></div></li>
  <li><span class="tile green">{ICONS['coin']}</span><div><b>Estimated savings</b><span>Every item you let go counts toward a running total, built entirely from prices you typed yourself.</span></div></li>
  <li><span class="tile amber">{ICONS['clock']}</span><div><b>Danger hours and rules</b><span>Make late nights a little stricter, or close one shop's door entirely between certain hours. The rule lifts on its own.</span></div></li>
  <li><span class="tile">{ICONS['lock']}</span><div><b>Strict mode</b><span>Hold your own setup in place so it can't be undone in the moment you would most like to undo it.</span></div></li>
  <li><span class="tile">{ICONS['widget']}</span><div><b>Widgets</b><span>This month's estimated savings and what's on ice, on the Home Screen and the Lock Screen, with a Live Activity while an item cools.</span></div></li>
</ul>
"""),
    card("requirements", "Requirements", f"""
<div class="table-wrap"><table>
<tr><th>Device</th><td>iPhone running <strong>iOS 17 or newer</strong>. Cooldown is designed for iPhone.</td></tr>
<tr><th>Permission</th><td><strong>Screen Time</strong> access, granted once during setup through Apple's own prompt. Cooldown uses Apple's Screen Time framework — the same system behind iOS's built-in app limits — and Apple, not Cooldown, is what actually stands in front of a shop.</td></tr>
<tr><th>Account</th><td>None. There is no sign-up, no email field and no password anywhere in the app.</td></tr>
<tr><th>Internet</th><td>Not needed. Every shield, capture, timer and total works offline. The only network traffic is Apple's when you buy or restore Premium — and the optional AI reflection, if you switch it on.</td></tr>
<tr><th>Notifications</th><td>Optional, and generated on the phone. Cooldown uses them to hand you from the shield into the capture screen, and to tell you when an item's cooldown is over.</td></tr>
</table></div>
"""),
    card("start", "Getting started", f"""
<p>Setup is a handful of screens and ends with protection already on.</p>
<ol class="steps">
  <li><div><b>Allow Screen Time access</b> when Apple asks. Cooldown cannot work without it, and you can withdraw it any time in <kbd>Settings</kbd> → <kbd>Screen Time</kbd>.</div></li>
  <li><div><b>Pick your shops</b> in Apple's picker, and add the websites you want shielded. Cooldown never learns their names — see <a href="{BASE}/privacy/">Privacy</a>.</div></li>
  <li><div><b>Set danger hours</b> if you want them — the hours when shopping goes badly for you. Optional, and changeable later.</div></li>
  <li><div><b>Done.</b> Open one of your shops and meet the shield.</div></li>
</ol>
{callout('info', 'The first shield can feel abrupt. That is the moment the app exists for — tap <strong>Something caught my eye</strong> and take fifteen seconds.')}
"""),
    card("money", "About the savings number", f"""
<p>Every price in Cooldown is one you typed yourself, and every figure the app shows is labelled <strong>estimated</strong>. That is not a disclaimer bolted on afterwards — it is the whole design.</p>
<ul>
  <li>Cooldown <strong>does not connect to your bank</strong>, read your purchase history, or check what anything actually costs.</li>
  <li>An item counts toward the total <strong>once</strong>, when you let it go after cooling down.</li>
  <li>Items you keep never touch the total, and keeping something is not treated as a failure anywhere in the app.</li>
</ul>
{callout('coin', 'The number is a record of what you decided not to buy, at the prices you guessed. It is a good number to be proud of and a bad number to put in a spreadsheet.', tone='green')}
"""),
    card("faq", "Frequently asked questions", f"""
<dl class="faq">
<dt>Is Cooldown free?</dt>
<dd>Yes, and free is a working product rather than a demo: <strong>one shopping app and one website</strong> shielded, the full twenty-four-hour cooldown list, and your estimated savings.</dd>
<dt>What does Premium add?</dt>
<dd>Every shop and website you want to shield, cooldown lengths of 12, 24, 48 or 72 hours, danger-hour and per-shop rules, strict mode, how purchases felt afterwards, widgets, and the optional reflection. Premium is a monthly or yearly subscription — the yearly plan starts with a <strong>free trial</strong> — or a single lifetime purchase. Prices are shown in the app for your country, and billing is handled by Apple.</dd>
<dt>Does it block me from buying things?</dt>
<dd>No. Every shield has a way through: <em>I need to shop now</em> opens the shop for a few minutes. Cooldown is a shield, not a wall — it asks you to notice, and then it gets out of the way.</dd>
<dt>What happens if my subscription lapses?</dt>
<dd>Nothing you built is taken away. Your history and your savings total stay, and the shops you already chose stay shielded. Only the ability to add more Premium content closes.</dd>
<dt>Can I restore a purchase on a new phone?</dt>
<dd>Yes. Open the Premium screen and tap <kbd>Restore purchases</kbd>. Premium belongs to your Apple ID, not to the phone.</dd>
<dt>Why can't Cooldown tell me which shops I protected?</dt>
<dd>Because it genuinely does not know. Apple's Screen Time hands Cooldown opaque tokens that are meaningless outside your phone — no app names, no identifiers. Cooldown can ask iOS to shield them; it cannot read them.</dd>
<dt>Does it shield websites, or only apps?</dt>
<dd>Both. A shielded shop is shielded in its app and on its website in Safari.</dd>
<dt>I can't turn protection off. Is something broken?</dt>
<dd>Check whether <strong>strict mode</strong> is running — the home screen says so. While it runs, your setup is held in place by design. It ends on its own at the time you chose.</dd>
<dt>Does Cooldown see what I buy?</dt>
<dd>No. It has no access to your bank, your orders, your browsing or your card. It records only its own events — that a shield was shown, and what you chose — and keeps those on your phone.</dd>
<dt>What is the AI reflection, and is it on?</dt>
<dd>It is one short question before the choices, and a few sentences about your week on Sundays. It is <strong>off until you turn it on</strong>. When it is on, it is the only thing in the app that sends anything off the phone, and the <a href="{BASE}/privacy/">Privacy Policy</a> lists exactly what.</dd>
<dt>Does it work on iPad or Mac?</dt>
<dd>Cooldown is built for iPhone. It is not offered on other devices.</dd>
</dl>
"""),
    card("trouble", "Troubleshooting", f"""
<h3>A shop opens without a shield</h3>
<ul>
  <li>Check the <strong>Protection</strong> switch on the home screen.</li>
  <li>Check that Screen Time access is still granted: <kbd>Settings</kbd> → <kbd>Screen Time</kbd> → <kbd>Apps with Screen Time access</kbd>. If it was withdrawn, Cooldown shows a recovery screen with a button to ask again.</li>
  <li>A <strong>shopping window</strong> you opened earlier may still be running. It closes on its own, and the shield comes back.</li>
  <li>If the shop is covered only by a <strong>rule</strong>, the shield appears only during that rule's hours.</li>
</ul>
<h3>The shield appears but the capture screen never opens</h3>
<ul>
  <li>Tapping <strong>Something caught my eye</strong> hands you to Cooldown through a notification. If notifications are off, iOS cannot deliver the hand-off — turn them on in <kbd>Settings</kbd> → <kbd>Notifications</kbd> → <kbd>Cooldown</kbd>.</li>
  <li>Opening Cooldown directly also opens the waiting capture.</li>
</ul>
<h3>A website isn't shielded</h3>
<p>Websites are shielded by domain. Make sure the domain you added matches the one you actually open, and note that a shop's app and its website are two separate things to add.</p>
<h3>Widgets are behind</h3>
<p>iOS refreshes widgets on its own schedule. Opening Cooldown brings them up to date immediately.</p>
<h3>Premium isn't recognised</h3>
<p>Tap <kbd>Restore purchases</kbd> on the Premium screen, and make sure the phone is signed into the same Apple ID that made the purchase. Refunds and billing questions are handled by Apple through <a href="https://support.apple.com/billing">Apple Support</a>.</p>
"""),
    card("contact", "Contact", f"""
<p>Questions, a bug, or something that should work and doesn't — write to us and a person will reply.</p>
{callout('mail', f'<strong>{MAIL}</strong><br><span class="small">Include your iPhone model, the iOS version, and what you expected to happen. Never send us your wishlist or your prices — we do not need them and would rather not hold them.</span>')}
<p style="margin-top:16px" class="small">Billing, refunds and subscription changes are handled by Apple: <a href="https://apps.apple.com/account/subscriptions">manage subscriptions</a> · <a href="https://support.apple.com/billing">request a refund</a>.</p>
"""),
])

support_hero = hero(
    "Support",
    "Help with Cooldown",
    "One night between you and the buy button. Cooldown shields the shopping apps and websites you chose and asks you to sleep on it first. This page covers how it works, what it needs, and how to reach us.",
    store_button(True) + f'<a class="btn quiet" href="#faq">Read the FAQ</a>',
    f'No account · no bank access · <a href="{BASE}/privacy/">Privacy Policy</a>',
)

# ---------------------------------------------------------------------------
# About — the App Store "Marketing URL"
# ---------------------------------------------------------------------------

about_body = f"""
<section class="card"><p class="lead">Cooldown puts one night between you and the buy button. Not a lockout, not a lecture — twenty-four hours to find out whether you actually wanted it.</p></section>
<div class="features">
  <section class="card"><span class="tile">{ICONS['moon']}</span><h3>Sleep on it.</h3><p>Open a shop you've chosen and Cooldown steps in before the checkout does — in the app and in Safari. Ten seconds of night sky instead of one-tap buying.</p></section>
  <section class="card"><span class="tile">{ICONS['note']}</span><h3>Note it, don't buy it.</h3><p>Name the thing, tap a price, tap how you feel. Fifteen seconds, one screen. The capture has to be faster than the craving.</p></section>
  <section class="card"><span class="tile amber">{ICONS['snow']}</span><h3>One night on ice.</h3><p>Captured items wait under a slow twenty-four-hour ring. Nothing is bought while an item cools, and tomorrow you gets the decision.</p></section>
  <section class="card"><span class="tile green">{ICONS['chart']}</span><h3>Watch it add up.</h3><p>Every item you let go counts toward your estimated savings — your own guesses, by month, next to the hours of the day the shields keep meeting you.</p></section>
  <section class="card"><span class="tile">{ICONS['shield']}</span><h3>A shield, not a wall.</h3><p>Sleep on it, walk away, or open the shop anyway for a few minutes. Nothing here scolds you for wanting things, and nothing turns red if you buy it.</p></section>
  <section class="card"><span class="tile">{ICONS['eye-off']}</span><h3>It never sees what you buy.</h3><p>No bank linking, no purchase history, no price tracking, no affiliate links. Apple hands Cooldown codes, not names. <a href="{BASE}/privacy/">How that works.</a></p></section>
</div>
<section class="card" id="pricing"><h2>What it costs</h2>
<p>Free is a working product, not a demo, and nothing you have already built is taken away if a subscription lapses.</p>
<div class="tiers" style="margin-top:16px">
  <div class="tier"><div class="lbl">Free</div><div class="price">$0</div><ul><li>One shopping app and one website, shielded</li><li>The full 24-hour cooldown list</li><li>Your estimated savings</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Monthly · Yearly · Lifetime</div><ul><li>Every shop and website you want</li><li>Cooldowns of 12, 24, 48 or 72 hours</li><li>Danger hours, per-shop rules and strict mode</li><li>How purchases felt afterwards</li><li>Widgets, and the optional reflection</li><li>Yearly starts with a free trial</li></ul></div>
</div>
<p class="small" style="margin-top:14px">Prices are shown in the app and on the App Store for your country. Billing is handled by Apple. <a href="{BASE}/terms/#subscriptions">Subscription terms.</a></p>
</section>
<section class="card"><h2>Built on Apple's Screen Time</h2>
<p>Cooldown uses the same framework that powers iOS's built-in app limits. Apple grants it only to apps it has reviewed for the purpose, and Apple — not Cooldown — is what actually stands between you and the shop. That is why Cooldown can shield a shop without ever learning its name.</p>
<p>iPhone · iOS 17 or newer · English</p>
</section>
<section class="card"><h2>Every figure is an estimate</h2>
<p>Cooldown asks you what something roughly costs and remembers your answer. It connects to no bank, verifies no price, and gives no financial advice. Every number it shows carries the word <em class="est">estimated</em>, in the app, in the widgets and on this site.</p>
</section>
"""

about_hero = hero(
    "About Cooldown",
    "One night between you and the buy button.",
    "Pick the shopping apps and websites that get you. From then on, opening one gets you a shield first — and a decision that tomorrow you gets to make.",
    store_button(True) + f'<a class="btn quiet" href="{BASE}/">Support</a>',
    "No account · no bank access · iPhone, iOS 17+",
)

# ---------------------------------------------------------------------------
# Privacy Policy
# ---------------------------------------------------------------------------

PRIVACY_TOC = [
    ("summary", "The short version"),
    ("collect", "What we collect"),
    ("device", "What stays on your phone"),
    ("screentime", "Screen Time and your shops"),
    ("ai", "The one thing that can leave the phone"),
    ("purchases", "Purchases"),
    ("notifications", "Notifications, widgets and the Lock Screen"),
    ("third", "Third parties"),
    ("delete", "Deleting your data"),
    ("rights", "Your rights"),
    ("children", "Children"),
    ("changes", "Changes to this policy"),
    ("contact", "Contact"),
]

privacy_body = "".join([
    f'<p class="stamp">Last updated: {UPDATED}</p>',
    card("summary", "The short version", f"""
<p class="lead"><strong>Cooldown has no account, no analytics, no advertising and no third-party SDKs.</strong> There is no bank connection, no purchase history, no price tracking and no affiliate link anywhere in it. Everything it knows is written to your iPhone and stays there.</p>
{callout("eye-off", "Cooldown does not even know which shops you chose to shield. Apple's Screen Time gives it opaque tokens that only your phone can interpret. There is no app name, no domain, no identifier, and nothing to send.")}
<p style="margin-top:16px">There is exactly one exception, and it is off until you switch it on: the optional <strong>AI reflection</strong>. What it sends is listed in full <a href="#ai">below</a> — and switching it off returns the app to making no network calls of its own at all.</p>
<p>This policy applies to the Cooldown app for iPhone, published by {COMPANY}, and to this website.</p>
"""),
    card("collect", "What we collect", f"""
<p>With the AI reflection off — the state the app ships in — nothing. In Apple's terms, "collecting" means transmitting data off the device and storing it somewhere that is not transient. Cooldown has no channel through which that could happen.</p>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Collected?</th><th>Why not</th></tr>
<tr><td>Financial info</td><td>No</td><td>No bank connection, no card, no transaction access, no purchase history. Every price in the app is a figure you typed and it never leaves the phone.</td></tr>
<tr><td>Contact info</td><td>No</td><td>There is no account, no sign-in and no email field anywhere in the app.</td></tr>
<tr><td>Identifiers</td><td>No</td><td>No user ID, no device ID, no advertising identifier. Cooldown never asks for App Tracking Transparency because it has nothing to ask about.</td></tr>
<tr><td>Usage data</td><td>No</td><td>No analytics SDK and no product-interaction events. Shields met, items cooled and items let go are counted on your phone, for your own screens.</td></tr>
<tr><td>Browsing history</td><td>No</td><td>Cooldown cannot see what you browse. It learns only that its own shield was shown, and what you chose on it.</td></tr>
<tr><td>User content</td><td>Only if you switch on the AI reflection</td><td>Your wishlist, prices, feelings and spend log live on the device. The one exception is described in <a href="#ai">the section below</a>.</td></tr>
<tr><td>Location, health, contacts, search, diagnostics</td><td>No</td><td>Cooldown does not link the frameworks that would read them and has no crash or performance reporter of its own.</td></tr>
</table></div>
<p style="margin-top:14px"><strong>Tracking:</strong> none. Cooldown does not link anything about you with data from other companies' apps or websites, and shares nothing with data brokers or advertisers. There are <strong>no affiliate links</strong>: Cooldown earns nothing when you buy something, which is the only arrangement compatible with an app whose job is to help you buy less.</p>
"""),
    card("device", "What stays on your phone", f"""
<p>Cooldown stores the following in its own private storage on your iPhone, protected by your device's passcode and encryption. None of it is uploaded, backed up by us, or visible to us.</p>
<ul>
  <li><strong>Your shop selection</strong> — as opaque Screen Time tokens Cooldown cannot read (see below).</li>
  <li><strong>Your wishlist</strong> — the item names you typed, the prices you estimated, the feeling you tapped, and when each item was captured.</li>
  <li><strong>What you decided</strong> — that a shield was shown, and whether you walked away, cooled the item, let it go or kept it. This is what your savings total and charts are made of.</li>
  <li><strong>Your spend log and any follow-up answers</strong> — how a purchase felt afterwards, if you chose to say.</li>
  <li><strong>Your rules</strong> — danger hours, per-shop rules, cooldown lengths and strict-mode state.</li>
  <li><strong>Your Premium entitlement</strong> — a tier and an expiry date, so the app knows what to unlock.</li>
</ul>
<p>If you use iCloud Backup or an encrypted local backup, Apple may include Cooldown's data in that backup under your own Apple ID and Apple's privacy terms. We have no access to it.</p>
"""),
    card("screentime", "Screen Time and your shops", f"""
<p>Cooldown is built on Apple's Screen Time framework (Family Controls, Managed Settings and Device Activity). You grant it access once, through Apple's own prompt, and can withdraw it at any time in <kbd>Settings</kbd> → <kbd>Screen Time</kbd>.</p>
<p>When you pick shops, Apple's picker returns <strong>tokens</strong>: values that identify the app or website to iOS but mean nothing to Cooldown and nothing outside your phone. Cooldown stores those tokens so it can ask iOS to shield what you chose. It never receives a bundle identifier, an app name or a domain, and it could not report one if it wanted to. Where its own components need to compare tokens, they compare one-way hashes of them, never the tokens themselves — and those hashes never leave the phone either.</p>
<p>Cooldown does not observe your browsing, your messages or what you do inside any app. iOS itself draws the shield and enforces it. Cooldown learns only that its own shield was shown and what you chose on it.</p>
"""),
    card("ai", "The one thing that can leave the phone", f"""
<p>The <strong>AI reflection</strong> is an optional Premium feature that asks one short question before the choices, and writes a few sentences about your week on Sundays. It ships <strong>off</strong>, and stays off until you switch it on.</p>
<h3>What is sent, when it is on</h3>
<ul>
  <li>The <strong>name of the item</strong> you just typed, and anything you write in answer to the question.</li>
  <li>A <strong>price band</strong> — a range, never the amount you actually typed — and your currency.</li>
  <li>The <strong>feeling</strong> you tapped, if you tapped one.</li>
  <li>The <strong>hour and minute</strong> on your clock. No date, no time zone.</li>
  <li><strong>How many shops you have opened today.</strong></li>
  <li>Your own <strong>regret rate for that one feeling</strong>, once you have rated enough purchases for it to mean anything.</li>
</ul>
<p>The Sunday write-up carries none of the above and <strong>no item names at all</strong> — only counts and totals.</p>
<h3>What is never sent</h3>
<ul>
  <li>Screen Time tokens or their hashes, bundle identifiers or domains.</li>
  <li>Which shops or websites you protect, or how many.</li>
  <li>The exact price you typed.</li>
  <li>Anything else on your wishlist — no names, no prices.</li>
  <li>Your estimated savings total, or anything in your spend log.</li>
  <li>How you rated any individual purchase.</li>
  <li>Your rules, danger hours or strict-mode state.</li>
  <li>Any name, account, email or device identifier. Nothing sent is linked to you.</li>
</ul>
<h3>Where it goes</h3>
<p>To Cooldown's own service, and on to Google's Gemini model on Vertex AI. <strong>Cooldown's service stores none of it</strong> — it keeps no copy of the question, your answer, or anything in the list above, only that a request happened, how long it took and whether it worked. Google does not use it to train its models; Google may keep it for up to 24 hours to speed things up and may log it to check for abuse, under their standard cloud terms. The model is served from Google's global endpoint, so we cannot promise your text is processed in any particular country.</p>
{callout('sparkle', 'Switching AI reflection off stops all of it immediately, deletes the weekly write-up from the phone, and takes the Sunday reminder out of your notifications. Cooldown goes back to making no network calls of its own at all.')}
"""),
    card("purchases", "Purchases", f"""
<p>Premium is sold through Apple's App Store using StoreKit. The transaction is between you and Apple, under <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>. Apple tells Cooldown whether a purchase is active — nothing else — and Cooldown tells Apple nothing about how you use the app. No wishlist, no savings total, no shop selection and no identifier of ours travels with a purchase. We never see a card.</p>
"""),
    card("notifications", "Notifications, widgets and the Lock Screen", f"""
<p><strong>Notifications</strong> are optional and are generated on your phone. Cooldown uses them to hand you from the shield into the capture screen, and to tell you when an item's cooldown is over. None is sent from a server.</p>
<p><strong>Widgets and the Live Activity</strong> read a small snapshot of counts and dates — this month's estimated savings, how many items are on ice, how long one has left. They deliberately have no Screen Time access and never see which shops you shielded. Anything that can appear on a Lock Screen is written to be readable by whoever is holding the phone.</p>
"""),
    card("third", "Third parties", f"""
<p>Cooldown contains no analytics, no advertising, no attribution and no crash reporter. Two other parties are involved, both narrowly:</p>
<ul>
  <li><strong>Apple</strong> — operates the App Store, processes purchases, enforces the Screen Time shield, and verifies through App Attest that a request comes from a genuine copy of the app. If you have opted in to sharing with developers, Apple may share crash logs with us under its own policy.</li>
  <li><strong>Google Cloud (Vertex AI)</strong> — only if you switch on the AI reflection, and only for what is listed <a href="#ai">above</a>.</li>
</ul>
<p>We do not sell, rent or share personal data with anyone.</p>
"""),
    card("delete", "Deleting your data", f"""
<p>Everything Cooldown holds is on your phone, so removing it does not require asking us. The <a href="{BASE}/delete-data/">Your data</a> page walks through it: items leave your list as you decide about them, switching the AI reflection off deletes the weekly write-up, and deleting the app removes everything at once.</p>
<p>There is nothing on our side to delete — but you are welcome to write to us anyway.</p>
"""),
    card("rights", "Your rights", f"""
<p>Wherever you live — including under the GDPR, the UK GDPR and the CCPA/CPRA — you have rights to access, correct, export, restrict and erase personal data a company holds about you, and to complain to a supervisory authority. Because Cooldown holds no personal data about you on any server, there is nothing for us to produce or delete; the data on your phone is already in your hands. If you believe otherwise, write to {MAIL} and we will respond.</p>
"""),
    card("children", "Children", f"""
<p>Cooldown is a self-directed tool for the person using the phone. It is not a parental-control product and does not manage another person's device. It is not directed at children under 13 (or the age of digital consent where you live), and we do not knowingly collect personal information from anyone — of any age.</p>
"""),
    card("changes", "Changes to this policy", f"""
<p>We may update this policy as the app changes. The date at the top moves when we do, and material changes will be noted in the app's release notes. Continued use of Cooldown after a change means you accept the revised policy.</p>
"""),
    card("contact", "Contact", f"""
<p>{COMPANY}, the publisher of Cooldown, is the controller for anything covered here. Questions about privacy: {MAIL}.</p>
"""),
])

privacy_hero = hero(
    "Privacy Policy",
    "It never sees what you buy.",
    "No bank linking, no purchase history, no price tracking, no affiliate links. Apple hands Cooldown codes, not names — and this page explains why that is not a slogan.",
    "",
    f"Effective {UPDATED} · applies to the Cooldown app for iPhone and to this site",
)

# ---------------------------------------------------------------------------
# Terms of Use (EULA)
# ---------------------------------------------------------------------------

TERMS_TOC = [
    ("acceptance", "1. Acceptance"),
    ("who", "2. Who may use Cooldown"),
    ("what", "3. What Cooldown is — and is not"),
    ("money", "4. Estimates, not financial advice"),
    ("screentime", "5. Screen Time, strict mode and hard blocks"),
    ("data", "6. Your data and your device"),
    ("subscriptions", "7. Premium, subscriptions and billing"),
    ("ai", "8. The AI reflection"),
    ("licence", "9. Licence and intellectual property"),
    ("use", "10. Acceptable use"),
    ("termination", "11. Termination"),
    ("warranty", "12. Warranties and liability"),
    ("apple", "13. Apple"),
    ("changes", "14. Changes to these Terms"),
    ("law", "15. Governing law"),
    ("contact", "16. Contact"),
]

terms_body = "".join([
    f'<p class="stamp">Last updated: {UPDATED}</p>',
    card("acceptance", "1. Acceptance of Terms", f"""
<p>These Terms of Use ("Terms") are an agreement between you and {COMPANY} ("we", "us"), the publisher of the Cooldown app for iPhone ("Cooldown" or "the app"). By installing or using Cooldown you accept these Terms and our <a href="{BASE}/privacy/">Privacy Policy</a>. If you do not agree, do not use the app.</p>
"""),
    card("who", "2. Who may use Cooldown", f"""
<p>You must be at least 13 years old, or the age of digital consent where you live, to use Cooldown. Cooldown is a tool you install for yourself, on your own iPhone. It is not a parental-control product and must not be used to manage or monitor another person's device.</p>
"""),
    card("what", "3. What Cooldown is — and is not", f"""
<p>Cooldown is a self-directed tool that shields shopping apps and websites you choose, lets you note down what caught your eye, holds it for a period you set, and records on your phone what you decided. It is designed to turn an automatic purchase into a decision you actually make.</p>
<p>Cooldown is <strong>not</strong> a medical, psychological or therapeutic service, and nothing in it — including feelings you tap, follow-up questions, insights or the optional reflection — is advice, diagnosis or treatment. If you are struggling with compulsive spending, debt, anxiety or anything else that affects your wellbeing, please speak to a qualified professional or a debt-advice service. In an emergency, call your local emergency number.</p>
<p>Cooldown is also <strong>not a security or parental-control product</strong>. It is designed to be exactly as strong as you ask it to be: the app can be deleted, Screen Time access can be withdrawn in iOS Settings, and the shield exists only while the app is installed and authorised.</p>
"""),
    card("money", "4. Estimates, not financial advice", f"""
<p>Every price in Cooldown is a figure <strong>you</strong> enter. The app does not connect to any bank, payment provider or retailer, does not read your transactions or order history, does not track prices, and does not verify what anything costs.</p>
<p>The savings figure Cooldown shows is therefore an <strong>estimate assembled from your own guesses</strong>, and is labelled as such everywhere it appears. It is not a statement of fact about money you have, a financial record, or anything you should rely on for budgeting, tax, credit or any other decision. {COMPANY} is not a financial adviser, and nothing in the app or on this site is financial, investment or debt advice.</p>
{callout('info', 'Cooldown carries no affiliate links and earns nothing from anything you buy or do not buy. Its only revenue is Premium, paid by you through Apple.', tone='green')}
"""),
    card("screentime", "5. Screen Time, strict mode and hard blocks", f"""
<p>Cooldown relies on Apple's Screen Time framework. Apple enforces the shield; Cooldown asks for it. Whether a shield appears, how quickly, and whether it persists across restarts and iOS updates is ultimately determined by iOS, and we cannot guarantee it in every circumstance. <strong>Cooldown cannot prevent a purchase</strong> — it can only put a screen in front of a shop you chose, which you remain free to pass.</p>
<p><strong>Strict mode</strong> is a commitment you make to yourself. While it runs, for the duration you chose, your setup cannot be undone — <em>including by you, and including by us</em>. We cannot end a strict-mode session early on request. Do not start one you are not prepared to keep, and do not start one on a phone you may need unrestricted access to.</p>
<p>A <strong>hard-block rule</strong> offers no way through during its hours. The same warning applies. Deleting the app ends every shield, as described in section 3.</p>
"""),
    card("data", "6. Your data and your device", f"""
<p>Everything Cooldown records is stored on your iPhone — see the <a href="{BASE}/privacy/">Privacy Policy</a>. You are responsible for your device, its passcode and its backups. If you delete the app or lose the device without a backup, your wishlist, rules, spend log and savings history are gone, and we have no copy to restore. Your Premium purchase is separate: it belongs to your Apple ID and can be restored on any iPhone signed into it.</p>
<p>What you write into Cooldown is yours. We claim no rights over it, and — except for the optional feature in section 8, which you must switch on yourself — we never receive it.</p>
"""),
    card("subscriptions", "7. Premium, subscriptions and billing", f"""
<p>Cooldown is free to download and use. <strong>Cooldown Premium</strong> unlocks additional features and is sold in three forms, at the price shown in the app and on the App Store for your country:</p>
<ul>
  <li><strong>Premium Monthly</strong> — an auto-renewing subscription, billed monthly.</li>
  <li><strong>Premium Yearly</strong> — an auto-renewing subscription, billed yearly, beginning with a <strong>free trial</strong> where one is offered.</li>
  <li><strong>Premium Lifetime</strong> — a one-time purchase that does not renew.</li>
</ul>
<p>Payment is charged to your Apple ID at confirmation of purchase. A free trial converts to a paid subscription unless you cancel at least 24 hours before the trial ends. Subscriptions renew automatically at the same price and period unless auto-renew is turned off at least 24 hours before the end of the current period; renewal is charged within the 24 hours before that period ends. You can manage or cancel a subscription in your <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; cancellation takes effect at the end of the current period, and no partial refund is given for the unused part of a period. Refunds are handled by Apple under Apple's policies. Use <kbd>Restore purchases</kbd> in the app to recover Premium on a new device.</p>
<p><strong>If a subscription lapses</strong>, nothing you have already built is removed: your wishlist, your history and your savings total stay, and shops you already shielded stay shielded. Only the ability to add more Premium content closes. The set of Premium features may change over time; we will not remove a feature from an active subscription without notice.</p>
"""),
    card("ai", "8. The AI reflection", f"""
<p>The optional AI reflection is <strong>off until you switch it on</strong>. When it is on, the text listed in the <a href="{BASE}/privacy/#ai">Privacy Policy</a> is sent to our service and on to Google's Gemini model on Vertex AI so that a short response can be generated.</p>
<p>What a language model writes is generated text. It may be wrong, generic or unhelpful, it is <strong>not advice of any kind</strong>, and it is never a statement of fact about your money. Do not enter anything into that screen you would not want processed by a third-party model. If a request fails, the app simply shows you the ordinary choice screen — nothing is queued, retried or stored for later.</p>
"""),
    card("licence", "9. Licence and intellectual property", f"""
<p>We grant you a personal, non-exclusive, non-transferable, revocable licence to install and use Cooldown on an iPhone you own or control, in accordance with these Terms and the App Store's usage rules. Cooldown, its name, design, artwork, text and code are owned by {COMPANY} and protected by copyright and other laws. You may not copy, modify, distribute, sell, lease, reverse-engineer or create derivative works from the app except where the law expressly allows it.</p>
<p>Names of retailers, apps and websites you choose to shield belong to their respective owners. Cooldown is not affiliated with, endorsed by or sponsored by any of them.</p>
"""),
    card("use", "10. Acceptable use", f"""
<p>You agree not to use Cooldown in any way that is unlawful, that interferes with the app or Apple's services, that attempts to bypass the App Store's purchase mechanisms, or that installs it on a device you are not entitled to manage. You agree not to use it to restrict or monitor another person without their informed consent, and not to submit content through the AI reflection that is unlawful or that you have no right to share.</p>
"""),
    card("termination", "11. Termination", f"""
<p>You may stop using Cooldown at any time by deleting it. We may suspend or end your licence if you breach these Terms. Sections 4, 6, 9, 12, 13 and 15 survive termination. Deleting the app does not cancel an active subscription — cancel it in your App Store settings.</p>
"""),
    card("warranty", "12. Warranties and liability", f"""
<p>Cooldown is provided "as is" and "as available", without warranties of any kind, express or implied, including that it will shield any app or website in every circumstance, that it will be uninterrupted or error-free, that any figure it displays is accurate, or that it will change your spending. To the fullest extent permitted by law, {COMPANY} shall not be liable for any indirect, incidental, special, consequential or punitive damages, or for any loss of data or money, arising from your use of or inability to use the app — including any purchase you did or did not make, any consequence of a shield that did or did not appear, and any strict-mode session you chose to start. Where liability cannot be excluded, it is limited to the amount you paid us for Premium in the twelve months before the claim. Nothing in these Terms limits rights you have as a consumer that cannot be waived.</p>
"""),
    card("apple", "13. Apple", f"""
<p>Cooldown is distributed through the Apple App Store. These Terms are between you and {COMPANY}, not Apple. Apple has no obligation to provide maintenance or support for the app, and is not responsible for addressing any claim relating to it, including product-liability, legal-compliance or intellectual-property claims. Apple and its subsidiaries are third-party beneficiaries of these Terms and may enforce them against you. Where these Terms are silent, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a> applies. You represent that you are not in a country subject to a U.S. government embargo or listed as a prohibited party, and you must comply with any applicable third-party terms when using the app.</p>
"""),
    card("changes", "14. Changes to these Terms", f"""
<p>We may update these Terms from time to time. The date at the top will change when we do, and material changes will be noted in the app's release notes. Continued use after an update means you accept the revised Terms.</p>
"""),
    card("law", "15. Governing law", f"""
<p>These Terms are governed by the laws of Pakistan, where {COMPANY} operates, without regard to conflict-of-law provisions. Where the law of your country of residence gives you protections that cannot be contracted out of, those protections apply.</p>
"""),
    card("contact", "16. Contact", f"""
<p>Questions about these Terms: {MAIL}.</p>
"""),
])

terms_hero = hero(
    "Terms of Use",
    "The agreement, in plain words.",
    "What Cooldown does, what it does not promise, why every figure is an estimate, how Premium is billed, and what strict mode asks of you.",
    "",
    f"Effective {UPDATED} · Cooldown by {COMPANY}",
)

# ---------------------------------------------------------------------------
# Your data / delete
# ---------------------------------------------------------------------------

DATA_TOC = [
    ("where", "What is stored where"),
    ("inapp", "Remove it in the app"),
    ("ai", "The weekly write-up"),
    ("uninstall", "Delete the app"),
    ("subscription", "Your subscription"),
    ("email", "Ask us"),
]

data_body = "".join([
    card("where", "What is stored where", f"""
<p class="lead">Cooldown has no account and keeps nothing about you on a server, so there is nothing to request from us. Everything it holds is on your iPhone.</p>
<div class="table-wrap"><table>
<tr><th>Data</th><th>Where it lives</th><th>How to remove it</th></tr>
<tr><td>Wishlist, prices, feelings, spend log, savings history, rules</td><td>The app's private storage on your phone</td><td>Delete the app, or restore the phone</td></tr>
<tr><td>Your shop selection</td><td>Opaque Screen Time tokens in the app's private storage</td><td>Change it in the app; withdrawing Screen Time access in iOS Settings also ends every shield</td></tr>
<tr><td>Widget and Live Activity snapshot</td><td>A small file of counts and dates on your phone</td><td>Removed with the app</td></tr>
<tr><td>The weekly write-up</td><td>On your phone, only if the AI reflection is on</td><td>Switching AI reflection off deletes it</td></tr>
<tr><td>Premium entitlement</td><td>Your Apple ID (Apple), and a copy of its status on your phone</td><td>Managed in your App Store settings — see below</td></tr>
<tr><td>Anything on our servers</td><td>—</td><td>There is none. Our service keeps no copy of anything the app sends it.</td></tr>
</table></div>
"""),
    card("inapp", "Remove it in the app", f"""
<p>Cooldown is built so that your own data thins out as you use it, rather than piling up:</p>
<ul>
  <li>An item leaves your list the moment you decide about it — let it go, or keep it.</li>
  <li>Changing your shops replaces the stored tokens; there is no history of shops you used to protect.</li>
  <li>Turning <strong>Protection</strong> off takes every shield down immediately.</li>
</ul>
{callout('lock', 'While <strong>strict mode</strong> is running, your setup is held in place — that is the one commitment you asked the app to keep for you. It ends on its own at the time you chose.', tone='amber')}
"""),
    card("ai", "The weekly write-up", f"""
<p>If you switched on the AI reflection, Cooldown keeps the latest Sunday write-up on your phone so you can read it again. Switching AI reflection off in Settings deletes it, removes the Sunday reminder from your notifications, and returns the app to making no network calls of its own.</p>
<p>Our service never held a copy to begin with — it keeps only that a request happened, how long it took and whether it worked. There is nothing there to delete.</p>
"""),
    card("uninstall", "Delete the app", f"""
<p>Deleting Cooldown from your iPhone removes all of its data with it, including the Screen Time tokens, and ends every shield immediately. If the app is included in an iCloud or encrypted local backup, that copy belongs to your Apple ID and is governed by Apple's terms; we have no access to it.</p>
"""),
    card("subscription", "Your subscription", f"""
<p>Deleting the app does not cancel a subscription — it belongs to your Apple ID, not to the app. Cancel it in <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; it stays active until the end of the current period. Refunds are handled by <a href="https://support.apple.com/billing">Apple Support</a>. A lifetime purchase does not renew and needs nothing cancelled.</p>
"""),
    card("email", "Ask us", f"""
<p>If you would like written confirmation that we hold nothing about you, or you believe we do, write to {MAIL} from any address. We will reply within 30 days. Please do not send us your wishlist, your prices or screenshots of them — we do not need them to answer.</p>
"""),
])

data_hero = hero(
    "Your data",
    "Delete your data",
    "Everything Cooldown knows is on your phone. Here is how to remove it, what happens to your subscription, and what — nothing — is left on our side.",
    "",
    f'See also the <a href="{BASE}/privacy/">Privacy Policy</a>',
)

# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------

nf_body = f"""<section class="card"><p class="lead">That page isn't here. Try <a href="{BASE}/">Support</a>, the <a href="{BASE}/privacy/">Privacy Policy</a> or the <a href="{BASE}/terms/">Terms of Use</a>.</p></section>"""
nf_hero = hero("404", "Nothing on ice here.", "Which, for once, is not the point.", f'<a class="btn primary" href="{BASE}/">Back to Support</a>')

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><radialGradient id="g" cx="38%" cy="32%" r="72%"><stop offset="0" stop-color="#D3DCFF"/><stop offset="1" stop-color="#8FA0EA"/></radialGradient></defs><rect width="64" height="64" rx="16" fill="#12152A"/><path d="M34 10a24 24 0 1 0 21.8 33.8A19.6 19.6 0 0 1 34 10Z" fill="url(#g)"/><circle cx="50" cy="17" r="2.4" fill="#D3DCFF" opacity=".85"/><circle cx="15" cy="46" r="1.8" fill="#D3DCFF" opacity=".6"/></svg>"""

PAGES = [
    ("index.html", page("support", f"{APP} — Support", "Official support for Cooldown, the iPhone app that puts one night between you and the buy button. How it works, requirements, FAQ and contact.", support_hero, support_body, SUPPORT_TOC, "/")),
    ("about/index.html", page("about", f"{APP} — One night between you and the buy button", "Cooldown shields the shopping apps and websites you choose and asks you to sleep on it first. No bank access, no price tracking, no affiliate links.", about_hero, about_body, None, "/about/")),
    ("privacy/index.html", page("privacy", f"Privacy Policy — {APP}", "Cooldown has no bank connection, no purchase history and no analytics. This policy explains what stays on your phone, and the one optional feature that sends anything.", privacy_hero, privacy_body, PRIVACY_TOC, "/privacy/")),
    ("terms/index.html", page("terms", f"Terms of Use — {APP}", "Terms of Use (EULA) for Cooldown: what the app is and is not, why every figure is an estimate, how Premium is billed, and what strict mode asks of you.", terms_hero, terms_body, TERMS_TOC, "/terms/")),
    ("delete-data/index.html", page("data", f"Delete your data — {APP}", "How to remove everything Cooldown holds — all of it on your phone — and what happens to your subscription.", data_hero, data_body, DATA_TOC, "/delete-data/")),
    ("404.html", page("404", f"Not found — {APP}", "Page not found.", nf_hero, nf_body, None, "/404.html")),
]

for rel, content in PAGES:
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)

with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(FAVICON)
print("wrote favicon.svg")

open(os.path.join(OUT, ".nojekyll"), "w").close()
print("wrote .nojekyll")
