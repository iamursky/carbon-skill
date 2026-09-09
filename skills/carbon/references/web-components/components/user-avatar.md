> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/user-avatar/user-avatar.mdx

# User-avatar

User avatars are a representation of a user or group of users. They can be used
to identify a user or indicate collaborators.

## Note on theming

The backgroundColor and font color will adapt dynamically based on the `theme`
prop.

## Getting started

Here's a quick example to get you started.

### JS (via import)

```javascript
import '@carbon/web-components/es/components/user-avatar/index.js';
```

### HTML

### Default

```html
<cds-user-avatar
  name="Thomas J. Watson"
  background-color="order-11-purple"
  size="lg"
  tooltip-text="TW, Thomas J. Watson user profile"
  tooltip-alignment="right"></cds-user-avatar>
```

### Example Usage

In this example, each of the four avatars is wrapped in a separate div to
demonstrate how the backgroundColor changes based on the theme prop.

### With Icon

For a custom icon, specify the slot by adding the `slot="rendericon"` attribute
to the element.

```html
<cds-user-avatar
  name="Thomas J. Watson"
  background-color="order-1-cyan"
  size="md"
  tooltip-text="TW, Thomas J. Watson user profile"
  tooltip-alignment="right"
  theme="light">
  ${iconLoader(Group, { slot: 'rendericon' })}
</cds-user-avatar>
```

### Example Usage

### With Image

For a profile picture, pass a full image URL to the `image` attribute and a
description to `image-description` for screen readers.

```html
<cds-user-avatar
  tooltip-alignment="right"
  tooltip-text="TW, Thomas J. Watson user profile"
  size="md"
  image="https://example.com/avatar.png"
  image-description="Avatar of Thomas J. Watson">
</cds-user-avatar>
```

### Example Usage

## `<cds-user-avatar>` attributes, properties and events

Note: For `boolean` attributes, `true` means simply setting the attribute.

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._
