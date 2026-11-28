# -*- coding: utf-8 -*-
"""The guides. One search problem per page.

Each guide gives the free way first (the settings iOS already has), says plainly
where that stops working, and only then says what On Ice does about it. A guide
that is only an advert earns nothing, from readers or from search engines.

`body` is HTML. `{BASE}` is the site root and `{PHONE[image|alt text|caption]}`
places a screenshot from assets/img. Names of iOS settings are written the way
iOS writes them; where Apple renamed one between versions, both names are given.
No long dashes anywhere (site_pages.check fails the build on one).
"""

GUIDES = [
    {
        "slug": "how-to-block-amazon-on-iphone",
        "ct": "block-amazon",
        "topic": "Blocking shops",
        "minutes": 6,
        "title": "How to block Amazon on iPhone (the app and Safari)",
        "seo_title": "How to Block Amazon on iPhone: App and Safari (3 Ways)",
        "description": "Three ways to block Amazon on an iPhone, from a Screen Time limit to a full block of "
                       "amazon.com in Safari, with exact steps and where each one stops working.",
        "blurb": "Three ways, from a soft limit to a full block, and the one tap that undoes most of them.",
        "standfirst": "Amazon lives in two places on your phone: the app, and amazon.com in Safari. Block one and "
                      "the other is still a tap away. Here are three ways to cover both, from lightest to firmest.",
        "box_title": "Put Amazon on ice, not in the bin",
        "box_text": "On Ice shields the Amazon app and amazon.com with the same pause. Note what you wanted, "
                    "wait a night, decide tomorrow. One app and one website are free.",
        "body": """
<p>Before you start, it helps to know what you want the block to do. If you want Amazon gone for good, skip to option 3. If you still need it for the odd real purchase and just want to stop the 1 a.m. orders, options 1 and 2 are closer, and the last section is closer still.</p>

<h2>Option 1: Put a daily time limit on the app</h2>
<p>This uses Screen Time, which is already on your iPhone. It doesn't block Amazon outright. It gives you a daily allowance and then covers the app.</p>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd> first.</li>
  <li>Tap <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>.</li>
  <li>Open the <kbd>Shopping &amp; Food</kbd> category and tick Amazon.</li>
  <li>Scroll to the bottom of the same list, open <kbd>Websites</kbd>, tap <kbd>Add Website</kbd> and type <kbd>amazon.com</kbd>. Now one limit covers the app and the site together.</li>
  <li>Tap <kbd>Next</kbd>, set the time (the smallest is 1 minute a day) and tap <kbd>Add</kbd>.</li>
</ol>
<p><strong>Where it stops working.</strong> When the time runs out, iOS covers the app with a Time Limit screen and a button under it. Tap the button and you are offered one more minute, a 15 minute reminder, or <kbd>Ignore Limit For Today</kbd>. That last one is a single tap, and at 1 a.m. almost everyone taps it.</p>
<p>You can close that door by setting a Screen Time passcode (<kbd>Screen Time</kbd>, then <kbd>Lock Screen Time Settings</kbd>) and switching on <kbd>Block at End of Limit</kbd> for the limit. It only really works if someone else chooses the passcode, because you can't forget a number you picked yourself.</p>

<h2>Option 2: Block amazon.com in Safari completely</h2>
<p>This one is a real block, with no allowance and no ignore button. It only covers the website, so pair it with option 1 or 3 for the app.</p>
<ol>
  <li>Open <kbd>Settings</kbd>, tap <kbd>Screen Time</kbd>, then <kbd>Content &amp; Privacy Restrictions</kbd>, and turn the switch on.</li>
  <li>Tap <kbd>Content Restrictions</kbd>. On newer versions of iOS this row is called <kbd>App Store, Media, Web &amp; Games</kbd>.</li>
  <li>Tap <kbd>Web Content</kbd> and choose <kbd>Limit Adult Websites</kbd>.</li>
  <li>Under <kbd>Never Allow</kbd>, tap <kbd>Add Website</kbd> and enter <kbd>amazon.com</kbd>. If you shop on another country's Amazon, add that address too.</li>
</ol>
<p>Open amazon.com in Safari now and you get a page saying the site is restricted. It applies to other browsers on the phone as well.</p>
<p><strong>Two side effects to know about.</strong> Choosing <kbd>Limit Adult Websites</kbd> also turns on Apple's own adult content filter, and it removes Private Browsing from Safari. Most people don't mind, but it surprises some.</p>

<h2>Option 3: Delete the app and stop it coming back</h2>
<p>Deleting the app takes a second: press and hold the Amazon icon, tap <kbd>Remove App</kbd>, then <kbd>Delete App</kbd>. The trouble is that reinstalling takes about twenty seconds. To stop that:</p>
<ol>
  <li>In <kbd>Settings</kbd>, go to <kbd>Screen Time</kbd>, then <kbd>Content &amp; Privacy Restrictions</kbd>.</li>
  <li>Tap <kbd>iTunes &amp; App Store Purchases</kbd>, then <kbd>Installing Apps</kbd>, and choose <kbd>Don't Allow</kbd>.</li>
</ol>
<p>The App Store icon disappears from your Home Screen until you switch this back. That is the catch: you can't install <em>anything</em> while it is on, including app updates you actually want. Combine it with option 2 and Amazon is properly gone from the phone.</p>

<h2>Which one should you use?</h2>
<table>
  <thead><tr><th>Method</th><th>Covers</th><th>How easy to undo in the moment</th></tr></thead>
  <tbody>
    <tr><td>App limit</td><td>App and website</td><td>One tap, unless someone else holds the passcode</td></tr>
    <tr><td>Never Allow list</td><td>Website only</td><td>About six taps through Settings</td></tr>
    <tr><td>Delete and block installs</td><td>App only</td><td>About six taps, then a reinstall</td></tr>
  </tbody>
</table>
<p>Two smaller things help whichever you pick. Turn off Amazon's notifications (<kbd>Settings</kbd>, <kbd>Notifications</kbd>, Amazon, then switch off <kbd>Allow Notifications</kbd>), because a deal alert is an invitation. And unsubscribe from the marketing emails the next time one arrives.</p>

<h2>If you don't want Amazon gone, just slower</h2>
<p>All three options above treat Amazon as the problem. For most people the problem is narrower: the order placed late, tired, for something that didn't matter by morning. A hard block also blocks the day you need printer ink.</p>
<p>This is the gap we built On Ice for. You pick Amazon in Apple's picker and add amazon.com as a website. From then on, opening either one shows a shield first: <em>Pause before you buy.</em> You tap <kbd>Note it</kbd>, type what you came for and a rough price, and it goes on a list for 24 hours. Tomorrow the app asks once whether you still want it.</p>
{PHONE[decide-later|On Ice's choice screen: Decide later? Wait 24h, then decide, or I need to shop now for 1, 5 or 15 minutes.|If you do need the shop right now, it opens for 1, 5 or 15 minutes and then shields itself again.]}
<p>It is deliberately not a wall. If you need the ink today, <kbd>I need to shop now</kbd> opens the shop for a few minutes. What changes is that the easy path is now "write it down" instead of "buy it", and that turns out to be enough most nights.</p>
<p>The free version covers one app and one website, which is exactly the Amazon app and amazon.com.</p>
""",
    },
    {
        "slug": "how-to-block-shopping-websites-on-iphone",
        "ct": "block-shopping-websites",
        "topic": "Blocking shops",
        "minutes": 5,
        "title": "How to block shopping websites on iPhone",
        "seo_title": "How to Block Shopping Websites on iPhone in Safari",
        "description": "How to block shopping websites in Safari on an iPhone with Screen Time: the Never Allow "
                       "list, website time limits, and a softer option that still lets you buy.",
        "blurb": "The Never Allow list, website time limits, and a softer option for sites you still need.",
        "standfirst": "Deleting a shopping app doesn't do much if the website opens in Safari in two taps. Your "
                      "iPhone can block sites by address. Here is how, and what each method costs you.",
        "box_title": "A pause on the websites that get you",
        "box_text": "Add a shop's website to On Ice and Safari shows a shield before the store: note it, sleep on "
                    "it, decide tomorrow. No bank linking, and it never sees what you buy.",
        "body": """
<p>There are two built in ways to do this, and they behave differently. One is a full block. The other is a daily allowance. Pick by how firm you want to be.</p>

<h2>The full block: the Never Allow list</h2>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>.</li>
  <li>Tap <kbd>Content &amp; Privacy Restrictions</kbd> and turn the switch on.</li>
  <li>Tap <kbd>Content Restrictions</kbd>. On newer versions of iOS the row is called <kbd>App Store, Media, Web &amp; Games</kbd>.</li>
  <li>Tap <kbd>Web Content</kbd>, then choose <kbd>Limit Adult Websites</kbd>.</li>
  <li>Under <kbd>Never Allow</kbd>, tap <kbd>Add Website</kbd> and type the shop's address. Repeat for each shop.</li>
</ol>
<p>From now on those sites show a "restricted" page in Safari and in other browsers on the phone.</p>
<div class="note"><b>Type the address you actually open.</b> Many shops use a different address per country or a separate mobile address. If the site still opens, look at the address bar and add exactly what you see there.</div>
<p><strong>What it costs you.</strong> <kbd>Limit Adult Websites</kbd> switches on Apple's adult content filter and removes Private Browsing from Safari. And because the block is total, the day you really do need that shop you have to go back through Settings and delete the entry, which most people then forget to put back.</p>

<h2>The allowance: a time limit on a website</h2>
<ol>
  <li>In <kbd>Settings</kbd>, tap <kbd>Screen Time</kbd>, then <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>.</li>
  <li>Scroll to the bottom of the list and open <kbd>Websites</kbd>.</li>
  <li>Tap <kbd>Add Website</kbd> and enter the address. You can add several sites to the same limit, and apps too.</li>
  <li>Tap <kbd>Next</kbd>, set a daily time, and tap <kbd>Add</kbd>.</li>
</ol>
<p>When the time is used up, Safari covers the site until midnight.</p>
<p><strong>What it costs you.</strong> Nothing much, and that is the problem. The cover has a button that offers <kbd>Ignore Limit For Today</kbd>. Unless someone else sets a Screen Time passcode for you, the limit is a suggestion.</p>

<h2>Don't use "Allowed Websites" for this</h2>
<p>In the same <kbd>Web Content</kbd> screen there is a third choice, <kbd>Allowed Websites</kbd> (older versions call it <kbd>Allowed Websites Only</kbd>). It blocks the whole internet except a short list. It is designed for a child's device and is far too blunt for an adult trying to stay off three shops.</p>

<h2>A softer option for shops you still need</h2>
<p>Both methods above are built for keeping something out. Neither is built for the more common case: a shop you use for real things, and also use too much when you're bored.</p>
<p>That middle case is what On Ice is for. You add the website's address, and Safari shows a shield before the shop loads. Tap <kbd>Note it</kbd>, say what you wanted and roughly what it costs, and it waits on a list for 24 hours. Nothing is bought, and tomorrow you get asked once if you still want it.</p>
{PHONE[note-it|On Ice's capture screen: What caught your eye? A name, a rough price, and how you are feeling.|Fifteen seconds: a name, a rough price, and how you feel.]}
<p>If you need the shop now, it opens for 1, 5 or 15 minutes and then shields itself again without you doing anything. So the block never becomes the thing you switch off and forget.</p>
<p>A shop's app and its website are two separate things on an iPhone, in On Ice and in Screen Time alike. Whatever method you use, cover both. We wrote up the app side, with Amazon as the example, in <a href="{BASE}/guides/how-to-block-amazon-on-iphone/">how to block Amazon on iPhone</a>.</p>
""",
    },
    {
        "slug": "24-hour-rule-for-shopping",
        "ct": "24-hour-rule",
        "topic": "Habits",
        "minutes": 5,
        "title": "The 24 hour rule for shopping: how to actually use it",
        "seo_title": "The 24 Hour Rule for Shopping: Does It Work? How to Use It",
        "description": "The 24 hour rule means waiting a day before any unplanned purchase. Why it works, how to "
                       "do it with just the Notes app, and where it usually breaks.",
        "blurb": "Why waiting one night works, how to do it with the Notes app, and where it usually breaks.",
        "standfirst": "The rule is one sentence long: if you didn't plan to buy it, wait a day. It is the most "
                      "reliable trick there is for impulse buying, and almost nobody manages to keep it up. "
                      "Both of those things are worth understanding.",
        "box_title": "The 24 hour rule, built into your phone",
        "box_text": "On Ice steps in when you open a shop, takes the note for you, runs the 24 hour clock and asks "
                    "the one question tomorrow. Free to start.",
        "body": """
<h2>Why one night is enough</h2>
<p>A want is strongest in the first minutes after you see the thing. That is not a character flaw. It is how wanting works, and checkout pages are designed around it: saved cards, one tap ordering, a countdown on the deal.</p>
<p>Psychologists have a name for the mismatch, the hot-cold empathy gap. When you are in the "hot" state of wanting, you overestimate how much you'll care tomorrow. When you've cooled off, you can hardly remember why it felt urgent. The 24 hour rule doesn't ask you to resist anything. It only moves the decision to the cool side of that gap.</p>
<p>That is why it works better than willpower. You are not saying no. You are saying "tomorrow".</p>

<h2>How to do it by hand</h2>
<p>You need a notes app and one reminder. That's all.</p>
<ol>
  <li><strong>Write it down before you close the tab.</strong> The item, the price, and one word for how you feel right now: bored, stressed, celebrating, worried the deal will end. The feeling is the useful part. After a few weeks you will see which one does most of your shopping.</li>
  <li><strong>Leave the shop.</strong> Close the tab or the app. Don't leave it in the cart "for later", because the shop will email you about it within the hour.</li>
  <li><strong>Set a reminder for this time tomorrow.</strong> Not a vague "later". The same hour.</li>
  <li><strong>Ask one question.</strong> Tomorrow, read the note and ask: do I still want this? Not "should I", not "can I afford it". Just whether the want is still there.</li>
  <li><strong>Either answer is fine.</strong> If you still want it, buy it and enjoy it. The rule is a filter, not a punishment. If you don't, cross it off and write the price next to it.</li>
</ol>
<p>That last step matters more than it looks. A list of crossed off prices is the only evidence you will ever get that the rule is working, since money you didn't spend is otherwise invisible.</p>

<h2>The three places it breaks</h2>
<h3>1. You forget the rule at exactly the wrong moment</h3>
<p>The rule lives in your head, and the moment you need it is the moment your head is busy wanting something. Nothing prompts you. This is the main reason people who love the idea drift away from it within a couple of weeks.</p>
<h3>2. Writing it down is slower than buying it</h3>
<p>Checkout is one tap. Opening Notes, typing the item, setting a reminder is a minute of fiddling. When the honest option is slower than the impulsive one, the impulsive one wins on tired days.</p>
<h3>3. "The deal ends tonight"</h3>
<p>Sometimes it really does. More often the timer resets, or the same price comes back next month. A useful test: would you buy it at this price if there were no timer? If yes, it was never an impulse buy and the rule doesn't apply. If no, the discount is the only thing you want, and a discount on something you didn't want isn't a saving.</p>

<h2>How long should the wait be?</h2>
<p>24 hours covers most everyday purchases, because most everyday wants are gone by morning. For bigger things, people often stretch it: 48 or 72 hours for something that costs a day's pay, a month for anything that needs a payment plan. The length matters less than the fact that you sleep at least once in between.</p>

<h2>Doing the same thing with On Ice</h2>
<p>We make On Ice, so read this part knowing that. The app exists because of the three breaks above. It is the 24 hour rule with the forgetting taken out.</p>
<p>You choose the shopping apps and websites that get you. When you open one, a shield appears before the shop does, so the prompt arrives at the right moment without you remembering anything. Tap <kbd>Note it</kbd> and the note takes about fifteen seconds: a name, a rough price, a feeling. Then the item waits under a 24 hour ring.</p>
{PHONE[on-ice-countdown|On Ice's countdown ring: 23:59:52 until you decide. It's on your list: a linen shirt.|The item waits. Nothing is bought, and nothing nags you in the meantime.]}
<p>Tomorrow at the same time it asks the one question. If you let the thing go, the price you guessed is added to your estimated savings, which is the crossed off list from step 5, kept for you. With Premium the wait can be 12, 48 or 72 hours instead.</p>
<p>You can keep the rule perfectly well with a notes app. The app is for people who have tried that and found, as we did, that the hard part was never the waiting. It was remembering to start.</p>
""",
    },
    {
        "slug": "how-to-not-overspend-on-black-friday",
        "ct": "sale-season",
        "topic": "Sale season",
        "minutes": 5,
        "title": "How to not overspend on Black Friday and Cyber Monday",
        "seo_title": "How to Not Overspend on Black Friday and Cyber Monday",
        "description": "A short, practical plan for sale season: a list made before the sales start, a price "
                       "ceiling, a quieter phone, and one question to ask at every checkout.",
        "blurb": "A list made before the sales start, a quieter phone, and one question for every checkout.",
        "standfirst": "Sale season is the one week of the year when buying things you don't want feels like being "
                      "sensible. You don't need to sit it out. You need to decide what you want before the shops "
                      "start telling you.",
        "box_title": "Close the shops for the evening",
        "box_text": "On Ice can shield your shopping apps and websites with a pause, or close them for a set time "
                    "with a timed block. Anything you note waits 24 hours. Free to start.",
        "body": """
<h2>Before the sales: make the list first</h2>
<p>The whole plan rests on one move, and it has to happen before the first sale email arrives.</p>
<ol>
  <li><strong>Write down what you already wanted.</strong> Things you were going to buy anyway: the winter coat, the replacement headphones, gifts for named people. If it wasn't on your mind last month, it doesn't go on the list.</li>
  <li><strong>Put a ceiling next to each one.</strong> The most you would pay. Look up the normal price now, while nothing is on sale, so that you can tell a real discount from a "was" price that nobody ever paid.</li>
  <li><strong>Set a total for everything else.</strong> A small amount for things not on the list is realistic. Zero usually isn't, and a rule you break on day one stops being a rule.</li>
</ol>
<p>During the sales, the list is the only question: is this on it, and is it under the ceiling? Everything else is the shop's list, not yours.</p>

<h2>Make your phone quieter for a week</h2>
<p>You will not out-think a hundred notifications. Remove them instead.</p>
<ul>
  <li><strong>Turn off shop notifications.</strong> Open <kbd>Settings</kbd>, tap <kbd>Notifications</kbd>, pick each shopping app and switch off <kbd>Allow Notifications</kbd>. Switch them back in December if you miss them. Most people don't.</li>
  <li><strong>Unsubscribe as the emails arrive.</strong> You don't need a clear out session. Each time a sale email lands, scroll to the bottom and unsubscribe from that one. A week of this ends most of it.</li>
  <li><strong>Move the shopping apps off your first Home Screen.</strong> It sounds trivial. It removes the opens you do without deciding to.</li>
  <li><strong>Pick your shopping hours.</strong> If you are going to browse the sales, do it once, in daylight, with the list open. The expensive orders happen late, on the sofa, after the plan has gone to bed.</li>
</ul>

<h2>At the checkout: one question</h2>
<p>Would I buy this at this price if there were no sale on?</p>
<p>If yes, it's a good deal on something you want. Buy it. If the honest answer is "no, but it's 40% off", then the discount is the only thing you want, and the cheapest way to enjoy a discount is to not pay the other 60%.</p>
<p>Two sale tricks are worth knowing by name:</p>
<ul>
  <li><strong>The countdown.</strong> Timers and "only 3 left" are there to stop you thinking. Sales now run for days and often repeat on Cyber Monday, so very few things are truly gone tomorrow.</li>
  <li><strong>The free shipping gap.</strong> "Add $12 more for free delivery" gets people to spend $12 to save $5. Pay the delivery.</li>
</ul>
<p>If you're unsure about something, the <a href="{BASE}/guides/24-hour-rule-for-shopping/">24 hour rule</a> still works in sale week. Write it down with the price and look again tomorrow. If the deal is gone, you have lost nothing you had planned to buy.</p>

<h2>Afterwards: returns are not a failure</h2>
<p>If something arrives and you feel nothing, send it back. Check the return window on the day it arrives rather than the day it expires, and put the date in your calendar. Returning a thing you don't want is the plan working late, not the plan failing.</p>
<p>And if you bought a few things that weren't on the list, that's a normal sale week. There is nothing to feel bad about. Note which shop and what time of day, because that tells you where to put a boundary next year.</p>

<h2>If you'd like the phone to help</h2>
<p>We make On Ice, an iPhone app for exactly this, so here is how it fits. You choose the shopping apps and websites that get you, and opening one shows a shield first. You can note what you wanted and let it wait 24 hours, or walk away.</p>
<p>For sale week in particular, a timed block is useful: it closes your chosen shops for the next 30 minutes or until a time you set, which covers the late evening well. With Premium you can also set danger hours, so late nights are stricter every day without you starting anything.</p>
{PHONE[protection-tools|On Ice's Protection tools screen: Block now, for 30 minutes, with a Start block button, plus a daily goal and daily limits.|A timed block closes your chosen shops until the time you set.]}
<p>Nothing in it will tell you off for buying something. If you still want the coat tomorrow, the shop opens and you buy the coat.</p>
""",
    },
    {
        "slug": "on-ice-vs-deleting-shopping-apps",
        "ct": "vs-deleting",
        "topic": "Comparisons",
        "minutes": 4,
        "title": "On Ice vs deleting your shopping apps: which works better?",
        "seo_title": "On Ice vs Deleting Your Shopping Apps: Which Works Better?",
        "description": "Deleting shopping apps, Screen Time limits and On Ice compared honestly: what each one "
                       "blocks, how easily each is undone at 1 a.m., and who each one suits.",
        "blurb": "An honest comparison, including the cases where deleting the app is the better choice.",
        "standfirst": "Deleting the app is the advice everyone gives, and it is free. We make an alternative, so "
                      "we have a side in this. Here is the comparison as fairly as we can put it, including "
                      "when you should not use our app.",
        "box_title": "Try the pause for a week",
        "box_text": "One shopping app and one website are free in On Ice, with the 24 hour list and your estimated "
                    "savings. If deleting never stuck for you, this is a different approach.",
        "body": """
<h2>Deleting the app</h2>
<p><strong>What it does well.</strong> It is instant, free and total. If you open a shopping app purely out of habit, like checking the weather, removing the icon removes the habit. For a shop you never truly need, deleting is the right answer and you can stop reading here.</p>
<p><strong>Where it fails.</strong></p>
<ul>
  <li><strong>The website is still there.</strong> Type the first three letters into Safari and you are back in the shop, usually already signed in.</li>
  <li><strong>Reinstalling takes about twenty seconds.</strong> And it tends to happen at the exact moment the block was for.</li>
  <li><strong>You probably do need the shop sometimes.</strong> Then the app comes back for one real order and stays for three months.</li>
  <li><strong>The want has nowhere to go.</strong> Deleting removes the door. It does nothing about the thing you saw, which is still in your head at midnight.</li>
</ul>

<h2>Screen Time limits</h2>
<p><strong>What they do well.</strong> They are built into iOS, cover apps and websites, and need no download. Set up by a partner or friend with a passcode you don't know, they are the firmest option on this page. We explain the steps in <a href="{BASE}/guides/how-to-block-amazon-on-iphone/">how to block Amazon on iPhone</a>.</p>
<p><strong>Where they fail.</strong> Set up by yourself, a limit ends in a button that says <kbd>Ignore Limit For Today</kbd>. It is one tap, there is no pause before it, and it clears the limit for the whole day. Apple designed Screen Time mainly for parents managing a child's device, and it shows.</p>

<h2>On Ice</h2>
<p><strong>What it does differently.</strong> It leaves the shop installed and puts a shield in front of it, on the app and on the website. The shield doesn't offer an "ignore" button. It offers <kbd>Note it</kbd>. You write down the thing and a rough price, and it waits on a list for 24 hours. Tomorrow you are asked once whether you still want it. If you let it go, the price is added to your estimated savings.</p>
{PHONE[still-want-it|On Ice's decision screen: Still want the linen shirt? Don't want it anymore, or Still want it. Either answer is a good one.|The question arrives a day later, when it is easier to answer.]}
<p>If you need the shop right now, you can open it for 1, 5 or 15 minutes and it shields itself again afterwards. So the block never has to be switched off, which is how most blocks quietly end.</p>
<p><strong>Where it fails.</strong></p>
<ul>
  <li><strong>It is a pause, not a wall.</strong> By default you can always get through. There are firmer settings (timed blocks, and daily limits and strict mode with Premium), but if what you want is a lock that you cannot open, a Screen Time passcode held by someone else is stronger.</li>
  <li><strong>iPhone and iPad only.</strong> It needs iOS 17 or newer. It does nothing about shopping on a laptop.</li>
  <li><strong>Free covers one app and one website.</strong> That is enough for one problem shop. Covering several needs Premium.</li>
  <li><strong>It is an app about a habit, not a treatment.</strong> If shopping is causing serious debt or distress, please talk to someone qualified as well. A pause screen is not enough on its own.</li>
</ul>

<h2>Side by side</h2>
<table>
  <thead><tr><th></th><th>Delete the app</th><th>Screen Time limit</th><th>On Ice</th></tr></thead>
  <tbody>
    <tr><td>Covers the website</td><td>No</td><td>Yes, if you add it</td><td>Yes, if you add it</td></tr>
    <tr><td>Undone in the moment by</td><td>A reinstall</td><td>One tap</td><td>Noting the item first</td></tr>
    <tr><td>Lets you shop when you need to</td><td>After reinstalling</td><td>By ignoring the limit</td><td>For 1, 5 or 15 minutes</td></tr>
    <tr><td>Remembers what you wanted</td><td>No</td><td>No</td><td>Yes, for 24 hours</td></tr>
    <tr><td>Shows what you didn't spend</td><td>No</td><td>No</td><td>Yes, as an estimate</td></tr>
    <tr><td>Cost</td><td>Free</td><td>Free</td><td>Free for one app and one site</td></tr>
  </tbody>
</table>

<h2>So which one?</h2>
<p><strong>Delete the app</strong> if you never need that shop and you don't use its website.</p>
<p><strong>Use Screen Time with someone else's passcode</strong> if you want a hard lock and have a person you trust to hold the key.</p>
<p><strong>Use On Ice</strong> if you have deleted and reinstalled the same app more than once. That pattern means the shop isn't the problem. The speed is. What you need is not a missing icon but a night between seeing and buying.</p>
""",
    },
    {
        "slug": "how-to-block-temu-on-iphone",
        "ct": "block-temu",
        "topic": "Blocking shops",
        "minutes": 6,
        "updated": "28 November 2026",
        "updated_iso": "2026-11-28",
        "title": "How to block Temu on iPhone (the app, the website and the alerts)",
        "seo_title": "How to Block Temu on iPhone: App, Website and Alerts",
        "description": "How to block the Temu app and temu.com on an iPhone with Screen Time, quiet its "
                       "notifications and emails, and what a block can't do about Temu adverts.",
        "blurb": "The app, temu.com, the notifications and the emails, plus what no block can do about the adverts.",
        "standfirst": "Blocking Temu on an iPhone means covering four things, not one: the app, the website, the "
                      "notifications and the emails. Miss one and the shop is still a tap away. Here they are in order.",
        "box_title": "Put Temu on ice",
        "box_text": "On Ice shields the Temu app and temu.com with the same pause. Note what caught your eye, "
                    "wait a night, decide tomorrow. One app and one website are free.",
        "body": """
<p>Like most shopping apps, Temu gives you plenty of reasons to open it: coupons with a timer, daily deals, delivery updates. That is why deleting the app on its own rarely lasts. The website still opens in Safari, and the messages keep arriving. Work through the four steps below and each of those doors is closed.</p>

<h2>1. Block the Temu app</h2>
<p>You have two built in choices. A daily limit keeps the app but covers it once your time is used. Deleting it and blocking installs removes it properly.</p>
<h3>A daily limit</h3>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>. If it has never been set up, turn on <kbd>App &amp; Website Activity</kbd> first.</li>
  <li>Tap <kbd>App Limits</kbd>, then <kbd>Add Limit</kbd>.</li>
  <li>Open the <kbd>Shopping &amp; Food</kbd> category and tick Temu.</li>
  <li>Tap <kbd>Next</kbd>, set the time (the smallest is 1 minute a day) and tap <kbd>Add</kbd>.</li>
</ol>
<p><strong>Where it stops working.</strong> When the time runs out, iOS covers the app, and under the cover is a button that leads to <kbd>Ignore Limit For Today</kbd>. One tap and the limit is gone until midnight. You can close that door with a Screen Time passcode (<kbd>Screen Time</kbd>, then <kbd>Lock Screen Time Settings</kbd>) and <kbd>Block at End of Limit</kbd> switched on for the limit, but it only holds if someone else knows the passcode and you don't.</p>
<h3>Delete it and stop it coming back</h3>
<ol>
  <li>Press and hold the Temu icon, tap <kbd>Remove App</kbd>, then <kbd>Delete App</kbd>.</li>
  <li>In <kbd>Settings</kbd>, go to <kbd>Screen Time</kbd>, then <kbd>Content &amp; Privacy Restrictions</kbd>, and turn the switch on.</li>
  <li>Tap <kbd>iTunes &amp; App Store Purchases</kbd>, then <kbd>Installing Apps</kbd>, and choose <kbd>Don't Allow</kbd>.</li>
</ol>
<p>The catch is that the App Store disappears from your Home Screen while this is on, so you can't install or update anything else either.</p>
<div class="note"><b>Deleting the app doesn't close your account.</b> Your Temu account, saved card and order history stay where they are. If you want those gone too, close the account from the account settings inside Temu before you delete the app.</div>

<h2>2. Block temu.com in Safari</h2>
<p>This is the step most people skip, and it is the one that matters. Without it, typing three letters into Safari puts you back in the shop.</p>
<ol>
  <li>Open <kbd>Settings</kbd>, tap <kbd>Screen Time</kbd>, then <kbd>Content &amp; Privacy Restrictions</kbd>, and turn the switch on.</li>
  <li>Tap <kbd>Content Restrictions</kbd>. On newer versions of iOS this row is called <kbd>App Store, Media, Web &amp; Games</kbd>.</li>
  <li>Tap <kbd>Web Content</kbd> and choose <kbd>Limit Adult Websites</kbd>.</li>
  <li>Under <kbd>Never Allow</kbd>, tap <kbd>Add Website</kbd> and enter <kbd>temu.com</kbd>.</li>
</ol>
<p>Open temu.com now and Safari shows a page saying the site is restricted. The same goes for other browsers on the phone. If your Temu opens on a different address, add the one you see in the address bar.</p>
<p><strong>Two side effects.</strong> <kbd>Limit Adult Websites</kbd> also switches on Apple's adult content filter, and it removes Private Browsing from Safari. We go through the alternatives in <a href="{BASE}/guides/how-to-block-shopping-websites-on-iphone/">how to block shopping websites on iPhone</a>.</p>

<h2>3. Turn off the notifications</h2>
<p>If you are keeping the app, this is the quickest win on the page. Open <kbd>Settings</kbd>, tap <kbd>Notifications</kbd>, choose Temu and switch off <kbd>Allow Notifications</kbd>. A coupon that expires tonight is an invitation, and you can't accept one you never saw.</p>

<h2>4. Stop the emails and texts</h2>
<p>You don't need a clear out. The next time a Temu email arrives, scroll to the bottom and unsubscribe from that one. For marketing texts, replying STOP ends them in the US and many other countries. A few days of this and the inbox goes quiet.</p>

<h2>What a block can't do: the adverts</h2>
<p>A lot of people searching for this are really asking about Temu's adverts on other websites, in games and on social apps. It is worth being straight about that: blocking temu.com stops you opening the shop, but it does not remove the adverts. They are placed by advertising networks, and no iPhone setting hides one advertiser.</p>
<p>Two things turn them down a little:</p>
<ul>
  <li>In <kbd>Settings</kbd>, open <kbd>Privacy &amp; Security</kbd>, then <kbd>Tracking</kbd>, and switch off <kbd>Allow Apps to Request to Track</kbd>. It makes it harder for adverts to follow you from one app to the next.</li>
  <li>On most social apps you can open the menu on an advert and choose to hide adverts from that advertiser.</li>
</ul>
<p>The useful part is what happens when you tap one anyway. With steps 1 and 2 done, the advert lands on a blocked page, not a checkout.</p>

<h2>If you'd rather slow Temu down than shut it out</h2>
<p>We make On Ice, so read this part knowing that. Everything above treats Temu as something to keep out. Some people want exactly that. Others still use it for real things and simply order too often, usually late and usually for a few dollars at a time.</p>
<p>Small prices are what makes a pause useful here. A $6 thing never feels like a decision, so it never gets one. On Ice gives it one. You pick Temu in Apple's picker and add temu.com as a website, and from then on opening either shows a shield first. Tap <kbd>Note it</kbd>, type what caught your eye and a rough price, and it waits on a list for 24 hours.</p>
{PHONE[choose-shops|Setup step 3 of 5: Your shops. Choose an app, a website, or both.|You choose the app in Apple's picker and add the website by its address.]}
<p>Tomorrow the app asks once whether you still want it. If you do, the shop opens. If you let it go, the price you guessed is added to your estimated savings.</p>
<p>The free version covers one app and one website, which is exactly the Temu app and temu.com.</p>
""",
    },
    {
        "slug": "how-to-stop-impulse-buying",
        "ct": "stop-impulse-buying",
        "topic": "Habits",
        "minutes": 6,
        "updated": "28 November 2026",
        "updated_iso": "2026-11-28",
        "title": "How to stop impulse buying online: 8 things that work",
        "seo_title": "How to Stop Impulse Buying Online: 8 Things That Work",
        "description": "Eight practical ways to stop impulse buying online, from removing your saved card to "
                       "the 24 hour rule, with what each one costs you and when to use it.",
        "blurb": "Eight ways to put something between seeing and buying, from a two minute fix to a real system.",
        "standfirst": "Impulse buying is rarely about the thing. It is about speed. You see it, you want it, and "
                      "the shop has made sure nothing stands between the two. Everything that works does the same "
                      "job: it puts something in between.",
        "box_title": "One night between you and the buy button",
        "box_text": "On Ice shields the shops you choose, takes a fifteen second note of what you wanted, and asks "
                    "again tomorrow. Free for one app and one website.",
        "body": """
<p>None of these ask for more self control. Self control is what you run out of at 11 p.m., which is when it is needed. They are ordered from the quickest to set up to the most complete, and you don't need all eight. Two or three that suit you will do more than the full list done badly.</p>

<h2>1. Take your card out of the shop</h2>
<p>A saved card turns buying into one tap. Remove it from the shops you overuse, in each shop's account or payment settings. Then remove it from Safari: open <kbd>Settings</kbd>, find <kbd>Safari</kbd> (on newer versions of iOS it sits under <kbd>Apps</kbd>), tap <kbd>AutoFill</kbd>, then <kbd>Saved Credit Cards</kbd>.</p>
<p>Typing sixteen digits is a small job. It is also the only pause most checkouts have left, and it is often enough.</p>

<h2>2. Switch off one tap ordering</h2>
<p>Many shops have an express checkout that skips the basket and the review page. Where the shop lets you turn it off, do. An order that has to go through the basket gives you one more screen on which to change your mind.</p>

<h2>3. Silence the invitations</h2>
<p>Most impulse buys start with the shop contacting you, not the other way round. Open <kbd>Settings</kbd>, tap <kbd>Notifications</kbd>, pick each shopping app and switch off <kbd>Allow Notifications</kbd>. Unsubscribe from marketing emails as they arrive, one at a time. Within a week your phone asks you to buy things far less often.</p>

<h2>4. Wait one night</h2>
<p>If you didn't plan to buy it, wait a day. Wants are strongest in the first minutes and most are gone by morning, so this one rule filters out a great deal. It has well known weak spots, and we cover them, with a way to do it by hand, in <a href="{BASE}/guides/24-hour-rule-for-shopping/">the 24 hour rule for shopping</a>.</p>

<h2>5. Shop from a list you wrote earlier</h2>
<p>When you do need to buy things, write down what before you open the shop. Inside the shop, the list is the only question: is this on it? Everything else you see there is the shop's list, not yours.</p>

<h2>6. Learn your hour and your feeling</h2>
<p>For two weeks, each time you buy something unplanned, note the time and one word for how you felt. A pattern shows up quickly, and it is usually narrow: the same hour, the same mood, often the same shop. A narrow problem needs a narrow fix. If yours is the evening, see <a href="{BASE}/guides/how-to-stop-late-night-online-shopping/">how to stop late night online shopping</a>. If it is a mood, see <a href="{BASE}/guides/how-to-stop-emotional-spending/">how to stop emotional spending</a>.</p>

<h2>7. Give the want somewhere to go</h2>
<p>A want that has nowhere to go sits in your head until you buy the thing to make it stop. Give it a place: one note on your phone with the item and a rough price. Not the shop's own wish list or basket, because the shop will email you about those within the hour. Writing it down is very often all the want needed.</p>

<h2>8. Put a pause on the door</h2>
<p>The first seven change what happens inside the shop or inside your head. The last one changes what happens when you open the shop at all.</p>
<p>Your iPhone can do a version of this with Screen Time: a daily limit on an app or a full block on a website. The steps are in <a href="{BASE}/guides/how-to-block-amazon-on-iphone/">how to block Amazon on iPhone</a> and they are the same for any shop. The weakness is the <kbd>Ignore Limit For Today</kbd> button, which is one tap with no pause before it.</p>

<h2>What usually doesn't work</h2>
<ul>
  <li><strong>Deciding to be stronger.</strong> It works on the days you didn't need it.</li>
  <li><strong>Deleting the app for the fourth time.</strong> If it keeps coming back, the app isn't the problem. We compare the options in <a href="{BASE}/guides/on-ice-vs-deleting-shopping-apps/">On Ice vs deleting your shopping apps</a>.</li>
  <li><strong>Feeling bad afterwards.</strong> Guilt arrives after the order and changes nothing about the next one. A slower checkout does more than a sterner conscience.</li>
</ul>

<h2>If it feels bigger than a habit</h2>
<p>Everything here is for the ordinary kind of buying too much. If shopping is causing debt you can't keep up with, or real distress, please talk to someone qualified as well, such as your doctor or a free debt advice service in your country. A list of tips is not a substitute for that.</p>

<h2>Where On Ice fits</h2>
<p>We make On Ice, an iPhone app, so here is how it lines up with the list. It is numbers 4, 6, 7 and 8 done for you. You choose the shopping apps and websites that get you, and opening one shows a shield before the shop. Tap <kbd>Note it</kbd> and in about fifteen seconds you have written the item, a rough price and how you feel. Then it waits 24 hours.</p>
{PHONE[still-want-it|On Ice's decision screen: Still want the linen shirt? Don't want it anymore, or Still want it. Either answer is a good one.|A day later the app asks once. Either answer is fine.]}
<p>If you still want it tomorrow, the shop opens and you buy it. If you let it go, the price you guessed is added to your estimated savings. And if you need the shop right now, <kbd>I need to shop now</kbd> opens it for 1, 5 or 15 minutes, so the pause never has to be switched off.</p>
<p>You can do every item on this page without an app. On Ice is for people who tried, and found that the hard part was remembering to start.</p>
""",
    },
    {
        "slug": "no-spend-challenge-rules",
        "ct": "no-spend",
        "topic": "Challenges",
        "minutes": 6,
        "updated": "28 November 2026",
        "updated_iso": "2026-11-28",
        "title": "No spend challenge: rules that last past the first week",
        "seo_title": "No Spend Challenge Rules: How to Do a No Buy Month",
        "description": "How to set up a no spend challenge or a no buy month: the rules to write down first, the "
                       "exceptions to allow, what to do with wants, and how to finish.",
        "blurb": "The rules to write before day one, the exceptions worth allowing, and where the wants go meanwhile.",
        "standfirst": "A no spend challenge is easy to describe: for a set time, you buy only what you need. A lot "
                      "of them fade out somewhere in the second week, and often for the same reason. The "
                      "rules were never written down.",
        "box_title": "A list that fills itself",
        "box_text": "On Ice shows a pause when you open a shop and keeps what you wanted on a list. What you let "
                    "go adds up as estimated savings. Free for one app and one website.",
        "body": """
<h2>Choose a length you will finish</h2>
<p>The well known versions are a no spend weekend, a no spend week, a no spend month (January is the popular one) and a no buy year. They are the same idea at different sizes.</p>
<p>If you have never done one, start with a week. A week you finish teaches you more than a month you drop on day nine, and you can go straight into a second one. The longer versions work best as a <em>low buy</em>, which we come to below.</p>

<h2>Write three lists before day one</h2>
<p>This is the whole method. It takes ten minutes, and it has to happen before you start, while you are calm and nothing is in your basket.</p>
<ol>
  <li><strong>Always fine.</strong> Rent or mortgage, bills, groceries, transport, medicine, and replacing something you rely on if it breaks. Nobody's challenge should include skipping a prescription.</li>
  <li><strong>Not this time.</strong> The things you are pausing. Be specific to you: clothes, gadgets, home things, takeaway coffee, delivery food, in app purchases. A short honest list beats a long heroic one.</li>
  <li><strong>Decided in advance.</strong> A birthday present for a named person, a trip already booked, one dinner out. Write them down with a rough cost.</li>
</ol>
<p>The third list is the one people leave out, and it is the one that saves the challenge. An exception you chose in advance is part of the plan. An exception invented at the checkout is how the plan ends.</p>

<h2>Decide where the wants go</h2>
<p>You will still want things. A no spend month doesn't switch wanting off. It postpones buying. So the wants need somewhere to wait.</p>
<p>Keep one list for the whole challenge: the item and a rough price, each time something catches your eye. Don't use a shop's basket or wish list for this, because the shop will remind you about it all month.</p>
<p>The list does two jobs. During the challenge, writing a thing down is usually enough to let you close the tab. At the end, it tells you what the challenge was worth.</p>

<h2>Make your phone match the rules</h2>
<p>A rule in your head is up against a phone that is asking you to buy things all day. Even the odds.</p>
<ul>
  <li><strong>Turn off shop notifications.</strong> <kbd>Settings</kbd>, <kbd>Notifications</kbd>, each shopping app, <kbd>Allow Notifications</kbd> off.</li>
  <li><strong>Unsubscribe as the emails arrive.</strong> One at a time, for the first week. Sale emails are hard on any challenge, and January has a lot of them.</li>
  <li><strong>Move shopping apps off your first Home Screen</strong>, or put a limit on them. The steps are in <a href="{BASE}/guides/how-to-block-amazon-on-iphone/">how to block Amazon on iPhone</a> and work for any shop.</li>
  <li><strong>Block the websites you open from habit.</strong> See <a href="{BASE}/guides/how-to-block-shopping-websites-on-iphone/">how to block shopping websites on iPhone</a>.</li>
</ul>

<h2>The low buy version</h2>
<p>All or nothing doesn't suit everyone, and it rarely suits a whole year. A low buy keeps the three lists and adds one allowance: a small fixed amount, or a set number of unplanned purchases, per month. Three, say. When they are used, they are used.</p>
<p>It sounds like a loophole. In practice it makes each purchase a choice between this thing and the next thing, which is most of what the challenge is trying to teach.</p>

<h2>When you buy something anyway</h2>
<p>It will probably happen once. It is one purchase. It is not the end of the challenge, and it says nothing about you.</p>
<p>Write down what it was and what time of day, then carry on the next morning as if the streak had never been the point. It wasn't. The point is to see your own habits clearly for a few weeks, and the purchase you didn't plan is the most useful thing you will see.</p>

<h2>On the last day</h2>
<ol>
  <li><strong>Read the wants list.</strong> Cross off everything you no longer care about. That is usually a good part of it.</li>
  <li><strong>Add up the prices you crossed off.</strong> That number is an estimate of what the challenge kept in your account. It is the only way to see money you didn't spend.</li>
  <li><strong>Buy what is left, if you still want it.</strong> Things that survived a month on a list are things you want. Enjoy them.</li>
  <li><strong>Keep one rule.</strong> Not the whole challenge. The one change that was easy and made a difference, such as no shop notifications, or a night's wait before anything unplanned. The <a href="{BASE}/guides/24-hour-rule-for-shopping/">24 hour rule</a> is the usual choice.</li>
</ol>

<h2>Doing it with On Ice</h2>
<p>We make On Ice, so here is how it fits, and where it doesn't. It has no challenge mode and no streaks, and we won't pretend otherwise. What it does is supply the two things a challenge most often lacks: a prompt at the moment you open a shop, and a wants list you don't have to remember to keep.</p>
<p>You choose your shopping apps and websites. Opening one shows a shield first. Tap <kbd>Note it</kbd>, give the thing a name and a rough price, and it goes on your list. A day later the app asks whether you still want it. Each thing you let go is added to your estimated savings, so on the last day the number from step 2 is already there.</p>
{PHONE[estimated-savings|The Savings screen: saved this month, about $180 estimated, from 2 items you let go.|What you let go adds up. It is an estimate, built from the prices you guessed.]}
<p>For the hard evenings there are timed blocks, which close your chosen shops for 30 minutes or until a time you set. With Premium, daily limits and strict mode make the rules firmer.</p>
<p>If you still want something tomorrow and it is on your "decided in advance" list, the shop opens and you buy it. That is the challenge working, not failing.</p>
""",
    },
    {
        "slug": "how-to-stop-late-night-online-shopping",
        "ct": "late-night",
        "topic": "Habits",
        "minutes": 5,
        "updated": "28 November 2026",
        "updated_iso": "2026-11-28",
        "title": "How to stop late night online shopping",
        "seo_title": "How to Stop Late Night Online Shopping on Your Phone",
        "description": "How to stop shopping on your phone late at night: an iPhone Downtime schedule, a quieter "
                       "evening, a charger outside the bedroom, and a softer option.",
        "blurb": "A Downtime schedule, a quieter evening phone, and a softer option for nights you still need a shop.",
        "standfirst": "The order you wonder about in the morning was usually placed late, in bed, with one thumb. "
                      "There is no mystery in it. You were tired, the phone was there, and the shop never closes. "
                      "So close it yourself.",
        "box_title": "Close the shops for the night",
        "box_text": "On Ice puts a pause in front of the shops you choose, and a timed block closes them until "
                    "a time you set. Anything you note waits 24 hours. Free to start.",
        "body": """
<h2>Why night is different</h2>
<p>Three things line up after dark. You are tired, and a tired mind takes the easy option, which a shop has made sure is "buy". You are alone, with nobody to ask whether you need it. And the phone is the last thing in your hand before sleep.</p>
<p>Meanwhile the shop is wide awake. Offers often end at midnight, and a lot of marketing email lands in the evening. You are not weak at night. Night is simply when selling is easiest.</p>
<p>That is good news, because a problem with a fixed hour is much easier to fix than a problem with you.</p>

<h2>Close the shops on a schedule with Downtime</h2>
<p>Downtime is part of Screen Time on every iPhone. Between the hours you set, only the apps you allow stay open.</p>
<ol>
  <li>Open <kbd>Settings</kbd> and tap <kbd>Screen Time</kbd>, then <kbd>Downtime</kbd>.</li>
  <li>Turn on <kbd>Scheduled</kbd> and set the hours, for example from 10 p.m. to 7 a.m. You can choose different hours for different days.</li>
  <li>Go back one screen and tap <kbd>Always Allowed</kbd>. Keep what you need at night, such as Phone, Messages, Clock and a reading or music app. Leave shopping apps off the list.</li>
</ol>
<p>During those hours the other app icons are dimmed. Safari is an app like any other, so if you leave it off the allowed list the shop websites are covered too. If you want Safari at night, block the shop sites separately: see <a href="{BASE}/guides/how-to-block-shopping-websites-on-iphone/">how to block shopping websites on iPhone</a>.</p>
<p><strong>Where it stops working.</strong> Tap a dimmed app and iOS offers a way round: a button that leads to <kbd>Ignore Limit For Today</kbd>. To remove it you need a Screen Time passcode with <kbd>Block at Downtime</kbd> switched on, and that only holds if someone else keeps the passcode. Downtime is also blunt. It closes everything you forgot to allow, and the first night that gets in your way is usually the night it gets switched off.</p>

<h2>Make the evening phone quieter</h2>
<ul>
  <li><strong>Turn off shop notifications.</strong> <kbd>Settings</kbd>, <kbd>Notifications</kbd>, each shopping app, <kbd>Allow Notifications</kbd> off. This matters most in the evening, when the "ends tonight" messages are sent.</li>
  <li><strong>Use a Sleep Focus.</strong> In <kbd>Settings</kbd>, tap <kbd>Focus</kbd>, then <kbd>Sleep</kbd>, and give it a schedule. It doesn't block any app, but it holds notifications back until morning. A deal alert you read at 8 a.m. is a lot less persuasive than one you read at 11 p.m.</li>
  <li><strong>Sign out of the shops you overuse.</strong> Having to find a password at midnight is a surprisingly good block.</li>
</ul>

<h2>Move the phone, not only the apps</h2>
<p>The simplest fix on this page costs nothing. Charge the phone somewhere you can't reach from bed: across the room, or outside the bedroom. If the phone is your alarm, a basic alarm clock replaces it. Put a book where the phone used to be.</p>
<p>You can still get up and fetch it. Almost nobody does, for a pair of trainers.</p>

<h2>Let the want wait until morning</h2>
<p>If something does catch your eye late, don't argue with it. Write it down: the item and the price. Then close the tab. Don't leave it in the basket, because the shop will email you about it before breakfast.</p>
<p>In the morning, read the note. If you still want it in daylight, buy it. That is the <a href="{BASE}/guides/24-hour-rule-for-shopping/">24 hour rule</a>, and night is where it earns its keep.</p>

<h2>The softer option: On Ice</h2>
<p>We make On Ice, so take this as our side of it. Downtime treats the whole phone as the problem. For most people the problem is two or three shops, at one time of day.</p>
<p>With On Ice you choose those shops, as apps and as websites. Open one at any hour and a shield appears first, with a slow breath before the choices if you want it. Tap <kbd>Note it</kbd>, type what you wanted and a rough price, and it waits on your list. The app asks about it a day later, when you are awake.</p>
{PHONE[breathe|The breathing pause: A moment before you choose.|A slow breath first. You can skip it whenever you prefer.]}
<p>For the nights you already know are risky, start a timed block. It closes your chosen shops for the next 30 minutes or until a time you set, and there is no way through until it ends. With Premium, danger hours make late nights stricter every night without you starting anything.</p>
<p>Outside a block, the shield is a pause and not a wall. If you need the shop at 11 p.m. for something real, <kbd>I need to shop now</kbd> opens it for 1, 5 or 15 minutes.</p>
""",
    },
    {
        "slug": "how-to-stop-emotional-spending",
        "ct": "emotional-spending",
        "topic": "Habits",
        "minutes": 5,
        "updated": "28 November 2026",
        "updated_iso": "2026-11-28",
        "title": "How to stop emotional spending: boredom, stress and the rest",
        "seo_title": "How to Stop Emotional Spending: Boredom, Stress and More",
        "description": "Emotional spending is buying to change how you feel. How to spot which feeling does your "
                       "shopping, what to do in its place, and when to simply buy the thing.",
        "blurb": "Find out which feeling does your shopping, then give that feeling something else to do.",
        "standfirst": "Emotional spending is buying something to change how you feel, not because you need the "
                      "thing. Everybody does it sometimes, and sometimes it is fine. It becomes a problem when one "
                      "feeling has learned that the answer is always a shop.",
        "box_title": "Notice the feeling before the checkout",
        "box_text": "When On Ice pauses a shop, the note asks what you wanted and how you feel. After a few weeks "
                    "you can see which feeling does your shopping. Free to start.",
        "body": """
<h2>The five feelings that shop</h2>
<p>You don't need a theory for this. You need to know which of these is yours, because the fix is different for each.</p>
<ul>
  <li><strong>Bored.</strong> Browsing is something to do with your hands. The parcel is a small event in a flat week. This one is often the easiest to change.</li>
  <li><strong>Stressed or worn out.</strong> After a hard day, choosing something nice feels like getting a bit of control back.</li>
  <li><strong>Low.</strong> This is what people mean by retail therapy. Buying something does lift your mood for a while. It just doesn't last as long as the delivery takes.</li>
  <li><strong>Celebrating.</strong> You earned it. Often you did, and this one is frequently fine.</li>
  <li><strong>Afraid of missing out.</strong> The timer, the last three in stock, the thing everyone else has.</li>
</ul>

<h2>Find yours in two weeks</h2>
<p>Guessing doesn't work well here, because the feeling is hard to see from inside it. Measure it.</p>
<p>For two weeks, each time you buy something you hadn't planned, or nearly do, write down three things: what it was, the time, and one word for how you felt just before. One word, chosen quickly. Don't judge it and don't try to change anything yet.</p>
<p>At the end, count the words. You will probably find that one feeling accounts for most of the list, often at the same time of day. That is the one to work on. The others you can leave alone.</p>

<h2>Give the feeling something else</h2>
<p>A feeling that shops is doing a job for you. Telling it to stop doesn't work. Giving it a different way to do the job does.</p>
<table>
  <thead><tr><th>If you feel</th><th>What the shop was giving you</th><th>Try first</th></tr></thead>
  <tbody>
    <tr><td>Bored</td><td>Something to do</td><td>Ten minutes of anything with your hands or feet: a walk, the washing up, a call</td></tr>
    <tr><td>Stressed</td><td>A sense of control</td><td>One small thing you can finish, or two minutes of slow breathing</td></tr>
    <tr><td>Low</td><td>A lift</td><td>A person. Message someone before you open the shop</td></tr>
    <tr><td>Celebrating</td><td>A reward</td><td>Choose the reward on purpose, tomorrow, and enjoy it</td></tr>
    <tr><td>Missing out</td><td>Relief from the timer</td><td>Ask whether you would buy it at this price with no timer</td></tr>
  </tbody>
</table>
<p>Keep the replacement small and close to hand. "Go to the gym" loses to a checkout every time. "Walk to the end of the road" sometimes wins.</p>

<h2>Wait for the feeling to pass, not the want</h2>
<p>Feelings move faster than wants. Boredom lasts an hour. A bad day ends. If you put a night between the feeling and the purchase, you get to decide in a different mood from the one that picked the thing.</p>
<p>So write it down, with the price, and look again tomorrow. That is the <a href="{BASE}/guides/24-hour-rule-for-shopping/">24 hour rule</a>, and emotional spending is what it is best at. If you still want it when the feeling has gone, it was never the feeling. Buy it.</p>

<h2>Sometimes the answer is yes</h2>
<p>A treat after a hard week is not a failure of anything. The aim here is not to stop buying things that make you happy. It is to notice when one feeling has started spending for you without asking, and to give yourself the choice back. Nothing on this page works by making you feel bad, and guilt after a purchase has never yet prevented the next one.</p>

<h2>When to talk to someone</h2>
<p>If shopping is how you cope with feelings that don't lift, or it is causing debt or arguments you can't get on top of, please talk to someone qualified, such as your doctor or a counsellor. That is a different thing from a habit, and it deserves better help than an article.</p>

<h2>How On Ice helps with this</h2>
<p>We make On Ice, an iPhone app, so here is our part in it. The two week exercise above is the thing the app does on its own. When you open a shop you've chosen, a shield appears first. Tap <kbd>Note it</kbd> and the note asks for a name, a rough price and how you are feeling. That takes about fifteen seconds, and it happens at the one moment the feeling is easy to name.</p>
<p>From there you can also go and do something else: a walk, a few pages, two minutes of breathing. Pick the small things you would enjoy, and one tap starts them.</p>
{PHONE[do-something-else|The Instead screen: Make room for something else. Walk 10 minutes, Read 10 minutes, Breathe 2 minutes.|Something small to do with the feeling, one tap from the shield.]}
<p>The thing you noted waits 24 hours, and the app asks about it once, when the mood has had time to change. With Premium you can also see your shopping patterns over time, including how purchases felt afterwards.</p>
<p>It never tells you off. If you still want the thing tomorrow, the shop opens.</p>
""",
    },
]
