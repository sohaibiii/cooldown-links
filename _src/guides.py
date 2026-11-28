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
]
