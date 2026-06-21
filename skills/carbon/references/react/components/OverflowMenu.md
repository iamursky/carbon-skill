> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/OverflowMenu/OverflowMenu.mdx

# OverflowMenu

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/OverflowMenu)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/overflow-menu/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/overflow-menu/accessibility)

## Table of Contents

- [Overview](#overview)
  - [`data-floating-menu-container`](#data-floating-menu-container)
- [Render Custom Icon](#render-custom-icon)
- [Customizing the tooltip](#customizing-the-tooltip)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

The overflow menu component is a clickable element that contains additional
options that are available to the user, but there is a space constraint.

### `data-floating-menu-container`

`OverflowMenu` uses React Portals to render the overflow menu into the DOM. To
determine where in the DOM the menu will be placed, it looks for a parent
element with the `data-floating-menu-container` attribute. If no parent with
this attribute is found, the menu will be placed on `document.body`.

## Render Custom Icon

## Customizing the tooltip

The `OverflowMenu` uses an `IconButton` under the hood, which means it can
accept any props that an `IconButton` can receive and will successfully pass
those forward. To modify the tooltip's alignment, you may make use of the
`align` property as described in the `IconButton` props:

```jsx
<OverflowMenu aria-label="overflow-menu" align="bottom">
  <OverflowMenuItem itemText="Stop app" />
  <OverflowMenuItem itemText="Restart app" />
  <OverflowMenuItem itemText="Rename app" />
  <OverflowMenuItem itemText="Clone and move app" disabled requireTitle />
  <OverflowMenuItem itemText="Edit routes and access" requireTitle />
  <OverflowMenuItem hasDivider isDelete itemText="Delete app" />
</OverflowMenu>
```

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/OverflowMenu/OverflowMenu.mdx).
