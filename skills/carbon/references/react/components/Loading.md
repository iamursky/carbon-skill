> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/Loading/Loading.mdx

# Loading

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/Loading)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/loading/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/loading/accessibility)

## Table of Contents

- [Overview](#overview)
- [Overlay loading](#overlay-loading)
  - [Overlay loading behind a modal](#overlay-loading-behind-a-modal)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

## Overlay loading

Setting `withOverlay` renders the indicator on top of a full-screen overlay that
blocks interaction with the content behind it. When the overlay is active and no
recognized modal is layered above it, focus moves to the loading dialog and
stays there. When loading finishes, focus returns to the previously focused
element when it is still available, or to a suitable fallback when possible.

Select **Start** to trigger a two second loading state.

### Overlay loading behind a modal

When a modal dialog is already active above the loading overlay, the overlay
does not take focus from the modal.

Open the modal and select **Save** to trigger a two second loading state behind
it. Focus remains on **Save**, and `Tab` continues cycling through the modal
instead of moving to the overlay underneath.

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/Loading/Loading.mdx).
