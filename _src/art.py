"""The three drawn scenes for the home page's "Three steps. One night."

Pictures, not screens: a shop with a pause on its door, the thing frozen in the
mark's ice cube for 24 hours, and the next morning's two answers. Each is an
inline SVG on a 400 x 320 canvas (the 5:4 panel in site.css). Colours are the
site's tokens written out, because an SVG attribute cannot read a CSS variable.
Green is only on the realized save; the waiting item is amber.
"""
import math

STARS = lambda pts: "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E8ECFB" opacity="{o}"/>' for x, y, r, o in pts)

def moon(x, y, r=17):
    return (f'<path d="M{x} {y-r}a{r} {r} 0 1 0 {r*0.95:.1f} {r*1.55:.1f}a{r*0.82:.1f} {r*0.82:.1f} 0 0 1 -{r*0.95:.1f} -{r*1.55:.1f}z" fill="#E8C170"/>')

SHIRT = "M30 8L13 17L0 38L15 49L24 40V92H76V40L85 49L100 38L87 17L70 8Q50 25 30 8Z"

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

# 1. Tonight: a shop, and a pause on its door.
def scene_shop():
    stripes = ""
    x0, w, n = 62, 276, 6
    sw = w / n
    for i in range(n):
        x = x0 + i * sw
        fill = "#E8C170" if i % 2 == 0 else "#F3EEE2"
        stripes += (f'<path d="M{x:.1f} 86H{x+sw:.1f}V120a{sw/2:.1f} 14 0 0 1 -{sw:.1f} 0Z" fill="{fill}"/>')
    return f'''<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{STARS([(36,40,1.6,.7),(92,24,1.2,.5),(150,46,1.4,.6),(236,26,1.3,.5),(292,52,1.5,.6),(378,120,1.3,.5),(22,140,1.2,.45)])}
{moon(346, 40, 14)}
<path d="M30 284H370" stroke="#E8ECFB" stroke-opacity=".3" stroke-width="2" stroke-linecap="round"/>
<rect x="78" y="100" width="244" height="184" rx="6" fill="#2B3266" stroke="#E8ECFB" stroke-opacity=".32" stroke-width="2"/>
<rect x="96" y="150" width="118" height="100" rx="5" fill="#E8C170" opacity=".22"/>
<rect x="96" y="150" width="118" height="100" rx="5" fill="none" stroke="#E8ECFB" stroke-opacity=".6" stroke-width="2"/>
<g transform="translate(108 168) scale(.46)"><path d="{SHIRT}" fill="#E8ECFB"/></g>
<g transform="translate(166 190)" stroke="#E8ECFB" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"><path d="M0 12H34L30 46H4Z" fill="#E8C170" stroke="none"/><path d="M10 12V7a7 7 0 0 1 14 0V12" fill="none" stroke="#E8C170"/></g>
<path d="M96 262H214" stroke="#E8ECFB" stroke-opacity=".35" stroke-width="2" stroke-linecap="round"/>
<rect x="234" y="150" width="70" height="134" rx="5" fill="#E8ECFB" opacity=".12"/>
<rect x="234" y="150" width="70" height="134" rx="5" fill="none" stroke="#E8ECFB" stroke-opacity=".6" stroke-width="2"/>
<rect x="62" y="78" width="276" height="10" rx="3" fill="#E8ECFB" opacity=".9"/>
{stripes}
<circle cx="269" cy="216" r="50" fill="#12152A" opacity=".4"/>
<circle cx="269" cy="212" r="42" fill="#12152A" stroke="#E8C170" stroke-width="4"/>
<rect x="253" y="194" width="11" height="36" rx="3.5" fill="#E8C170"/><rect x="274" y="194" width="11" height="36" rx="3.5" fill="#E8C170"/>
</svg>'''

# 2. Still tonight: the thing goes on ice for 24 hours.
def scene_ice():
    ticks = ""
    for i in range(48):
        a = math.radians(i * 7.5 - 90)
        r1, r2 = (118, 126) if i % 4 else (114, 126)
        ticks += (f'<path d="M{200+r1*math.cos(a):.1f} {166+r1*math.sin(a):.1f}L{200+r2*math.cos(a):.1f} {166+r2*math.sin(a):.1f}" '
                  f'stroke="#E8ECFB" stroke-opacity="{".5" if i % 4 == 0 else ".22"}" stroke-width="2" stroke-linecap="round"/>')
    # an amber arc for the first hours of the wait
    a0, a1 = math.radians(-90), math.radians(-90 + 52)
    arc = (f'<path d="M{200+134*math.cos(a0):.1f} {166+134*math.sin(a0):.1f}A134 134 0 0 1 {200+134*math.cos(a1):.1f} {166+134*math.sin(a1):.1f}" '
           f'fill="none" stroke="#E8C170" stroke-width="5" stroke-linecap="round"/>')
    shirt = f'<g transform="translate(404 560) rotate(-7 108 100) scale(2.16)"><path d="{SHIRT}" fill="#E8C170" stroke="#fff" stroke-width="6" stroke-linejoin="round"/></g>'
    return f'''<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{STARS([(30,60,1.5,.6),(64,250,1.3,.5),(352,40,1.4,.6),(376,212,1.3,.5),(330,286,1.2,.45),(24,170,1.2,.45)])}
<circle cx="200" cy="166" r="134" fill="none" stroke="#E8ECFB" stroke-opacity=".14" stroke-width="5"/>
{arc}
{ticks}
{cube(200, 170, .255, shirt)}
{moon(60, 44, 15)}
<g transform="translate(296 262)"><rect width="74" height="34" rx="17" fill="#12152A" stroke="#E8C170" stroke-width="2"/><text x="37" y="23" text-anchor="middle" class="mono" font-size="16" font-weight="600" fill="#E8C170">24h</text></g>
</svg>'''

# 3. Tomorrow: one question, two good answers.
def scene_decide():
    rays = ""
    for i in range(9):
        a = math.radians(180 + i * 22.5)
        rays += (f'<path d="M{200+62*math.cos(a):.1f} {142+62*math.sin(a):.1f}L{200+78*math.cos(a):.1f} {142+78*math.sin(a):.1f}" '
                 f'stroke="#E8C170" stroke-width="4" stroke-linecap="round"/>')
    return f'''<svg viewBox="0 0 400 320" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<defs><linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFDF8"/><stop offset="1" stop-color="#F6E7C4"/></linearGradient>
<clipPath id="sunclip"><rect x="0" y="0" width="400" height="142"/></clipPath></defs>
<rect width="400" height="142" fill="url(#dawn)"/><rect y="142" width="400" height="178" fill="#FFFDF8"/>
<g clip-path="url(#sunclip)"><circle cx="200" cy="142" r="50" fill="#E8C170"/></g>
{rays}
<path d="M0 142H400" stroke="#171A2B" stroke-opacity=".22" stroke-width="2"/>
<g transform="translate(158 62) scale(.84)"><path d="{SHIRT}" fill="#FFFDF8" stroke="#171A2B" stroke-width="3.8" stroke-linejoin="round"/></g>
<path d="M176 158C140 166 112 176 104 196" fill="none" stroke="#171A2B" stroke-opacity=".6" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="1 8"/>
<path d="M224 158C260 166 288 176 296 196" fill="none" stroke="#171A2B" stroke-opacity=".6" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="1 8"/>
<!-- don't want it: a jar of what you did not spend -->
<g transform="translate(62 190)">
  <rect x="14" y="0" width="56" height="11" rx="4" fill="#2E7D4F"/>
  <path d="M8 17H76Q84 17 84 26V74Q84 86 72 86H12Q0 86 0 74V26Q0 17 8 17Z" fill="#E3F1E7" stroke="#2E7D4F" stroke-width="3"/>
  <ellipse cx="42" cy="70" rx="27" ry="7.5" fill="#7FC98F" stroke="#2E7D4F" stroke-width="2"/>
  <ellipse cx="42" cy="60" rx="27" ry="7.5" fill="#7FC98F" stroke="#2E7D4F" stroke-width="2"/>
  <ellipse cx="42" cy="50" rx="27" ry="7.5" fill="#7FC98F" stroke="#2E7D4F" stroke-width="2"/>
  <ellipse cx="42" cy="40" rx="27" ry="7.5" fill="#A9DDB4" stroke="#2E7D4F" stroke-width="2"/>
</g>
<!-- still want it: the shop opens -->
<g transform="translate(256 186)">
  <path d="M4 26H76L70 90H10Z" fill="#E1E5F9" stroke="#4352BA" stroke-width="3" stroke-linejoin="round"/>
  <path d="M24 32V17a16 16 0 0 1 32 0V32" fill="none" stroke="#4352BA" stroke-width="3" stroke-linecap="round"/>
  <path d="M28 58l9 9 16-18" fill="none" stroke="#4352BA" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>
</g>
<g font-size="15.5" font-weight="600" text-anchor="middle">
  <text x="104" y="303" fill="#22643E">Don\'t want it anymore</text>
  <text x="296" y="303" fill="#4352BA">Still want it</text>
</g>
</svg>'''
