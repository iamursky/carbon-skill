> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/FileUploader/FileUploader.featureflag.mdx

# Enhanced FileUploader Callbacks

The `enable-enhanced-file-uploader` flag enables enhanced functionality for the
FileUploader component, including richer callback data and expanded trigger
events for `onChange` and `onDelete`.

When this flag is enabled, the `onChange` callback is consistently triggered for
all file list modifications (additions, deletions, programmatic clears), and
both `onChange` and `onDelete` events are augmented with detailed file
information like `deletedFile`, `addedFiles`, and `currentFiles` on
`event.target`.

the `getCurrentFiles` and `setCurrentFiles` methods are available on the
`FileUploader` component, which can be used to get and update the file state and
to disable specific files based on disabled prop.

## Enable enhanced FileUploader callbacks

```js
<FeatureFlags enableEnhancedFileUploader>
  <FileUploader
    multiple
    filenameStatus="edit"
    onChange={(evt) =>
      console.log('onChange', evt.target.action, evt.target.currentFiles)
    }
    onDelete={(evt) => console.log('onDelete', evt.target.deletedFile)}
  />
</FeatureFlags>
```
