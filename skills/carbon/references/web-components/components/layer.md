> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/layer/layer.mdx

# Layer

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/layer)

## Table of Contents

- [Overview](#overview)
- [Setting a custom level](#setting-a-custom-level)
- [With background](#with-background)
- [Get the current layer](#get-the-current-layer)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

The `cds-layer` component is used to render components on different layers. Each
layer has a specific set of token values associated with it. You can use these
tokens directly, or use contextual tokens from our styles package like `$layer`
or `$field`.

The layer component accepts child elements. Each child of a layer component is
rendered using the layer tokens at that layer. Layer components can be nested
indefinitely, but the token sets typically end after 3 layers.

```html
<cds-layer>
  <div>Test component</div>
  <cds-layer>
    <div>Test component</div>
    <cds-layer>
      <div>Test component</div>
    </cds-layer>
  </cds-layer>
</cds-layer>
```

## With Background

The layer component updates layer tokens at each level and theme. When you add
the `with-background` attribute, it automatically sets a background color using
the `$layer-background` token. Without it, you can manually set the background
with `background-color: $layer-background`.

## Setting a custom level

You can override the `level` of a layer if you would like to change the
presentation of a layer in your application. This is particularly helpful if you
would like to reset the layer level back to `0` or if you want to make sure a
part of a page always renders in a certain level.

To do this, you can use the `level` attribute:

## Get the current layer

If you are building a component and would like to know what layer the component
resides within, you can use the `cds-user-layer` custom event.

This event returns a custom event with details of current element, as well as
its layer:

```javascript
document.addEventListener(`cds-use-layer`, (e) => {
  const { layer, level } = (e as any).detail;
  layer.querySelector('.example-layer-test-component.use-layer').innerText =
    `The current layer level is: ${level + 1}`;
});
```

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0-rc.0/layer.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/layer/layer.mdx).
