"""The animated demo in the home page's hero: one loop of On Ice at work.

It is HTML and CSS only: no video, no script. A drawn iPhone plays the real
flow in the app's own words: open a shop, meet the shield, note the thing,
choose to wait, a day passes, answer once, see the estimated saving.

Everything runs off ONE clock. Every animated element has the same duration
(`T` seconds) and loops forever, so the scenes, the tap dot, the typing and
the captions cannot drift apart. `SCENES` and `TAPS` below are the timeline;
the keyframes are generated from them, so to retime the demo change a number
here and rebuild. Sizes are plain pixels for a 276 x 582 screen; smaller
viewports scale the whole phone (see `.demo` in `css()`).

Rules this keeps: money always says "estimated", green is only on the
realized save, nothing shames a purchase, and the shop's name is written as a
word under a drawn icon (never another company's logo). With "reduce motion"
on, nothing moves and the shield is shown as a still.
"""

T = 23.0  # seconds for one loop

# name, start, end (seconds). A scene fades in over the one before it.
SCENES = [
    ("home", 0.0, 2.7),
    ("shop", 2.7, 6.9),      # the shield arrives inside it, at SHIELD_AT
    ("note", 6.9, 11.1),
    ("later", 11.1, 13.7),
    ("ice", 13.7, 17.1),
    ("ask", 17.1, 20.1),
    ("saved", 20.1, T),
]
SHIELD_AT = 3.8

# when, x, y (pixels on the 276 x 582 screen): where the finger lands.
TAPS = [
    (1.8, 107, 174),    # the Amazon icon
    (6.3, 84, 360),     # Note it
    (9.5, 166, 231),    # the price chip
    (10.6, 138, 532),   # Next
    (13.1, 138, 422),   # Wait 24h, then decide
    (19.5, 138, 466),   # Don't want it anymore
]

CAPTIONS = [
    (0.0, SHIELD_AT, "You open a shopping app"),
    (SHIELD_AT, 6.9, "On Ice steps in first"),
    (6.9, 11.1, "You note what you wanted"),
    (11.1, 13.7, "You choose to wait"),
    (13.7, 17.1, "24 hours pass. Nothing is bought."),
    (17.1, 20.1, "Tomorrow, On Ice asks once"),
    (20.1, T, "You let it go and keep the money"),
]

TYPED = "Linen shirt"
TYPE_FROM, TYPE_TO = 7.5, 9.0

FADE = 0.35


def pct(t):
    t = min(max(t, 0.0), T)
    return f"{t / T * 100:.2f}".rstrip("0").rstrip(".") + "%"


def frames(name, stops):
    """@keyframes from [(seconds, 'css'), ...]; stops at the same percent keep the last."""
    seen = {}
    for t, css_text in stops:
        seen[pct(t)] = css_text
    body = "".join(f"{p}{{{c}}}" for p, c in sorted(seen.items(), key=lambda kv: float(kv[0][:-1])))
    return f"@keyframes {name}{{{body}}}"


def window(name, start, end, on="opacity:1", off="opacity:0", fade=FADE, linger=FADE):
    """Off, then on from `start` to `end`, then off. Held, not tweened, outside the fades."""
    stops = []
    if start > 0:
        stops += [(0, off), (start, off), (start + fade, on)]
    else:
        stops += [(0, on)]
    if end >= T:
        stops += [(T, on)]
    else:
        stops += [(end + linger, on), (end + linger + 0.01, off), (T, off)]
    return frames(name, stops)


def switch(name, at, before, after):
    """`before` until `at`, then `after` to the end of the loop."""
    return frames(name, [(0, before), (at, before), (at + 0.01, after), (T, after)])


SHIRT = "M30 8L13 17L0 38L15 49L24 40V92H76V40L85 49L100 38L87 17L70 8Q50 25 30 8Z"

# A drawn Home Screen. The shop keeps its name as a word; the icon is ours.
APPS = [("Mail", "#3E7BD6"), ("Photos", "#E9A23B"), ("Maps", "#58B37A"), ("Notes", "#E5C558"),
        ("Music", "#D95B6A"), ("Amazon", "#1B2330"), ("Clock", "#2A2F3A"), ("Weather", "#5AA7DE"),
        ("Books", "#E08A3C"), ("Health", "#F2F2F4"), ("Files", "#4B8FE0"), ("Camera", "#8A8F99")]

CART = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h2.4l2.1 9.2h9.4L19 8H7.2" fill="none" '
        'stroke="#F2A93B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
        '<circle cx="9.4" cy="18" r="1.5" fill="#F2A93B"/><circle cx="16" cy="18" r="1.5" fill="#F2A93B"/></svg>')


def html(base):
    icons = "".join(
        f'<span class="ic{" shop-ic" if n == "Amazon" else ""}"><i style="background:{c}">'
        f'{CART if n == "Amazon" else ""}</i><em>{n}</em></span>' for n, c in APPS)
    typed = "".join(f'<i class="l{i}">{"&nbsp;" if ch == " " else ch}</i>' for i, ch in enumerate(TYPED))
    caps = "".join(f'<span class="c{i}">{text}</span>' for i, (_, _, text) in enumerate(CAPTIONS))
    label = ("An animated drawing of On Ice at work. Someone opens Amazon on an iPhone. On Ice covers it with a "
             "shield: Pause before you buy. They tap Note it, type Linen shirt at about 50 dollars, and tap "
             "Wait 24h, then decide. A day passes and nothing is bought. Then On Ice asks once: Still want the "
             "linen shirt? They tap Don't want it anymore, and about 50 dollars joins their estimated savings.")
    return f"""<div class="hero-art demo">
  <input type="checkbox" id="demo-pause" class="demo-pause">
  <div class="phone dphone" role="img" aria-label="{label}"><div class="dscreen" aria-hidden="true">

    <div class="sc s-home">
      <div class="grid">{icons}</div>
      <div class="dock"><i style="background:#58B37A"></i><i style="background:#3E7BD6"></i><i style="background:#E9E9EC"></i><i style="background:#D95B6A"></i></div>
    </div>

    <div class="sc s-shop">
      <div class="shop-top"><b>Amazon</b><span></span></div>
      <div class="shop-pic"><svg viewBox="0 0 100 100" aria-hidden="true"><path d="{SHIRT}" fill="#F7F3EA" stroke="#B9AD96" stroke-width="2.5" stroke-linejoin="round"/></svg></div>
      <div class="shop-txt"><b>Linen shirt</b><span>In stock</span></div>
      <div class="shop-buy">Buy now</div>
      <div class="shop-row"><i></i><i></i><i></i></div>
      <div class="dim"></div>
      <div class="shield-in"><div class="shield">
        <span class="tag">In a shop you chose</span>
        <img src="{base}/mark.svg" alt="" width="44" height="44">
        <b>Pause before you buy.</b>
        <p>Want something here? Note it in On Ice and decide later.</p>
        <div class="btns"><span>Note it</span><span>Never mind</span></div>
      </div></div>
    </div>

    <div class="sc app s-note">
      <span class="round">×</span>
      <div class="ttl">What caught your eye?</div>
      <div class="card note-card">
        <small>Name</small>
        <div class="field"><span class="typed">{typed}</span><u></u></div>
        <small>Roughly what does it cost? <q>Optional</q></small>
        <div class="chips four"><span>≈ $10</span><span>≈ $25</span><span class="pick">≈ $50</span><span>≈ $100</span></div>
        <small>How are you feeling? <q>Optional</q></small>
        <div class="chips"><span>Bored</span><span>Stressed</span><span>Deal FOMO</span></div>
      </div>
      <div class="btn main" style="bottom:30px">Next</div>
    </div>

    <div class="sc app s-later">
      <span class="round">‹</span>
      <div class="ttl">Decide later?</div>
      <div class="card later-card">
        <b>A linen shirt</b>
        <p class="est">≈ $50 <q>estimated</q></p>
        <dl>
          <dt>Right now</dt><dd>Nothing is bought. Your note goes on the list.</dd>
          <dt>Tomorrow</dt><dd>On Ice asks once: still want it?</dd>
          <dt>If you let it go</dt><dd>≈ $50 joins your estimated savings.</dd>
        </dl>
      </div>
      <div class="btn main" style="bottom:140px">Wait 24h, then decide</div>
      <p class="now">I need to shop now</p>
      <div class="chips mins"><span>1 minute</span><span>5 minutes</span><span>15 minutes</span></div>
      <p class="nvm">Never mind</p>
    </div>

    <div class="sc app s-ice">
      <div class="ring">
        <svg viewBox="0 0 180 180" aria-hidden="true"><circle cx="90" cy="90" r="80" fill="#0C1626" stroke="rgba(232,193,112,.2)" stroke-width="8"/><circle class="arc" cx="90" cy="90" r="80" fill="none" stroke="#E8C170" stroke-width="8" stroke-linecap="round" transform="rotate(-90 90 90)" stroke-dasharray="503" stroke-dashoffset="0"/></svg>
        <div class="clock"><b class="k0">23:59:52</b><b class="k1">16:00:00</b><b class="k2">08:00:00</b><b class="k3">00:00:00</b></div>
        <span>until you decide</span>
      </div>
      <div class="ttl big">It's on your list</div>
      <p class="sub">A linen shirt</p>
      <div class="card ice-card"><b>Tomorrow at 9:41 PM</b><p>On Ice asks once: still want it? If you do, the shop opens for you.</p></div>
      <div class="btn main" style="bottom:30px">Done</div>
    </div>

    <div class="sc app s-ask">
      <span class="pill">Later</span>
      <div class="ttl left">Still want the linen shirt?</div>
      <p class="left sub">You noted it yesterday · ≈ $50 estimated</p>
      <div class="btn go" style="bottom:96px">Don't want it anymore</div>
      <div class="btn main" style="bottom:48px">Still want it</div>
      <p class="either">Either answer is a good one.</p>
    </div>

    <div class="sc s-saved">
      <div class="ttl left">Savings</div>
      <div class="seg"><span>Today</span><span>Week</span><span class="on">Month</span></div>
      <div class="card saved-card">
        <small>Saved this month</small>
        <p class="sum"><b>≈ $50</b> <q>estimated</q></p>
        <p>From 1 item you let go this month. Your own estimate, nothing is tracked.</p>
      </div>
      <div class="card let-go"><i>✓</i><div><b>Linen shirt</b><span>Let go today · ≈ $50 estimated</span></div></div>
    </div>

    <div class="sbar"><b>9:41</b><i></i></div>
    <div class="tap"></div>
  </div></div>
  <p class="dcap" aria-hidden="true">{caps}</p>
  <label class="demo-ctl" for="demo-pause"><span class="p1">Pause the demo</span><span class="p2">Play the demo</span></label>
</div>"""


def css():
    k = []
    names = [n for n, _, _ in SCENES]
    for i, (name, start, end) in enumerate(SCENES):
        if name == "home":
            # the last scene fades out over it, so it has to be back before the loop ends
            k.append(frames("d-home", [(0, "opacity:1"), (end + FADE, "opacity:1"), (end + FADE + 0.01, "opacity:0"),
                                       (T - 0.6, "opacity:0"), (T - 0.59, "opacity:1"), (T, "opacity:1")]))
        elif i == len(SCENES) - 1:
            k.append(frames(f"d-{name}", [(0, "opacity:0"), (start, "opacity:0"), (start + FADE, "opacity:1"),
                                          (T - 0.45, "opacity:1"), (T, "opacity:0")]))
        else:
            on = "opacity:1;transform:none"
            off = "opacity:0;transform:translateY(14px)" if name != "shop" else "opacity:0;transform:scale(.6)"
            k.append(frames(f"d-{name}", [(0, off), (start, off), (start + FADE, on), (end + FADE, on),
                                          (end + FADE + 0.01, "opacity:0;transform:none"), (T, "opacity:0;transform:none")]))
    shop_end = dict((n, e) for n, _, e in SCENES)["shop"]
    k.append(window("d-dim", SHIELD_AT, shop_end))
    k.append(frames("d-shield", [(0, "opacity:0;transform:translateY(26px) scale(.94)"),
                                 (SHIELD_AT, "opacity:0;transform:translateY(26px) scale(.94)"),
                                 (SHIELD_AT + 0.4, "opacity:1;transform:none"), (shop_end + FADE, "opacity:1;transform:none"),
                                 (shop_end + FADE + 0.01, "opacity:0;transform:none"), (T, "opacity:0;transform:none")]))
    # the finger
    stops = []
    first = TAPS[0]
    stops.append((0, f"opacity:0;transform:translate({first[1]}px,{first[2]}px) scale(1)"))
    for i, (t, x, y) in enumerate(TAPS):
        at = f"transform:translate({x}px,{y}px)"
        stops += [(t - 0.6, f"opacity:0;{at} scale(1.25)"), (t - 0.3, f"opacity:.9;{at} scale(1)"),
                  (t, f"opacity:.9;{at} scale(.7)"), (t + 0.18, f"opacity:.45;{at} scale(1.2)"),
                  (t + 0.36, f"opacity:0;{at} scale(1.6)")]
        if i + 1 < len(TAPS):
            nx = TAPS[i + 1]
            stops.append((t + 0.37, f"opacity:0;transform:translate({nx[1]}px,{nx[2]}px) scale(1.25)"))
    stops.append((T, f"opacity:0;transform:translate({first[1]}px,{first[2]}px) scale(1)"))
    k.append(frames("d-tap", stops))
    # the icon answers the first tap
    t0 = TAPS[0][0]
    k.append(frames("d-icon", [(0, "transform:none"), (t0 - 0.05, "transform:none"), (t0 + 0.1, "transform:scale(.88)"),
                               (t0 + 0.3, "transform:none"), (T, "transform:none")]))
    # typing, one letter at a time
    step = (TYPE_TO - TYPE_FROM) / len(TYPED)
    letters = []
    for i in range(len(TYPED)):
        k.append(switch(f"d-l{i}", TYPE_FROM + i * step, "max-width:0", "max-width:1em"))
        letters.append(f".demo .typed .l{i}{{animation-name:d-l{i}}}")
    k.append(switch("d-pick", TAPS[2][0], "background:transparent;color:#C9D2DF", "background:#7B8CDE;color:#0F1214"))
    # a day goes by on the ring
    ice_start = dict((n, s) for n, s, _ in SCENES)["ice"]
    a, b = ice_start + 0.9, ice_start + 2.7
    k.append(frames("d-arc", [(0, "stroke-dashoffset:0"), (a, "stroke-dashoffset:0"), (b, "stroke-dashoffset:503"),
                              (T - 0.5, "stroke-dashoffset:503"), (T - 0.49, "stroke-dashoffset:0"), (T, "stroke-dashoffset:0")]))
    third = (b - a) / 3
    marks = [0, a + third * 0.5, a + third * 1.5, a + third * 2.5, T]
    for i in range(4):
        lo, hi = marks[i], marks[i + 1]
        st = [(0, "opacity:0")] if lo > 0 else [(0, "opacity:1")]
        if lo > 0:
            st += [(lo, "opacity:0"), (lo + 0.01, "opacity:1")]
        if hi < T:
            st += [(hi, "opacity:1"), (hi + 0.01, "opacity:0"), (T, "opacity:0")]
        else:
            st += [(T, "opacity:1")]
        k.append(frames(f"d-k{i}", st))
    saved_start = dict((n, s) for n, s, _ in SCENES)["saved"]
    k.append(frames("d-sum", [(0, "transform:scale(.8)"), (saved_start + 0.2, "transform:scale(.8)"),
                              (saved_start + 0.6, "transform:scale(1.06)"), (saved_start + 0.8, "transform:none"),
                              (T, "transform:none")]))
    caps = []
    for i, (start, end, _) in enumerate(CAPTIONS):
        k.append(window(f"d-c{i}", start, end, fade=0.25, linger=0))
        caps.append(f".demo .dcap .c{i}{{animation-name:d-c{i}}}")
    scene_rules = "".join(f".demo .s-{n}{{animation-name:d-{n}}}" for n in names)
    clock_rules = "".join(f".demo .clock .k{i}{{animation-name:d-k{i}}}" for i in range(4))

    return f"""
/* hero demo: one loop of the app, drawn in HTML. Timeline lives in _src/demo.py. */
.hero-art.demo{{height:auto;overflow:visible;padding:0 0 clamp(28px,5vw,56px);width:auto;display:grid;justify-items:center;align-self:center;position:relative}}
.demo .dphone{{width:290px;height:596px;border-radius:46px;flex:none}}
.demo .dscreen{{position:relative;width:276px;height:582px;overflow:hidden;border-radius:39px;background:#0b0e1a;font-family:var(--sans);color:#F2F4F7;line-height:1.3;text-align:left}}
.demo .dscreen *,.demo .dcap span{{animation-duration:{T:g}s;animation-iteration-count:infinite;animation-timing-function:ease-in-out;animation-fill-mode:both}}
.demo .sc{{position:absolute;inset:0;opacity:0}}
{scene_rules}
.demo .sbar{{position:absolute;left:0;right:0;top:0;height:40px;display:flex;justify-content:space-between;align-items:center;padding:6px 26px 0;font:600 13px/1 var(--sans);color:#fff}}
.demo .sbar i{{width:22px;height:10px;border-radius:3px;border:1.5px solid #fff;position:relative}}
.demo .sbar i::after{{content:"";position:absolute;inset:1.5px;right:5px;background:#fff;border-radius:1px}}
.demo .tap{{position:absolute;left:-19px;top:-19px;width:38px;height:38px;border-radius:50%;background:rgba(255,255,255,.55);box-shadow:0 0 0 2px rgba(255,255,255,.9),0 4px 14px rgba(0,0,0,.35);opacity:0;animation-name:d-tap}}

.demo .s-home{{background:radial-gradient(120% 80% at 80% 0%,#3a4580 0%,#1D2347 45%,#12152A 100%)}}
.demo .grid{{position:absolute;left:20px;right:20px;top:64px;display:grid;grid-template-columns:repeat(4,50px);justify-content:space-between;row-gap:20px}}
.demo .ic{{display:grid;justify-items:center;gap:5px}}
.demo .ic i{{width:50px;height:50px;border-radius:13px;display:grid;place-items:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.25)}}
.demo .ic i svg{{width:30px;height:30px}}
.demo .ic em{{font:500 10px/1 var(--sans);color:#E8ECFB;font-style:normal}}
.demo .shop-ic i{{animation-name:d-icon}}
.demo .dock{{position:absolute;left:14px;right:14px;bottom:16px;height:74px;border-radius:26px;background:rgba(255,255,255,.14);display:flex;justify-content:space-between;align-items:center;padding:0 14px}}
.demo .dock i{{width:50px;height:50px;border-radius:13px}}

.demo .s-shop{{background:#F4F1EA;color:#171A2B;transform-origin:107px 175px}}
.demo .shop-top{{height:84px;background:#1B2330;color:#fff;padding:44px 14px 0;display:flex;align-items:center;gap:10px}}
.demo .shop-top b{{font:700 15px/1 var(--sans)}}
.demo .shop-top span{{flex:1;height:26px;border-radius:8px;background:#fff}}
.demo .shop-pic{{margin:14px 14px 0;height:190px;border-radius:14px;background:#E3DAC8;display:grid;place-items:center}}
.demo .shop-pic svg{{width:120px;height:120px}}
.demo .shop-txt{{padding:12px 16px 0}}
.demo .shop-txt b{{display:block;font:700 17px/1.2 var(--sans)}}
.demo .shop-txt span{{font-size:12.5px;color:#4d7a56}}
.demo .shop-buy{{margin:12px 14px 0;background:#F2A93B;color:#2a1d02;border-radius:999px;font:700 15px/1 var(--sans);text-align:center;padding:13px}}
.demo .shop-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:16px 14px 0}}
.demo .shop-row i{{height:96px;border-radius:12px;background:#D9D2C3}}
.demo .dim{{position:absolute;inset:0;background:rgba(12,14,24,.62);opacity:0;animation-name:d-dim}}
.demo .shield-in{{position:absolute;left:14px;right:14px;top:188px;opacity:0;animation-name:d-shield}}
.demo .shield-in .shield{{text-align:center}}

.demo .app{{background:linear-gradient(180deg,#0E1626 0%,#16304A 55%,#1E4A60 100%)}}
.demo .ttl{{margin:0;position:absolute;left:14px;right:14px;top:84px;text-align:center;font:700 19px/1.2 var(--sans);letter-spacing:-.01em;color:#fff}}
.demo .ttl.left,.demo p.left{{text-align:left;left:16px;right:16px}}
.demo .round{{position:absolute;left:14px;top:46px;width:26px;height:26px;border-radius:50%;background:rgba(255,255,255,.12);display:grid;place-items:center;font:500 16px/1 var(--sans);color:#D9E0EC}}
.demo .card{{position:absolute;left:14px;right:14px;border-radius:16px;background:rgba(255,255,255,.07);box-shadow:inset 0 0 0 1px rgba(255,255,255,.14);padding:12px}}
.demo .card small{{display:block;font:600 11px/1 var(--sans);color:#E3E8F1;margin:0 0 7px}}
.demo q{{quotes:none;font:500 9.5px/1 var(--sans);color:#A9B4C4;background:rgba(255,255,255,.1);border-radius:999px;padding:2px 6px;margin-left:3px}}
.demo .btn{{position:absolute;left:14px;right:14px;height:40px;border-radius:12px;display:grid;place-items:center;font:600 14px/1 var(--sans);color:#0F1214}}
.demo .btn.main{{background:linear-gradient(180deg,#8E9CE6,#7B8CDE)}}
.demo .btn.go{{background:linear-gradient(180deg,#93D6A1,#7FC98F)}}
.demo .chips{{display:flex;flex-wrap:wrap;gap:6px}}
.demo .chips span{{font:500 11px/1 var(--sans);color:#C9D2DF;padding:7px 9px;border-radius:999px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.18)}}

.demo .note-card{{top:122px}}
.demo .field{{height:34px;border-radius:10px;background:rgba(255,255,255,.08);box-shadow:inset 0 0 0 1px rgba(255,255,255,.16);display:flex;align-items:center;padding:0 11px;font:600 13.5px/1 var(--sans);margin-bottom:13px}}
.demo .typed i{{display:inline-block;overflow:hidden;max-width:0;font-style:normal;vertical-align:bottom;white-space:pre}}
{"".join(letters)}
.demo .field u{{width:1.5px;height:17px;background:#7B8CDE;margin-left:1px}}
.demo .chips.four{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-radius:999px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.18);margin-bottom:13px}}
.demo .chips.four span{{box-shadow:none;text-align:center;padding:8px 0}}
.demo .chips.four .pick{{animation-name:d-pick}}

.demo .later-card{{top:120px}}
.demo .later-card>b{{font:700 15px/1.2 var(--sans)}}
.demo .est{{margin:3px 0 10px;font:600 12.5px/1.2 var(--sans);padding-bottom:10px;border-bottom:1px solid rgba(255,255,255,.14)}}
.demo dl{{margin:0}}
.demo dt{{font:700 12px/1.2 var(--sans);margin-top:8px}}
.demo dt:first-child{{margin-top:0}}
.demo dd{{margin:2px 0 0;font-size:10.5px;line-height:1.35;color:#B9C3D2}}
.demo .now{{position:absolute;left:0;right:0;bottom:114px;margin:0;text-align:center;font-size:10.5px;color:#C9D2DF}}
.demo .mins{{position:absolute;left:0;right:0;bottom:78px;justify-content:center}}
.demo .mins span{{color:#8FA0E8;background:rgba(123,140,222,.14);box-shadow:none}}
.demo .nvm{{position:absolute;left:0;right:0;bottom:44px;margin:0;text-align:center;font-size:12.5px;color:#C9D2DF}}

.demo .ring{{position:absolute;left:50%;top:52px;width:170px;height:170px;margin-left:-85px;display:grid;place-items:center}}
.demo .ring svg{{position:absolute;inset:0;width:100%;height:100%}}
.demo .arc{{animation-name:d-arc;animation-timing-function:linear}}
.demo .clock{{position:relative;width:100%;height:30px;margin-top:-6px}}
.demo .clock b{{position:absolute;inset:0;text-align:center;font:700 27px/30px var(--sans);letter-spacing:.01em;font-variant-numeric:tabular-nums;opacity:0}}
{clock_rules}
.demo .ring span{{position:absolute;left:0;right:0;top:106px;text-align:center;font-size:10px;color:#C9D2DF}}
.demo .ttl.big{{top:240px;font-size:22px}}
.demo .sub{{position:absolute;left:14px;right:14px;top:272px;margin:0;text-align:center;font-size:13px;color:#D9E0EC}}
.demo .ice-card{{top:306px}}
.demo .ice-card b{{font:700 12.5px/1.2 var(--sans)}}
.demo .ice-card p{{margin:3px 0 0;font-size:10.5px;line-height:1.35;color:#B9C3D2}}

.demo .pill{{position:absolute;left:14px;top:46px;font:500 11.5px/1 var(--sans);color:#D9E0EC;background:rgba(255,255,255,.12);border-radius:999px;padding:8px 11px}}
.demo .s-ask .ttl{{top:96px;font-size:22px}}
.demo .s-ask .sub{{top:156px;font-size:12px;color:#C9D2DF}}
.demo .either{{position:absolute;left:0;right:0;bottom:22px;margin:0;text-align:center;font-size:10px;color:#C9D2DF}}

.demo .s-saved{{background:#111418}}
.demo .s-saved .ttl{{top:62px;font-size:22px}}
.demo .seg{{position:absolute;left:14px;right:14px;top:100px;display:grid;grid-template-columns:repeat(3,1fr);border-radius:9px;background:rgba(255,255,255,.08);padding:2px;font:500 10.5px/1 var(--sans);text-align:center}}
.demo .seg span{{padding:6px 0;border-radius:7px;color:#C9D2DF}}
.demo .seg .on{{background:rgba(255,255,255,.2);color:#fff}}
.demo .saved-card{{top:140px;background:#1A1F26}}
.demo .saved-card small{{font-weight:500;color:#A9B4C4}}
.demo .sum{{margin:8px 0;transform-origin:0 60%;animation-name:d-sum}}
.demo .sum b{{font:700 34px/1 var(--sans);color:#7FC98F;letter-spacing:-.01em}}
.demo .saved-card p:last-child{{margin:0;font-size:10.5px;line-height:1.4;color:#A9B4C4}}
.demo .let-go{{top:282px;background:#1A1F26;display:flex;gap:10px;align-items:center}}
.demo .let-go i{{width:28px;height:28px;border-radius:50%;background:rgba(127,201,143,.18);color:#7FC98F;display:grid;place-items:center;font:700 14px/1 var(--sans);font-style:normal;flex:none}}
.demo .let-go b{{display:block;font:700 12.5px/1.2 var(--sans)}}
.demo .let-go span{{font-size:10.5px;color:#A9B4C4}}

.demo .dcap{{position:relative;width:290px;height:24px;margin:18px 0 0;text-align:center;font:500 15.5px/24px var(--sans);color:var(--ice)}}
.demo .dcap span{{position:absolute;inset:0;opacity:0;white-space:nowrap}}
{"".join(caps)}
.demo-pause{{position:absolute;opacity:0;width:1px;height:1px}}
.demo-ctl{{margin-top:8px;font:500 12.5px/1 var(--sans);color:var(--ice-2);cursor:pointer;padding:6px 10px;border-radius:999px;text-decoration:underline;text-underline-offset:3px}}
.demo-ctl .p2{{display:none}}
.demo-pause:checked~.demo-ctl .p1{{display:none}}
.demo-pause:checked~.demo-ctl .p2{{display:inline}}
.demo-pause:focus-visible~.demo-ctl{{outline:2px solid var(--amber);outline-offset:2px}}
.demo-pause:checked~.dphone *,.demo-pause:checked~.dcap span{{animation-play-state:paused}}
{"".join(k)}
@media (max-width:860px){{
  .hero-art.demo{{display:grid;padding-bottom:36px}}
  .hero-copy{{padding-bottom:28px}}
}}
@media (max-width:380px){{
  .demo .dphone{{transform:scale(.9);transform-origin:top center;margin-bottom:-60px}}
}}
@media (prefers-reduced-motion:reduce){{
  .demo .dscreen *,.demo .dcap span{{animation:none!important}}
  .demo .s-shop,.demo .dim,.demo .shield-in,.demo .dcap .c1{{opacity:1}}
  .demo-ctl{{display:none}}
}}
"""
