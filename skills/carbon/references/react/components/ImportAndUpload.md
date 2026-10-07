> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/examples/ImportAndUpload/ImportAndUpload.mdx

# Import and Upload

[Usage guidelines](https://carbondesignsystem.com/patterns/file-upload/)
|
[Carbon modal usage guidelines](https://www.carbondesignsystem.com/components/modal/usage)
|
[Carbon modal documentation](https://react.carbondesignsystem.com/?path=/docs/components-modal)

## Table of Contents

- [Overview](#overview)
- [Example usage](#example-usage)

## Overview

Modal dialog version of the Import and Upload pattern. The import action
transfers data or objects from an external source into a system.

> NOTE: Patterns have multiple ways of accomplishing a user need and typically
> use a combination of components with additional design considerations. The
> pattern code we share is meant to serve as an example implementation that can
> be built and extended further.

To build this pattern, we recommend including the following ingredients:

- [ComposedModal](https://react.carbondesignsystem.com/?path=/docs/components-composedmodal)
- [Button](https://react.carbondesignsystem.com/?path=/docs/components-button)
- [TextInput](https://react.carbondesignsystem.com/?path=/docs/components-textinput)
- [FileUploaderDropContainer](https://react.carbondesignsystem.com/?path=/docs/components-fileuploader)
- [FileUploaderItem](https://react.carbondesignsystem.com/?path=/docs/components-fileuploader)

```jsx
import {
  Button,
  ComposedModal,
  FileUploaderDropContainer,
  FileUploaderItem,
  ModalBody,
  ModalFooter,
  ModalHeader,
  TextInput,
} from '@carbon/react';
```

## Example usage

> 💡 Check our
> [Stackblitz](https://stackblitz.com/github/carbon-design-system/carbon/tree/main/packages/react/src/examples/ImportAndUpload/example)
> example implementation.

[![Edit react-patterns](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/carbon-design-system/carbon/tree/main/packages/react/src/examples/ImportAndUpload/example)

### Import and Upload
