> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/Slider/Slider.mdx

# Slider

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/Slider)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/slider/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/slider/accessibility)

## Table of Contents

- [Overview](#overview)
- [Controlled Slider](#controlled-slider)
- [Skeleton](#skeleton)
- [Slider With Custom Value](#slider-with-custom-value)
- [Slider With Hidden Inputs](#slider-with-hidden-inputs)
  - [`step` Prop](#step-prop)
  - [`unstable_valueUpper` Prop](#unstable_valueupper-prop)
- [Two Handle Skeleton](#two-handle-skeleton)
- [Two Handle Slider](#two-handle-slider)
- [Two Handle Slider With Hidden Inputs](#two-handle-slider-with-hidden-inputs)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

Sliders provide a visual indication of adjustable content, where the user can
increase or decrease the value by moving the handle along a horizontal track.

## Controlled Slider

## Skeleton

## Slider With Custom Value

## Slider With Hidden Inputs

### `step` Prop

If a `step` value other than `1` is provided, any number entered into the text
input must adhere to the step value. For example, if the `step` is `5`, with a
range of values from `0-100`, `40` would be valid, and `42` would be considered
`invalid`.

### `unstable_valueUpper` Prop

The Slider component can support two handles to specify a range. To enable this
behavior pass a value for the `unstable_valueUpper` prop. This sets the upper
bound of the range in addition to the `value` prop, which specifies the lower
bound. When in two handle mode, both `value` and `valueUpper` are provided as
keys to `onChange` function prop that is passed to the component.

## Two Handle Skeleton

## Two Handle Slider

## Two Handle Slider With Hidden Inputs

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/Slider/Slider.mdx).
