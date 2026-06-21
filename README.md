# Carbon — a Claude skill for the IBM Carbon Design System

[![skills.sh](https://skills.sh/b/iamursky/carbon-skill)](https://skills.sh/iamursky/carbon-skill)

<!-- Add a cover image at .github/images/cover.webp and reference it here -->

A Claude skill that teaches Claude to build UIs with **[Carbon](https://carbondesignsystem.com)** —
IBM's open-source design system. It bundles a faithful, offline copy of Carbon's in-repo
documentation as structured Markdown references, with a concise, task-oriented guide on top.

## What it does

Ask Claude to build a UI with Carbon — or anything involving `@carbon/react`,
`@carbon/web-components`, Carbon Sass/styles, themes, the 2x Grid, Carbon icons, or feature flags —
and the skill activates so Claude answers from the real docs instead of guessing. It covers:

- **Component usage** for both flagship libraries — `@carbon/react` (React) and
  `@carbon/web-components` (the `cds-*` custom elements), including feature-flagged behavior
- **Styling** with `@carbon/styles` Sass — `@use`, Dart Sass setup, per-component imports, the
  `cds` class prefix
- **Theming** — `white`/`g10`/`g90`/`g100`, the `<Theme>` component, `$theme` with-config, Layer
- **Elements (foundations)** — `@carbon/colors`, `@carbon/themes`, `@carbon/grid`, `@carbon/layout`,
  `@carbon/type` (IBM Plex), `@carbon/motion`, `@carbon/icons(-react/-vue)`, `@carbon/pictograms`
- **Feature flags & preview code**, and the **v10 → v11** migration

## What's inside

```
skills/carbon/
├── SKILL.md            # the guide Claude loads on trigger (workflow + reference map)
└── references/         # 245 pages of faithful Markdown from the Carbon monorepo
    ├── CONTENTS.md     # full navigation, by section
    ├── react/components/         @carbon/react component usage (one file per component)
    ├── web-components/components/ @carbon/web-components (cds-*) usage
    ├── elements/       per-package READMEs (styles, themes, colors, grid, type, icons, …)
    ├── guides/         Sass, accessibility, icons, colors, IBM Plex, feature flags, …
    ├── migration/      v11 and per-element v10.x → v11 migration guides
    └── LICENSE         # upstream documentation license (Apache-2.0, IBM Corp.)
```

Every reference page keeps a `> Source:` link to its file on
[github.com/carbon-design-system/carbon](https://github.com/carbon-design-system/carbon). Design and
usage guidance for the system as a whole lives at https://www.carbondesignsystem.com.

## Installation

### Via `npx skills` (recommended)

```bash
npx skills add iamursky/carbon-skill
```

### Claude Desktop / Web

1. Download [`skills/carbon/SKILL.md`](skills/carbon/SKILL.md)
2. Go to **Customize → Skills → + → Upload a skill**
3. Upload `SKILL.md`
4. The skill activates automatically when you ask about Carbon, `@carbon/react`, or `@carbon/web-components`

### Manual install for Claude Code

```bash
# Personal (available across all projects)
git clone https://github.com/iamursky/carbon-skill ~/carbon-skill
ln -s ~/carbon-skill/skills/carbon ~/.claude/skills/carbon

# Per-project (shared with the team via git)
git clone https://github.com/iamursky/carbon-skill .carbon-skill
ln -s .carbon-skill/skills/carbon .claude/skills/carbon
```

## How it activates

The skill triggers automatically when you:

- Ask Claude to build a UI, screen, or component with Carbon
- Mention `@carbon/react`, `@carbon/web-components`, `cds-*` elements, `@carbon/styles`, or Carbon tokens
- Ask about Carbon theming (g10/g90/g100), the 2x Grid, Carbon icons / IBM Plex, or feature flags
- Need to migrate a Carbon project from v10 to v11

## Provenance & license

The `references/` are converted from the official
[carbon-design-system/carbon](https://github.com/carbon-design-system/carbon) monorepo — the
colocated Storybook MDX (component usage), the per-package READMEs (the foundational *elements*), and
selected root `docs/` guides — and kept faithful. Live Storybook `<Canvas>` demos and the
auto-generated `<ArgTypes>` prop tables can't be rendered statically, so each page keeps its
**Source code** link and a pointer to the live Storybook for the exact API. They are redistributed
under the upstream **Apache-2.0 license**
([`skills/carbon/references/LICENSE`](skills/carbon/references/LICENSE)).

The skill itself — `SKILL.md`, structure, and this repository — is MIT licensed; see [license](license).

> Unofficial, community-built skill. Not affiliated with or endorsed by IBM or the Carbon Design System.
