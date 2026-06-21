> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/ProgressIndicator/ProgressIndicator.mdx

# ProgressIndicator

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/ProgressIndicator)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/progress-indicator/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/progress-indicator/accessibility)

## Table of Contents

- [Overview](#overview)
- [Interactive](#interactive)
- [Skeleton](#skeleton)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

## Interactive

## Skeleton

For React usage, `ProgressIndicator` holds the `currentIndex` state to indicate
which `ProgressStep` is the current step. The `ProgressIndicator` component
should always be used with `ProgressStep` components as its children.

Changing the `currentIndex` prop will automatically set the `ProgressStep`
components props (`complete`, `incomplete`, `current`). For general usage,
Progress Indicators display steps in a process. It should indicate when steps
have been complete, the active step, and the steps to come.

If you register an `onChange` handler, the Progress Indicator will become
interactive. Your parent component should update the `currentIndex` prop within
the `onChange` handler.

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/ProgressIndicator/ProgressIndicator.mdx).
