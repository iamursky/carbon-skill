> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/ComboButton/ComboButton.mdx

# ComboButton

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/ComboButton)

## Table of Contents

- [Overview](#overview)
- [With Icons](#with-icons)
- [With Danger](#with-danger)
- [Menu Alignment (experimental)](#menu-alignment-experimental)
- [Experimental Auto Align](#experimental-auto-align)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

A `ComboButton` can be used to offer additional, secondary actions in a
disclosed list next to the primary action. These additional actions must be
`MenuItem`s passed as `children`. The primary action's label is passed as
`props.label`.

```jsx
<ComboButton label="Primary action">
  <MenuItem label="Second action" />
  <MenuItem label="Third action" />
  <MenuItem label="Fourth action" />
</ComboButton>
```

## With Icons

## With Danger

## Menu Alignment (experimental)

The `menuAlignment` prop enables you to define the placement of the Menu in
relation to the `ComboButton`. For instance, setting `menuAlignment="top"` on
the `ComboButton` will render the Menu above the button.

If it seems your specified `menuAlignment` isn't working, it's because we
prioritize ensuring the Menu remains visible. We calculate the optimal position
to display the Menu in case the provided `menuAlignment` obscures it.

We encourage you to play around in the Storybook Default stories to better
understand the `menuAlignment` prop.

## Experimental Auto Align

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/ComboButton/ComboButton.mdx).
