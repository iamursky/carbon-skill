> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/combo-button/combo-button.mdx

# ComboButton

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/combo-button)

## Table of Contents

- [Overview](#overview)
- [With Danger](#with-danger)
- [With Icons](#with-icons)
- [Menu Alignment](#menu-alignment)
- [Experimental Auto Align](#experimental-auto-align)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

A `cds-menu-button` can be used to offer additional, secondary actions in a
disclosed list next to the primary action. These additional actions must be
`cds-menu-item` passed as `children`. The primary action's label is passed as
`label`.

```html
<cds-combo-button label="Primary action">
  <cds-menu>
    <cds-menu-item label="Second action"></cds-menu-item>
    <cds-menu-item label="Third action"></cds-menu-item>
    <cds-menu-item label="Fourth action"></cds-menu-item>
  </cds-menu>
</cds-combo-button>
```

## With Icons

## With Danger

## Menu Alignment (experimental)

The `menu-alignment` attribute enables you to define the placement of the Menu
in relation to the `cds-menu-button`. For instance, setting
`menu-alignment="top"` on the `cds-menu-button` will render the Menu above the
button.

If it seems your specified `menu-alignment` isn't working, it's because we
prioritize ensuring the Menu remains visible. We calculate the optimal position
to display the Menu in case the provided `menu-alignment` obscures it.

We encourage you to play around in the Storybook Default stories to better
understand the `menu-alignment` attribute.

## Experimental Auto Align

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0-rc.0/combo-button.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/combo-button/combo-button.mdx).
