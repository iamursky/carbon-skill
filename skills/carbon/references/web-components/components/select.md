> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/select/select.mdx

# Select

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/select)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/select/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/select/accessibility)

## Table of Contents

- [Default state](#default-state)
- [Inline](#inline)
- [Skeleton](#skeleton)
- [AI Label](#ai-label)
- [Skeleton](#skeleton)
- [Component API](#component-api)
- [Feedback](#feedback)

## Default state

Carbon recommends that a select has an empty option selected by default.
Depending on the use case, this default behavior can be modified to be a
prefilled selection to the first option in the list, which is typically shown in
alphabetical order, or the prefilled selection could be a frequent or commonly
used option that is on the list.

To get a default empty selection on your select, do not use the `placeholder`
attribute in `cds-select`.

## Inline

## Skeleton

## Form item

If the select is part of a form, make sure to import and wrap the select with
`<cds-form-item>`

```javascript
import '@carbon/web-components/es/components/form/index.js';
```

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.58.0/form.min.js"></script>
```

```html
<cds-form-item>
  <cds-select
    id="id_for_label"
    helper-text="Optional helper text"
    label-text="Select"
    placeholder="Optional placeholder text">
    <cds-select-item-group label="Category 1">
      <cds-select-item value="all">Option 1</cds-select-item>
      <cds-select-item value="cloudFoundry">Option 2</cds-select-item>
    </cds-select-item-group>
    <cds-select-item-group label="Category 2">
      <cds-select-item value="staging">Option 3</cds-select-item>
      <cds-select-item value="dea">Option 4</cds-select-item>
      <cds-select-item value="router">Option 5</cds-select-item>
    </cds-select-item-group>
  </cds-select>
</cds-form-item>
```

## `<cds-select>` attributes, properties and events

## AI Label

## Component API

## `cds-select`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## `cds-select-item-group`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## `cds-select-item`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.58.0/select.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/select/select.mdx).
