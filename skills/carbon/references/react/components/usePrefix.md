> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/internal/usePrefix.mdx

# usePrefix

[Source code](https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/internal/usePrefix.ts)

## Overview

A hook that returns the prefix used in our classes.

## Examples

```js
import { usePrefix } from '@carbon/react';

function ExampleComponent() {
  const prefix = usePrefix();
}
```

Typically, `usePrefix` will be used alongside `classnames`.

```js
import { usePrefix } from '@carbon/react';
import { cx } from 'classnames';

function ExampleComponent() {
  const prefix = usePrefix();
  const className = cx(`${prefix}--custom-component`);
}
```

To _set_ the prefix, use

ClassPrefix
