# -*- coding: utf-8 -*-
"""The English home page, How it works, Pricing and the guides.

`gen.py` owns the support and legal pages in eight languages and calls `build()`
here at the end of its run. These pages are English only for now; their words
live in this file and in `guides.py`, their styles in `assets/site.css`.

Rules these pages keep, same as the app (CLAUDE.md in the app repo):
  * every money figure is the reader's own estimate and says "estimated";
  * nothing shames a purchase;
  * only features the app has, named the way its screens name them;
  * no long dashes in copy, and the name "Cooldown" never reaches a reader.
"""
import hashlib
import json
import os
import shutil

import art
import demo
import analytics
import gen
from gen import APP, APP_STORE_ID, APP_STORE_URL, BASE, COMPANY, E, EMAIL, SITE, YEAR

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = BASE + "/assets"

# App Store Connect campaign links. Paste the provider token from
# App Store Connect > Analytics > Sources > Campaigns ("pt=" in a generated link)
# and every button on these pages reports which page sent the download.
PROVIDER_TOKEN = None

UPDATED = "27 November 2026"
UPDATED_ISO = "2026-11-27"

# The stylesheet is cached for a year (see HEADERS in gen.py), so its address
# carries a hash of its contents: change the file and every page asks for a new one.
with open(os.path.join(ROOT, "assets", "site.css"), "rb") as _f:
    CSS_VERSION = hashlib.sha256(_f.read()).hexdigest()[:10]

# Who publishes the site, in the words search engines read.
ORG = {"@context": "https://schema.org", "@type": "Organization", "name": COMPANY, "url": SITE + "/",
       "logo": SITE + "/apple-touch-icon.png", "email": EMAIL}


def crumbs(*trail):
    """A breadcrumb trail from the home page: crumbs(("Guides", "/guides/"), ...)."""
    items = [("Home", "/")] + list(trail)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": name, "item": SITE + path}
        for i, (name, path) in enumerate(items, 1)]}

APPLE = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.37 12.6c-.02-2.2 1.8-3.26 '
         '1.88-3.31-1.02-1.5-2.62-1.7-3.19-1.73-1.36-.14-2.65.8-3.34.8-.69 0-1.75-.78-2.88-.76-1.48.02-2.85.86-3.61 '
         '2.19-1.54 2.67-.39 6.62 1.11 8.79.73 1.06 1.6 2.25 2.75 2.21 1.1-.04 1.52-.71 2.85-.71 1.33 0 1.71.71 '
         '2.88.69 1.19-.02 1.94-1.08 2.67-2.15.84-1.23 1.19-2.42 1.21-2.48-.03-.01-2.32-.89-2.34-3.54zM14.2 '
         '6.13c.61-.74 1.02-1.76.91-2.78-.88.04-1.94.59-2.57 1.32-.56.65-1.06 1.7-.93 2.7.98.08 1.98-.5 2.59-1.24z"/></svg>')


def store_url(ct):
    if PROVIDER_TOKEN:
        return f"{APP_STORE_URL}?pt={PROVIDER_TOKEN}&ct={ct}&mt=8"
    return APP_STORE_URL


def store(ct):
    return (f'<a class="store" href="{E(store_url(ct))}">{APPLE}'
            f'<span><small>Download on the</small><b>App Store</b></span></a>')


def phone(img, alt, lazy=True):
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return (f'<figure class="phone"><img src="{ASSETS}/img/{img}.webp" alt="{E(alt)}" width="660" height="1434"'
            f'{load}></figure>')


SHIELD = f"""<div class="shield" role="img" aria-label="The On Ice shield: Pause before you buy. Buttons: Note it, Never mind.">
  <span class="tag">In a shop you chose</span>
  <img src="{BASE}/mark.svg" alt="" width="44" height="44">
  <b>Pause before you buy.</b>
  <p>Want something here? Note it in On Ice and decide later.</p>
  <div class="btns"><span>Note it</span><span>Never mind</span></div>
</div>"""

NAV = [("how-it-works", "How it works", "/how-it-works/"), ("pricing", "Pricing", "/pricing/"),
       ("guides", "Guides", "/guides/"), ("support", "Support", "/support/")]


def layout(key, path, title, description, body, *, ct, dark_top=False, jsonld=(), og_type="website", head=""):
    """One page. `path` is its address under the site root, `ct` its campaign name."""
    url = SITE + path
    current = ' aria-current="page"'
    nav = "".join(
        f'<a href="{BASE}{p}"{current if k == key else ""}>{label}</a>' for k, label, p in NAV
    )
    get = f'<a class="get" href="{E(store_url(ct + "-nav"))}">Get the app</a>'
    ld = "".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in jsonld)
    top = f"""<header class="top"><div class="wrap">
  <a class="brand" href="{BASE}/"><img src="{BASE}/mark.svg" alt="" width="30" height="30">{APP}</a>
  <a class="get get-m" href="{E(store_url(ct + "-nav"))}">Get the app</a>
  <nav aria-label="Pages">{nav}{get}</nav>
</div></header>"""
    languages = " · ".join(
        f'<a href="{BASE}{p}/" lang="{c}" hreflang="{c}">{E(gen.NATIVE_NAME[c])}</a>'
        for c, p in gen.LANGUAGES if c != "en"
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(description)}">
<meta name="robots" content="{gen.ROBOTS}">
<link rel="canonical" href="{E(url)}">
<meta name="apple-itunes-app" content="app-id={APP_STORE_ID}">
<meta name="theme-color" content="{'#1D2347' if dark_top else '#F6F3EC'}">
<meta property="og:site_name" content="{APP}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta property="og:url" content="{E(url)}">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{APP}: stop impulse buying. Sleep on it first.">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{BASE}/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{BASE}/apple-touch-icon.png">
<link rel="preload" href="{ASSETS}/fonts/newsreader-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{ASSETS}/site.css?v={CSS_VERSION}">
{head}{ld}
{analytics.head()}</head>
<body class="{'' if dark_top else 'on-paper'}">
<a class="skip" href="#content">Skip to content</a>
{'' if dark_top else top}
{body.replace('<!--TOP-->', top) if dark_top else body}
<footer><div class="wrap">
  <div class="who">
    <a class="brand" href="{BASE}/"><img src="{BASE}/mark.svg" alt="" width="30" height="30">{APP}</a>
    <p>One night between you and the buy button. Made by {COMPANY}. Write to <a href="mailto:{EMAIL}">{EMAIL}</a> and a person will reply.</p>
  </div>
  <div><h4>The app</h4><ul>
    <li><a href="{BASE}/how-it-works/">How it works</a></li>
    <li><a href="{BASE}/pricing/">Pricing</a></li>
    <li><a href="{E(store_url(ct + "-footer"))}">Download on the App Store</a></li>
  </ul></div>
  <div><h4>Read</h4><ul>
    <li><a href="{BASE}/guides/">All guides</a></li>
    <li><a href="{BASE}/guides/how-to-block-amazon-on-iphone/">Block Amazon on iPhone</a></li>
    <li><a href="{BASE}/guides/24-hour-rule-for-shopping/">The 24 hour rule</a></li>
  </ul></div>
  <div><h4>Help and legal</h4><ul>
    <li><a href="{BASE}/support/">Support</a></li>
    <li><a href="{BASE}/privacy/">Privacy Policy</a></li>
    <li><a href="{BASE}/terms/">Terms of Use</a></li>
    <li><a href="{BASE}/delete-data/">Your data</a></li>{analytics.footer_link(BASE)}
  </ul></div>
  <p class="legal">© {YEAR} {APP} · {COMPANY}. Money figures on this site are sample estimates. On Ice does not connect to a bank and does not give financial advice. Apple, iPhone, iPad, Safari and App Store are trademarks of Apple Inc. Amazon is a trademark of Amazon.com, Inc. or its affiliates, and On Ice is not affiliated with it. Support in other languages: {languages}</p>
</div></footer>
{analytics.banner(BASE)}</body>
</html>
"""
    return html


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------

FAQ = [
    ("Will On Ice lock me out of my shopping apps?",
     "No. An ordinary shield is a pause, not a wall. Tap <kbd>Note it</kbd>, say what caught your eye, and "
     "<kbd>I need to shop now</kbd> opens the shop for 1, 5 or 15 minutes. The only things with no way through are "
     "ones you set up yourself, such as a daily limit you have reached, a timed block or a hard rule for one shop. "
     "Each of those ends on its own."),
    ("Does it block shopping websites, or only apps?",
     "Both. Add a shop's app and its website separately and each is shielded, the website in Safari."),
    ("Does it work with Amazon, Temu, Shein and the rest?",
     "You pick the apps in Apple's own Screen Time picker and add websites by address, so it works with whichever "
     "shops get you. On Ice never learns the names of the apps you pick. Apple hands it private codes instead."),
    ("Does On Ice see what I buy?",
     "No. It has no access to your bank, your orders, your browsing or your card. It records only its own events: "
     "that a shield was shown, and what you chose. Those stay on your device."),
    ("What happens to the thing I noted?",
     "It waits on your list for 24 hours. Then On Ice asks once: still want it? If you let it go, the price you "
     "guessed joins your estimated savings. If you still want it, the shop opens for you. Either answer is a good one."),
    ("Is On Ice free?",
     "Yes, and free is a working product, not a demo: one shopping app and one website shielded, the 24 hour wait "
     "and your list, your estimated savings, the breathing pause, three things to do instead, the journal, a daily "
     "shopping time goal, and timed blocks."),
    ("What does Premium add?",
     "Every shop and website you want to shield, waits of 12, 24, 48 or 72 hours, danger hours for late nights, "
     "daily limits, strict mode, your shopping patterns, widgets and the optional AI reflection. "
     f'<a href="{BASE}/pricing/">See the plans.</a>'),
    ("How is this different from deleting the app?",
     "Deleting works until the reinstall, which takes about twenty seconds, and the website is still one tap away in "
     "Safari. On Ice leaves the shop where it is and gives the want somewhere to go: a list, a night, and one "
     f'question tomorrow. <a href="{BASE}/guides/on-ice-vs-deleting-shopping-apps/">The longer comparison.</a>'),
    ("Which devices does it need?",
     "An iPhone or iPad running iOS 17 or newer. There is no account. Each device keeps its own shops, list and "
     "history, and nothing syncs between them."),
]


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def home():
    from guides import GUIDES
    faq = [(q, a) for q, a in FAQ if not q.startswith(("What does Premium add", "How is this different"))]
    faq_html = "".join(f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in faq)
    guide_rows = "".join(
        f'<li><a href="{BASE}/guides/{g["slug"]}/"><b>{g["title"]}</b><i>{g["minutes"]} min read</i>'
        f'<span>{g["blurb"]}</span></a></li>' for g in GUIDES[:3]
    )
    body = f"""<div class="night hero">
<!--TOP-->
<main id="content">
<div class="wrap hero-grid">
  <div class="hero-copy">
    <p class="kicker">Shopping blocker for iPhone and iPad</p>
    <h1>Stop impulse buying. <em>Sleep on it first.</em></h1>
    <p class="lede">On Ice pauses you when you open a shopping app or website. Note what you wanted, wait one night, then decide.</p>
    <div class="cta-row">
      {store("home-hero")}
      <p class="cta-note">Free to start. No account.<br>No bank linking.</p>
    </div>
  </div>
  {demo.html(BASE)}
</div>
</div>

<div class="paper">
<section class="sec" id="how"><div class="wrap">
  <h2>Three steps. <em>One night.</em></h2>
  <ol class="how3">
    <li>
      <div class="n"><span>1 · Tonight</span><i></i></div>
      <div class="pic art" role="img" aria-label="A drawing of a shopping bag with a pause button on it, and the words: Pause before you buy.">{art.scene_pause()}</div>
      <h3>On Ice pauses you</h3>
      <p>Open a shopping app or website and On Ice steps in before you can buy.</p>
    </li>
    <li>
      <div class="n"><span>2 · Still tonight</span><i></i></div>
      <div class="pic art" role="img" aria-label="A drawing of a shirt frozen inside an ice cube. Under it, a line from tonight's moon to tomorrow's sun, marked 24 hours.">{art.scene_ice()}</div>
      <h3>You wait one night</h3>
      <p>Write down what you wanted. It waits on your list for 24 hours. Nothing is bought.</p>
    </li>
    <li>
      <div class="n"><span>3 · Tomorrow</span><i></i></div>
      <div class="pic art day" role="img" aria-label="A drawing of two answers. Don't want it anymore, with a savings jar: you keep the money. Or, Still want it, with a shopping bag: the shop opens.">{art.scene_decide()}</div>
      <h3>You decide</h3>
      <p>Don't want it anymore? Its price joins your estimated savings. Still want it? The shop opens. Either answer is a good one.</p>
    </li>
  </ol>
  <p class="fine">Really need to buy something now? The shop opens for 1, 5 or 15 minutes.</p>
  <p class="after-steps"><a class="more" href="{BASE}/how-it-works/">See the real screens, step by step</a></p>
</div></section>

<section class="sec"><div class="wrap split">
  <div>
    <h2>See what you <em>didn't</em> spend.</h2>
    <p class="intro">Every item you let go adds to a running total. It is built from prices you typed yourself, and it always says estimated.</p>
    <ul class="facts">
      <li><b>No bank linking</b><span>On Ice never connects to an account or reads a transaction.</span></li>
      <li><b>No account</b><span>No sign up, no email field.</span></li>
      <li><b>Private</b><span>Your list stays on your device.</span></li>
    </ul>
    <p class="fine"><a href="{BASE}/privacy/">How the privacy works, in full</a></p>
  </div>
  <div class="receipt" aria-label="A sample receipt of things not bought this month">
    <div class="head">ON ICE</div>
    <div class="sub">THINGS YOU DIDN'T BUY</div>
    <div class="row"><span>Linen shirt</span><i></i><span>≈ $45</span></div>
    <div class="row"><span>Running shoes</span><i></i><span>≈ $135</span></div>
    <hr>
    <div class="row total"><span>LET GO THIS MONTH</span><i></i><span>≈ $180</span></div>
    <div class="row"><span></span><i style="border:0"></i><span class="est">estimated</span></div>
    <div class="foot">Sample figures. Every amount is your own estimate.</div>
  </div>
</div></section>

<section class="sec" id="pricing"><div class="wrap">
  <h2>Free to start. <em>Premium if you want more.</em></h2>
  <div class="plans">
    <div><h3>Free</h3><p class="price">No charge, no trial clock</p><ul>
      <li>One shopping app and one website, shielded</li>
      <li>The 24 hour wait and your list</li>
      <li>Your estimated savings</li>
    </ul></div>
    <div><h3>Premium</h3><p class="price">Monthly · Yearly · Lifetime · Family</p><ul>
      <li>Every shop and website you want</li>
      <li>Waits of 12, 24, 48 or 72 hours</li>
      <li>Daily limits, danger hours and strict mode</li>
    </ul></div>
  </div>
  <p class="fine">Nothing you built is taken away if a subscription lapses. <a href="{BASE}/pricing/">Plans and prices</a></p>
</div></section>

<section class="sec" id="faq"><div class="wrap">
  <h2>Questions people ask first</h2>
  <div class="faq">{faq_html}</div>
  <p class="fine">Something else? <a href="{BASE}/support/#faq">The full support page</a> covers setup, troubleshooting and how to reach us.</p>
</div></section>

<section class="sec"><div class="wrap">
  <h2>Guides, <em>with or without the app.</em></h2>
  <p class="intro">Plain instructions for the settings your iPhone already has, and honest notes on where they stop working.</p>
  <ul class="toc-list">{guide_rows}</ul>
  <p><a class="more" href="{BASE}/guides/">All guides</a></p>
</div></section>
</div>

<section class="night closing"><div class="wrap">
  <h2>Put your next impulse buy <em>on ice.</em></h2>
  <div class="cta-row">
    {store("home-closing")}
    <p class="cta-note">iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.</p>
  </div>
</div></section>
</main>"""
    ld = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": APP, "alternateName": "On Ice app",
         "url": SITE + "/"},
        ORG,
        {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "On Ice: Stop Impulse Buying",
         "operatingSystem": "iOS", "applicationCategory": "FinanceApplication",
         "image": SITE + "/apple-touch-icon.png",
         "description": "A shopping blocker for iPhone and iPad that shields the shopping apps and websites you "
                        "choose and holds each want for 24 hours.",
         "url": SITE + "/", "downloadUrl": APP_STORE_URL,
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": ORG},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faq]},
    ]
    return layout("home", "/", "Stop Impulse Buying: On Ice, the Shopping Blocker for iPhone",
                  "On Ice shields the shopping apps and websites you choose, holds each want for 24 hours, and "
                  "adds up what you didn't spend. Free to start, no account.",
                  body, ct="home", dark_top=True, jsonld=ld, head=f"<style>{demo.css()}</style>\n")


# ---------------------------------------------------------------------------
# How it works
# ---------------------------------------------------------------------------

def how_it_works():
    def step(when, h, ps, pic):
        return (f'<li><div class="txt"><div class="when">{when}</div><h2>{h}</h2>'
                + "".join(f"<p>{p}</p>" for p in ps) + f'</div><div class="pic">{pic}</div></li>')

    steps = "".join([
        step("Setup, once", "Choose the shops that get you",
             ["Pick shopping apps in Apple's own picker and add shopping websites by address. One of each is free, and Premium covers as many as you like.",
              "On Ice uses Apple's Screen Time, the same system behind iOS's built in app limits. It asks for that permission once, and you can withdraw it in Settings at any time."],
             phone("choose-shops", "Setup step 3 of 5: Your shops. Choose an app, a website, or both.")),
        step("When you open one", "The shield comes first",
             ["Instead of the shop, you see On Ice's shield: <em>Pause before you buy.</em> Tap <kbd>Note it</kbd> to write the thing down, or <kbd>Never mind</kbd> to walk away.",
              "It covers the app and the website in Safari, so closing one and opening the other doesn't get around it."],
             f'<div class="phone frame-shield"><div class="inner">{SHIELD}</div></div>'),
        step("A moment", "Breathe before you choose",
             ["Before the choices there is a short pause. Follow the circle at a comfortable pace, or skip it and breathe normally.",
              "It is ten seconds, and it is often enough."],
             phone("breathe", "The breathing pause: A moment before you choose.")),
        step("15 seconds", "Say what caught your eye",
             ["Name the thing, tap a rough price, and tap how you feel: bored, stressed, celebrating, deal FOMO, or “I need it”. Price and feeling are optional.",
              "One screen, no forms. Noting it has to be faster than the craving."],
             phone("note-it", "The capture screen: What caught your eye? Running shoes, about $50, feeling bored.")),
        step("Then", "Decide later",
             ["<kbd>Wait 24h, then decide</kbd> puts the item on your list. Nothing is bought, and the shop shields itself again.",
              "If you really need the shop now, <kbd>I need to shop now</kbd> opens it for 1, 5 or 15 minutes, and the shield comes back on its own. You can also write a few lines instead, or go do something else."],
             phone("decide-later", "The choice screen: Decide later? Right now nothing is bought. Tomorrow On Ice asks once.")),
        step("Overnight", "It waits on ice",
             ["Your item sits under a slow 24 hour ring. With Premium the wait can be 12, 24, 48 or 72 hours.",
              "Nothing is bought while an item cools, and nothing nags you in the meantime."],
             phone("on-ice-countdown", "A countdown ring reading 23:59:52 until you decide. It's on your list: a linen shirt.")),
        step("Tomorrow", "One calm question",
             ["Still want it? Tap <kbd>Still want it</kbd> and the shop opens for you. Tap <kbd>Don't want it anymore</kbd> and the price you guessed joins your estimated savings.",
              "Either answer is a good one. On Ice never scolds you for wanting things, and nothing turns red if you buy it."],
             phone("still-want-it", "The decision screen: Still want the linen shirt? Don't want it anymore, or Still want it.")),
        step("Over time", "Watch it add up",
             ["Savings shows what you let go today, this week and this month. Every figure is your own estimate and is labelled estimated.",
              "An item counts once, when you let it go. Items you keep don't touch the total."],
             phone("estimated-savings", "The Savings screen: saved this month, about $180 estimated, from 2 items you let go.")),
    ])
    body = f"""<main id="content">
<div class="wrap page-head">
  <p class="kicker">How it works</p>
  <h1>A shield, a note, <em>and a night.</em></h1>
  <p class="lede">On Ice doesn't delete your shopping apps or lock them away. It steps in at the moment you open one, gives the want somewhere to go, and lets tomorrow's you decide.</p>
</div>
<div class="wrap"><ol class="steps">{steps}</ol></div>

<section class="sec" style="border-top:1px solid var(--line)"><div class="wrap">
  <h2>Firmer, <em>when you want it.</em></h2>
  <p class="intro">Some nights a pause is enough. Some weeks you want a boundary that holds. You choose how strict On Ice is, and you can change your mind.</p>
  <div class="tools">
    <div class="shots">
      {phone("do-something-else", "The Instead screen: Make room for something else. Walk 10 minutes, Read 10 minutes, Breathe 2 minutes.")}
      {phone("protection-tools", "The Protection tools screen: Block now, for 30 minutes, with a Start block button, plus a daily goal and daily limits.")}
    </div>
    <dl class="tool-list">
      <div><dt>A breath first</dt><dd>Before the choices, a moment to follow a slow circle. You can skip it whenever you prefer.</dd></div>
      <div><dt>Something else to do</dt><dd>A walk, a page, a call. Pick the small things you would enjoy and start one in a tap.</dd></div>
      <div><dt>Timed blocks</dt><dd>Close your shops for the next 30 minutes, or until a time you set.</dd></div>
      <div><dt>A daily goal</dt><dd>A gentle target for shopping time each day. It counts, it doesn't block.</dd></div>
      <div><dt>Daily limits <span class="prem">Premium</span></dt><dd>When the day's allowance is used, those shops rest until tomorrow.</dd></div>
      <div><dt>Danger hours <span class="prem">Premium</span></dt><dd>Make late nights stricter, or close one shop's door entirely.</dd></div>
      <div><dt>Strict mode <span class="prem">Premium</span></dt><dd>So your setup can't be undone in the moment.</dd></div>
      <div><dt>A private journal</dt><dd>A question a day and a place to write. Lock it with Face ID. It never leaves your device.</dd></div>
      <div><dt>Widgets <span class="prem">Premium</span></dt><dd>Your estimated savings and what's on ice, on the Home Screen and Lock Screen.</dd></div>
    </dl>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <h2>Setting it up takes <em>about two minutes.</em></h2>
  <ol class="setup">
    <li><span><b>Try a ten second pause.</b> The same moment the shield will give you later.</span></li>
    <li><span><b>Allow Screen Time access</b> when Apple asks. On Ice can't work without it.</span></li>
    <li><span><b>Pick your shops.</b> Apps in Apple's picker, websites by address.</span></li>
    <li><span><b>Set danger hours if you want them.</b> The late hours when shopping goes badly. Optional, and changeable later.</span></li>
    <li><span><b>Done.</b> Open one of your shops and meet the shield.</span></li>
  </ol>
  <p class="fine">The first shield can feel abrupt. That is the moment the app exists for. Tap <kbd>Note it</kbd> and take fifteen seconds.</p>
  <div class="cta-row" style="margin-top:34px">{store("how-it-works")}<p class="cta-note">Free to start.<br>iPhone and iPad, iOS 17 or newer.</p></div>
</div></section>
</main>"""
    return layout("how-it-works", "/how-it-works/", "How On Ice Works: A Shopping Blocker That Waits 24 Hours",
                  "Step by step: choose your shops, meet the shield, note what caught your eye, wait a night, "
                  "then decide. With real screens from the app.", body, ct="how-it-works",
                  jsonld=[crumbs(("How it works", "/how-it-works/"))])


# ---------------------------------------------------------------------------
# Pricing
# ---------------------------------------------------------------------------

def pricing():
    body = f"""<main id="content">
<div class="wrap page-head">
  <p class="kicker">Pricing</p>
  <h1>Free is a working app, <em>not a demo.</em></h1>
  <p class="lede">Shield one shopping app and one website for as long as you like. Premium is there when you want every shop covered and firmer rules.</p>
</div>
<div class="wrap">
  <div class="plans">
    <div><h3>Free</h3><p class="price">No charge, no trial clock</p><ul>
      <li>One shopping app and one website, shielded</li>
      <li>The 24 hour wait and your list</li>
      <li>Your estimated savings</li>
      <li>The breathing pause</li>
      <li>Three things to do instead</li>
      <li>The journal and a daily shopping time goal</li>
      <li>Timed blocks and Focus blocks</li>
    </ul></div>
    <div><h3>Premium</h3><p class="price">Everything in Free, plus</p><ul>
      <li>Every shop and website you want to shield</li>
      <li>Waits of 12, 24, 48 or 72 hours</li>
      <li>Danger hours, and rules for a single shop</li>
      <li>Daily limits and strict mode</li>
      <li>Every kind of pause, and your own reminders</li>
      <li>Your shopping patterns, and how purchases felt afterwards</li>
      <li>Six things to do instead, and a look back at your journal</li>
      <li>Home Screen and Lock Screen widgets</li>
      <li>The optional AI reflection, off until you turn it on</li>
    </ul></div>
  </div>

  <div class="table-scroll"><table class="price-table">
    <thead><tr><th>Premium plan</th><th>US price</th><th>Good to know</th></tr></thead>
    <tbody>
      <tr><td>Monthly</td><td class="num">$4.99 a month</td><td>Cancel any time in your App Store settings.</td></tr>
      <tr><td>Yearly</td><td class="num">$29.99 a year</td><td>Starts with a 7 day free trial where one is offered.</td></tr>
      <tr><td>Lifetime</td><td class="num">$79.99 once</td><td>One payment. No renewal.</td></tr>
      <tr><td>Family Yearly</td><td class="num">$44.99 a year</td><td>Shared with up to five family members through Apple's Family Sharing. 7 day free trial where offered.</td></tr>
      <tr><td>Family Lifetime</td><td class="num">$119.99 once</td><td>One payment for the whole family group.</td></tr>
    </tbody>
  </table></div>
  <p class="fine">These are US prices. The App Store shows the price in your own currency before you pay, and that is the price that applies. Billing, refunds and cancellations are handled by Apple. <a href="{BASE}/terms/#subscriptions">Subscription terms</a></p>
</div>

<section class="sec" style="margin-top:clamp(48px,7vw,90px);border-top:1px solid var(--line)"><div class="wrap">
  <h2>The small print, <em>in plain words.</em></h2>
  <div class="faq">
    <details open><summary>What happens if my subscription ends?</summary><div><p>Nothing you built is taken away. Your list, history and estimated savings stay, the shops you chose stay shielded, and your rules, limits and a running strict mode keep holding. Your wait goes back to 24 hours, the AI reflection switches off, and widgets and the pattern screens wait for Premium to return.</p></div></details>
    <details><summary>How do the family plans work?</summary><div><p>Family Yearly and Family Lifetime are shared through Apple's Family Sharing with up to five other people in your family group, six in all. Each person gets Premium in their own copy of On Ice, on their own device. Nobody sees anyone else's shops, list, journal or savings.</p></div></details>
    <details><summary>Can I restore Premium on a new phone?</summary><div><p>Yes. Open <kbd>Settings</kbd> in On Ice and tap <kbd>Restore purchases</kbd>. Premium belongs to your Apple Account, not to the device. Your list and journal live on the device that made them and move only with a backup of the whole device.</p></div></details>
    <details><summary>Does On Ice make money from what I buy?</summary><div><p>No. There are no affiliate links, no ads and no price tracking. Premium is the only way On Ice earns anything, which is why it has no reason to nudge you toward a checkout.</p></div></details>
  </div>
  <div class="cta-row" style="margin-top:34px">{store("pricing")}<p class="cta-note">Start free.<br>Upgrade inside the app if you want to.</p></div>
</div></section>
</main>"""
    return layout("pricing", "/pricing/", "On Ice Pricing: Free Plan and Premium",
                  "On Ice is free for one shopping app and one website. Premium adds every shop, longer waits, "
                  "daily limits and strict mode. Monthly, yearly and lifetime plans.", body, ct="pricing",
                  jsonld=[crumbs(("Pricing", "/pricing/"))])


# ---------------------------------------------------------------------------
# Guides
# ---------------------------------------------------------------------------

def guides_index():
    from guides import GUIDES
    rows = "".join(
        f'<li><a href="{BASE}/guides/{g["slug"]}/"><b>{g["title"]}</b><i>{g["minutes"]} min read</i>'
        f'<span>{g["blurb"]}</span></a></li>' for g in GUIDES
    )
    body = f"""<main id="content">
<div class="wrap page-head">
  <p class="kicker">Guides</p>
  <h1>How to shop less, <em>without white knuckles.</em></h1>
  <p class="lede">Step by step instructions for the settings your iPhone already has, written by the people who make On Ice. Each guide starts with the free way and says plainly where it stops working.</p>
</div>
<div class="wrap" style="padding-bottom:clamp(56px,8vw,110px)">
  <ul class="toc-list" style="margin-top:0">{rows}</ul>
</div>
</main>"""
    return layout("guides", "/guides/", "Guides: Block Shopping Apps and Stop Impulse Buying",
                  "Practical guides to blocking shopping apps and websites on iPhone, the 24 hour rule, and "
                  "getting through sale season without overspending.", body, ct="guides",
                  jsonld=[crumbs(("Guides", "/guides/"))])


def guide_page(g):
    from guides import GUIDES
    others = [o for o in GUIDES if o["slug"] != g["slug"]][:3]
    rel = "".join(
        f'<li><a href="{BASE}/guides/{o["slug"]}/"><b>{o["title"]}</b><i>{o["minutes"]} min read</i></a></li>'
        for o in others
    )
    ct = "guide-" + g["ct"]
    appbox = f"""<aside class="appbox">
  <img src="{BASE}/apple-touch-icon.png" alt="" width="64" height="64">
  <div><b>{g["box_title"]}</b><p>{g["box_text"]}</p>{store(ct)}</div>
</aside>"""
    content = g["body"].format(BASE=BASE, ASSETS=ASSETS, PHONE=PhoneFmt())
    body = f"""<main id="content">
<article class="article">
  <header>
    <p class="crumbs"><a href="{BASE}/guides/">Guides</a> / {g["topic"]}</p>
    <h1>{g["title"]}</h1>
    <p class="standfirst">{g["standfirst"]}</p>
    <p class="byline">By the On Ice team · Updated {UPDATED} · {g["minutes"]} min read</p>
  </header>
  <div class="prose">
{content}
{appbox}
  </div>
</article>
<div class="related"><h2>Keep reading</h2><ul class="toc-list">{rel}</ul></div>
</main>"""
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": g["title"],
           "description": g["description"], "dateModified": UPDATED_ISO, "datePublished": UPDATED_ISO,
           "author": {"@type": "Organization", "name": "On Ice"},
           "publisher": ORG, "image": SITE + "/assets/og.png",
           "mainEntityOfPage": SITE + f'/guides/{g["slug"]}/'},
          crumbs(("Guides", "/guides/"), (g["title"], f'/guides/{g["slug"]}/'))]
    return layout("guides", f'/guides/{g["slug"]}/', g["seo_title"], g["description"], body, ct=ct,
                  jsonld=ld, og_type="article")


class PhoneFmt:
    """`{PHONE[name|alt text|caption]}` inside a guide body."""

    def __getitem__(self, spec):
        img, alt, cap = spec.split("|")
        return f'<figure class="shot">{phone(img, alt)}<figcaption>{cap}</figcaption></figure>'


# ---------------------------------------------------------------------------

def check(rel, html):
    """The two things a reader of these pages must never meet."""
    if "—" in html or "–" in html:
        raise SystemExit(f"{rel}: long dash in copy")
    import re
    if re.search(r"\bCooldown\b", html):
        raise SystemExit(f"{rel}: the codebase's name reached a page")


def build():
    """[(file, html, sitemap path or None)]"""
    from guides import GUIDES
    out = [
        ("index.html", home(), "/"),
        ("how-it-works/index.html", how_it_works(), "/how-it-works/"),
        ("pricing/index.html", pricing(), "/pricing/"),
        ("guides/index.html", guides_index(), "/guides/"),
    ]
    for g in GUIDES:
        out.append((f'guides/{g["slug"]}/index.html', guide_page(g), f'/guides/{g["slug"]}/'))
    for rel, html, _ in out:
        check(rel, html)
    return out


def copy_assets(out):
    """When building somewhere other than the repo root, bring the static files along."""
    if os.path.abspath(out) == ROOT:
        return
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(out, "assets"), dirs_exist_ok=True)
    shutil.copy(os.path.join(ROOT, "apple-touch-icon.png"), out)
