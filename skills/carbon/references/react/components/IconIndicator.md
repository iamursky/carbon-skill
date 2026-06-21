> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/IconIndicator/IconIndicator.mdx

# IconIndicator

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/IconIndicator)
&nbsp;

## Table of Contents

- [Overview](#overview)
- [Kind](#kind)
- [Size](#size)
- [Customizing the label](#customizing-the-label)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

The `IconIndicator` component is useful for communicating severity level
information to users. The shapes and colors, communicate severity that enables
users to quickly assess and identify status and respond accordingly.

```jsx
import { preview__IconIndicator as IconIndicator } from '@carbon/react';

function ExampleComponent() {
  return (
    <IconIndicator kind="failed" label="Failed">
  );
}
```

## Kind

Icon indicators can take the form of failed, caution major, caution minor,
undefined, succeeded, normal, in-progress incomplete, not started, pending,
unknown, and informative.

## Size

Icon indicators have two size options 16 and 20. The default is 16.

## Customizing the label

You can set a string to customize the label of the Icon indicator.

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/IconIndicator/IconIndicator.mdx).
