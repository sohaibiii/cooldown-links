"""The three drawn scenes for the home page's "Three steps. One night."

Pictures, not screens, and each one has to explain itself: one big object and
a few plain words. A shopping bag with a pause button on it; the thing frozen
in the mark's ice cube between tonight's moon and tomorrow's sun; and the two
answers side by side with what each one leads to. Each is an inline SVG on a
400 x 320 canvas (the 5:4 panel in site.css). Colours are the site's tokens
written out, because an SVG attribute cannot read a CSS variable. Green is
only on the realized save; the waiting item is amber.
"""
import math

from i18n import t

SHIRT = "M30 8L13 17L0 38L15 49L24 40V92H76V40L85 49L100 38L87 17L70 8Q50 25 30 8Z"


def stars(pts):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E8ECFB" opacity="{o}"/>' for x, y, r, o in pts)


def moon(x, y, r):
    return (f'<path d="M{x} {y-r}a{r} {r} 0 1 0 {r*0.95:.1f} {r*1.55:.1f}'
            f'a{r*0.82:.1f} {r*0.82:.1f} 0 0 1 -{r*0.95:.1f} -{r*1.55:.1f}z" fill="#E8C170"/>')


def sun(x, y, r):
    rays = ""
    for i in range(8):
        a = math.radians(i * 45)
        rays += (f'<path d="M{x+(r+6)*math.cos(a):.1f} {y+(r+6)*math.sin(a):.1f}'
                 f'L{x+(r+13)*math.cos(a):.1f} {y+(r+13)*math.sin(a):.1f}" '
                 f'stroke="#E8C170" stroke-width="3.4" stroke-linecap="round"/>')
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E8C170"/>{rays}'


def cube(tx, ty, s, inner):
    """The ice cube from the app's mark, with something else frozen inside it."""
    return f'''<g transform="translate({tx} {ty}) scale({s}) translate(-512 -538)">
<polygon points="512,250 786,388 786,688 512,826 238,688 238,388" fill="#C7CFF2" stroke="#C7CFF2" stroke-width="64" stroke-linejoin="round"/>
<polygon points="238,388 512,526 512,826 238,688" fill="#BCC6F0"/>
<polygon points="512,526 786,388 786,688 512,826" fill="#93A1E4"/>
{inner}
<polygon points="238,388 512,526 512,826 238,688" fill="#fff" opacity=".16"/>
<polygon points="512,526 786,388 786,688 512,826" fill="#fff" opacity=".1"/>
<polygon points="512,250 786,388 512,526 238,388" fill="#EEF1FD"/>
<path d="M268 386L506 278" stroke="#fff" stroke-width="16" stroke-linecap="round"/>
<circle cx="300" cy="610" r="10" fill="#fff" opacity=".6"/><circle cx="322" cy="572" r="6" fill="#fff" opacity=".5"/><circle cx="716" cy="500" r="7" fill="#fff" opacity=".45"/>
</g>'''


# 1. Tonight: you go to buy, and On Ice presses pause.
def scene_pause():
    return f'''<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{stars([(40,48,1.6,.7),(96,26,1.2,.5),(60,150,1.3,.5),(322,34,1.4,.6),(364,96,1.5,.6),(344,190,1.2,.45),(30,226,1.2,.45)])}
{moon(350, 44, 13)}
<path d="M152 96V78a34 34 0 0 1 68 0V96" fill="none" stroke="#F3D99A" stroke-width="9" stroke-linecap="round"/>
<path d="M108 92H264L278 226Q279 236 269 236H103Q93 236 94 226Z" fill="#E8C170"/>
<path d="M108 92H264L266 112H106Z" fill="#D9AE55"/>
<circle cx="152" cy="112" r="6" fill="#12152A"/><circle cx="220" cy="112" r="6" fill="#12152A"/>
<circle cx="262" cy="190" r="56" fill="#12152A"/>
<circle cx="262" cy="190" r="48" fill="#7B8CDE"/>
<rect x="243" y="168" width="14" height="44" rx="4.5" fill="#fff"/><rect x="267" y="168" width="14" height="44" rx="4.5" fill="#fff"/>
<rect x="84" y="258" width="232" height="42" rx="21" fill="#12152A" stroke="#E8ECFB" stroke-opacity=".35" stroke-width="1.5"/>
<text x="200" y="285" text-anchor="middle" font-size="17.5" font-weight="600" fill="#F2F4F7">{t("Pause before you buy.")}</text>
</svg>'''


# 2. Still tonight: it goes on ice for 24 hours.
def scene_ice():
    shirt = (f'<g transform="translate(404 560) rotate(-7 108 100) scale(2.16)">'
             f'<path d="{SHIRT}" fill="#E8C170" stroke="#fff" stroke-width="6" stroke-linejoin="round"/></g>')
    return f'''<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{stars([(34,40,1.5,.6),(84,96,1.3,.5),(46,170,1.2,.45),(352,36,1.4,.6),(322,112,1.3,.5),(370,176,1.2,.45)])}
{cube(200, 118, .25, shirt)}
<path d="M92 252H308" stroke="#E8ECFB" stroke-opacity=".5" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="1 9"/>
{moon(52, 250, 15)}
{sun(344, 252, 13)}
<rect x="140" y="232" width="120" height="40" rx="20" fill="#12152A" stroke="#E8C170" stroke-width="2"/>
<text x="200" y="258" text-anchor="middle" font-size="17.5" font-weight="600" fill="#E8C170">{t("24 hours")}</text>
<g font-size="13.5" font-weight="500" fill="#C9CFE6" text-anchor="middle">
  <text x="58" y="300">{t("Tonight")}</text><text x="344" y="300">{t("Tomorrow")}</text>
</g>
</svg>'''


# 3. Tomorrow: two answers, and what each one leads to.
def scene_decide():
    return f'''<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<rect width="200" height="320" fill="#E9F4EC"/><rect x="200" width="200" height="320" fill="#E8ECFB"/>
<path d="M200 0V320" stroke="#FFFDF8" stroke-width="4"/>
<circle cx="200" cy="160" r="20" fill="#FFFDF8"/>
<text x="200" y="165.5" text-anchor="middle" font-size="14" font-weight="600" fill="#565B70">{t("or")}</text>
<g text-anchor="middle" font-weight="600">
  <text x="98" y="50" font-size="16" fill="#22643E">{t("Don't want it anymore")}</text>
  <text x="302" y="50" font-size="16" fill="#35429A">{t("Still want it")}</text>
</g>
<!-- a jar of what you did not spend -->
<g transform="translate(46 84)">
  <rect x="18" y="0" width="68" height="13" rx="5" fill="#2E7D4F"/>
  <path d="M10 20H94Q104 20 104 31V98Q104 112 90 112H14Q0 112 0 98V31Q0 20 10 20Z" fill="#FFFDF8" stroke="#2E7D4F" stroke-width="3.4"/>
  <ellipse cx="52" cy="92" rx="34" ry="9" fill="#7FC98F" stroke="#2E7D4F" stroke-width="2.4"/>
  <ellipse cx="52" cy="80" rx="34" ry="9" fill="#7FC98F" stroke="#2E7D4F" stroke-width="2.4"/>
  <ellipse cx="52" cy="68" rx="34" ry="9" fill="#7FC98F" stroke="#2E7D4F" stroke-width="2.4"/>
  <ellipse cx="52" cy="56" rx="34" ry="9" fill="#A9DDB4" stroke="#2E7D4F" stroke-width="2.4"/>
</g>
<!-- the bag you went for -->
<g transform="translate(254 78)">
  <path d="M30 36V22a18 18 0 0 1 36 0V36" fill="none" stroke="#4352BA" stroke-width="3.4" stroke-linecap="round"/>
  <path d="M6 32H90L84 118H12Z" fill="#FFFDF8" stroke="#4352BA" stroke-width="3.4" stroke-linejoin="round"/>
  <path d="M32 74l11 11 21-24" fill="none" stroke="#4352BA" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round"/>
</g>
<g fill="none" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
  <path d="M98 214V234M91 228l7 7 7-7" stroke="#2E7D4F"/><path d="M302 214V234M295 228l7 7 7-7" stroke="#4352BA"/>
</g>
<g text-anchor="middle" font-size="16" font-weight="600" fill="#171A2B">
  <text x="98" y="266">{t("You keep the money")}</text>
  <text x="302" y="266">{t("The shop opens")}</text>
</g>
</svg>'''
