> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/ContentSwitcher/ContentSwitcher.mdx

# Content Switcher

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/ContentSwitcher)
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
  - [ContentSwitcher `className`](#contentswitcher-classname)
  - [ContentSwitcher `light`](#contentswitcher-light)
  - [ContentSwitcher `onChange`](#contentswitcher-onchange)
  - [ContentSwitcher `selectedIndex`](#contentswitcher-selectedindex)
  - [ContentSwitcher `selectionMode`](#contentswitcher-selectionmode)
  - [Switch `className`](#switch-classname)
  - [Switch `disabled`](#switch-disabled)
  - [Switch `index`, `name` and `text`](#switch-index-name-and-text)
- [References](#references)
  - [Accessibility concerns](#accessibility-concerns)
- [Feedback](#feedback)

## Overview

Content switchers allow users to toggle between two or more content sections
within the same space on screen. Only one content section is shown at a time.
Create Switch components for each section in the content switcher.

## Icon Only

## Icon Only With Layer

## With Layer

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

### ContentSwitcher `className`

The className prop passed into `ContentSwitcher` will be forwarded along to the
underlying wrapper `div.cds--content-switcher` element. This is useful for
specifying a custom class name for layout.

```jsx
<ContentSwitcher className="some-class">...</ContentSwitcher>
```

### ContentSwitcher `light`

In certain circumstances, a `ContentSwitcher` will exist on a container element
with the same background color. To improve contrast, set the `light` property to
toggle the light variant of the `ContentSwitcher`.

```jsx
<ContentSwitcher light onChange={() => {}}>
  ...
</ContentSwitcher>
```

### ContentSwitcher `onChange`

This required prop specifies a function to run when the selection of the
`ContentSwitcher` changes.

```jsx
<ContentSwitcher
  onChange={() => {
    /* Code to run on change */
  }}>
  ...
</ContentSwitcher>
```

### ContentSwitcher `selectedIndex`

This prop specifies which `ContentSwitcher` index should be selected. This
number defaults to `0`, and updates to this prop will update the selected
switch.

```jsx
<ContentSwitcher selectedIndex={2} onChange={() => {}}>
  <Switch name="one" text="First section" />
  <Switch name="two" text="Second section" />
  <Switch name="three" text="Third section" />
</ContentSwitcher>
```

### ContentSwitcher `selectionMode`

By default, when a `ContentSwitcher` is focused and an arrow key is pressed, the
selection is updated immediately and the `onChange` is fired. In some cases, it
is preferable to change `selectedIndex` only once a selection has been made. To
do this, set `selectionMode` to `manual`, and the `onChange` will only fire when
a selection is made.

```jsx
<ContentSwitcher
  selectionMode="manual"
  onChange={() => {
    console.log('change');
  }}>
  <Switch name="one" text="First section" />
  <Switch name="two" text="Second section" />
  <Switch name="three" text="Third section" />
</ContentSwitcher>
```

### Switch `className`

The className prop passed into `Switch` will be forwarded along to the
underlying wrapper `button` element.

```jsx
<ContentSwitcher onChange={() => {}}>
  <Switch className="switch-one" />
  <Switch className="switch-two " />
</ContentSwitcher>
```

### Switch `disabled`

The `ContentSwitcher` can be disabled by passing `disabled` to the `Switch`
elements directly.

```jsx
<ContentSwitcher onChange={() => {}}>
  <Switch disabled name="one" text="First section" />
  <Switch disabled name="two" text="Second section" />
  <Switch disabled name="three" text="Third section" />
</ContentSwitcher>
```

### Switch `index`, `name` and `text`

These are the values that will be returned in the `onChange` call.

```jsx
<ContentSwitcher
  onChange={(obj) => {
    let { index, name, text } = obj;
    alert(`index: ${index} ||  name: ${name} || text: ${text}`);
  }}>
  <Switch name="one" text="First section" />
  <Switch name="two" text="Second section" />
  <Switch name="three" text="Third section" />
</ContentSwitcher>
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
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/ContentSwitcher/ContentSwitcher.mdx).
