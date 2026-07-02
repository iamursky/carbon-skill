> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/content-switcher/content-switcher.mdx

# Content switcher

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/content-switcher)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/content-switcher/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/content-switcher/accessibility)

## Table of Contents

- [Overview](#overview)
- [Icon Only](#icon-only)
- [Icon Only With Layer](#icon-only-with-layer)
- [With Layer](#with-layer)
- [Component API](#component-api)
- [CDN](#cdn)
- [Accessibility concerns](#accessibility-concerns)
- [References](#references)
- [Feedback](#feedback)

## Overview

Content switchers allow users to toggle between two or more content sections
within the same space on screen. Only one content section is shown at a time.
Create Switch components for each section in the content switcher.

## Icon Only

## Icon Only With Layer

## With Layer

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

### ContentSwitcher `onChange`

You can use the `cds-content-switcher-selected` or
`cds-content-switcher-beingselected` custom events to call a custom function for
event handling.

```javascript
document.addEventListener('cds-content-switcher-selected', (event) => {
  const { currentTarget } = event;
  const { detail } = event as CustomEvent;
  const { evt } = detail;
  console.log('details:', currentTarget, evt);
});
```

### Switch `disabled`

You can disable the content switcher items by adding the `disabled` attribute to
`cds-content-switcher-item` elements directly.

```html
<cds-content-switcher>
  <cds-content-switcher-item disabled value="all" name="one">
    First section
  </cds-content-switcher-item>
  <cds-content-switcher-item disabled value="cloudFoundry" name="two">
    Second section
  </cds-content-switcher-item>
  <cds-content-switcher-item disabled value="staging" name="three">
    Third section
  </cds-content-switcher-item>
</cds-content-switcher>
```

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.58.0/content-switcher.min.js"></script>
```

## References

### Accessibility concerns

Each content switcher tab must have a unique title that clearly describes the
content panel. This is particularly helpful for users of assistive technologies
so they have the necessary information to efficiently navigate the content.

Content authors need to ensure the content that is added to the tab panel is
accessible. For example, if you add an image to the panel you need to include
alternative text to pass accessibility testing.

[W3C WAI-ARIA Tab Design Pattern](https://www.w3.org/TR/wai-aria-practices-1.1/#tabpanel)
covers the usage of ARIA names, state and roles, as well as the expected
keyboard interactions.

[Carbon Usage Guidelines](https://www.carbondesignsystem.com/components/content-switcher/usage/)

## Feedback

Help us improve this component by providing feedback, asking questions, and
leaving any other comments on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/content-switcher/content-switcher.mdx).
