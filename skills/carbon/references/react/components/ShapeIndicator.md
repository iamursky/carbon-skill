> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/ShapeIndicator/ShapeIndicator.mdx

# ShapeIndicator

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/ShapeIndicator)
&nbsp;

## Table of Contents

- [Overview](#overview)
- [Kind](#kind)
- [Text Size](#text-size)
- [Compact mode](#compact-mode)
- [Customizing the label](#customizing-the-label)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

`ShapeIndicator`

```jsx
import { preview__ShapeIndicator as ShapeIndicator } from '@carbon/react';

function ExampleComponent() {
  return (
    <ShapeIndicator kind="failed" label="Failed">
  );
}
```

## Kind

Shape indicators can take the form of failed, critical, high, medium, low,
cautious, undefined, stable, informative, incomplete, and draft.

## Text Size

Shape indicators have two text size options 12 and 14. The default is 12.

## Compact mode

When the `compact` prop is set to `true`, the shape indicator displays only the
shape with the label shown in a tooltip on hover/focus. This is useful when
space is limited or when you want to display multiple indicators in a space
constrained layout.

```jsx
<ShapeIndicator kind="failed" label="Failed" compact />
```

## Customizing the label

You can set a string to customize the label of the Shape indicator.

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/ShapeIndicator/ShapeIndicator.mdx).
