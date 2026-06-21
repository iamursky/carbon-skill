> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/ClassPrefix/ClassPrefix.mdx

# ClassPrefix

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/ClassPrefix)

## Table of Contents

- [Overview](#overview)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

The `ClassPrefix` component is used to change the prefix in the classes used by
components in Carbon.

By default, the prefix used by components is `cds`. However, you can change this
prefix in Sass and coordinate that change to React using the `ClassPrefix`
component.

In Sass, you can customize this prefix by writing the following:

```scss
@use '@carbon/react' with (
  $prefix: 'custom'
);
```

Similarly, you can configure `scss/config` directly:

```scss
@use '@carbon/react/scss/config' with (
  $prefix: 'custom'
);
```

In React, you use `ClassPrefix` at the top-level of your project and specify the
prefix with the `prefix` prop:

```jsx
import { ClassPrefix } from '@carbon/react';

export default function MyApp() {
  return (
    <ClassPrefix prefix="custom">
      <Page />
    </ClassPrefix>
  );
}
```

To _get_ the prefix, use

usePrefix

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/ClassPrefix/ClassPrefix.mdx).
