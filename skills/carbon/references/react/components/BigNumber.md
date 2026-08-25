> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/BigNumber/BigNumber.mdx

# BigNumber

## Table of Contents

- [Overview](#overview)
- [Example usage](#example-usage)
- [Component API](#component-api)

## Overview

BigNumber is used to display large values in a small area. The display of values
can be the value itself, or grouped in a `numerator/denominator` fashion.
Control over the total fraction decimals displayed as well as how the
values/totals are displayed are done via a locale prop. Other optional props
allow control over size, truncation, if the value is a percentage, the addition
of a button as well as tooltip functionality. The default locale is English
(`en-US`) if one is not provided or if the provided one is not supported.

[Supported locales](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#locales)

## Example usage

## Component API

```jsx
<Controls />
```
