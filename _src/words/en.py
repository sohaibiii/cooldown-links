# -*- coding: utf-8 -*-
"""English — the development language, and the fallback behind all seven others.

A key missing from another catalogue renders as the English here, never as an
identifier. That is the same rule the app follows (CLAUDE.md §11).

Every value is an HTML fragment. `{name}` placeholders are filled by
`gen.context()`: `{BASE}` and `{L}` build an in-language link, `{MAIL}` is the
support address, `{COMPANY}` the publisher, `{DATE}` the localised date, `{K_*}`
one of the app's own labels in a <kbd>, and the rest are icons.

Written against On Ice 0.2.0. Everything a page claims about the app — what is
stored, what is sent, what is free — was checked against the code; change a
claim here only in step with the app (README, "What the copy promises").
"""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Support",
"nav.about": "About",
"nav.privacy": "Privacy",
"nav.terms": "Terms",
"nav.data": "Your data",

"ui.skip": "Skip to content",
"ui.pages": "Pages",
"ui.footer": "Footer",
"ui.lang": "Language",
"ui.toc": "On this page",
"ui.rights": "All rights reserved.",
"ui.store_soon": "Coming soon to the App Store",
"ui.store_get": "Download on the App Store",
"ui.date": "22 October 2026",
"ui.last_updated": "Last updated: {DATE}",

# The app's own labels, exactly as its screens write them. In every other
# catalogue these are copied from the app's Localizable.xcstrings, never
# translated afresh. `ios_settings`, `screen_time`, `apps_with_st` and
# `notifications` are iOS's own labels, as iOS writes them in that language.
"k.settings": "Settings",
"k.ios_settings": "Settings",
"k.screen_time": "Screen Time",
"k.apps_with_st": "Apps with Screen Time Access",
"k.notifications": "Notifications",
"k.restore": "Restore purchases",
"k.protection_tools": "Protection tools",
"k.repair": "Repair protection",
"k.someone_key": "Someone holds the key",
"k.only_these": "Only these apps",
"k.ai_reflection": "AI reflection",
"k.writer": "Reflection writer",
"k.what_gets_sent": "What gets sent",
"k.lock_journal": "Lock journal",
"k.export_journal": "Export journal",
"k.delete_entry": "Delete entry",
"k.reflect_week": "Reflect on my week",
"k.help_privacy": "Help & privacy",
"k.email_support": "Email support",
"k.language": "Language",
"k.note_it": "Note it",
"k.never_mind": "Never mind",
"k.need_to_shop": "I need to shop now",
"k.done_block": "I'm done — block it again",
"k.remove": "Remove",
"k.follow_ups": "Follow-up questions",

"meta.support.title": "On Ice — Support",
"meta.support.desc": "Official support for On Ice, the iPhone and iPad app that puts one night between you and the buy button. How it works, requirements, FAQ and contact.",
"meta.about.title": "On Ice — One night between you and the buy button",
"meta.about.desc": "On Ice shields the shopping apps and websites you choose and asks you to sleep on it first. No bank access, no price tracking, no affiliate links.",
"meta.privacy.title": "Privacy Policy — On Ice",
"meta.privacy.desc": "On Ice has no account, no bank connection and no analytics. What stays on your device, and exactly what the one optional AI feature sends.",
"meta.terms.title": "Terms of Use — On Ice",
"meta.terms.desc": "Terms of Use (EULA) for On Ice: what the app is and is not, why every figure is an estimate, how Premium and family plans are billed, and what strict mode asks of you.",
"meta.data.title": "Delete your data — On Ice",
"meta.data.desc": "How to remove what On Ice holds — all of it on your device — and what happens to your subscription.",
"meta.nf.title": "Not found — On Ice",
"meta.nf.desc": "Page not found.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Support",
"s.h1": "Help with On Ice",
"s.sub": "One night between you and the buy button. On Ice shields the shopping apps and websites you chose and asks you to sleep on it first. This page covers how it works, what it needs, and how to reach us.",
"s.cta": "Read the FAQ",
"s.meta": 'No account · no bank access · <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

"s.how.h": "How On Ice works",
"s.how.b": """
<p class="lead">On Ice puts one night between you and the buy button.</p>
<p>You choose the shopping apps and websites that get you. From then on, opening one does not take you straight to the checkout — On Ice's shield comes first: <em>Pause before you buy.</em> Tap {K_note_it} to write the thing down, or {K_never_mind} to walk away. Nothing is ever bought or cancelled on your behalf.</p>
<p>Anything you note down waits on your list — twenty-four hours, unless you chose another length. When the wait is over, On Ice asks one question: still want it? Most wants don't survive the night, and the ones that do were real. Either answer is a good one.</p>
<ul class="rows">
  <li><span class="tile">{shield}</span><div><b>Protection</b><span>One switch on the home screen, and one for each shop. While it is on, the shops you chose show On Ice's shield instead of opening — the app <em>and</em> the website, in Safari too.</span></div></li>
  <li><span class="tile">{moon}</span><div><b>A short pause</b><span>Before anything else, a moment to breathe, type a sentence, read a reminder or say what you came for. You choose which, and how long.</span></div></li>
  <li><span class="tile">{note}</span><div><b>Note it</b><span>Name the thing, tap a rough price, tap how you feel — bored, stressed, celebrating, deal FOMO, or “I need it”. One screen, fifteen seconds.</span></div></li>
  <li><span class="tile amber">{snow}</span><div><b>On ice</b><span>Noted items wait under a countdown ring. Nothing is bought while an item cools. If you really need the shop now, it opens for a few minutes and the shield comes back on its own.</span></div></li>
  <li><span class="tile green">{coin}</span><div><b>Estimated savings</b><span>Every item you let go counts toward a running total, built entirely from prices you typed yourself — for today, this week and this month.</span></div></li>
  <li><span class="tile amber">{clock}</span><div><b>Goals, limits and blocks</b><span>A daily shopping-time goal, daily limits, timed blocks, Focus blocks, and rules for the hours that go badly. Strict mode holds your setup in place.</span></div></li>
  <li><span class="tile">{book}</span><div><b>Something else to do</b><span>A private journal, and a few things to do instead — a walk, a book, a call — for when the craving needs somewhere to go.</span></div></li>
  <li><span class="tile">{widget}</span><div><b>Widgets, Live Activities and Shortcuts</b><span>Estimated savings and what's on ice on the Home Screen and Lock Screen, a countdown while a shop is open, and Siri and Shortcuts actions to start a block.</span></div></li>
</ul>
""",

"s.requirements.h": "Requirements",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Device</th><td>iPhone or iPad running <strong>iOS 17 or newer</strong>. A few extras need more: Control Center controls need iOS 18, and writing with Apple Intelligence needs a device and language that support it.</td></tr>
<tr><th>Permission</th><td><strong>Screen Time</strong> access, granted once during setup through Apple's own prompt. On Ice uses Apple's Screen Time framework — the same system behind iOS's built-in app limits — and Apple, not On Ice, is what actually stands in front of a shop.</td></tr>
<tr><th>Account</th><td>None. There is no sign-up, no email field and no password anywhere in the app.</td></tr>
<tr><th>Internet</th><td>Not needed. Every shield, pause, list, timer and total works offline. The only network traffic is Apple's when you buy or restore Premium — and the optional AI reflection, if you switch it on with OpenAI as its writer.</td></tr>
<tr><th>Languages</th><td>English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil) and 简体中文. On Ice follows your device's language, or the one you choose in {K_settings} → {K_language}.</td></tr>
<tr><th>Optional</th><td><strong>Notifications</strong>, generated on the device, to hand you from the shield into the app and to tell you when an item's wait is over. <strong>Motion &amp; Fitness</strong>, only to show live steps during a walk. <strong>Face ID or Touch ID</strong>, only if you lock your journal.</td></tr>
</table></div>
""",

"s.start.h": "Getting started",
"s.start.b": """
<p>Setup is a handful of screens and ends with protection already on.</p>
<ol class="steps">
  <li><div><b>Try a ten-second pause</b> — the same moment the shield will give you later.</div></li>
  <li><div><b>Allow Screen Time access</b> when Apple asks. On Ice cannot work without it, and you can withdraw it any time in {K_ios_settings} → {K_screen_time}.</div></li>
  <li><div><b>Pick your shops</b> in Apple's picker, and add the shopping websites you want shielded. On Ice never learns the names of the apps you pick — see <a href="{BASE}{L}/privacy/#screentime">Privacy</a>.</div></li>
  <li><div><b>Set danger hours</b> if you want them — the late hours when shopping goes badly. Optional, and changeable later.</div></li>
  <li><div><b>Done.</b> Open one of your shops and meet the shield.</div></li>
</ol>
<div class="callout"><span class="tile">{info}</span><div>The first shield can feel abrupt. That is the moment the app exists for — tap {K_note_it} and take fifteen seconds.</div></div>
""",

"s.money.h": "About the savings number",
"s.money.b": """
<p>Every price in On Ice is one you typed yourself, and every money figure the app shows is labelled <strong>estimated</strong>. That is not a disclaimer bolted on afterwards — it is the whole design.</p>
<ul>
  <li>On Ice <strong>does not connect to your bank</strong>, read your purchase history, check what anything actually costs, or convert between currencies.</li>
  <li>An item counts toward the total <strong>once</strong>, when you let it go after its wait.</li>
  <li>If you never come back to an item, On Ice reminds you, and 48 hours after its wait ends it counts the item as let go. You can decide any time before then.</li>
  <li>Items you keep don't touch the total — unless you later tell On Ice you bought one for less than you guessed, in which case the difference counts.</li>
  <li>The <strong>spend log</strong> is for impulse buys On Ice never saw. It is kept separate from your savings.</li>
</ul>
<div class="callout green"><span class="tile">{coin}</span><div>The number is a record of what you decided not to buy, at the prices you guessed. It is a good number to be proud of and a bad number to put in a spreadsheet.</div></div>
""",

"s.faq.h": "Frequently asked questions",
"s.faq.b": """
<dl class="faq">
<dt>Is On Ice free?</dt>
<dd>Yes, and free is a working product rather than a demo: <strong>one shopping app and one website</strong> shielded, the twenty-four-hour wait and your list, your estimated savings, the breathing pause, three things to do instead, the journal, a daily shopping-time goal, and timed and Focus blocks.</dd>
<dt>What does Premium add?</dt>
<dd>Every shop and website you want to shield; waits of 12, 24, 48 or 72 hours; every kind of pause, pauses that grow with repeated attempts, and your own reminders; danger-hour and per-shop rules; daily limits; strict mode; your shopping patterns and how purchases felt afterwards; a look back at your journal; six things to do instead; widgets; and the optional AI reflection. Premium is a monthly or yearly subscription — yearly starts with a <strong>free trial</strong> where one is offered — or a single lifetime purchase, and yearly and lifetime also come as <strong>family plans</strong>. Prices are shown in the app for your country, and billing is handled by Apple.</dd>
<dt>How do the family plans work?</dt>
<dd>Premium Family Yearly and Premium Family Lifetime are shared through Apple's Family Sharing with up to five other people in your family group — six in all. Each person gets Premium in their own copy of On Ice, on their own device. Nobody sees anyone else's shops, list, journal or savings.</dd>
<dt>Does it stop me from buying things?</dt>
<dd>No. An ordinary shield is a pause, not a wall: tap {K_note_it}, say what caught your eye, and {K_need_to_shop} opens the shop for a few minutes. {K_done_block} closes it again early. The only things with no way through are the ones you set up yourself — a hard-block rule, a daily limit that has been reached, a timed block or a Focus block — and each of them ends on its own.</dd>
<dt>What happens if my subscription lapses?</dt>
<dd>Nothing you built is taken away. Your list, history and estimated savings stay, the shops you chose stay shielded, and your rules, limits and a running strict mode keep holding. Your wait goes back to 24 hours, the AI reflection switches off, and widgets and the pattern screens wait for Premium to return. You just can't add more Premium features.</dd>
<dt>Can I restore a purchase on a new device?</dt>
<dd>Yes. Open {K_settings} and tap {K_restore}. Premium belongs to your Apple Account, not to the device. Your list, journal and history do not travel with it — they live on the device that made them, and move to a new one only with a backup of the whole device.</dd>
<dt>Does it work on iPad?</dt>
<dd>Yes — iPhone and iPad, iOS 17 or newer. Each device keeps its own shops, list and history; nothing syncs between them.</dd>
<dt>Why can't On Ice tell me which apps I protected?</dt>
<dd>Because it genuinely does not know. Apple's Screen Time hands On Ice opaque tokens that are meaningless outside your device — no app names, no identifiers. On Ice can ask iOS to shield them, and iOS draws their names and icons for you; On Ice cannot read them. Websites you add by typing an address are the exception: On Ice keeps that address on your device so iOS can shield it.</dd>
<dt>Does it shield websites, or only apps?</dt>
<dd>Both. Add a shop's app and its website separately, and each is shielded — the website in Safari.</dd>
<dt>Does On Ice see what I buy?</dt>
<dd>No. It has no access to your bank, your orders, your browsing or your card. It records only its own events — that a shield was shown, and what you chose — and keeps those on your device.</dd>
<dt>Does my journal leave my device?</dt>
<dd>Never. Not to us, not to OpenAI, not with any setting. You can lock it with Face ID, Touch ID or your passcode, and its optional weekly summary is written by Apple Intelligence on your device.</dd>
<dt>Where do my walking steps go?</dt>
<dd>Nowhere. During a walk On Ice shows your steps live, and forgets them when the walk ends. It does not read from or write to Apple Health.</dd>
<dt>What is the AI reflection, and is it on?</dt>
<dd>It is one short question before the choices, now and then, and a few sentences about your week on Sundays. It is <strong>off until you turn it on</strong>. You choose who writes it: <strong>Apple Intelligence</strong>, on your device, or <strong>OpenAI</strong> — the only thing in the app that sends anything off the device. The <a href="{BASE}{L}/privacy/#ai">Privacy Policy</a> lists exactly what.</dd>
</dl>
""",

"s.trouble.h": "Troubleshooting",
"s.trouble.b": """
<h3>A shop opens without a shield</h3>
<ul>
  <li>Check that protection is on at the top of the home screen, and that the shop's own switch is on.</li>
  <li>Check that Screen Time access is still granted: {K_ios_settings} → {K_screen_time} → {K_apps_with_st}. If it was withdrawn, On Ice shows a screen with a way to ask again.</li>
  <li>A <strong>shopping window</strong> you opened may still be running. It closes on its own — or tap {K_done_block} — and the shield comes back.</li>
  <li>If the shop is covered only by a <strong>rule</strong>, the shield appears only during that rule's hours.</li>
  <li>Still nothing? {K_settings} → {K_protection_tools} → {K_repair} applies every shield and schedule again.</li>
</ul>
<h3>Tapping “Note it” doesn't open On Ice</h3>
<ul>
  <li>On some versions of iOS the shield hands you over with a notification. If notifications are off, iOS cannot deliver it — turn them on in {K_ios_settings} → {K_notifications} → On Ice.</li>
  <li>Opening On Ice yourself picks up the item waiting to be noted.</li>
</ul>
<h3>A website isn't shielded</h3>
<p>Websites are shielded by address. Make sure the address you added matches the one you actually open, and remember that a shop's app and its website are two separate things to add.</p>
<h3>My daily goal or limit shows fewer minutes than I expected</h3>
<p>iOS does not tell apps how long you spent in another app. It only tells On Ice when time in your protected shops passes a step — every five minutes at first — so On Ice shows “at least” that many minutes. The real figure can be a little higher.</p>
<h3>I can't turn protection off or remove a shop</h3>
<p>Check whether <strong>strict mode</strong>, a <strong>timed block</strong> or a <strong>Focus block</strong> is running — the home screen says so. While strict mode runs, your setup is held in place by design, and it ends on its own at the time you chose. If you set up {K_someone_key}, the person with the PIN can end it early.</p>
<h3>The AI question never appears</h3>
<p>It needs Premium, and it is off until you switch it on in {K_settings} → {K_ai_reflection}. Even then it asks only when there is a reason — a feeling you have often regretted, a danger hour, or a larger price. With OpenAI as the writer it needs an internet connection. If anything goes wrong it quietly shows you the ordinary choices instead.</p>
<h3>Widgets are behind</h3>
<p>iOS refreshes widgets on its own schedule. Opening On Ice brings them up to date. The savings and “On ice” widgets come with Premium.</p>
<h3>Premium isn't recognised</h3>
<p>Tap {K_restore} in {K_settings}, and make sure the device is signed into the same Apple Account that made the purchase — or, for a family plan, that you are in the purchaser's Family Sharing group. Refunds and billing questions are handled by Apple through <a href="https://support.apple.com/billing">Apple Support</a>.</p>
<h3>The app is in the wrong language</h3>
<p>Choose one in {K_settings} → {K_language}. Apple's own app picker follows the next time you open On Ice.</p>
""",

"s.contact.h": "Contact",
"s.contact.b": """
<p>Questions, a bug, or something that should work and doesn't — write to us and a person will reply. The quickest way is {K_settings} → {K_help_privacy} → {K_email_support}, which adds your On Ice version, iOS version and device model for you.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Include your device model, the iOS version, and what you expected to happen. Never send us your list, your prices or your journal — we do not need them and would rather not hold them.</span></div></div>
<p class="small">Billing, refunds and subscription changes are handled by Apple: <a href="https://apps.apple.com/account/subscriptions">manage subscriptions</a> · <a href="https://support.apple.com/billing">request a refund</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "About On Ice",
"a.h1": "One night between you and the buy button.",
"a.sub": "Pick the shopping apps and websites that get you. From then on, opening one gets you a shield first — and a decision that tomorrow you gets to make.",
"a.cta": "Support",
"a.meta": "No account · no bank access · iPhone and iPad, iOS 17+ · 8 languages",
"a.lead": "On Ice puts one night between you and the buy button. Not a lockout, not a lecture — a short pause, and time to find out whether you actually wanted it. Nothing here scolds you for wanting things, and nothing turns red if you buy it.",

"a.f1.h": "Pause before you buy.",
"a.f1.p": "Open a shop you've chosen and On Ice steps in before the checkout does — in the app and in Safari. Take a breath, type a sentence, read a reminder, or say what you came for.",
"a.f2.h": "Note it, don't buy it.",
"a.f2.p": "Name the thing, tap a rough price, tap how you feel. Fifteen seconds, one screen. Noting it has to be faster than the craving.",
"a.f3.h": "One night on ice.",
"a.f3.p": "Noted items wait under a countdown ring — 24 hours, or anywhere from 12 to 72. Nothing is bought while an item cools, and tomorrow you gets the decision.",
"a.f4.h": "Watch it add up.",
"a.f4.p": "Every item you let go counts toward your estimated savings — your own guesses, for today, this week and this month, next to the hours when the shields keep meeting you.",
"a.f5.h": "Something else to do.",
"a.f5.p": "When the craving needs somewhere to go: a walk with live steps, a book, a playlist, a call. Pick what works for you and start it in one tap.",
"a.f6.h": "Firmer when you want it.",
"a.f6.p": "A daily shopping-time goal, daily limits, timed and Focus blocks, danger-hour rules for late nights, and strict mode to hold it all in place.",
"a.f7.h": "A journal just for you.",
"a.f7.p": "A question a day and a place to write. Lock it with Face ID. Nothing in it ever leaves your device.",
"a.f8.h": "It never sees what you buy.",
"a.f8.p": 'No bank linking, no purchase history, no price tracking, no affiliate links, no analytics. Apple hands On Ice codes, not names. <a href="{BASE}{L}/privacy/">How that works.</a>',

"a.price.h": "What it costs",
"a.price.b": """
<p>Free is a working product, not a demo, and nothing you have already built is taken away if a subscription lapses.</p>
<div class="tiers">
  <div class="tier"><div class="lbl">Free</div><div class="price">No charge</div><ul><li>One shopping app and one website, shielded</li><li>The 24-hour wait and your list</li><li>Your estimated savings</li><li>The breathing pause and three things to do instead</li><li>The journal, a daily goal, timed and Focus blocks</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Monthly · Yearly · Lifetime</div><ul><li>Every shop and website you want</li><li>Waits of 12, 24, 48 or 72 hours</li><li>Every kind of pause, and your own reminders</li><li>Danger hours, per-shop rules, daily limits and strict mode</li><li>Your shopping patterns, and how purchases felt afterwards</li><li>Widgets, a look back at your journal, and the optional AI reflection</li><li>Yearly starts with a free trial; yearly and lifetime also come as family plans for up to six people</li></ul></div>
</div>
<p class="small">Prices are shown in the app and on the App Store for your country. Billing is handled by Apple. <a href="{BASE}{L}/terms/#subscriptions">Subscription terms.</a></p>
""",

"a.st.h": "Built on Apple's Screen Time",
"a.st.b": """
<p>On Ice uses the same framework that powers iOS's built-in app limits. Apple grants it only to apps it has reviewed for the purpose, and Apple — not On Ice — is what actually stands between you and the shop. That is why On Ice can shield an app without ever learning its name.</p>
<p>iPhone and iPad · iOS 17 or newer · English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil), 简体中文</p>
""",

"a.est.h": "Every figure is an estimate",
"a.est.b": """
<p>On Ice asks you what something roughly costs and remembers your answer. It connects to no bank, verifies no price, converts no currency and gives no financial advice. Every number it shows carries the word <em class="est">estimated</em> — in the app, in the widgets and on this site.</p>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Privacy Policy",
"p.h1": "It never sees what you buy.",
"p.sub": "No account, no bank linking, no purchase history, no price tracking and no analytics. What On Ice knows stays on your device — with one optional feature, off until you switch it on, whose exact contents are listed below.",
"p.meta": "Effective {DATE} · applies to the On Ice app for iPhone and iPad, and to this site",

"p.summary.h": "The short version",
"p.summary.b": """
<p class="lead"><strong>On Ice has no account, no analytics, no advertising and no third-party code.</strong> There is no bank connection, no purchase history, no price tracking and no affiliate link anywhere in it. Everything it knows is written to your iPhone or iPad and stays there.</p>
<div class="callout"><span class="tile">{eye-off}</span><div>The apps you pick in Apple's Screen Time picker reach On Ice as opaque tokens that only your device can interpret. There is no app name, no identifier, and nothing to send.</div></div>
<p>There is exactly one exception, and it is off until you switch it on: the optional <strong>AI reflection</strong>. With <strong>Apple Intelligence</strong> as its writer it runs on your device and nothing leaves. With <strong>OpenAI</strong> as its writer, a short, fixed list of details leaves — listed in full <a href="#ai">below</a>. Your journal never leaves the device, whichever writer you choose.</p>
<p>This policy applies to the On Ice app for iPhone and iPad, published by {COMPANY}, and to this website.</p>
""",

"p.collect.h": "What we collect",
"p.collect.b": """
<p>“Collect”, in Apple's sense and in ours, means sending data off the device and keeping it somewhere that is not transient. With the AI reflection off — how every install starts — On Ice sends nothing about you anywhere. The table shows what changes if you switch it on with OpenAI as the writer.</p>
<div class="table-wrap"><table>
<tr><th>Category</th><th>Sent?</th><th>What that means</th></tr>
<tr><td>Financial info</td><td>Only with OpenAI reflections on</td><td>No bank connection, no card, no transaction access, no purchase history. With OpenAI reflections on, a <em>price band</em> for the item in front of you and a rounded weekly estimated-savings total are sent — never an exact price, an account or a balance.</td></tr>
<tr><td>Contact info</td><td>No</td><td>There is no account, no sign-in and no email field anywhere in the app.</td></tr>
<tr><td>Identifiers</td><td>Only with OpenAI reflections on</td><td>No user ID, no advertising identifier, and On Ice never asks to track you. Our AI service sees a random App Attest key identifier, used only to count requests per device per day and deleted after two days.</td></tr>
<tr><td>Usage data</td><td>Only with OpenAI reflections on</td><td>No analytics and no product-interaction events. Shields, pauses and decisions are counted on your device, for your own screens. A reflection carries today's count of shields; the weekly write-up carries the week's counts.</td></tr>
<tr><td>User content</td><td>Only with OpenAI reflections on</td><td>Your list, prices, journal, spend log and reminders stay on the device. With OpenAI as the writer, the name of the item in front of you and what you type in answer to the question are sent.</td></tr>
<tr><td>Browsing history</td><td>No</td><td>On Ice cannot see what you browse. It learns only that its own shield was shown, and what you chose on it.</td></tr>
<tr><td>Location, health, fitness, contacts, search, diagnostics</td><td>No</td><td>Steps during a walk are shown live and never stored or sent. On Ice has no crash or performance reporter of its own.</td></tr>
</table></div>
<p><strong>Tracking:</strong> none. On Ice does not link anything about you with data from other companies' apps or websites, and shares nothing with data brokers or advertisers. There are <strong>no affiliate links</strong>: On Ice earns nothing when you buy something, which is the only arrangement compatible with an app whose job is to help you buy less.</p>
""",

"p.device.h": "What stays on your device",
"p.device.b": """
<p>On Ice keeps the following in its own private storage on your iPhone or iPad, protected by your device's passcode and encryption. None of it is uploaded, synced to iCloud, backed up by us, or visible to us.</p>
<ul>
  <li><strong>Your shops</strong> — apps and categories as opaque Screen Time tokens On Ice cannot read, and websites you added by address as that address (see below).</li>
  <li><strong>Your list</strong> — the item names you typed, the prices you estimated, the feeling you tapped, and when each item was noted and decided.</li>
  <li><strong>What happened at each shield</strong> — that it was shown, when, and whether you walked away, waited, opened the shop, let the item go or kept it, and what you said you came for. Your estimated savings, streaks and patterns are made of this.</li>
  <li><strong>What you add yourself</strong> — the spend log, how a purchase felt afterwards, your journal, your own reminders, and the things you chose to do instead, including any app link or web address you gave one.</li>
  <li><strong>Your rules and settings</strong> — danger hours, per-shop rules, your daily goal and limits, blocks, strict-mode state, your pause, your day start, your language and the AI writer you chose. If someone holds your strict-mode key, only a salted one-way hash of their PIN is stored, never the PIN.</li>
  <li><strong>Usage steps</strong> — the highest time step iOS has reported for your protected shops today, for your goal and limits (see below).</li>
  <li><strong>Your Premium status</strong> — the plan and when it renews or ends, so the app knows what to unlock.</li>
  <li><strong>The latest weekly write-up</strong> — only while the AI reflection is on.</li>
</ul>
<p>If you use iCloud Backup or an encrypted backup to a computer, Apple may include On Ice's data in that backup under your own Apple Account and Apple's privacy terms. We have no access to it.</p>
""",

"p.journal.h": "Your journal",
"p.journal.b": """
<p>The journal is the one place in On Ice you write for nobody. Entries — and the mood, item or feeling attached to one — are stored on your device and <strong>never leave it</strong>: not with the AI reflection, not with OpenAI, not with any setting.</p>
<ul>
  <li>{K_lock_journal} asks for Face ID, Touch ID or your device passcode before the journal opens, and closes it again when you leave the app. iOS performs the check; On Ice never sees your face, fingerprint or passcode. The lock guards the screen; the entries themselves are protected by your device's own encryption, like the rest of On Ice's data.</li>
  <li>{K_reflect_week} summarises your recent entries with Apple Intelligence, <em>on your device</em>. There is no server version of it.</li>
  <li>{K_export_journal} makes a plain-text file and hands it to iOS, so you choose where to save it. On Ice sends it nowhere.</li>
  <li>The journal widget shows only the day's question. It never reads an entry.</li>
</ul>
""",

"p.permissions.h": "What On Ice asks to use",
"p.permissions.b": """
<p>iOS asks for each of these in its own words, and each can be changed in {K_ios_settings} at any time.</p>
<div class="table-wrap"><table>
<tr><th>Permission</th><th>Why</th><th>Needed?</th></tr>
<tr><td>Screen Time</td><td>To shield the shops you choose, run your blocks, rules and limits, and receive usage steps.</td><td>Yes — On Ice cannot work without it.</td></tr>
<tr><td>Notifications</td><td>To hand you from the shield into the app, to say when an item's wait is over or nearly over, and for follow-up questions, activity timers and suggestions you leave on.</td><td>No</td></tr>
<tr><td>Motion &amp; Fitness</td><td>To show your steps live during a walk. The motion sensor is used only while a walk is on screen, and steps are never stored or sent.</td><td>No — only if you start a walk</td></tr>
<tr><td>Face ID or Touch ID</td><td>To unlock the journal, if you lock it.</td><td>No</td></tr>
</table></div>
<p>When you choose what a “thing to do instead” opens, On Ice asks iOS whether a short list of apps is installed — Books, Kindle, Audible, Podcasts, Music, Spotify, Duolingo, Headspace, Calm, Notes, Messages and Shortcuts — so it can offer the ones you have. The answer is used on the spot to build that list; it is neither stored nor sent.</p>
""",

"p.screentime.h": "Screen Time and your shops",
"p.screentime.b": """
<p>On Ice is built on Apple's Screen Time framework (Family Controls, Managed Settings and Device Activity). You grant it access once, through Apple's own prompt, and can withdraw it at any time in {K_ios_settings} → {K_screen_time}.</p>
<p>When you pick apps, categories or websites in Apple's picker, it returns <strong>tokens</strong>: values that identify them to iOS but mean nothing to On Ice and nothing outside your device. On Ice stores those tokens so it can ask iOS to shield what you chose; iOS draws their names and icons for you. On Ice never receives a bundle identifier or an app name. Where its own components need to compare tokens, they compare one-way hashes of them, never the tokens themselves.</p>
<p><strong>Websites you add by address are different.</strong> A site you type, or pick from On Ice's suggestions, is stored as that address — <code>example.com</code> — because iOS needs it to shield the site. It stays on your device with everything else and is never sent.</p>
<p><strong>Usage is reported in steps.</strong> iOS never gives On Ice a total of your screen time. It only tells On Ice when time in your protected shops passes a step registered in advance — five minutes, ten, fifteen… — which is enough for a daily goal and a limit, and nothing more.</p>
<p>On Ice does not observe your browsing, your messages or what you do inside any app. iOS itself draws the shield and enforces it. On Ice learns only that its own shield was shown and what you chose on it.</p>
""",

"p.ai.h": "The AI reflection — the one thing that can leave",
"p.ai.b": """
<p class="lead">The AI reflection is an optional Premium feature. <strong>It is off when you install On Ice and stays off until you switch it on</strong> in {K_settings} → {K_ai_reflection}.</p>
<p>With it on, some noted items get one short question before you choose — not every item, only when there is a reason: a feeling you have often regretted, a danger hour, or a larger price. On Sundays it can also write a few sentences about your week.</p>
<h3>Two writers, and only one of them leaves the device</h3>
<ul>
  <li><strong>Apple Intelligence</strong> writes on your device. Nothing is sent anywhere. If Apple Intelligence becomes unavailable, On Ice shows you the ordinary choices instead — <strong>it never falls back to a server</strong>.</li>
  <li><strong>OpenAI</strong> writes on OpenAI's servers, through On Ice's own service. Only what is listed below is sent.</li>
</ul>
<p>You choose under {K_writer}. If you switch the AI reflection on without choosing, On Ice uses Apple Intelligence where your device and language support it, and OpenAI where they do not.</p>
<h3>What is sent, with OpenAI as the writer</h3>
<p>For a question:</p>
<ul>
  <li>The <strong>name of the item</strong> you just typed, and anything you write in answer to the question.</li>
  <li>A <strong>price band</strong> — a range such as “250 to 500”, never the amount you typed — and your currency.</li>
  <li>The <strong>feeling</strong> you tapped, if you tapped one.</li>
  <li>The <strong>hour and minute</strong> on your clock. No date, no time zone.</li>
  <li><strong>How many shopping shields you have met today.</strong></li>
  <li>Your own <strong>regret rate for that one feeling</strong>, as a percentage — only once you have rated at least five purchases.</li>
  <li>Your <strong>language</strong>, such as “English (UK)”, so the question comes back in it.</li>
</ul>
<p>For the weekly write-up, <strong>counts and totals only</strong>: shields met, items you waited on, let go, kept or walked away from, how often you opened a shop, your current and best streak, your busiest hour, the share of items you let go, your estimated savings for the week rounded to a whole number with its currency, the date the week began, and your language. <strong>No item names and no individual prices.</strong></p>
<h3>What is never sent</h3>
<ul>
  <li>Screen Time tokens or their hashes, bundle identifiers, or website addresses.</li>
  <li>Which shops or websites you protect, or how many.</li>
  <li>The exact price you typed.</li>
  <li>Anything else on your list — no names, no prices.</li>
  <li>Your spend log, or any individual purchase price.</li>
  <li>How you rated any individual purchase.</li>
  <li>Your journal, rules, limits, blocks, danger hours or strict-mode state.</li>
  <li>Any name, account, email or advertising identifier — nothing that identifies you as a person.</li>
</ul>
<h3>Where it goes, and how long it is kept</h3>
<p>Requests go to <strong>On Ice's own service, hosted on Cloudflare</strong>, and on to <strong>OpenAI</strong>, which runs the model. There is no API key inside the app to be extracted, and the app never calls OpenAI directly.</p>
<p>Before answering, the service uses <strong>Apple's App Attest</strong> to check that the request comes from a genuine copy of On Ice. That check rests on a key created on your device — not on your name or your Apple Account. <strong>The service stores no question, answer or item detail.</strong> It keeps a count of requests per device per day, under that random key identifier, and deletes it after two days; daily totals of requests and model usage for the whole service, which name no device, for about 90 days; and a record of each one-time App Attest challenge until it expires. Its logs record a request's status, how long it took and how many tokens it used — never its contents.</p>
<p><strong>OpenAI does not use this data to train its models.</strong> We switch off OpenAI's stored responses; OpenAI may still keep inputs and outputs in its abuse-monitoring logs, normally for up to 30 days, with exceptions under its own terms. We do not promise that your text is processed in any particular country.</p>
<p><strong>Earlier versions of On Ice</strong> send the same kinds of details to <strong>Google's Gemini model on Vertex AI</strong> instead, through an earlier On Ice service on Google Cloud that also stores no content. Google does not use them to train its models, may keep them for up to 24 hours, and may log them to check for abuse.</p>
<div class="callout"><span class="tile">{sparkle}</span><div>Switching the AI reflection off stops every future request at once, deletes the weekly write-up from your device, and removes the Sunday reminder. On Ice goes back to making no network calls of its own. {K_settings} → {K_ai_reflection} → {K_what_gets_sent} shows the same list inside the app.</div></div>
""",

"p.purchases.h": "Purchases and family plans",
"p.purchases.b": """
<p>Premium is sold through Apple's App Store using StoreKit. The transaction is between you and Apple, under <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>. Apple tells On Ice which plan is active and when it renews or ends — nothing else — and On Ice tells Apple nothing about how you use the app. We never see a card.</p>
<p>With a <strong>family plan</strong>, Apple's Family Sharing gives each member Premium in their own copy of On Ice. Nothing passes between those copies — no shops, list, journal, savings or settings — and On Ice learns only that Premium was shared, not who shared it.</p>
""",

"p.notifications.h": "Notifications, widgets and the Lock Screen",
"p.notifications.b": """
<p><strong>Notifications</strong> are optional and are all scheduled on your device. None is sent from a server, and there is no push service. On Ice uses them to hand you from the shield into the app, to say when an item's wait is over or nearly over, for follow-up questions you can switch off in {K_settings} → {K_follow_ups}, for activity timers and suggestions you choose, and — only with the AI reflection on — for the Sunday write-up. A notification about an item names the item.</p>
<p><strong>Widgets, Live Activities and Control Center controls</strong> read a small snapshot on your device: totals, counts, your streak, and the names and times of up to three of the soonest items. They have no Screen Time access and never see which shops you chose. <strong>The “On ice” widget and an item's Live Activity show the item's name</strong>, so on a Lock Screen anyone holding the device can read it. Money amounts are hidden there while the device is locked. Put them where you are comfortable seeing them.</p>
""",

"p.third.h": "Third parties",
"p.third.b": """
<p>On Ice contains <strong>no third-party code</strong>: no analytics, no advertising, no attribution, no crash reporter, no SDKs. Only these parties are involved, and only as described here:</p>
<ul>
  <li><strong>Apple</strong> — operates the App Store and Family Sharing, processes purchases, enforces the Screen Time shield, runs Apple Intelligence on your device, and provides App Attest. If you have opted in to sharing with developers, Apple may share crash logs with us under its own policy.</li>
  <li><strong>Cloudflare</strong> — hosts On Ice's AI service. When the AI reflection uses OpenAI, requests pass through it, and it stores none of their content.</li>
  <li><strong>OpenAI</strong> — runs the model behind OpenAI reflections, only while that writer is in use, and receives only what is listed <a href="#ai">above</a>.</li>
  <li><strong>Google Cloud</strong> — plays that part for earlier versions of the app only.</li>
</ul>
<p>We do not sell, rent or share personal data with anyone, and we share nothing with data brokers or advertisers. A link you give a “thing to do instead” opens the app or website you chose, under that app's or site's own policy.</p>
""",

"p.delete.h": "Deleting your data",
"p.delete.b": """
<p>Everything On Ice holds is on your device, so removing it does not require asking us. You can delete journal entries, spend-log entries, rules, limits, reminders and activities one by one in the app; switching the AI reflection off deletes the weekly write-up; and <strong>deleting the app removes everything at once</strong>. There is no single button inside the app that erases your whole history, so deleting the app is the way to start fresh. The <a href="{BASE}{L}/delete-data/">Your data</a> page walks through each.</p>
<p>On our side there is nothing to delete: the AI service keeps no content, and its per-device count disappears on its own after two days.</p>
""",

"p.rights.h": "Your rights",
"p.rights.b": """
<p>Wherever you live — including under the GDPR, the UK GDPR and the CCPA/CPRA — you have rights to access, correct, export and erase personal data a company holds about you, to restrict or object to its processing, and to complain to a supervisory authority. On Ice keeps no profile of you on any server, so there is nothing on our side to produce or delete; the data on your device is already in your hands. Using OpenAI reflections is your choice, and switching the AI reflection off withdraws it at once. If you believe we hold something about you, write to {MAIL} and we will respond.</p>
""",

"p.children.h": "Children",
"p.children.b": """
<p>On Ice is a self-directed tool for the person using the device. It is not a parental-control product and does not manage another person's device; a family plan shares Premium, never control or data. It is not directed at children under 13 (or the age of digital consent where you live), and we do not knowingly collect personal information from anyone, of any age.</p>
""",

"p.changes.h": "Changes to this policy",
"p.changes.b": """
<p>We may update this policy as the app changes. The date at the top moves when we do, and material changes are noted in the app's release notes. This version describes the choice between Apple Intelligence and OpenAI for the AI reflection, the journal, walking steps, usage steps, family plans, iPad, and seven more languages. Continued use of On Ice after a change means you accept the revised policy.</p>
<p>This policy is published in eight languages. If a translation and the English differ, the English applies.</p>
""",

"p.contact.h": "Contact",
"p.contact.b": """
<p>{COMPANY}, the publisher of On Ice, is the controller for anything covered here. Questions about privacy: {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Terms of Use",
"t.h1": "The agreement, in plain words.",
"t.sub": "What On Ice does, what it does not promise, why every figure is an estimate, how Premium and family plans are billed, and what blocks and strict mode ask of you.",
"t.meta": "Effective {DATE} · On Ice by {COMPANY}",

"t.acceptance.h": "1. Acceptance of Terms",
"t.acceptance.b": """
<p>These Terms of Use (“Terms”) are an agreement between you and {COMPANY} (“we”, “us”), the publisher of the On Ice app for iPhone and iPad (“On Ice” or “the app”). By installing or using On Ice you accept these Terms and our <a href="{BASE}{L}/privacy/">Privacy Policy</a>. If you do not agree, do not use the app.</p>
<p>These Terms are published in eight languages. If a translation and the English differ, the English applies.</p>
""",

"t.who.h": "2. Who may use On Ice",
"t.who.b": """
<p>You must be at least 13 years old, or the age of digital consent where you live, to use On Ice. On Ice is a tool you install for yourself, on your own device. It is not a parental-control product and must not be used to manage or monitor another person's device. A family plan shares Premium with members of your Family Sharing group; it gives no one control over another member's On Ice.</p>
""",

"t.what.h": "3. What On Ice is — and is not",
"t.what.b": """
<p>On Ice is a self-directed tool that shields shopping apps and websites you choose, offers a short pause, lets you note down what caught your eye, holds it for a period you set, and records on your device what you decided. It also offers a journal, things to do instead, goals, limits and blocks. It is designed to turn an automatic purchase into a decision you actually make.</p>
<p>On Ice is <strong>not</strong> a medical, psychological or therapeutic service, and nothing in it — including feelings you tap, pauses, reminders, journal questions, insights or AI-written text — is advice, diagnosis or treatment. If you are struggling with compulsive spending, debt, anxiety or anything else that affects your wellbeing, please speak to a qualified professional or a debt-advice service. In an emergency, call your local emergency number.</p>
<p>On Ice is also <strong>not a security or parental-control product</strong>. It is designed to be exactly as strong as you ask it to be: the app can be deleted, Screen Time access can be withdrawn in iOS Settings, and shields exist only while the app is installed and authorised.</p>
""",

"t.money.h": "4. Estimates, not financial advice",
"t.money.b": """
<p>Every price in On Ice is a figure <strong>you</strong> enter. The app does not connect to any bank, payment provider or retailer, does not read your transactions or order history, does not track prices, does not convert currencies, and does not verify what anything costs.</p>
<p>The savings figure On Ice shows is therefore an <strong>estimate assembled from your own guesses</strong>, and is labelled as such everywhere it appears. It is not a statement of fact about money you have, a financial record, or anything you should rely on for budgeting, tax, credit or any other decision. {COMPANY} is not a financial adviser, and nothing in the app or on this site is financial, investment or debt advice.</p>
<div class="callout green"><span class="tile">{info}</span><div>On Ice carries no affiliate links and earns nothing from anything you buy or do not buy. Its only revenue is Premium, paid by you through Apple.</div></div>
""",

"t.screentime.h": "5. Screen Time, blocks and strict mode",
"t.screentime.b": """
<p>On Ice relies on Apple's Screen Time framework. Apple enforces the shield; On Ice asks for it. Whether a shield appears, how quickly, whether a usage step is reported, and whether shields persist across restarts and iOS updates is ultimately determined by iOS, and we cannot guarantee it in every circumstance. <strong>On Ice cannot prevent a purchase</strong> — it can only put a screen in front of a shop you chose.</p>
<p>Some tools you can switch on offer <strong>no way through</strong> while they run: a <strong>hard-block rule</strong> during its hours, a <strong>daily limit</strong> once it is reached (until your next day begins), a <strong>timed block</strong> until it ends, and a <strong>Focus block</strong> while that Focus is on. A timed block set to {K_only_these} shields <em>every</em> app on your device except the essential apps you chose. Before starting one, make sure you can reach what you might need — for calls, messages, maps, payments, health or work.</p>
<p><strong>Strict mode</strong> is a commitment you make to yourself. While it runs, for the time you chose, protection stays on, rules stay as they are, shops can be added but not removed, and limits and your day start cannot be changed — <em>including by you, and including by us</em>. We cannot end strict mode, a block or a rule early on request. If you set up {K_someone_key}, the person holding the PIN can end strict mode early, and you can request a delayed escape that ends it 24 hours later; we cannot recover a forgotten PIN. Do not start a commitment you are not prepared to keep, and do not start one on a device you may need unrestricted access to.</p>
<p>Deleting the app ends every shield, block and limit, as described in section 3.</p>
""",

"t.data.h": "6. Your data and your device",
"t.data.b": """
<p>Everything On Ice records is stored on your device — see the <a href="{BASE}{L}/privacy/">Privacy Policy</a>. Nothing syncs between devices. You are responsible for your device, its passcode and its backups. If you delete the app or lose the device without a backup, your list, journal, rules, spend log and savings history are gone, and we have no copy to restore. Your Premium purchase is separate: it belongs to your Apple Account and can be restored on any iPhone or iPad signed into it.</p>
<p>What you write into On Ice is yours. We claim no rights over it, and — except for the optional OpenAI reflection in section 8, which you must switch on yourself — we never receive it.</p>
""",

"t.subscriptions.h": "7. Premium, subscriptions and billing",
"t.subscriptions.b": """
<p>On Ice is free to download and use. <strong>On Ice Premium</strong> unlocks additional features and is sold in five forms, at the price shown in the app and on the App Store for your country:</p>
<ul>
  <li><strong>Premium Monthly</strong> — an auto-renewing subscription, billed monthly.</li>
  <li><strong>Premium Yearly</strong> — an auto-renewing subscription, billed yearly, beginning with a <strong>free trial</strong> where one is offered.</li>
  <li><strong>Premium Lifetime</strong> — a one-time purchase that does not renew.</li>
  <li><strong>Premium Family Yearly</strong> — an auto-renewing subscription, billed yearly, beginning with a <strong>free trial</strong> where one is offered, for up to six people through Family Sharing.</li>
  <li><strong>Premium Family Lifetime</strong> — a one-time purchase that does not renew, for up to six people through Family Sharing.</li>
</ul>
<p>The two family plans are shared through Apple's <strong>Family Sharing</strong> with up to five other members of your family group. Each person gets Premium in their own copy of On Ice, on their own device; no shops, lists, journals, savings or settings are shared between them. Monthly, Yearly and Lifetime are for you alone and are not shared.</p>
<p>Payment is charged to your Apple Account at confirmation of purchase. A free trial converts to a paid subscription unless you cancel at least 24 hours before the trial ends. Subscriptions renew automatically at the same price and period unless auto-renew is turned off at least 24 hours before the end of the current period; renewal is charged within the 24 hours before that period ends. You can manage or cancel a subscription in your <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; cancellation takes effect at the end of the current period, and no partial refund is given for the unused part of a period. Buying a lifetime plan, or receiving a family plan, does not cancel a subscription you already have — cancel it yourself. Refunds are handled by Apple under Apple's policies. Use {K_restore} in the app to recover Premium on a new device.</p>
<p><strong>If a subscription lapses</strong>, nothing you have already built is removed: your list, journal, history and estimated savings stay, the shops you chose stay shielded, and existing rules, limits and a running strict mode keep holding. Your wait returns to 24 hours, the AI reflection switches off, and widgets and pattern screens wait for Premium to return. Only the ability to add more Premium features closes. The set of Premium features may change over time; we will not remove a feature from an active subscription without notice.</p>
""",

"t.ai.h": "8. The AI reflection",
"t.ai.b": """
<p>The optional AI reflection is <strong>off until you switch it on</strong>. With <strong>Apple Intelligence</strong> as its writer, text is generated on your device under Apple's terms. With <strong>OpenAI</strong> as its writer, the details listed in the <a href="{BASE}{L}/privacy/#ai">Privacy Policy</a> are sent to our service and on to OpenAI so that a short response can be generated. Earlier versions of the app use Google's Gemini model on Vertex AI for this instead. The journal's {K_reflect_week} uses Apple Intelligence on your device only.</p>
<p>What a language model writes is generated text. It may be wrong, generic or unhelpful, it is <strong>not advice of any kind</strong>, and it is never a statement of fact about your money. Do not type anything into that screen you would not want processed by a third-party model. If a request fails, the app simply shows you the ordinary choices — nothing is queued, retried later or stored. We may limit how many reflections a device can request each day.</p>
""",

"t.licence.h": "9. Licence and intellectual property",
"t.licence.b": """
<p>We grant you a personal, non-exclusive, non-transferable, revocable licence to install and use On Ice on an iPhone or iPad you own or control, in accordance with these Terms and the App Store's usage rules. On Ice, its name, design, artwork, text and code are owned by {COMPANY} and protected by copyright and other laws. You may not copy, modify, distribute, sell, lease, reverse-engineer or create derivative works from the app except where the law expressly allows it.</p>
<p>Names of retailers, apps and websites you choose to shield, or to open as a thing to do instead, belong to their respective owners. On Ice is not affiliated with, endorsed by or sponsored by any of them, and they are governed by their own terms.</p>
""",

"t.use.h": "10. Acceptable use",
"t.use.b": """
<p>You agree not to use On Ice in any way that is unlawful, that interferes with the app, its AI service or Apple's services, that attempts to bypass the App Store's purchase mechanisms or the AI service's limits, or that installs it on a device you are not entitled to manage. You agree not to use it to restrict or monitor another person without their informed consent, and not to submit content through the AI reflection that is unlawful or that you have no right to share.</p>
""",

"t.termination.h": "11. Termination",
"t.termination.b": """
<p>You may stop using On Ice at any time by deleting it. We may suspend or end your licence, or your access to the AI service, if you breach these Terms. Sections 4, 6, 9, 12, 13 and 15 survive termination. Deleting the app does not cancel an active subscription — cancel it in your App Store settings.</p>
""",

"t.warranty.h": "12. Warranties and liability",
"t.warranty.b": """
<p>On Ice is provided “as is” and “as available”, without warranties of any kind, express or implied, including that it will shield any app or website in every circumstance, that it will measure usage exactly, that it will be uninterrupted or error-free, that any figure it displays is accurate, or that it will change your spending. To the fullest extent permitted by law, {COMPANY} shall not be liable for any indirect, incidental, special, consequential or punitive damages, or for any loss of data or money, arising from your use of or inability to use the app — including any purchase you did or did not make, any consequence of a shield that did or did not appear, and any block, limit or strict-mode session you chose to start. Where liability cannot be excluded, it is limited to the amount you paid us for Premium in the twelve months before the claim. Nothing in these Terms limits rights you have as a consumer that cannot be waived.</p>
""",

"t.apple.h": "13. Apple",
"t.apple.b": """
<p>On Ice is distributed through the Apple App Store. These Terms are between you and {COMPANY}, not Apple. Apple has no obligation to provide maintenance or support for the app, and is not responsible for addressing any claim relating to it, including product-liability, legal-compliance or intellectual-property claims. Apple and its subsidiaries are third-party beneficiaries of these Terms and may enforce them against you. Where these Terms are silent, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a> applies. You represent that you are not in a country subject to a U.S. government embargo or listed as a prohibited party, and you must comply with any applicable third-party terms when using the app.</p>
""",

"t.changes.h": "14. Changes to these Terms",
"t.changes.b": """
<p>We may update these Terms from time to time. The date at the top will change when we do, and material changes will be noted in the app's release notes. Continued use after an update means you accept the revised Terms.</p>
""",

"t.law.h": "15. Governing law",
"t.law.b": """
<p>These Terms are governed by the laws of Pakistan, where {COMPANY} operates, without regard to conflict-of-law provisions. Where the law of your country of residence gives you protections that cannot be contracted out of, those protections apply.</p>
""",

"t.contact.h": "16. Contact",
"t.contact.b": """
<p>Questions about these Terms: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Your data",
"d.h1": "Delete your data",
"d.sub": "Everything On Ice knows is on your device. Here is how to remove it, piece by piece or all at once, what happens to your subscription, and why there is nothing on our side to ask for.",
"d.meta": 'See also the <a href="{BASE}{L}/privacy/">Privacy Policy</a>',

"d.where.h": "What is stored where",
"d.where.b": """
<p class="lead">On Ice has no account and keeps no profile of anyone on a server. Everything it holds is on your device, and you can remove it without asking us.</p>
<div class="table-wrap"><table>
<tr><th>Data</th><th>Where it lives</th><th>How to remove it</th></tr>
<tr><td>Your list, decisions, estimated savings history, streaks and patterns</td><td>The app's private storage on your device</td><td>Delete the app. Your history is what the savings total is made of, so it is not erased item by item.</td></tr>
<tr><td>Journal entries</td><td>On your device</td><td>{K_delete_entry} on any entry, or delete the app</td></tr>
<tr><td>Spend log, rules, limits, reminders, activities</td><td>On your device</td><td>Remove each one in the app, or delete the app</td></tr>
<tr><td>Your shops</td><td>Screen Time tokens and website addresses on your device</td><td>Change them in the app; withdrawing Screen Time access in iOS Settings also ends every shield</td></tr>
<tr><td>Widget and Live Activity snapshot</td><td>A small file on your device</td><td>Removed with the app</td></tr>
<tr><td>The weekly write-up</td><td>On your device, only while the AI reflection is on</td><td>Switch the AI reflection off</td></tr>
<tr><td>Premium status</td><td>Your Apple Account (Apple), and a copy of its status on your device</td><td>Managed in your App Store settings — see below</td></tr>
<tr><td>What an OpenAI reflection sent</td><td>Not on our service, which keeps no content. OpenAI may keep it in abuse-monitoring logs, normally for up to 30 days (Google, for earlier versions: up to 24 hours)</td><td>Nothing for you to delete. Switch the AI reflection off and nothing more is sent</td></tr>
<tr><td>A count of AI requests per device</td><td>On Ice's AI service, under a random key identifier</td><td>Deleted automatically after two days</td></tr>
<tr><td>An account, a profile, anything with your name on it</td><td>—</td><td>There is none. We never had one to delete.</td></tr>
</table></div>
""",

"d.inapp.h": "Remove it in the app",
"d.inapp.b": """
<ul>
  <li><strong>Journal entries:</strong> open an entry and tap {K_delete_entry}.</li>
  <li><strong>Spend log:</strong> tap {K_remove} on an entry.</li>
  <li><strong>Rules, limits, reminders and activities:</strong> each has its own delete or remove button.</li>
  <li><strong>Shops:</strong> change your selection, or switch a shop off on the home screen. Turning protection off takes every shield down at once.</li>
  <li><strong>Decided items stay in your history</strong> — that is what your estimated savings and patterns are made of. To remove that history, delete the app.</li>
</ul>
<div class="callout amber"><span class="tile">{lock}</span><div>While <strong>strict mode</strong> is running, your setup is held in place — shops can't be removed, and rules and limits can't be deleted. That is the one commitment you asked the app to keep for you. It ends on its own at the time you chose.</div></div>
""",

"d.journal.h": "Your journal",
"d.journal.b": """
<p>Journal entries live only on your device, and On Ice never sent them anywhere, so there is nothing to remove elsewhere. Delete them one at a time with {K_delete_entry}. To keep a copy before you delete the app, use {K_export_journal}: it makes a plain-text file that you save wherever you choose.</p>
""",

"d.ai.h": "The AI reflection",
"d.ai.b": """
<p>If you switched on the AI reflection, On Ice keeps the latest weekly write-up on your device so you can read it again. Switching the AI reflection off in {K_settings} → {K_ai_reflection} deletes it, removes the Sunday reminder, ends the app's session with the service, and returns On Ice to making no network calls of its own.</p>
<p>The service never held a copy of what you sent. It keeps only a per-device count under a random key, which it deletes after two days, and daily totals that name no device.</p>
""",

"d.uninstall.h": "Delete the app",
"d.uninstall.b": """
<p>Deleting On Ice from your iPhone or iPad removes all of its data with it — your list, history, journal, settings and Screen Time tokens — and ends every shield, block and limit immediately. It is the way to erase everything at once. If the app is included in an iCloud or computer backup, that copy belongs to your Apple Account and is governed by Apple's terms; we have no access to it.</p>
""",

"d.subscription.h": "Your subscription",
"d.subscription.b": """
<p>Deleting the app does not cancel a subscription — it belongs to your Apple Account, not to the app. Cancel it in <a href="https://apps.apple.com/account/subscriptions">App Store subscription settings</a>; it stays active until the end of the current period. Refunds are handled by <a href="https://support.apple.com/billing">Apple Support</a>. A lifetime purchase does not renew and needs nothing cancelled. If you belong to a family plan, the purchaser manages it.</p>
""",

"d.email.h": "Ask us",
"d.email.b": """
<p>If you would like written confirmation that we hold nothing about you, or you believe we do, write to {MAIL} from any address. We will reply within 30 days. Please do not send us your list, your prices, your journal or screenshots of them — we do not need them to answer.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Nothing on ice here.",
"nf.sub": "Which, for once, is not the point.",
"nf.cta": "Back to Support",
"nf.b": 'That page isn\'t here. Try <a href="{BASE}/">Support</a>, the <a href="{BASE}/privacy/">Privacy Policy</a> or the <a href="{BASE}/terms/">Terms of Use</a>.',

}
