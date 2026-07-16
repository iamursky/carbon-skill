> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/icon/icon.mdx

# Icon

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/icon)
&nbsp;|&nbsp;
[Usage guidelines](https://carbondesignsystem.com/elements/icons/usage/)

## Table of Contents

- [Overview](#overview)
- [Feedback](#feedback)

## Overview

The `cds-icon` component can render icons both from Javascript imports, as well
as inline SVG elements.

## With Javascript

```html
<script>
  import Add16 from '@carbon/icons/es/add/16.js';
  import ChevronRight16 from '@carbon/icons/es/chevron--right/16.js';
  import Search16 from '@carbon/icons/es/search/16.js';
</script>

<cds-icon .icon="${Add16}"></cds-icon>
<cds-icon .icon="${ChevronRight16}"></cds-icon>
<cds-icon .icon="${Search16}"></cds-icon>
```

## With Custom SVG

## With Custom Classes

## With ARIA label

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0/icon.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/icons/icons.mdx).
