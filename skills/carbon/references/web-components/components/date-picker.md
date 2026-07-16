> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/date-picker/date-picker.mdx

# Date picker

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/date-picker)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/date-picker/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/date-picker/accessibility)

## Table of Contents

- [Overview](#overview)
  - [Simple date picker](#simple-datepicker)
  - [Range date picker](#range-datepicker)
  - [Skeleton state](#skeleton-state)
  - [AI label](#ai-label)
- [Component API](#component-api)
  - [Date picker `date-format`](#date-picker-date-format)
  - [Date picker `kind`](#date-picker-kind)
  - [Date picker `max-date`](#date-picker-max-date)
  - [Date picker `min-date`](#date-picker-min-date)
  - [Date picker `value`](#date-picker-value)
- [CDN](#cdn)
- [References](#references)
- [Feedback](#feedback)

## Overview

Date pickers allow users to select a single or a range of dates. Pickers are
used to display past, present, or future dates. The kind of date (exact,
approximate, memorable) you are requesting from the user will determine which
picker is best to use. Each picker’s format can be customized depending on
location or need. The `date-picker` component expects a `cds-date-picker-input`
as a child.

### Simple date picker

The simple date input provides the user with only a text field in which they can
manually input a date. It allows dates to be entered without adding unnecessary
interactions that come with the calendar menu or a dropdown.

### Range date picker

Calendar pickers default to showing today’s date when opened and only one month
is shown at a time. Calendar pickers allow users to navigate through months and
years, however they work best when used for recent or near future dates.

### Skeleton state

You can use the `cds-date-picker-skeleton` component to render a skeleton
variant of a date picker. This is useful to display while an initial date range
in your date picker is being fetched from an external resource like an API.

### AI label

## Component API

## `cds-date-picker`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## `cds-date-picker-input`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

### Date picker `date-format`

You can use the `date-format` attribute to change how the selected date is
displayed in the input. For a complete list of supported date formatting tokens,
please see the Flatpickr
[documentation](https://flatpickr.js.org/formatting/#date-formatting-tokens).

```html
<cds-date-picker date-format="Y-m-d">
  <cds-date-picker-input
    kind="single"
    placeholder="yyyy/mm/dd"></cds-date-picker-input>
</cds-date-picker>
```

### Date picker `kind`

There are three supported variations of `date-picker` in Carbon.

- `simple` will render a simple text input _without_ a calendar dropdown.
- `single` will render a a single text input _with_ a calendar dropdown.
- For `range` , two `cds-date-picker-input` will need to be provided as
  children.

For `simple` and `single`, set the `kind` attribute of the
`cds-date-picker-input` component to the desired version.

```html
<cds-date-picker>
  <cds-date-picker-input
    kind="single"
    placeholder="mm/dd/yyyy"></cds-date-picker-input>
</cds-date-picker>
```

For the `range`, the `kind` attributes should be set to `from` and `to`,
corresponding to the start and end dates of the range.

```html
<cds-date-picker>
  <cds-date-picker-input
    kind="from"
    label-text="Start date"
    placeholder="mm/dd/yyyy">
  </cds-date-picker-input>
  <cds-date-picker-input
    kind="to"
    label-text="End date"
    placeholder="mm/dd/yyyy">
  </cds-date-picker-input>
</cds-date-picker>
```

### Date picker `max-date`

Limits the date selection to any date before the date specified.

```html
<cds-date-picker max-date="09/15/2020">
  <cds-date-picker-input
    kind="single"
    placeholder="mm/dd/yyyy"></cds-date-picker-input>
</cds-date-picker>
```

### Date picker `min-date`

Works similarly to the `min-date` attribute. [See above](#date-picker-max-date).

```html
<cds-date-picker min-date="09/15/2025">
  <cds-date-picker-input
    kind="single"
    placeholder="mm/dd/yyyy"></cds-date-picker-input>
</cds-date-picker>
```

### Date picker `value`

By default the date picker will set the current date as its value. If you'd like
to start this at a different date, you can pass in a date string or date object.

```html
<cds-date-picker>
  <cds-date-picker-input
    kind="single"
    placeholder="mm/dd/yyyy"
    value="04/17/2025"></cds-date-picker-input>
</cds-date-picker>
```

## References

- The date picker component utilizes Flatpickr under the hood. We will pass any
  extra options down to the FlatPickr instance. For a full list of options,
  please see the [Flatpickr docs](https://flatpickr.js.org/options/)
- The `cds-date-picker-input` component takes in similar attributes to the
  `cds-text-input` component, such as `size` and `placeholder`. For more
  information on these attributes, check out the
  [text input](https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/?path=/docs/components-text-input--overview) page.

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0/date-picker.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/date-picker/date-picker.mdx).
