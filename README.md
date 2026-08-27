# cooldown-links

The pages Cooldown's App Store listing points at, hosted with GitHub Pages at
https://sohaibiii.github.io/cooldown-links/

| Page | URL | App Store Connect field |
|---|---|---|
| Support | `/` | Support URL |
| About | `/about/` | Marketing URL |
| Privacy Policy | `/privacy/` | Privacy Policy URL |
| Terms of Use (EULA) | `/terms/` | EULA / linked from the paywall |
| Your data | `/delete-data/` | — (linked from Privacy) |

## Editing

Everything is rendered by one script from one file — edit `_src/gen.py`, then:

```
python3 _src/gen.py
```

and commit the regenerated `index.html` files alongside it. The colours, radii and type are
Cooldown's own tokens (`Cooldown/Core/DesignSystem/DesignTokens.swift` in the app repo):
night-sky background, dusk indigo, savings green kept for realised saves only, cooling amber
for items still on ice — dark-first with a light counterpart, so the pages read as the same
product as the app.

Once App Store Connect has assigned the app its Apple ID, set `APP_STORE_URL` at the top of
`_src/gen.py` and regenerate — every "App Store" button turns from *coming soon* into a link.

## What the copy promises

The privacy and terms pages are written against what the app actually does, not a template:

- Every money figure is the user's own estimate and is labelled **estimated**. The app connects
  to no bank, verifies no price, carries no affiliate link, and gives no financial advice.
- Screen Time hands the app opaque tokens, so it cannot name the shops it shields.
- The **one** feature that sends anything off the phone is the optional AI reflection, which
  ships off. `/privacy/#ai` lists field by field what it sends, what it never sends, where it
  goes, and what switching it off deletes. Keep that section in step with
  `Cooldown/Features/Settings/AIPrivacyView.swift` and `CLAUDE.md` §6.1.

If any of that changes in the app, change it here in the same commit.
