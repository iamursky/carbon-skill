> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/heading/heading.mdx

# Heading

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/heading)

## Table of Contents

- [Overview](#overview)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

For people using screen readers, headings in HTML are one of the most common
ways to navigate a page. Correctly using headings and levels helps with
understanding a page and its hierarchy and can be used to jump between sections
on a page.

Normally, in a component you would have to specify the heading level manually.
This can become problematic if your component is used in various parts of a page
where the heading level needs to be different.

To help address this, the `heading` component will automatically infer the
appropriate heading level without you having to manually specify it. To do this,
you use the `section` component for each section of your page. Every `heading`
component in that `section` will use the correct heading level.

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.57.0/heading.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback through, asking questions
on Slack, or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/heading/heading.mdx).
