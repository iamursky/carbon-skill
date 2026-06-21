> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/icon-button/icon-button.mdx

# Icon button

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/icon-button)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/button/usage)

## Table of Contents

- [Overview](#overview)
- [Component API](#component-api)
- [CDN](#cdn)
- [Feedback](#feedback)

The `icon-button` component is useful when you have a button where the content
is an icon. In this situation, it's important that the button itself is labeled
in a way that can be understandable by mouse, keyboard, and screen readers. As a
result, this component makes it easy to create accessible icon buttons.

```javascript
import '@carbon/web-components/es/components/icon-button/index.js';
import Edit16 from '@carbon/icons/es/edit/16.js';

function App() {
  return html`<cds-icon-button>
    ${iconLoader(Edit16, { slot: 'icon' })}
    <span slot="tooltip-content">label</span>
  </cds-icon-button>`;
}
```

## Kind

Icon buttons can take the form of Primary, Secondary, Tertiary, and Ghost but
most commonly will be styled as primary or ghost buttons. Icon only buttons do
not support Danger, Danger tertiary, or Danger ghost.

## Alignment

The `align` attribute allows you to specify where your content should be placed
relative to the `icon-button`. For example, if you provide `align="top"` to the
`icon-button` component then the tooltip will render above your component.
Similarly, if you provide `align="bottom"` then the tooltip will render below
your component.

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.57.0/icon-button.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/icon-button/icon-button.mdx).
