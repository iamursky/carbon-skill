> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/Icons/Icons.mdx

# Icons

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/Icons)
&nbsp;|&nbsp;
[Usage guidelines](https://carbondesignsystem.com/elements/icons/usage/)

## Table of Contents

- [Overview](#overview)
  - [Customizing icon size with `rem` units](#customizing-icon-size-with-rem-units)
- [Feedback](#feedback)

## Overview

This guide demonstrates how to make icons scale using `rem` units, without
requiring any changes to the component’s default configuration. In Carbon, icons
accept a `size` prop that can be a number or a string. Numbers are unitless and
interpreted as pixels. This approach is effective for most scenarios, but if
your goal is to improve accessibility or ensure that icons respond to changes in
the browser’s font-size, using a string with `rem` units offers greater
adaptability.

### Customizing icon size with `rem` units

To create scalable, responsive icons, you can pass a `rem` value to the `size`
prop:

```jsx
<Edit size="1rem" />
```

Some components use a `renderIcon` prop to display icons internally.

In these cases, you can still pass a responsive size by using an inline function
that returns the icon:

```jsx
<MenuItem renderIcon={(props) => <Edit size="1rem" {...props} />} />
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/Icons/Icons.mdx).
