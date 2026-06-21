> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/popover/autoalign.mdx

# Auto align

## Table of Contents

- [Overview](#overview)
- [Popover](#popover)
- [Toggletip](#toggletip)
- [Tooltip](#tooltip)
- [AI Label](#ai-label)
- [Feedback](#feedback)

## Overview

The experimental `align` prop allows you to specify where your content should be
placed relative to the popover. For example, if you provide `align="top"` to the
`Popover` component then the popover will render above your component.
Similarly, if you provide `align="bottom"` then the popover will render below
your component.

You can also configure the placement of the caret, if it is enabled, by choosing
between `left` and `right` or `bottom` and `top`, depending on where your
popover is being rendered.

If you are using `align="top"`, then you can choose between `align="top-left"`
and `align="top-right"`. These options will place the caret closer to the left
or right edges of the popover.

If you are using `align="left"` or `align="right"`, you can use `top` or
`bottom` to control this alignment.

## Popover

## Toggletip

## Tooltip

## AI Label

          <p class="secondary">Model type</p>
          <p class="bold">Foundation model</p>
        </div>
        <cds-icon-button kind="ghost" slot="actions" size="lg" tab-index="0" tooltip-alignment="" tooltip-position="top" type="button" align="top" close-on-activation="">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" width="16" height="16" viewBox="0 0 16 16" slot="icon"><path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path><path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path></svg>
          <span slot="tooltip-content"> View </span>
        </cds-icon-button>
        <cds-icon-button kind="ghost" slot="actions" size="lg">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" width="16" height="16" viewBox="0 0 32 32" slot="icon"><path d="M28,8H20.8284L17.4143,4.5859A2,2,0,0,0,16,4H4A2,2,0,0,0,2,6V26a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10A2,2,0,0,0,28,8ZM8,26V14h8v6.17l-2.59-2.58L12,19l5,5,5-5-1.41-1.41L18,20.17V14a2.0025,2.0025,0,0,0-2-2H8a2.0025,2.0025,0,0,0-2,2V26H4V6H16l4,4h8v2H22v2h6V26Z"></path></svg>
          <span slot="tooltip-content"> Open folder</span>
        </cds-icon-button>
        <cds-icon-button kind="ghost" slot="actions" size="lg">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" width="16" height="16" viewBox="0 0 32 32" slot="icon"><path d="M26 28H6a2.0021 2.0021 0 01-2-2V11A2.0021 2.0021 0 016 9h5.6665a2.0119 2.0119 0 011.2007.4L16.3335 12H26a2.0021 2.0021 0 012 2V26A2.0021 2.0021 0 0126 28zM11.6665 11H5.9985L6 26H26V14H15.6665zM28 9H17.6665l-4-3H6V4h7.6665a2.0119 2.0119 0 011.2007.4L18.3335 7H28z"></path></svg>
          <span slot="tooltip-content"> Folders </span>
        </cds-icon-button>
        <cds-ai-label-action-button>View details</cds-ai-label-action-button>
      </cds-ai-label>
    `,
  }}
  of={AutoAlignStories.AILabel}
/>

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/popover/autoalign.mdx).
