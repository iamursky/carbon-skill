> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/shape-indicator/shape-indicator.mdx

# Shape indicator

## Table of Contents

- [Overview](#overview)
  - [Kind](#kind)
  - [Size](#size)
  - [Compact mode](#compact-mode)
  - [Customizing the label](#customizing-the-label)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

## Kind

Shape indicators can take the form of failed, critical, high, medium, low,
cautious, undefined, stable, informative, incomplete, and draft.

## Size

Shape indicators have two text size options 12 and 14. The default is 12.

## Compact mode

When the `compact` attribute is set to `true`, the shape indicator displays only
the shape with the label shown in a tooltip on hover/focus. This is useful when
space is limited or when you want to display multiple indicators in a space
constrained layout.

```html
<cds-shape-indicator kind="failed" label="Failed" compact></cds-shape-indicator>
```

## Customizing the label

You can set a string to customize the label of the Shape indicator.

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0-rc.0/shape-indicator.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/shape-indicator/shape-indicator.mdx).
