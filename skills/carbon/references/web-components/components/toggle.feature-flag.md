> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/toggle/toggle.feature-flag.mdx

# Reduced toggle label spacing

Reduced spacing between the toggle control and its label to improve visual
consistency with other form inputs.

```
import '@carbon/web-components/es/components/feature-flags/feature-flags.js';
import '@carbon/web-components/es/components/toggle/toggle.js';

<feature-flags enable-v12-toggle-reduced-label-spacing>
  <cds-toggle
    label-text="Label"
    label-a="On"
    label-b="Off"
    toggled></cds-toggle>
</feature-flags>
```
