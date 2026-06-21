# tools — docs sync pipeline

The bundled references under [`skills/carbon/references/`](../skills/carbon/references/) are
**generated**, not hand-written. They are produced from the upstream
[carbon-design-system/carbon](https://github.com/carbon-design-system/carbon) monorepo and kept in
sync automatically. Don't edit `references/` by hand — edit the converter and rebuild.

Carbon has no separate docs site repo: its practitioner docs live _inside_ the monorepo as
Storybook-flavoured MDX colocated with each component, plus the per-package READMEs (the
foundational "elements") and a handful of root `docs/` guides. The pipeline reads all three.

## Scripts (stdlib-only Python 3, no dependencies)

### `build_references.py`

Converts a checkout of `carbon` into the reference bundle: Storybook MDX / Markdown → faithful
Markdown, reorganized into the `react/` + `web-components/` + `elements/` + `guides/` + `migration/`
layout, with `CONTENTS.md` (navigation) and `LICENSE` (copied from upstream) regenerated.
Deterministic — same input produces byte-identical output.

```bash
git clone --depth 1 https://github.com/carbon-design-system/carbon.git /tmp/carbon
python3 tools/build_references.py --carbon-repo /tmp/carbon --out skills/carbon/references
```

It renders Carbon's Storybook MDX dialect: multiline `import`/`export`, `{/* comments */}`,
`<Meta>`, `<Canvas of={…}>` story embeds, `<ArgTypes>` auto-generated prop tables (replaced with a
pointer to the live API table, which can't be rendered statically), `<StorybookDemo>` live-demo
embeds (turned into a Storybook link + variant list), `<Markdown>{`${cdnJs(…)}`}</Markdown>` CDN
blocks (reproduced faithfully from the package version), `<Unstyled>` and other top-level raw JSX
live examples (kept as fenced code, de-duplicated against an adjacent canonical fence). Code fences
are protected end-to-end, so JSX inside ```jsx examples is never altered. Relative links are
rewritten to absolute GitHub URLs, and each page keeps a `> Source:` link to its upstream file.

The script only ever writes `references/` — it does not touch the sync cache key (`.source-commit`
at the repo root), which the workflow manages so nothing build-related leaks into the shipped
`skills/` bundle.

### `check_references.py`

A guard that fails (exit 1) if the generated bundle has defects: empty/short files, missing H1,
unbalanced code fences, broken intra-bundle links, leftover MDX imports, or **any unhandled JSX
wrapper outside code** — including unknown `<Capitalized>` tags, which signal that upstream
introduced a Storybook component the converter doesn't know about yet. (JSX _inside_ ```jsx code
examples is intentional and ignored.)

```bash
python3 tools/check_references.py skills/carbon/references
```

## Automation

[`.github/workflows/sync-docs.yml`](../.github/workflows/sync-docs.yml) runs daily (and on demand).
It first does a cheap `git ls-remote` to read the upstream HEAD **without cloning** and compares it
to `.source-commit` (a one-line file at the repo root). If they match, the run stops there (no
clone, no rebuild, no PR). Otherwise it clones the upstream monorepo, rebuilds the references, writes
the new commit to `.source-commit`, runs the guard, and opens a PR. If the guard finds an unhandled
component, the PR is labeled `needs-converter-update` so the converter is fixed before merge.

`.source-commit` lives at the repo root (not under `skills/`, which ships to end users) and moves
only inside a sync PR, so it never causes day-to-day churn — most days the gate matches and the job
is a no-op.

### Repo settings required

- **Settings → Actions → General → Workflow permissions:** enable *"Allow GitHub Actions to create
  and approve pull requests"* (the workflow uses the default `GITHUB_TOKEN` to open PRs).
- The scheduled trigger only fires from the workflow file on the **default branch**.

## When upstream adds a new component

1. The daily PR is labeled `needs-converter-update` and the job summary shows e.g.
   `[unknown-jsx] react/components/Foo.md :: NewThing`.
2. Add handling for `<NewThing>` in `build_references.py` (`process_mdx()`), and — if it is a wrapper
   that should never survive into prose — add it to the `KNOWN` tuple in `check_references.py`.
3. Re-run `build_references.py` + `check_references.py` locally until the guard is clean.
