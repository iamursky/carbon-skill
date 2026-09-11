> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/full-page-error/full-page-error.mdx

# FullPageError

Display a full-page error when the requested page is unavailable to the user.
This is typically caused by issues with the requested URL or access permissions.
Errors caused by server connectivity issues are not covered in this guideline.

```jsx
<Unstyled style={{ marginBottom: '1.5rem' }}>
  <cds-inline-notification
    kind="info"
    title="Migrated component:"
    subtitle="This component has been migrated from Carbon for IBM Products. While visible in the v12 Storybook, migrated components are not available in the published v11 package and enabling enable-v12-release does not expose them — they will be part of the public @carbon/web-components API when v12 ships."
  />
</Unstyled>
```

## Getting started

Here's a quick example to get you started.

### JS (via import)

```javascript
import '@carbon/web-components/es/components/full-page-error/index.js';
```

### HTML

```html
<cds-full-page-error
  label="Error 404"
  class="my-custom-class"
  title="Page not found"
  description="The page you requested has moved or is unavailable, or the specified URL is not valid. Please check the URL or search the site for the requested content."
  kind="404">
  <!-- Pass any content you want to display to the user here -->
  <a class="cds--link" href="#">– Forwarding Link 1</a>
  <br />
  <a class="cds--link" href="#">– Forwarding Link 2</a>
</cds-full-page-error>
```

### Example Usage

## `<cds-full-page-error>` attributes, properties and events

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._
