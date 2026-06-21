#!/usr/bin/env python3
"""Guard for the generated reference bundle. Catches conversion defects so an automated
docs sync never silently ships broken Markdown — most importantly, unhandled Storybook
MDX from new upstream components that `build_references.py` doesn't know about yet.

Checks: empty/tiny files, missing H1, unbalanced code fences, broken intra-bundle links,
leftover MDX imports / {props.X} / known JSX wrappers, and any unknown `<Capitalized>`
JSX-looking tag outside code (a signal the converter needs updating).

Note: Carbon's component docs legitimately contain JSX *inside* ```jsx examples (e.g.
`<Button>`, `<Modal>`). Those live in code fences and are intentionally preserved, so the
unknown-JSX scan only looks at prose with code stripped out.

Exit code 0 = clean, 1 = issues found (printed). Stdlib only.

Usage: python tools/check_references.py <references-dir>
"""
import os, re, sys

# Wrapper components the converter consumes; if any survive into prose it's a bug.
KNOWN = ("Meta", "Canvas", "ArgTypes", "StorybookDemo", "Markdown", "Unstyled")


def strip_code(text):
    text = re.sub(r"^```.*?^```", "", text, flags=re.DOTALL | re.M)
    text = re.sub(r"^~~~.*?^~~~", "", text, flags=re.DOTALL | re.M)
    text = re.sub(r"`[^`\n]*`", "", text)          # inline code spans
    return text


def main():
    if len(sys.argv) != 2:
        print("usage: check_references.py <references-dir>", file=sys.stderr)
        return 2
    root = sys.argv[1]
    mds = [os.path.join(dp, f) for dp, _, fs in os.walk(root)
           for f in fs if f.endswith(".md")]
    issues = []

    def add(kind, path, detail=""):
        issues.append((kind, os.path.relpath(path, root), detail))

    for m in mds:
        base = os.path.basename(m)
        text = open(m, encoding="utf-8").read()
        if base not in ("CONTENTS.md", "LICENSE"):
            if len(text) < 120:
                add("empty/tiny", m)
            if not re.search(r"^# ", text, re.M):
                add("missing-H1", m)
        if len(re.findall(r"^```", text, re.M)) % 2:
            add("unbalanced-fences", m)
        nocode = strip_code(text)
        for c in KNOWN:
            if re.search(r"<%s\b" % c, nocode):
                add("leftover-component", m, c)
        for tag in sorted(set(re.findall(r"<([A-Z][A-Za-z][A-Za-z0-9]*)\b", nocode))):
            if tag not in KNOWN:
                add("unknown-jsx", m, tag)
        # real leftover JS imports only (`… from '…'` / side-effect), not prose that
        # happens to begin with the word "import"
        if (re.search(r"^import\b[^\n]*\bfrom\s*['\"]", nocode, re.M)
                or re.search(r"^import\s+['\"]", nocode, re.M)):
            add("leftover-import", m)
        # broken intra-bundle links (relative, not http/anchor)
        d = os.path.dirname(m)
        for tgt in re.findall(r"\]\(([^)]+)\)", text):
            t = tgt.split("#", 1)[0]
            if not t or t.startswith(("http", "mailto:")):
                continue
            p = (root + t) if t.startswith("/") else os.path.normpath(os.path.join(d, t))
            if not os.path.exists(p):
                add("broken-link", m, tgt)

    if not issues:
        n = len([m for m in mds if os.path.basename(m) not in ("CONTENTS.md",)])
        print("OK: %d pages, no issues." % n)
        return 0
    print("FOUND %d issue(s):" % len(issues))
    for kind, path, detail in issues:
        print("  [%s] %s%s" % (kind, path, (" :: " + detail) if detail else ""))
    return 1


if __name__ == "__main__":
    sys.exit(main())
