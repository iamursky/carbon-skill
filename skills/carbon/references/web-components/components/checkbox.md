> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/checkbox/checkbox.mdx

# Checkbox

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/checkbox)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/checkbox/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/checkbox/accessibility)

## Table of Contents

- [Overview](#overview)
- [Horizontal](#horizontal)
- [Single](#single)
- [Skeleton state](#skeleton-state)
- [AI Label](#With-ai-label)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

You can build a checkbox using the `checkbox` in combination with a
`<cds-checkbox-group>` element to group controls and `legend-text` attribute for
the label.

## Horizontal

## Single

## Skeleton state

You can use the `cds-checkbox-skeleton` component to render a skeleton variant
of a checkbox. This is useful to display while content in your checkbox is being
fetched from an external resource like an API.

## With AI label

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

### Checkbox `checked`

You can use the `checked` attribute to specify weather a checkbox is checked by
default or not on page load.

```html
<cds-checkbox checked=""></cds-checkbox>
```

### Checkbox `id`

The `id` attribute should be used to provide each checkbox input with a unique
id.

```html
<cds-checkbox id="checkbox"></cds-checkbox>
```

### Checkbox `label-text`

The `label-text` attribute should be used to provide a label that describes the
checkbox input that is being exposed to the user.

```html
<cds-checkbox label-text="Checkbox label"></cds-checkbox>
```

### Checkbox `onChange`

You can use the `cds-checkbox-changed` custom event to call a custom function
for event handling.

```javascript
document.addEventListener('cds-checkbox-changed', (event) => {
  const { currentTarget } = event;
  const { detail } = event as CustomEvent;
  const { evt } = detail;
  console.log('checkbox clicked', currentTarget, evt);
});
```

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0-rc.0/checkbox.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/checkbox/checkbox.mdx).
