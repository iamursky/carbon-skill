> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/contained-list/contained-list.mdx

# Contained list

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/contained-list)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/contained-list/usage)

## Table of Contents

- [Overview](#overview)
- [Search](#search)
  - [Expandable Search](#expandable-search)
  - [Persistent Search](#persistent-search)
- [Disclosed](#disclosed)
- [With Actions](#with-actions)
- [With Icons](#with-icons)
- [With Interactive Items](#with-interactive-items)
- [With Interactive Items and Actions](#with-interactive-items-and-actions)
- [With List Title Decorators](#with-list-title-decorators)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

> **Note:** When using multiple consecutive `on-page` contained lists,
> `$spacing-05` can be added to maintain proper spacing between 2 consecutive
> on-page lists:
>
> ```css
> cds-contained-list[kind='on-page'] + cds-contained-list[kind='on-page'] {
>   margin-block-start: 1rem;
> }
> ```

## Search

### Expandable Search

Within the Contained List you can pass in a `cds-search` component with the
`expandable` attribute within the `action` slot. The expandable search will give
you the capability to expand and collapse the search bar within the title.
However, we do not support passing in the expandable `cds-search` within the
title action slot while passing in a regular `cds-search` component as a child
at the same time. If this happens, the expandable search in the title will
override any other `cds-search` passed in as a child. To prevent this potential
conflict, we have added functionality to support both designs and both use
cases. Please see [Persistent Search](#persistent-search) docs below.

### Persistent Search

We have added in the capability to pass down the `cds-search` component as a
child of `cds-contained-list`. The `cds-search` component itself is not a slot
but does render with specific styling such that the search bar appears below the
Contained List title as opposed to rendering inline. If you would like the
Search to render inline to the Contained List title, please see the
[Expandable Search](#expandable-search) docs above. The `cds-search` component
will also remain persistent under the title, so that it remains visible on
scroll, when there are many list items passed in.

## Disclosed

## With Actions

## With Icons

## With Interactive Items

## With Interactive Items and Actions

## With List Title Decorators

## Component API

### `cds-contained-list`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

### `cds-contained-list-item`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0-rc.0/contained-list.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/contained-list/contained-list.mdx).
