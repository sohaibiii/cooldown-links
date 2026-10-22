# cooldown-links

The pages On Ice's App Store listing points at, hosted with GitHub Pages at
https://sohaibiii.github.io/cooldown-links/

The repository keeps the codebase's name, Cooldown, because shipped builds of the app link to
this URL. Everything a reader sees says **On Ice**, the app's public name; `_src/check.py` fails
if "Cooldown" reaches any page.

| Page | URL | App Store Connect field |
|---|---|---|
| Support | `/` | Support URL |
| About | `/about/` | Marketing URL |
| Privacy Policy | `/privacy/` | Privacy Policy URL |
| Terms of Use (EULA) | `/terms/` | EULA / linked from the paywall |
| Your data | `/delete-data/` | — (linked from Privacy) |

The app links to `/#faq` and `/privacy/`; both anchors, and `/privacy/#ai`, `/terms/#subscriptions`
and `/about/#pricing`, must keep their names.

## Languages

Every page exists in the **eight languages On Ice ships in**, and a row of tabs under the navigation
switches between them without leaving the page you are on. English lives at the root and each other
language under its own code, spelled exactly as the app's `AppLanguage` spells it, so `/de/privacy/`
is the German privacy policy:

`en` · `/de` · `/es` · `/fr` · `/ja` · `/ko` · `/pt-BR` · `/zh-Hans`

The App Store fields above should still point at the **English** URLs. Apple shows the listing in
the reader's own language, and the tabs let them carry that through to these pages.

Each page declares `hreflang` alternates for all eight plus `x-default`, and `sitemap.xml` repeats
them, so a search engine treats eight translations of the privacy policy as one page in eight
languages.

Wording that names a screen in the app — <kbd>Settings</kbd> → <kbd>AI reflection</kbd>,
<kbd>Restore purchases</kbd>, <kbd>Export journal</kbd> — is a `k.*` key, copied from the app's own
catalogue (`Cooldown/Resources/Localizable.xcstrings`), and iOS's own labels (Screen Time, Apps with
Screen Time Access) are copied from the app's strings that quote them. A page never tells somebody
to tap a button whose label is written differently on their screen.

## Editing

`_src/gen.py` owns the markup; `_src/words/<lang>.py` owns the words. English is the fallback behind
all seven others, so a key that has not been translated yet renders as English, never as an
identifier — the same rule the app follows.

```
python3 _src/check.py     # the eight catalogues agree
python3 _src/gen.py       # rewrite every page
```

Run **both**, and commit the regenerated HTML alongside the source. `check.py` is the half no reader
of that language can proofread for us: it holds every catalogue to the same key set, the same
`{placeholders}`, the same link targets and balanced tags, renders every value once, and rejects the
old name. `check.py de fr` checks just those languages.

To add a language: add it to `LANGUAGES` and `NATIVE_NAME` in `_src/gen.py`, add
`_src/words/<code>.py` (underscores for a hyphen: `pt_BR.py`), translate, then run the two commands
above. Keep the list and its order in step with `AppLanguage` in the app.

The colours, radii and type are On Ice's own tokens (`Cooldown/Core/DesignSystem/DesignTokens.swift`
in the app repo): night-sky hero, dusk indigo, savings green kept for realised saves only, cooling
amber for items still on ice. The mark (`mark.svg`, and inside `favicon.svg`) is the app's "frozen
want" — `BrandMark.svg` from the app's asset catalogue, copied verbatim into `MARK` in `gen.py`;
`apple-touch-icon.png` is the app icon at 180 px. If the app's mark changes, copy it again here.

Once App Store Connect has assigned the app its Apple ID, set `APP_STORE_URL` at the top of
`_src/gen.py` and regenerate — every "App Store" button turns from *coming soon* into a link.

## What the copy promises

The privacy and terms pages are written against what the app actually does, checked in the code,
not a template:

- Every money figure is the user's own estimate and is labelled **estimated**. The app connects
  to no bank, verifies no price, converts no currency, carries no affiliate link, and gives no
  financial advice.
- Screen Time hands the app opaque tokens, so it cannot name the apps it shields. Websites added by
  address are the exception, kept on the device as that address.
- Everything is stored on the device; nothing syncs. There is no in-app "reset all data" — deleting
  the app is the way to erase everything — and the Your data page says so.
- The journal never leaves the device. Its optional summary is Apple Intelligence on the device.
  Walking steps are shown live and never stored.
- The **one** feature that sends anything off the device is the optional AI reflection, which ships
  off, and then only with **OpenAI** as its writer (Apple Intelligence runs on the device and never
  falls back to a server). `/privacy/#ai` lists field by field what it sends, what it never sends,
  where it goes (the `cooldown-api` Cloudflare Worker, then OpenAI), what the Worker keeps
  (per-device daily counts for two days, service totals, spent attestation challenges — never
  content), OpenAI's abuse-monitoring retention, and that earlier builds use Google's Gemini on
  Vertex AI. Keep that section in step with `Cooldown/Features/Settings/AIPrivacyView.swift`,
  `ReflectionContext` / `WeeklyStats`, `Worker/README.md` and `CLAUDE.md` §6.1.
- The "On ice" widget and an item's Live Activity show item names on the Lock Screen; money
  amounts are hidden while the device is locked.

If any of that changes in the app, change it here in the same release, in all eight languages.
