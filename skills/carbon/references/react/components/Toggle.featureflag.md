> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/Toggle/Toggle.featureflag.mdx

# Reduced toggle label spacing

Reduced spacing between the toggle control and its label to improve visual
consistency with other form inputs.

```scss
@use '@carbon/react' with (
  $feature-flags: (
    'enable-v12-toggle-reduced-label-spacing': true,
  )
);
```
