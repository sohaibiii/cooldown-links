# -*- coding: utf-8 -*-
"""Renders the On Ice App Store pages, in every language On Ice ships in.

    python3 _src/gen.py

One renderer, no dependencies. This file owns the markup; `_src/words/<lang>.py`
owns the words. English lives at the root of the site and every other language
under its own code — `/de/privacy/` is the German privacy policy — so a link
somebody was given keeps working and keeps its language.

The repository and its URL keep the codebase's name, Cooldown, because the
shipped app links here. Everything a reader sees says On Ice, the app's public
name; the lowercase word "cooldown" stays the name of the wait itself.

Every visual value below is taken from the app's own design tokens
(Cooldown/Core/DesignSystem/DesignTokens.swift in the app repo) so the pages read
as the same product: the same night-sky hero, the same dusk indigo, savings green
reserved for realised saves, cooling amber for items still on ice, and the same
radii. The mark is the app's own "frozen want" (BrandMark.svg), copied verbatim.

Run `python3 _src/check.py` after touching a words file: it holds the eight
catalogues to the same key set and the same links, which is the half of a
translation that no reader of that language will ever check for us.
"""
import importlib
import os
import sys
import html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)
sys.path.insert(0, HERE)

BASE = "/cooldown-links"
SITE = "https://sohaibiii.github.io" + BASE
APP = "On Ice"
COMPANY = "TOPSOL"
EMAIL = "topsol.org@gmail.com"
YEAR = "2026"

# Set this to the App Store page once App Store Connect has assigned the Apple ID,
# e.g. "https://apps.apple.com/app/id1234567890". Until then every "App Store"
# button renders as a quiet "coming soon" label rather than a dead link.
APP_STORE_URL = None

# The eight languages On Ice ships in, in the order the app's own picker shows
# them (Core/Localization/AppLanguage.swift). The directory is spelled exactly as
# `AppLanguage` spells its raw value, so the app can build a link to any of them.
LANGUAGES = [
    ("en", ""),
    ("de", "/de"),
    ("es", "/es"),
    ("fr", "/fr"),
    ("ja", "/ja"),
    ("ko", "/ko"),
    ("pt-BR", "/pt-BR"),
    ("zh-Hans", "/zh-Hans"),
]

# Each language's own name for itself. **Never translated** — somebody looking for
# 日本語 on a page that is speaking German is looking for exactly those characters.
NATIVE_NAME = {
    "en": "English",
    "de": "Deutsch",
    "es": "Español",
    "fr": "Français",
    "ja": "日本語",
    "ko": "한국어",
    "pt-BR": "Português (Brasil)",
    "zh-Hans": "简体中文",
}

# The catalogue codes are already valid BCP 47 tags — "pt-BR" carries its region
# and "zh-Hans" its script — so <html lang> and hreflang use them as they stand.
HTML_LANG = {code: code for code, _ in LANGUAGES}

PAGE_PATH = {
    "support": "/",
    "about": "/about/",
    "privacy": "/privacy/",
    "terms": "/terms/",
    "data": "/delete-data/",
}
PAGE_FILE = {
    "support": "index.html",
    "about": "about/index.html",
    "privacy": "privacy/index.html",
    "terms": "terms/index.html",
    "data": "delete-data/index.html",
}
NAV_ORDER = ["support", "about", "privacy", "terms", "data"]

# The cards each long page is made of, in order. The identifier is the anchor,
# the table of contents, and the two copy keys (`<prefix>.<id>.h` and `.b`).
# Anchors other pages or the app link to — #faq, #ai, #subscriptions, #pricing —
# must keep their names.
SUPPORT_CARDS = ["how", "requirements", "start", "money", "faq", "trouble", "contact"]
PRIVACY_CARDS = [
    "summary", "collect", "device", "journal", "permissions", "screentime", "ai",
    "purchases", "notifications", "third", "delete", "rights", "children", "changes",
    "contact",
]
TERMS_CARDS = [
    "acceptance", "who", "what", "money", "screentime", "data", "subscriptions", "ai",
    "licence", "use", "termination", "warranty", "apple", "changes", "law", "contact",
]
DATA_CARDS = ["where", "inapp", "journal", "ai", "uninstall", "subscription", "email"]

# The About page's feature cards: (id, icon, tone). Icon and tone are markup, so
# they live here; the words for each are `a.<id>.h` and `a.<id>.p`.
ABOUT_FEATURES = [
    ("f1", "moon", ""),
    ("f2", "note", ""),
    ("f3", "snow", "amber"),
    ("f4", "chart", "green"),
    ("f5", "wind", ""),
    ("f6", "clock", "amber"),
    ("f7", "book", ""),
    ("f8", "eye-off", ""),
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
  --max:760px;--wide:1080px;--anchor:112px;
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
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,Helvetica,Arial,"Hiragino Sans","Apple SD Gothic Neo","PingFang SC","Noto Sans CJK JP","Noto Sans CJK KR","Noto Sans CJK SC",sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
:lang(ja),:lang(ko),:lang(zh-Hans){line-break:strict;word-break:normal;overflow-wrap:anywhere}
:lang(ja) :is(h1,h2,h3,.sub,.lead){word-break:auto-phrase}
a{color:var(--accent);text-decoration:underline;text-decoration-color:color-mix(in srgb,var(--accent) 40%,transparent);text-underline-offset:3px;overflow-wrap:anywhere}
a:hover{text-decoration-color:var(--accent)}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px}
.skip{position:absolute;top:8px;left:8px;background:var(--surface);color:var(--ink);padding:8px 12px;z-index:20;border-radius:var(--r-chip);box-shadow:var(--card-shadow)}
.skip:not(:focus){clip:rect(0 0 0 0);clip-path:inset(50%);width:1px;height:1px;overflow:hidden;white-space:nowrap;padding:0;margin:-1px}
h1,h2,h3{margin:0;letter-spacing:-.022em;text-wrap:balance;font-family:var(--display);font-weight:800}
:lang(ja) :is(h1,h2,h3),:lang(ko) :is(h1,h2,h3),:lang(zh-Hans) :is(h1,h2,h3){letter-spacing:0;font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Apple SD Gothic Neo","PingFang SC",sans-serif;font-weight:700}
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
.brand{display:inline-flex;align-items:center;gap:10px;color:var(--ink);text-decoration:none;font-family:var(--display);font-weight:800;font-size:20px;letter-spacing:-.02em;white-space:nowrap}
.mark{width:30px;height:30px;border-radius:9px;flex:none;display:grid;place-items:center;background:linear-gradient(160deg,#1D2347,#12152A);box-shadow:0 0 0 1px var(--hero-stroke),0 0 14px var(--moon-glow)}
.mark img{width:22px;height:22px;display:block}
nav.pages{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
nav.pages a{text-decoration:none;color:var(--ink-2);font-size:15px;font-weight:500;padding:7px 12px;border-radius:999px;white-space:nowrap}
nav.pages a[aria-current="page"]{color:var(--accent);background:var(--accent-soft)}
nav.pages a:hover{color:var(--ink)}
@media (max-width:640px){nav.pages{margin-left:0;width:100%;overflow-x:auto;flex-wrap:nowrap;scrollbar-width:none;padding-bottom:2px}nav.pages::-webkit-scrollbar{display:none}nav.pages a{flex:none}}

/* language tabs — the same page, in the reader's own language */
.langrow{border-top:1px solid var(--line)}
.langrow .in{max-width:var(--wide);margin:0 auto;padding:7px 20px;display:flex;align-items:center;gap:12px}
.langrow .lbl{flex:none;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);font-family:var(--display)}
nav.langs{display:flex;gap:2px;min-width:0;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}
nav.langs::-webkit-scrollbar{display:none}
nav.langs a{flex:none;text-decoration:none;color:var(--ink-2);font-size:14.5px;font-weight:500;padding:6px 11px;border-radius:999px;white-space:nowrap}
nav.langs a:hover{color:var(--ink);background:var(--fill)}
nav.langs a[aria-current="page"]{color:var(--accent);background:var(--accent-soft)}
@media (max-width:640px){.langrow .lbl{display:none}.langrow .in{padding:6px 20px}:root{--anchor:150px}}

/* hero — the app's protection island, dark in both appearances */
.hero-wrap{max-width:var(--wide);margin:24px auto 0;padding:0 20px}
.hero{position:relative;overflow:hidden;border-radius:var(--r-hero);background:linear-gradient(135deg,var(--hero-top),var(--hero-bottom));color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke),0 24px 60px rgba(15,18,20,.20);padding:clamp(36px,6vw,64px) clamp(24px,5vw,56px)}
.hero::before{content:"";position:absolute;inset:-40% -18% auto auto;width:62%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,var(--hero-glow) 0,transparent 62%);pointer-events:none}
.hero>*{position:relative}
.hero .eyebrow{display:inline-flex;align-items:center;gap:9px;font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--hero-ink-2);margin-bottom:18px;font-family:var(--display)}
.hero .eyebrow .dot{width:9px;height:9px;border-radius:50%;background:var(--moon-edge);box-shadow:0 0 10px var(--moon-glow)}
.hero h1{max-width:18ch}
:lang(ja) .hero h1,:lang(ko) .hero h1,:lang(zh-Hans) .hero h1{max-width:22ch}
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
.toc{position:sticky;top:var(--anchor);padding:20px 22px;border-radius:var(--r-card);background:var(--surface);box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge)}
@media (max-width:899px){.toc{position:static}}
.toc .lbl{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);margin-bottom:10px;font-family:var(--display)}
.toc ol{list-style:none;padding:0;margin:0}
.toc li{margin:0}
.toc a{display:block;padding:6px 0;font-size:15px;color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--line)}
.toc li:last-child a{border-bottom:0}
.toc a:hover{color:var(--accent)}
.stack{display:grid;gap:20px;max-width:var(--max)}
.grid.with-toc .stack{max-width:none}
.card{background:var(--surface);border-radius:var(--r-card);padding:clamp(22px,3.4vw,32px);box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge);scroll-margin-top:calc(var(--anchor) + 8px)}
.card h2{margin-bottom:12px}
.card h3{margin:20px 0 6px}
.card h3:first-of-type{margin-top:0}
.card p+h3,.card ul+h3,.card .table-wrap+h3{margin-top:18px}
.card ul+p,.card .table-wrap+p,.card .callout+p,.card p+.callout,.card ul+.callout{margin-top:16px}
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
.tiers{display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin-top:16px}
.tier{background:var(--surface);border-radius:var(--r-card);padding:24px;box-shadow:var(--card-shadow),inset 0 0 0 1px var(--card-edge);display:flex;flex-direction:column;gap:10px}
.card .tier{background:var(--fill);box-shadow:none}
.tier .lbl{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);font-family:var(--display)}
.tier .price{font-family:var(--display);font-size:26px;font-weight:800;letter-spacing:-.02em;line-height:1.2}
.tier ul{margin-top:4px;color:var(--ink-2);font-size:15.5px}
.card .tier.premium,.tier.premium{background:linear-gradient(135deg,var(--hero-top),var(--hero-bottom));color:var(--hero-ink);box-shadow:inset 0 0 0 1px var(--hero-stroke)}
.tier.premium .lbl,.tier.premium ul{color:var(--hero-ink-2)}
.tier.premium li::marker{color:#8FA0EA}
.tiers+p{margin-top:14px}
dl.faq{margin:0}
dl.faq dt{font-weight:600;margin-top:18px}
dl.faq dt:first-child{margin-top:0}
dl.faq dd{margin:6px 0 0;color:var(--ink-2)}
table{width:100%;border-collapse:collapse;font-size:15.5px}
th,td{text-align:left;vertical-align:top;padding:10px 12px 10px 0;border-bottom:1px solid var(--line)}
th{font-weight:700;color:var(--ink-2);font-size:13px;letter-spacing:.08em;text-transform:uppercase;font-family:var(--display)}
tr:last-child td,tr:last-child th{border-bottom:0}
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

# The app's "frozen want" — Cooldown/Resources/BrandAssets.xcassets/BrandMark.imageset/
# BrandMark.svg, verbatim. Regenerated there by Scripts/export-brand-assets.py; copy
# it again here if it changes, never redraw it.
MARK = """<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="182 208 660 660">
<defs>
  <linearGradient id="top" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7F8FE"/><stop offset="1" stop-color="#DBE0F8"/></linearGradient>
  <linearGradient id="left" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#CDD4F4"/><stop offset="1" stop-color="#ACB7EB"/></linearGradient>
  <linearGradient id="right" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#A7B2EA"/><stop offset="1" stop-color="#7B8CDE"/></linearGradient>
  <linearGradient id="frost" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.34"/><stop offset="0.6" stop-color="#FFFFFF" stop-opacity="0.06"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.2"/></linearGradient>
</defs>
<polygon points="512,250 786,388 786,688 512,826 238,688 238,388" fill="#C7CFF2" stroke="#C7CFF2" stroke-width="64" stroke-linejoin="round"/>
<polygon points="238,388 512,526 512,826 238,688" fill="url(#left)"/>
<polygon points="512,526 786,388 786,688 512,826" fill="url(#right)"/>
<g transform="rotate(-7 512 676)">
  <path d="M441.3 590.0L582.7 590.0Q601.4 590.0 603.7 608.7L616.0 767.3Q618.0 786.0 597.3 786.0L426.7 786.0Q406.0 786.0 408.0 767.3L420.3 608.7Q422.6 590.0 441.3 590.0Z" fill="#E8C170" fill-opacity="0.95" stroke="#FFFFFF" stroke-opacity="0.95" stroke-width="16" stroke-linejoin="round"/>
  <path d="M472.5 615.5V578.2C472.5 531.2 551.5 531.2 551.5 578.2V615.5" stroke="#E8C170" stroke-opacity="0.95" stroke-width="21" stroke-linecap="round" fill="none"/>
</g>
<polygon points="238,388 512,526 512,826 238,688" fill="url(#frost)"/>
<polygon points="512,526 786,388 786,688 512,826" fill="url(#frost)"/>
<polygon points="512,250 786,388 512,526 238,388" fill="url(#top)"/>
<path d="M268 386L506 278" stroke="#FFFFFF" stroke-opacity="0.95" stroke-width="16" stroke-linecap="round"/>
<path d="M512 550V796" stroke="#FFFFFF" stroke-opacity="0.28" stroke-width="6" stroke-linecap="round"/>
<circle cx="300" cy="610" r="10" fill="#FFFFFF" fill-opacity="0.6"/>
<circle cx="322" cy="572" r="6" fill="#FFFFFF" fill-opacity="0.5"/>
<circle cx="716" cy="500" r="7" fill="#FFFFFF" fill-opacity="0.45"/>
</svg>
"""

# The mark on the home hero's night, the way the app icon sets it.
FAVICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#1D2347"/><stop offset="1" stop-color="#12152A"/></linearGradient></defs>'
    '<rect width="64" height="64" rx="15" fill="url(#bg)"/>'
    + MARK.replace('width="64" height="64"', 'x="6" y="6" width="52" height="52"', 1)
         .replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg ', 1).strip()
    + "</svg>\n"
)

ICONS = {
    "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/></svg>',
    "snow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 2v20M3.5 7l17 10M20.5 7l-17 10"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/></svg>',
    "note": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h11l4 4v12H5z"/><path d="M9 11h7M9 15h5"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2V5z"/><path d="M4 19a2 2 0 0 0 2 2h14"/></svg>',
    "wind": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 8h11a3 3 0 1 0-3-3M3 12h15a3 3 0 1 1-3 3M3 16h8a2.5 2.5 0 1 1-2.5 2.5"/></svg>',
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
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg>',
    "walk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="13" cy="4" r="1.8"/><path d="M10 21l2-6 3 3v3M8 12l2-4 4 1 2 3 3 1M12 15l-1.5-6"/></svg>',
    "family": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="8" cy="7" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M2.5 20a5.5 5.5 0 0 1 11 0M13.5 20a4 4 0 0 1 8 0"/></svg>',
}


def copy_for(code):
    """The catalogue for one language, with English behind it.

    A key that has not been translated yet renders as English — the same rule
    the app follows, and for the same reason: a missing translation must read
    as a sentence, never as an identifier.
    """
    english = importlib.import_module("words.en").COPY
    if code == "en":
        return dict(english)
    module = importlib.import_module("words." + code.replace("-", "_"))
    merged = dict(english)
    merged.update(module.COPY)
    return merged


def context(code, prefix, C):
    """Everything a copy string may interpolate with `{name}`.

    Every `k.<name>` in a catalogue is one of the app's own labels, written the
    way that language's screen writes it, and `{K_<name>}` puts it in a <kbd> —
    so a page never tells somebody to tap a button whose label reads differently
    on their screen.
    """
    ctx = dict(ICONS)
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    ctx.update(
        BASE=BASE, L=prefix, APP=APP, COMPANY=COMPANY, EMAIL=EMAIL, MAIL=mail, YEAR=YEAR,
        DATE=C["ui.date"],
    )
    for key, label in C.items():
        if key.startswith("k."):
            ctx["K_" + key[2:]] = f"<kbd>{label}</kbd>"
    return ctx


def store_button(fmt):
    if APP_STORE_URL:
        return f'<a class="btn primary" href="{E(APP_STORE_URL)}">{ICONS["apple"]} {fmt("ui.store_get")}</a>'
    return f'<span class="soon">{ICONS["apple"]} {fmt("ui.store_soon")}</span>'


def hero(eyebrow, h1, sub, ctas="", meta=""):
    return (
        f'<div class="eyebrow"><span class="dot" aria-hidden="true"></span>{eyebrow}</div>'
        f'<h1>{h1}</h1><p class="sub">{sub}</p>'
        + (f'<div class="ctas">{ctas}</div>' if ctas else "")
        + (f'<p class="meta">{meta}</p>' if meta else "")
    )


def page(code, prefix, key, title, description, hero_html, body, toc=None, canonical=""):
    """One rendered page, in one language."""
    C = copy_for(code)
    fmt = lambda k: C[k].format(**context(code, prefix, C))

    nav = "".join(
        f'<a href="{E(BASE + prefix + PAGE_PATH[n])}"{CUR if n == key else ""}>{fmt("nav." + n)}</a>'
        for n in NAV_ORDER
    )
    footnav = " · ".join(
        f'<a href="{E(BASE + prefix + PAGE_PATH[n])}">{fmt("nav." + n)}</a>' for n in NAV_ORDER
    )
    # The same page in the seven other languages. 404 has no counterpart per
    # language — GitHub Pages serves one for the whole site — so its tabs point
    # at each language's front door instead.
    here = PAGE_PATH.get(key, "/")
    langs = "".join(
        f'<a href="{E(BASE + p + here)}" lang="{c}" hreflang="{c}"'
        f'{CUR if c == code else ""}>{E(NATIVE_NAME[c])}</a>'
        for c, p in LANGUAGES
    )
    alternates = "".join(
        f'<link rel="alternate" hreflang="{c}" href="{E(SITE + p + here)}">' for c, p in LANGUAGES
    ) + f'<link rel="alternate" hreflang="x-default" href="{E(SITE + here)}">'

    toc_html = ""
    grid_cls = "grid"
    if toc:
        grid_cls = "grid with-toc"
        toc_html = (
            f'<aside class="toc" aria-label="{E(fmt("ui.toc"))}"><div class="lbl">{fmt("ui.toc")}</div><ol>'
            + "".join(f'<li><a href="#{E(i)}">{t}</a></li>' for i, t in toc)
            + "</ol></aside>"
        )

    return f"""<!DOCTYPE html>
<html lang="{HTML_LANG[code]}">
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
<meta property="og:locale" content="{HTML_LANG[code].replace('-', '_')}">
<meta property="og:url" content="{E(SITE + prefix + canonical)}">
<link rel="canonical" href="{E(SITE + prefix + canonical)}">
{alternates}
<link rel="icon" href="{BASE}/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png">
<title>{E(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#content">{fmt("ui.skip")}</a>
<header class="topbar">
  <div class="in">
    <a class="brand" href="{BASE + prefix}/"><span class="mark" aria-hidden="true"><img src="{BASE}/mark.svg" alt="" width="22" height="22"></span>{APP}</a>
    <nav class="pages" aria-label="{E(fmt("ui.pages"))}">{nav}</nav>
  </div>
  <div class="langrow"><div class="in">
    <span class="lbl">{fmt("ui.lang")}</span>
    <nav class="langs" aria-label="{E(fmt("ui.lang"))}">{langs}</nav>
  </div></div>
</header>
<div class="hero-wrap"><section class="hero">{hero_html}</section></div>
<main id="content"><div class="{grid_cls}">{toc_html}<div class="stack">{body}</div></div></main>
<footer><div class="in">
  <div>© {YEAR} {APP} · {COMPANY} · {fmt("ui.rights")}</div>
  <nav aria-label="{E(fmt("ui.footer"))}">{footnav} · <a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body>
</html>
"""


def cards(fmt, prefix, ids):
    return "".join(
        f'<section class="card" id="{i}"><h2>{fmt(f"{prefix}.{i}.h")}</h2>{fmt(f"{prefix}.{i}.b")}</section>'
        for i in ids
    )


def toc_of(fmt, prefix, ids):
    return [(i, fmt(f"{prefix}.{i}.h")) for i in ids]


# ---------------------------------------------------------------------------
# The five pages, assembled from whichever language's words
# ---------------------------------------------------------------------------

def render(code, prefix):
    C = copy_for(code)
    ctx = context(code, prefix, C)
    fmt = lambda k: C[k].format(**ctx)
    out = []

    def mk(key, title, desc, hero_html, body, toc=None):
        out.append((PAGE_FILE[key], page(code, prefix, key, title, desc, hero_html, body,
                                         toc, PAGE_PATH[key])))

    # Support — the App Store "Support URL"
    mk("support", fmt("meta.support.title"), fmt("meta.support.desc"),
       hero(fmt("s.eyebrow"), fmt("s.h1"), fmt("s.sub"),
            store_button(fmt) + f'<a class="btn quiet" href="#faq">{fmt("s.cta")}</a>',
            fmt("s.meta")),
       cards(fmt, "s", SUPPORT_CARDS), toc_of(fmt, "s", SUPPORT_CARDS))

    # About — the App Store "Marketing URL"
    features = "".join(
        f'<section class="card"><span class="tile{" " + tone if tone else ""}">{ICONS[icon]}</span>'
        f'<h3>{fmt(f"a.{f}.h")}</h3><p>{fmt(f"a.{f}.p")}</p></section>'
        for f, icon, tone in ABOUT_FEATURES
    )
    about_body = (
        f'<section class="card"><p class="lead">{fmt("a.lead")}</p></section>'
        f'<div class="features">{features}</div>'
        f'<section class="card" id="pricing"><h2>{fmt("a.price.h")}</h2>{fmt("a.price.b")}</section>'
        f'<section class="card" id="platform"><h2>{fmt("a.st.h")}</h2>{fmt("a.st.b")}</section>'
        f'<section class="card" id="estimates"><h2>{fmt("a.est.h")}</h2>{fmt("a.est.b")}</section>'
    )
    mk("about", fmt("meta.about.title"), fmt("meta.about.desc"),
       hero(fmt("a.eyebrow"), fmt("a.h1"), fmt("a.sub"),
            store_button(fmt)
            + f'<a class="btn quiet" href="{BASE + prefix}/">{fmt("a.cta")}</a>',
            fmt("a.meta")),
       about_body)

    # Privacy Policy
    mk("privacy", fmt("meta.privacy.title"), fmt("meta.privacy.desc"),
       hero(fmt("p.eyebrow"), fmt("p.h1"), fmt("p.sub"), "", fmt("p.meta")),
       f'<p class="stamp">{fmt("ui.last_updated")}</p>' + cards(fmt, "p", PRIVACY_CARDS),
       toc_of(fmt, "p", PRIVACY_CARDS))

    # Terms of Use (EULA)
    mk("terms", fmt("meta.terms.title"), fmt("meta.terms.desc"),
       hero(fmt("t.eyebrow"), fmt("t.h1"), fmt("t.sub"), "", fmt("t.meta")),
       f'<p class="stamp">{fmt("ui.last_updated")}</p>' + cards(fmt, "t", TERMS_CARDS),
       toc_of(fmt, "t", TERMS_CARDS))

    # Your data
    mk("data", fmt("meta.data.title"), fmt("meta.data.desc"),
       hero(fmt("d.eyebrow"), fmt("d.h1"), fmt("d.sub"), "", fmt("d.meta")),
       cards(fmt, "d", DATA_CARDS), toc_of(fmt, "d", DATA_CARDS))

    return out


def render_404():
    """One 404 for the whole site — GitHub Pages serves the repo root's.

    English, because it is the one page that cannot know who is asking, and its
    language tabs go to each front door rather than to a page that isn't there.
    """
    C = copy_for("en")
    fmt = lambda k: C[k].format(**context("en", "", C))
    body = f'<section class="card"><p class="lead">{fmt("nf.b")}</p></section>'
    hero_html = hero(fmt("nf.eyebrow"), fmt("nf.h1"), fmt("nf.sub"),
                     f'<a class="btn primary" href="{BASE}/">{fmt("nf.cta")}</a>')
    return page("en", "", "404", fmt("meta.nf.title"), fmt("meta.nf.desc"),
                hero_html, body, None, "/404.html")


def sitemap():
    """Every URL, each one naming its counterparts.

    Without the alternates a search engine treats eight translations of the
    privacy policy as eight competing pages rather than one page in eight
    languages, and picks a winner on its own.
    """
    urls = []
    for key in NAV_ORDER:
        here = PAGE_PATH[key]
        alts = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{c}" href="{SITE + p + here}"/>'
            for c, p in LANGUAGES
        ) + f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE + here}"/>'
        for _, p in LANGUAGES:
            urls.append(f"  <url>\n    <loc>{SITE + p + here}</loc>{alts}\n  </url>")
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
        ' xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )


def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


if __name__ == "__main__":
    for code, prefix in LANGUAGES:
        for rel, content in render(code, prefix):
            write(os.path.join(prefix.lstrip("/"), rel) if prefix else rel, content)
    write("404.html", render_404())
    write("mark.svg", MARK)
    write("favicon.svg", FAVICON)
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    write(".nojekyll", "")
