# -*- coding: utf-8 -*-
"""Holds the eight catalogues in `_src/words/` to the same shape.

    python3 _src/check.py

This is the half of a translation nobody here can proofread. A German reader
will notice a clumsy sentence; nobody will notice that the French privacy
policy quietly lost its link to the data page, or that a `{K_settings}` became a
`{K_setting}` and now renders as a literal brace. So the machine checks the shape
and leaves the prose to the translator:

  * every key English has, each language has — a missing one would silently
    render as English, which is fine at runtime and a lie in a review;
  * no key a language has that English does not, which is always a typo;
  * the same `{placeholders}` in every translation as in its English, because
    an invented one is a crash and a dropped one is a missing link;
  * the same link targets, in the same number;
  * balanced tags, because one unclosed <p> takes the rest of the page with it;
  * the public name. The app ships as "On Ice"; "Cooldown" is the codebase's
    name and must never reach a reader, in any language.

Exits non-zero on any of those. Values that are identical to English are only
listed, not failed: "Premium" is "Premium" in most of them.
"""
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from gen import LANGUAGES, NATIVE_NAME, context, copy_for  # noqa: E402
import words.en as english  # noqa: E402

EN = english.COPY

PLACEHOLDER = re.compile(r"\{([A-Za-z_][A-Za-z0-9_\-]*)\}")
HREF = re.compile(r'href="([^"]*)"')
TAG = re.compile(r"<(/?)([a-z0-9]+)(?=[\s/>])")
VOID = {"br", "img", "input", "hr", "meta", "link", "path", "circle", "rect", "stop", "svg", "use"}
OLD_NAME = re.compile(r"\bCooldown\b")


def shape(value):
    opens, closes = Counter(), Counter()
    for slash, tag in TAG.findall(value):
        if tag in VOID:
            continue
        (closes if slash else opens)[tag] += 1
    return {
        "placeholders": Counter(PLACEHOLDER.findall(value)),
        "hrefs": Counter(HREF.findall(value)),
        "unclosed": {t: opens[t] - closes[t] for t in set(opens) | set(closes)
                     if opens[t] != closes[t]},
    }


def main(only=None):
    """Check every catalogue, or just the codes in `only` (`check.py de fr`)."""
    failures = []
    languages = [(c, p) for c, p in LANGUAGES if not only or c == "en" or c in only]
    unknown_codes = set(only or ()) - {c for c, _ in LANGUAGES}
    if unknown_codes:
        print(f"Unknown language codes: {sorted(unknown_codes)}")
        return 2

    for key, value in EN.items():
        if shape(value)["unclosed"]:
            failures.append(f"en: {key!r} has unbalanced tags {shape(value)['unclosed']}")

    for code, _ in languages:
        if code == "en":
            continue
        module = __import__("words." + code.replace("-", "_"), fromlist=["COPY"])
        catalogue = module.COPY
        name = f"{code} ({NATIVE_NAME[code]})"

        missing = sorted(set(EN) - set(catalogue))
        unknown = sorted(set(catalogue) - set(EN))
        for key in missing:
            failures.append(f"{name}: missing key {key!r}")
        for key in unknown:
            failures.append(f"{name}: unknown key {key!r} — not in English")

        same = []
        for key in sorted(set(EN) & set(catalogue)):
            want, got = shape(EN[key]), shape(catalogue[key])
            if want["placeholders"] != got["placeholders"]:
                failures.append(
                    f"{name}: {key!r} placeholders differ — English has "
                    f"{sorted(want['placeholders'].elements())}, this has "
                    f"{sorted(got['placeholders'].elements())}"
                )
            if want["hrefs"] != got["hrefs"]:
                failures.append(
                    f"{name}: {key!r} links differ — English has "
                    f"{sorted(want['hrefs'].elements())}, this has "
                    f"{sorted(got['hrefs'].elements())}"
                )
            if got["unclosed"]:
                failures.append(f"{name}: {key!r} has unbalanced tags {got['unclosed']}")
            if EN[key].strip() == catalogue[key].strip():
                same.append(key)

        note = f" · {len(same)} identical to English" if same else ""
        print(f"{name}: {len(catalogue)} keys{note}")
        if same:
            print("   " + ", ".join(same))

    # The public name, and every value actually renders: a stray brace or an
    # unknown placeholder is a KeyError here rather than a broken page.
    for code, prefix in languages:
        C = copy_for(code)
        ctx = context(code, prefix, C)
        for key, value in C.items():
            if OLD_NAME.search(value):
                failures.append(f"{code}: {key!r} says \"Cooldown\" — the app is called On Ice")
            try:
                value.format(**ctx)
            except (KeyError, IndexError, ValueError) as error:
                failures.append(f"{code}: {key!r} does not render: {error!r}")

    if failures:
        print("\n".join(["", "FAILED:"] + ["  " + f for f in failures]))
        return 1
    print("\nAll catalogues agree.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
