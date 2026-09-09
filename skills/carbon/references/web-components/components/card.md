> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/card/card.mdx

# Card

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/card)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/card/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/card/accessibility)

## Table of Contents

- [Overview](#overview)
- [Clickable](#clickable)
- [Disabled](#disabled)
- [Productive and Expressive](#productive-and-expressive)
- [With AI Label](#with-ai-label)
- [With Flush Body](#with-flush-body)
- [With Header Actions](#with-header-actions)
- [With Header Media](#with-header-media)
- [With Horizontal Media](#with-horizontal-media)
- [With Icon](#with-icon)
- [With Media](#with-media)
- [With Title Leading Icon](#with-title-leading-icon)
- [With Title Media](#with-title-media)
- [With Title Trailing Icon](#with-title-trailing-icon)
- [With Truncated Title](#with-truncated-title)
- [With Video](#with-video)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

The `cds-card` component is a composable container built from ten custom
elements. The root `cds-card` element owns layout and interactivity while child
elements handle each visual region.

## Clickable

A clickable card makes the entire surface interactive. Set `aria-label` or
`aria-labelledby` to provide an accessible name. When `href` is set the card
renders as an `<a>` element; otherwise it uses `role="button"` with full
keyboard support (Enter / Space).

## Disabled

## Productive and Expressive

The `density` attribute controls the heading typography token used inside the
card title.

## With AI Label

Place `cds-ai-label` in the `decorator` slot. The card automatically adds the
`has-ai-label` attribute and applies the AI gradient border treatment.

## With Flush Body

`is-flush` on `cds-card-body` removes all padding so content sits edge-to-edge.

## With Header Actions

`cds-card-actions` renders action icon buttons in the header and automatically
collapses overflow items into a `cds-overflow-menu`.

## With Header Media

`cds-card-header-media` renders a full-width icon or image above the title row.

## With Horizontal Media

Set `horizontal` on `cds-card`. `cds-card-media` will self-assign to the `media`
slot and the card renders a flex row layout. Use `media-position="end"` to move
media to the right.

## With Icon

Override the default `ArrowRight` icon in the clickable footer via the
`footer-icon` slot.

## With Media

## With Title Leading Icon

## With Title Media

`cds-card-title-media` places a media element to the left of the title row.

## With Title Trailing Icon

## With Truncated Title

Use `title-truncate` to clip long titles. A boolean attribute gives single-line
ellipsis; a numeric value sets `-webkit-line-clamp` for multi-line truncation.

## With Video

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.63.0/card.min.js"></script>
```

## Feedback

Help us improve this component by submitting
[feedback](https://github.com/carbon-design-system/carbon/issues/new/choose).
