> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/tooltip/definition-tooltip.mdx

# DefinitionTooltip

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/tooltip)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/tooltip/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/tooltip/accessibility)

## Table of Contents

- [Overview](#overview)
  - [Customizing the content of a definition tooltip](#customizing-the-content-of-a-definition-tooltip)
  - [Tooltip alignment](#tooltip-alignment)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

The `cds-definition-tooltip` component is used to provide additional information
about a particular term or phrase in text content. It is similar to a
`cds-tooltip` component but has fewer alignment options and has a slightly
different interaction pattern.

The `cds-definition-tooltip` is made up of two parts: a term and the tooltip
itself. You can customize the contents of the tooltip through the `definition`
slot. You can customize the term by providing your own slotted content to this
component.

### Customizing the content of a definition tooltip

You can customize the content of the tooltip through the `definition` slot. This
slot allows you to provide text or your own custom elements to be rendered as a
definition for your term.

Note: content passed into the `definition` slot must not contain any interactive
content. If you pass in interactive content, it's semantics will not be
available to users of screen reader software.

### Tooltip alignment

The `align` attribute allows you to specify where your content should be placed
relative to the tooltip. For example, if you provide `align="top"` to the
`cds-definition-tooltip` component then the tooltip will render above your
component. Similarly, if you provide `align="bottom"` then the tooltip will
render below your component.

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0/tooltip.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/tooltip/definition-tooltip.mdx).
