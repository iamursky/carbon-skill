> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/ContextMenu/useContextMenu.mdx

# useContextMenu

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/ContextMenu)

## Table of Contents

- [Overview](#overview)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

The `useContextMenu` hook is meant to be used in conjunction with `Menu` (see
this [component's documentation](https://github.com/carbon-design-system/carbon/blob/main/docs/components-menu--default) for more
details). It provides an easy way to generate the necessary props for `Menu`.

By default, it will listen to the `contextmenu` event on `document`. In most
cases you'll want to restrict a context menu to a certain element or group of
elements only. You can pass that element as the argument for `useContextMenu`.

```jsx
function SomeComponent() {
  const el = useRef(null);
  const menuProps = useContextMenu(el);

  return (
    <>
      <div ref={el}>…</div>

      <Menu {...menuProps}>
        <MenuItem label="Cut" />
        <MenuItem label="Copy" />
        <MenuItem label="Paste" />
      </Menu>
    </>
  );
}
```

Be aware that the following props are not set by `useContextMenu` and can
therefore be configured by the user:

- className
- label
- size
- target

## Component API

```js
// returns an object with 'x', 'y', 'open' and 'onClose' set accordingly intended
// to be passed as pros to the <Menu> component.
const menuProps = useContextMenu(
  // the DOM element or react ref the "contextmenu" event should be attached to.
  // defaults to document.
  trigger
);
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/ContextMenu/useContextMenu.mdx).
