#!/usr/bin/env python3
"""Build the carbon-skill reference bundle from a checkout of the upstream
carbon-design-system/carbon monorepo.

Carbon's practitioner docs are not a separate docs site — they live inside the
monorepo as Storybook-flavoured MDX colocated with each component, plus the
per-package READMEs (the foundational "elements") and a handful of root `docs/`
guides. This script converts that material into clean, faithful Markdown,
reorganizes it into a react/ + web-components/ + elements/ + guides/ + migration/
layout, regenerates CONTENTS.md, and copies the upstream LICENSE.

Deterministic and stdlib-only (no third-party dependencies), so it can run
unattended in CI to keep the bundle in sync with the monorepo.

Usage:
    python tools/build_references.py --carbon-repo <path-to-carbon> \
           --out skills/carbon/references

Handles the Storybook MDX dialect: multiline `import`/`export`, `{/* comments */}`,
`<Meta>`, `<Canvas of={...}>` story embeds, `<ArgTypes>` auto-generated prop tables,
`<StorybookDemo>` live-demo embeds, `<Markdown>{`${cdnJs(...)}`}</Markdown>` CDN
blocks (reproduced faithfully from the package version), and `<Unstyled>` live
examples (kept as fenced code). Rewrites relative links to absolute GitHub URLs.
Code fences are protected end-to-end, so JSX inside ```jsx examples is never touched.
"""
import argparse, json, os, re, posixpath, textwrap, shutil

GH = "https://github.com/carbon-design-system/carbon"
BRANCH = "main"
WEBSITE = "https://www.carbondesignsystem.com"
SB_REACT = "https://react.carbondesignsystem.com"
SB_WC = "https://web-components.carbondesignsystem.com"
CDN_BASE = "https://1.www.s81c.com/common/carbon/web-components"

# ---------------------------------------------------------------------------
# Curated, non-component sources (the component MDX is discovered by walking).
# ---------------------------------------------------------------------------
# Per-package READMEs that document a consumer-facing library ("elements").
ELEMENTS_PKGS = [
    "react", "web-components", "styles", "themes", "type", "colors", "grid",
    "layout", "motion", "icons", "icons-react", "icons-vue", "pictograms",
    "pictograms-react", "icon-helpers", "elements", "feature-flags",
    "utilities", "utilities-react", "cli", "upgrade",
]
# Root docs/ guides relevant to consumers of the system.
GUIDE_DOCS = [
    "guides/sass.md", "guides/accessibility.md", "guides/icons.md",
    "guides/colors.md", "guides/ibm-plex.md", "guides/versioning.md",
    "feature-flags.md", "experimental-code.md", "preview-code.md",
    "package-structure.md",
]
# Migration guides (docs/migration/* is globbed; these are extras).
MIGRATION_EXTRA = ["guides/cwc-v2-migration.md"]


def dedent(s):
    return textwrap.dedent(s.strip("\n"))


# ---------------------------------------------------------------------------
# Fence protection: stash fenced code blocks so no later transform touches them.
# ---------------------------------------------------------------------------
def protect_fences(text):
    blocks = []

    def stash(m):
        blocks.append(m.group(0))
        return "\x00FENCE%d\x00" % (len(blocks) - 1)

    text = re.sub(r"^```.*?^```", stash, text, flags=re.DOTALL | re.M)
    text = re.sub(r"^~~~.*?^~~~", stash, text, flags=re.DOTALL | re.M)
    return text, blocks


def restore_fences(text, blocks):
    return re.sub(r"\x00FENCE(\d+)\x00", lambda m: blocks[int(m.group(1))], text)


# ---------------------------------------------------------------------------
# Storybook MDX component handlers.
# ---------------------------------------------------------------------------
def render_cdn(captured, wc_version):
    """Reproduce the markdown that cdnJs()/cdnCss() would emit (storybook-cdn.ts),
    given the template-literal body captured from <Markdown>{`...`}</Markdown>."""
    out = []
    for m in re.finditer(r"cdnJs\(\{\s*components:\s*\[([^\]]*)\]\s*\}\)", captured):
        comps = re.findall(r"'([^']+)'|\"([^\"]+)\"", m.group(1))
        names = [a or b for a, b in comps]
        scripts = "\n".join(
            '<script type="module" src="%s/version/v%s/%s.min.js"></script>'
            % (CDN_BASE, wc_version, n)
            for n in names
        )
        out.append(
            "## CDN\n\nThis component is also available via CDN.\n\n"
            "```html\n// SPECIFIC VERSION (available starting v2.0.0)\n%s\n```" % scripts
        )
    if re.search(r"cdnCss\(\)", captured):
        out.append(
            "### Carbon CDN style helpers (optional)\n\n"
            "There are optional CDN artifacts available that can assist with global "
            "Carbon styles in lieu of including into your specific application bundle.\n\n"
            "[Click here to learn more](https://github.com/carbon-design-system/"
            "carbon-for-ibm-dotcom/blob/main/packages/web-components/docs/"
            "carbon-cdn-style-helpers.md)"
        )
    return "\n\n".join(out)


def storybook_demo(m, sb_url):
    block = m.group(0)
    um = re.search(r'url="([^"]+)"', block)
    url = um.group(1) if um else sb_url
    labels = re.findall(r"label:\s*'([^']*)'|label:\s*\"([^\"]*)\"", block)
    labels = [a or b for a, b in labels]
    lines = ["Explore the interactive examples in [Storybook](%s)." % url]
    if labels:
        lines.append("")
        lines += ["- %s" % lbl for lbl in labels]
    return "\n".join(lines)


def linkto(m):
    """<LinkTo ...>inner</LinkTo> (a Storybook cross-link) -> readable label text."""
    inner = m.group(1)
    lbl = re.search(r"\{'([^']*)'\}|\{\"([^\"]*)\"\}", inner)
    return (lbl.group(1) or lbl.group(2)) if lbl else inner.strip()


def process_mdx(text, sb_url, wc_version):
    text, fences = protect_fences(text)

    def stash(code):
        fences.append(code)
        return "\x00FENCE%d\x00" % (len(fences) - 1)

    # import statements: only real ones (`... from '...'` or side-effect `'...'`),
    # never prose that merely starts with the word "import".
    text = re.sub(r"^import\s*\{[\s\S]*?\}\s*from\s*['\"][^'\"]+['\"];?[ \t]*$", "", text, flags=re.M)
    text = re.sub(r"^import\b[^\n]*?\bfrom\s*['\"][^'\"]+['\"];?[ \t]*$", "", text, flags=re.M)
    text = re.sub(r"^import\s+['\"][^'\"]+['\"];?[ \t]*$", "", text, flags=re.M)
    # MDX comments {/* ... */}
    text = re.sub(r"\{/\*.*?\*/\}", "", text, flags=re.DOTALL)
    # <Meta ... />
    text = re.sub(r"<Meta\b[\s\S]*?/>", "", text)
    # <StorybookDemo ... /> -> live-demo link + variant list
    text = re.sub(r"<StorybookDemo\b[\s\S]*?/>",
                  lambda m: storybook_demo(m, sb_url), text)
    # <Canvas ...>...</Canvas> and self-closing <Canvas ... /> -> drop (story embeds)
    text = re.sub(r"<Canvas\b[\s\S]*?</Canvas>", "", text)
    text = re.sub(r"<Canvas\b[\s\S]*?/>", "", text)
    # <ArgTypes ... /> -> pointer to the live API table
    text = re.sub(
        r"<ArgTypes\b[\s\S]*?/>",
        "_The full props/attributes table is generated from the component source. "
        "See the **Source code** link at the top of this page, or the live API table "
        "in [Storybook](%s)._" % sb_url,
        text,
    )
    # <Markdown>{`...`}</Markdown> -> reproduce CDN block (or unwrap plain literal)
    def md_literal(m):
        body = m.group(1)
        if "cdnJs(" in body or "cdnCss(" in body:
            return "\n" + render_cdn(body, wc_version) + "\n"
        if "${" in body:
            return ""  # other interpolated content we can't evaluate
        return "\n" + dedent(body) + "\n"

    text = re.sub(r"<Markdown>\s*\{`([\s\S]*?)`\}\s*</Markdown>", md_literal, text)
    text = re.sub(r"<Markdown>([\s\S]*?)</Markdown>",
                  lambda m: "\n" + dedent(m.group(1)) + "\n", text)
    # <LinkTo ...>...</LinkTo> -> label text
    text = re.sub(r"<LinkTo\b[^>]*>([\s\S]*?)</LinkTo>", linkto, text)
    # <Unstyled>...</Unstyled> -> live example as fenced code (stashed so the generic
    # raw-JSX pass below never re-scans its contents)
    def unstyled(m):
        inner = dedent(m.group(1))
        return stash("```jsx\n%s\n```" % inner) if inner.strip() else ""

    text = re.sub(r"<Unstyled>([\s\S]*?)</Unstyled>", unstyled, text)

    # Remaining top-level JSX (col-0 live examples like `<div style=…>…</div>` or
    # `<DatePicker>…</DatePicker>`). If a canonical ```code fence immediately follows,
    # drop the live render (the fence is the example); otherwise keep it as fenced code.
    # open tag may span lines (e.g. `<ContentSwitcher\n  onChange={() => {}}>`); the
    # first `>` that ends its own line is the tag's close (`=>` arrows are skipped).
    paired = re.compile(
        r"^(?P<block><(?P<tag>[A-Za-z][\w.-]*)\b[\s\S]*?(?<!/)>[ \t]*\n[\s\S]*?\n</(?P=tag)>[ \t]*)$"
        r"(?P<tail>\n\s*\x00FENCE\d+\x00)?", re.M)
    selfclose = re.compile(
        r"^(?P<block><[A-Z][\w.]*\b[\s\S]*?/>[ \t]*)$(?P<tail>\n\s*\x00FENCE\d+\x00)?", re.M)

    def fence_block(m):
        if m.group("tail"):
            return m.group("tail").lstrip("\n")
        return stash("```jsx\n%s\n```" % m.group("block").rstrip())

    text = paired.sub(fence_block, text)
    text = selfclose.sub(fence_block, text)
    return text, fences


# ---------------------------------------------------------------------------
# Links: rewrite relative targets to absolute GitHub URLs.
# ---------------------------------------------------------------------------
def rewrite_links(text, src_rel):
    cur = posixpath.dirname(src_rel)

    def repl(m):
        label, target = m.group(1), m.group(2).strip()
        if (not target or target.startswith("#")
                or target.startswith(("http://", "https://", "mailto:"))):
            return m.group(0)
        path, anchor = (target.split("#", 1) + [""])[:2]
        anchor = ("#" + anchor) if anchor else ""
        if path.startswith("/"):
            resolved = path.lstrip("/")
        else:
            resolved = posixpath.normpath(posixpath.join(cur, path))
        return "[%s](%s/blob/%s/%s%s)" % (label, GH, BRANCH, resolved, anchor)

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", repl, text)


# ---------------------------------------------------------------------------
# Conversion entry points.
# ---------------------------------------------------------------------------
def humanize(slug):
    """Best-effort human title from a file slug for pages that lack their own H1."""
    s = re.sub(r"-overview$", "", slug)
    s = re.sub(r"-section$", " section", s)
    if re.search(r"[A-Z]", s) and "-" not in s and "." not in s:
        return s  # already a PascalCase / camelCase identifier
    words = [w for w in re.split(r"[-_.]", s) if w]
    return " ".join(w[:1].upper() + w[1:] for w in words) or slug


def finish(out, src_rel, title=None):
    out = rewrite_links(out, src_rel)
    if title and not re.search(r"^#\s", out.lstrip()[:300], re.M):
        out = "# %s\n\n%s" % (title, out)
    out = re.sub(r"[ \t]+$", "", out, flags=re.M)
    out = re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"
    return "> Source: %s/blob/%s/%s\n\n%s" % (GH, BRANCH, src_rel, out)


def convert_mdx(path, src_rel, sb_url, wc_version, title=None):
    raw = open(path, encoding="utf-8").read()
    body, fences = process_mdx(raw, sb_url, wc_version)
    body = restore_fences(body, fences)
    return finish(body, src_rel, title)


def convert_md(path, src_rel, title=None):
    raw = open(path, encoding="utf-8").read()
    body, fences = protect_fences(raw)
    body = restore_fences(body, fences)
    return finish(body, src_rel, title)


# ---------------------------------------------------------------------------
# Component-MDX discovery + path mapping.
# ---------------------------------------------------------------------------
def slug_for(mdx_path, comp_root):
    """Output slug for a component MDX, relative to the package's components root."""
    rel = os.path.relpath(mdx_path, comp_root)         # e.g. Accordion/Accordion.mdx
    parts = rel[:-len(".mdx")].split(os.sep)
    base = parts[-1]
    if base == "overview":
        # name after the owning component dir; tag nested (experimental) variants
        comp = parts[0]
        mids = [p for p in parts[1:-1] if p != "docs"]
        return comp + ("-" + "-".join(mids) if mids else "")
    if base == "section" and len(parts) >= 2:           # web-components heading/section
        return parts[0] + "-section"
    return base


def collect_components(src_dir, out_section, sb_url, wc_version, results):
    comp_root = os.path.join(src_dir, "components")
    # Gather candidates; group by slug so a rich doc supersedes a thin live-demo page
    # even when the two live in different component directories (e.g. Grid/FlexGrid.mdx
    # vs FlexGrid/docs/overview.mdx).
    groups = {}  # slug -> list of (full, is_overview)
    for dp, _, files in os.walk(src_dir):
        for fn in sorted(files):
            if not fn.endswith(".mdx"):
                continue
            full = os.path.join(dp, fn)
            under = os.path.commonpath([full, comp_root]) == comp_root
            slug = slug_for(full, comp_root) if under else fn[:-len(".mdx")]
            groups.setdefault(slug, []).append((full, fn == "overview.mdx"))

    for slug in sorted(groups):
        entries = groups[slug]
        rich = [e for e in entries if not e[1]]
        chosen = rich or entries
        for i, (full, _) in enumerate(sorted(chosen)):
            tag = slug if i == 0 else "%s-%d" % (slug, i + 1)  # deterministic on collision
            out_rel = "%s/components/%s" % (out_section, tag)
            src_rel = os.path.relpath(full, results["repo"])
            md = convert_mdx(full, src_rel, sb_url, wc_version, title=humanize(tag))
            results["pages"].append((out_rel, md))


# ---------------------------------------------------------------------------
# CONTENTS.md + LICENSE.
# ---------------------------------------------------------------------------
SECTION_ORDER = ["react", "web-components", "elements", "guides", "migration"]
SECTION_LABELS = {
    "react": "@carbon/react — React components",
    "web-components": "@carbon/web-components — Web Components",
    "elements": "Elements & packages (foundations)",
    "guides": "Guides (styling, a11y, icons, feature flags)",
    "migration": "Migration",
}


def first_h1(path):
    for line in open(path, encoding="utf-8"):
        m = re.match(r"#\s+(.+)", line)
        if m:
            return m.group(1).strip()
    return os.path.basename(path)


def write_index(out_root):
    sections = {}
    for dp, _, files in os.walk(out_root):
        for fn in sorted(files):
            if not fn.endswith(".md") or fn in ("CONTENTS.md",):
                continue
            rel = os.path.relpath(os.path.join(dp, fn), out_root).replace(os.sep, "/")
            top = rel.split("/")[0]
            sections.setdefault(top, []).append(
                (rel, first_h1(os.path.join(dp, fn))))
    keys = ([k for k in SECTION_ORDER if k in sections]
            + [k for k in sorted(sections) if k not in SECTION_ORDER])
    total = sum(len(v) for v in sections.values())
    lines = [
        "# Carbon Design System — reference index", "",
        "Faithful Markdown conversion of the Carbon Design System practitioner docs, "
        "generated from the [carbon-design-system/carbon](%s) monorepo by "
        "`tools/build_references.py` — the colocated Storybook MDX (component usage), "
        "the per-package READMEs (foundational *elements*), and selected root `docs/` "
        "guides. Each file keeps a `> Source:` link to its file on GitHub. "
        "See `LICENSE` (Apache-2.0)." % GH, "",
        "Design and usage guidance for the system as a whole lives at %s." % WEBSITE, "",
        "**%d pages.**" % total, "",
    ]
    for k in keys:
        lines += ["## " + SECTION_LABELS.get(k, k), ""]
        for rel, title in sorted(sections[k]):
            lines.append("- [%s](%s) — `%s`" % (title, rel, rel))
        lines.append("")
    open(os.path.join(out_root, "CONTENTS.md"), "w", encoding="utf-8").write(
        "\n".join(lines) + "\n")


def write_license(repo, out_root):
    note = (
        "The reference material in this directory is derived from the Carbon Design\n"
        "System (https://github.com/carbon-design-system/carbon), converted from its\n"
        "Storybook MDX and package READMEs to Markdown. It is redistributed here under\n"
        "the original Apache-2.0 license, reproduced verbatim below.\n\n"
        "--------------------------------------------------------------------------------\n\n"
    )
    up = os.path.join(repo, "LICENSE")
    text = open(up, encoding="utf-8").read() if os.path.isfile(up) else ""
    open(os.path.join(out_root, "LICENSE"), "w", encoding="utf-8").write(note + text)


# ---------------------------------------------------------------------------
# Build.
# ---------------------------------------------------------------------------
def build(repo, out_root):
    if os.path.isdir(out_root):
        shutil.rmtree(out_root)
    os.makedirs(out_root)

    wc_pkg = os.path.join(repo, "packages/web-components/package.json")
    wc_version = json.load(open(wc_pkg, encoding="utf-8"))["version"]

    results = {"repo": repo, "pages": []}
    collect_components(os.path.join(repo, "packages/react/src"),
                       "react", SB_REACT, wc_version, results)
    collect_components(os.path.join(repo, "packages/web-components/src"),
                       "web-components", SB_WC, wc_version, results)

    # Elements: per-package READMEs.
    for pkg in ELEMENTS_PKGS:
        readme = os.path.join(repo, "packages", pkg, "README.md")
        if os.path.isfile(readme):
            src_rel = os.path.relpath(readme, repo)
            results["pages"].append(
                ("elements/" + pkg, convert_md(readme, src_rel, title="@carbon/" + pkg)))

    # Guides + migration from root docs/.
    for rel in GUIDE_DOCS:
        p = os.path.join(repo, "docs", rel)
        if os.path.isfile(p):
            slug = os.path.basename(rel)[:-3]
            results["pages"].append(
                ("guides/" + slug, convert_md(p, os.path.relpath(p, repo), humanize(slug))))

    mig_dir = os.path.join(repo, "docs/migration")
    mig = []
    if os.path.isdir(mig_dir):
        mig = [os.path.join("docs/migration", f) for f in os.listdir(mig_dir)
               if f.endswith(".md")]
    for rel in sorted(mig) + [os.path.join("docs", r) for r in MIGRATION_EXTRA]:
        p = os.path.join(repo, rel)
        if os.path.isfile(p):
            slug = os.path.basename(rel)[:-3]
            results["pages"].append(
                ("migration/" + slug, convert_md(p, os.path.relpath(p, repo), humanize(slug))))

    for out_rel, md in results["pages"]:
        dest = os.path.join(out_root, out_rel + ".md")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(md)

    write_index(out_root)
    write_license(repo, out_root)
    return len(results["pages"])


def main():
    ap = argparse.ArgumentParser(
        description="Build the carbon-skill reference bundle from the carbon monorepo.")
    ap.add_argument("--carbon-repo", required=True,
                    help="Path to a checkout of carbon-design-system/carbon")
    ap.add_argument("--out", required=True,
                    help="Output references directory (rebuilt from scratch)")
    args = ap.parse_args()
    n = build(args.carbon_repo, args.out)
    print("Built %d reference pages -> %s" % (n, args.out))


if __name__ == "__main__":
    main()
