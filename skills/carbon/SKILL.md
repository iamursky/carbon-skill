---
name: carbon
description: >-
  Build UIs with the IBM Carbon Design System. Use when working with
  `@carbon/react` (React components) or `@carbon/web-components` (the `cds-*`
  custom elements / Lit), styling with `@carbon/styles` Sass (`@use`, Dart Sass,
  the `cds` class prefix), theming (white/g10/g90/g100, the `<Theme>` component or
  `$theme` with-config), the 2x Grid (`Grid`/`Column` vs `FlexGrid`), Carbon icons
  & pictograms (`@carbon/icons-react`), IBM Plex type, design tokens
  (`@carbon/colors`, `@carbon/themes`, `@carbon/layout`, `@carbon/motion`),
  feature flags / preview code (`@carbon/feature-flags`, `<FeatureFlags>`,
  `enable-*`), or migrating to v11. Covers component usage and APIs for both
  flagship libraries.
license: MIT
metadata:
  version: "1.0.0"
---

# Carbon Design System — components, styles & elements

Carbon is IBM's open-source design system. As code it is a **monorepo of layered
npm packages**: two _flagship_ component libraries on top of a set of foundational
_elements_ (design tokens, grid, type, icons, motion) that are all driven by **Sass**.

- **`@carbon/react`** — React components (`<Button>`, `<DataTable>`, …). Bundles the styles.
- **`@carbon/web-components`** — the same components as framework-agnostic custom elements
  (`<cds-button>`, Lit-based). React and web-components are a **dual-flagship pair**: equal
  feature/visual parity, different implementations. Pick one per app.
- **Elements** (used directly or transitively): `@carbon/styles` (all Sass), `@carbon/themes`,
  `@carbon/colors`, `@carbon/grid`, `@carbon/layout`, `@carbon/type`, `@carbon/motion`,
  `@carbon/icons` (+ `@carbon/icons-react`, `@carbon/icons-vue`), `@carbon/pictograms`.
- Deprecated re-exports: `carbon-components` → `@carbon/styles`, `carbon-components-react` → `@carbon/react`.

This skill is a faithful offline copy of Carbon's in-repo docs. The narrative below is the map;
**open the matching file under `references/` for exact usage, props, and full detail.** Start
navigation at [`references/CONTENTS.md`](references/CONTENTS.md). Design/usage guidance for the
system as a whole (do/don't, anatomy, accessibility) lives at https://www.carbondesignsystem.com.

## Mental model — three layers

1. **Components** render the UI. Import from one flagship and use it; props/attributes drive variants.
   - React: `import { Button } from '@carbon/react'` → `<Button kind="secondary">`.
   - Web components: `import '@carbon/web-components/es/components/button/index.js'` → `<cds-button kind="secondary">`.
2. **Styles are Sass, and required.** Components are unstyled without Carbon's CSS. `@carbon/react`
   ships its styles through `@carbon/styles`; bring them in with `@use '@carbon/styles'`. Everything
   is namespaced under the **`cds` class prefix**.
3. **Elements are the tokens** underneath — colors, themes, spacing, type, motion, breakpoints. Use
   their Sass functions/maps (`$spacing-05`, `theme.$background`, `type.type-style('body-01')`)
   instead of hard-coded values so theming and density work.

→ Per-language quickstart: [`references/elements/react.md`](references/elements/react.md) ·
[`references/elements/web-components.md`](references/elements/web-components.md) ·
[`references/elements/styles.md`](references/elements/styles.md).

## Install & wire up styles

`@carbon/styles` (and therefore `@carbon/react`) **requires Dart Sass**, and Sass must be able to
resolve `node_modules` (add it to `loadPaths`/`includePaths` — see [`references/guides/sass.md`](references/guides/sass.md)).

```bash
npm install -S @carbon/react        # React flagship (bundles styles)
# or
npm install -S @carbon/web-components
```

```scss
// the simplest setup: bring in everything
@use '@carbon/styles';

// or only what you use (smaller CSS) — reset + per-component partials
@use '@carbon/styles/scss/reset';
@use '@carbon/styles/scss/components/button';
@use '@carbon/styles/scss/grid';
```

React components import from the package root; styles are a separate Sass import:
`@use '@carbon/react'` (Sass) alongside `import { Button } from '@carbon/react'` (JS).

## Theming

Four themes ship: **`white`, `g10`** (light) and **`g90`, `g100`** (dark). Set a global default in
Sass, or switch regions at runtime with the `<Theme>` component / `cds-theme` (React/WC) or the
`data-carbon-theme` attribute.

```scss
@use '@carbon/styles/scss/themes';
@use '@carbon/styles/scss/theme' with ($theme: themes.$g100);   // global default
```

```jsx
<Theme theme="g100"><MyDarkPanel /></Theme>   // a subtree on a different theme
```

Always consume theme **tokens** (`theme.$background`, `theme.$text-primary`, `theme.$layer-01`) so
both light/dark and the **Layer** model work. → [`references/elements/themes.md`](references/elements/themes.md),
[`references/guides/colors.md`](references/guides/colors.md), `references/react/components/Theme.md`,
[`Layer`](references/react/components/Layer.md) · [`useLayer`](references/react/components/use-layer-overview.md).

## The 2x Grid

Two grid implementations, same 16-column 2x Grid system:
- **CSS Grid** (default, recommended): `<Grid>` + `<Column>` with `sm`/`md`/`lg`/`xlg`/`max` span objects.
- **Flexbox grid** (legacy): `<FlexGrid>` + `<Row>` + `<Column>`.

```jsx
<Grid>
  <Column sm={4} md={8} lg={16}>full-width on small, …</Column>
</Grid>
```

→ [`references/react/components/Grid.md`](references/react/components/Grid.md) ·
[`FlexGrid`](references/react/components/FlexGrid.md) · [`references/elements/grid.md`](references/elements/grid.md) ·
spacing tokens [`references/elements/layout.md`](references/elements/layout.md).

## Icons, pictograms & type

- **Icons** as components: `import { Add, TrashCan } from '@carbon/icons-react'` → `<Add size={16} />`.
  Carbon icons come in 16/20/24/32 px. Vue: `@carbon/icons-vue`; raw SVG/JS: `@carbon/icons`.
- **Pictograms**: `@carbon/pictograms-react`.
- **Type**: IBM Plex via `@carbon/type`; use type tokens/`type-style` mixins, not raw font sizes.

→ [`references/elements/icons-react.md`](references/elements/icons-react.md) ·
[`references/guides/icons.md`](references/guides/icons.md) · [`references/elements/type.md`](references/elements/type.md) ·
[`references/guides/ibm-plex.md`](references/guides/ibm-plex.md) · `references/react/components/Icon.md`.

## Prefix (`cds`)

All CSS classes use the **`cds`** prefix. Change it (e.g. to avoid clashes) at runtime with
`<ClassPrefix prefix="…">` (and `<IdPrefix>` for generated ids), and in Sass with
`@use '@carbon/styles' with ($prefix: '…')` — **the two must match**.
→ [`ClassPrefix`](references/react/components/ClassPrefix.md) · [`IdPrefix`](references/react/components/IdPrefix.md).

## Web components specifics

- Custom elements are `cds-*`; import the side-effecting ES module to register each:
  `import '@carbon/web-components/es/components/dropdown/index.js'`.
- **CDN**: each component is published as a standalone module — every web-component page lists a
  `## CDN` `<script type="module" src="…s81c.com/common/carbon/web-components/version/v<ver>/<name>.min.js">`.
- React-only authoring concepts (`renderIcon` props, JSX children) map to slots/attributes; check the
  component's own page for the `cds-*` API. → [`references/elements/web-components.md`](references/elements/web-components.md).

## Feature flags & preview code

New/breaking behavior ships **off by default** behind flags so you can opt in incrementally.
- Sass flags: `@use '@carbon/styles' with ($feature-flags: ('enable-v12-...': true))`.
- React: wrap a subtree in `<FeatureFlags enableV12Overflowmenu>…</FeatureFlags>` or the global API in `@carbon/feature-flags`.
- Web components: boolean attribute on `<cds-feature-flags>` / per-component flags (e.g. `enable-dialog-element`).

→ [`references/guides/feature-flags.md`](references/guides/feature-flags.md) ·
[`references/guides/preview-code.md`](references/guides/preview-code.md) ·
[`references/guides/experimental-code.md`](references/guides/experimental-code.md) ·
React [`FeatureFlags`](references/react/components/FeatureFlags.md).

## Finding a component

Component docs are one file per component, named after the component:
- React → `references/react/components/<Name>.md` (e.g. `DataTable.md`, `Dropdown.md`, `Modal.md`).
- Web components → `references/web-components/components/<name>.md` (e.g. `data-table.md`).
- Feature-flag behavior for a component is a sibling `*.featureflag.md` / `*.feature-flag.md`.

Each page opens with **Source code · Usage guidelines · Accessibility** links, then usage prose and
code examples. The **Component API** section points at the live, source-generated props/attributes
table (Storybook) — the exact prop list is not duplicated statically. Browse everything in
[`references/CONTENTS.md`](references/CONTENTS.md).

## Gotchas

- **Styles don't appear** → you didn't `@use '@carbon/styles'` (or a per-component partial), or Sass
  can't resolve `node_modules`. Carbon needs **Dart Sass**, not the deprecated `node-sass`.
- **Prefix mismatch** → JS `<ClassPrefix>` and Sass `$prefix` must be identical or styles won't apply.
- **Don't hard-code colors/spacing/type** — use tokens (`theme.$…`, `$spacing-0x`, `type-style(...)`),
  otherwise theming, Layer, and density break.
- **React vs web components**: APIs are parallel but **not identical** (props vs attributes/slots,
  `kind="danger--tertiary"` in React vs `danger-tertiary` in web components). Read the right page.
- **Experimental / `unstable_` / feature-flagged code can change** between minors — see preview-code.
- **v10 → v11** is a major migration (Sass modules with `@use`, new package names, token renames).
  → [`references/migration/v11.md`](references/migration/v11.md) and the per-element `migration/10.x-*.md` guides.

## Provenance

`references/` is converted from the **[carbon-design-system/carbon](https://github.com/carbon-design-system/carbon)**
monorepo — the colocated Storybook **MDX** (component usage), the per-package **READMEs** (the
foundational *elements*), and selected root `docs/` guides. Live Storybook `<Canvas>` demos and the
auto-generated `<ArgTypes>` prop tables can't be rendered statically, so each page keeps its
**Source code** link and a pointer to the live Storybook for the exact API. Every file retains a
`> Source:` link to its file on GitHub. Redistributed under the upstream **Apache-2.0 license** —
see [`references/LICENSE`](references/LICENSE).
