> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/IdPrefix/IdPrefix.mdx

# Prefix

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/ClassPrefix)

## Table of Contents

- [Overview](#overview)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

The `IdPrefix` component is used to change the prefix applied to the
automatically generated `id` attributes placed on certain DOM elements.

This component is intended to be used in limited cases, primarily only if you
have id conflicts when using v10 and v11 packages at the same time during
migration.

In React, you can use `IdPrefix` anywhere in your component tree and specify the
prefix with the `prefix` prop. Most often it's used in the project root wrapping
the entire project:

```jsx
import { IdPrefix } from '@carbon/react';

export default function MyApp() {
  return (
    <IdPrefix prefix="custom">
      <Page />
    </IdPrefix>
  );
}
```

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/ClassPrefix/ClassPrefix.mdx).
