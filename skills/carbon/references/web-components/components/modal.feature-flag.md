> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/modal/modal.feature-flag.mdx

# Modal Feature Flag

## `enable-dialog-element`

`Modal` supports the `enable-dialog-element` feature flag. When enabled, Modal
will use the native `<dialog>` element instead of `role="dialog"`.

```
import '@carbon/web-components/es/components/feature-flags/feature-flags.js';
import '@carbon/web-components/es/components/modal/modal.js';

<feature-flags enable-dialog-element>
  <cds-modal open>
    <cds-modal-header> ... </cds-modal-header>
    <cds-modal-body> ... </cds-modal-body>
    <cds-modal-footer> ... </cds-modal-footer>
  </cds-modal>
</feature-flags>
```
