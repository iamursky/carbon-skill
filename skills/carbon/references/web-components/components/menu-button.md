> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/menu-button/menu-button.mdx

# MenuButton

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/menu-button)
&nbsp;|&nbsp;

## Table of Contents

- [Overview](#overview)
- [With Danger](#with-danger)
- [With Dividers](#with-dividers)
- [With icons](#with-icons)
- [Menu Alignment](#menu-alignment)
  - [Experimental Auto Align](#experimental-auto-align)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

A `cds-menu-button` can be used to group a set of actions that are related.
These actions must be `cds-menu-item` passed as child elements. The trigger
buttons's label is passed as `label`.

#### With Danger

#### With Dividers

#### With Icons

## Menu Alignment

The `menu-alignment` attribute enables you to define the placement of the menu
in relation to the menu button. For instance, setting `menu-alignment="top"` on
the menu button will render the menu above the button.

If it seems your specified `menu-alignment` isn't working, it's because we
prioritize ensuring the menu remains visible. We calculate the optimal position
to display the menu in case the provided `menu-alignment` obscures it.

We encourage you to play around in the Storybook Default stories to better
understand the `menu-alignment` attribute.

## Experimental Auto Align

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0-rc.0/menu-button.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/menu-button/menu-button.mdx).
