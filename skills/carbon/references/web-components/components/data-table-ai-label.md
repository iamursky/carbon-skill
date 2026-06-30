> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/data-table/stories/data-table-ai-label.mdx

# AI Label in DataTable

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/ai-label)
&nbsp;|&nbsp;
[AILabel release status](https://airtable.com/appCAqlGVN8tRUbAp/shr71ZyLlIGORz3Vh/tblHqPusgkK8hIeHo)

## Table of Contents

- [Overview](#overview)
- [AI Label anatomy](#ai-label-anatomy)
- [Using AI Label in DataTable](#using-ai-label-in-datatable)
  - [Using as a column header](#using-as-a-column-header)
  - [Using in a row](#using-in-a-row)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

The `cds-table` component supports placing a `cds-ai-label` in both the column
header and row.

## AI Label anatomy

The `AI Label` itself is a button that acts as a `toggle-tip` trigger. To
construct the contents of the `AI Label` callout, you can place the desired
elements as a child of `cds-ai-label`, like so:

```html
<cds-ai-label size="mini" alignment="bottom-left">
  <div slot="body-text">{Content Here}</div>
</cds-ai-label>
```

The `AI Label` also supports the rendering of an action bar at the bottom of the
callout. To achieve this, you can add elements with `slot="actions"` inside the
`slot="body-text"` element

```html
<cds-ai-label size="mini" alignment="bottom-left">
  <div slot="body-text">
    {Content Here} {Optional AI Label action bar}
    <cds-icon-button kind="ghost" slot="actions" size="lg">
      <cds-icon .icon="${View16}" slot="icon"></cds-icon>
      <span slot="tooltip-content"> View </span>
    </cds-icon-button>
    <cds-icon-button kind="ghost" slot="actions" size="lg">
      <cds-icon .icon="${FolderOpen16}" slot="icon"></cds-icon>
      <span slot="tooltip-content"> Open folder</span>
    </cds-icon-button>
    <cds-icon-button kind="ghost" slot="actions" size="lg">
      <cds-icon .icon="${Folders16}" slot="icon"></cds-icon>
      <span slot="tooltip-content"> Folders </span>
    </cds-icon-button>
    <cds-ai-label-action-button>View details</cds-ai-label-action-button>
  </div>
</cds-ai-label>
```

## Using `AI Label` in `DataTable`

### Using as a column header

To use a `AI Label` inside a column header, you'll need to add an `cds-ai-label`
component to the appropriate `cds-table-header-cell`.

```html
<cds-table-header-cell>
  Attached groups
  <cds-ai-label alignment="bottom-left">
    <div slot="body-text">{Content Here}</div>
  </cds-ai-label>
</cds-table-header-cell>
```

### Using in a row

To use a `AI Label` inside a `DataTable` row, you'll need to pass in your
`ai-label` component to `cds-table-row`:

```html
<cds-table-row>
  <cds-ai-label alignment="bottom-left">
    <div slot="body-text">{Content Here}</div>
  </cds-ai-label>
  <cds-table-cell>Load Balancer 1</cds-table-cell>
  <cds-table-cell>HTTP</cds-table-cell>
  ...
</cds-table-row>
```

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.58.0-rc.0/ai-label.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/data-table/stories/data-table-ai-label.mdx).
