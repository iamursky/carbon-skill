> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/web-components/src/components/notification/notification.mdx

# Notification

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/web-components/src/components/notification)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/notification/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/notification/accessibility)

## Table of Contents

- [Overview](#overview)
- [Actionable notification](#actionable-notification)
- [Inline notification & Toast notification](#inline-notification-and-toast-notification)
- [Callout](#callout)
- [Component API](#component-api)
- [Actionable](#actionable)
- [Inline](#inline)
- [Toast](#toast)
- [Callout](#callout-1)
- [CDN](#cdn)
- [Feedback](#feedback)

## Overview

There are 4 different types of notification components:
`cds-actionable-notification`, `cds-inline-notification`,
`cds-toast-notification`, and `cds- callout-notification`.

### Actionable notification

The `cds-actionable-notification` component should be used when user action is
required. It can include an action, other interactive elements or rich text. It
uses Toast-like styling by default, but if you'd like it to be visually similar
to an `cds-inline-notification`, you can use the `inline` attribute. If
`action-button-label` is not provided, an action button will not be rendered.
This component grabs and traps focus until the action is acted upon or the
notification is dismissed.

### Inline notification and Toast notification

The `cds-inline-notification` and `cds-toast-notification` components cannot
contain interactive elements or rich text. These are announced by screenreaders
when rendered. They don't grab focus. Use them to provide the user with an
alert, status, or log.

### Callout

`cds-callout-notification` is non-modal and should only be used inline with
content on the initial render of the page or modal because it will not be
announced to screenreader users like the other notification components.

As such, this should not be used for real-time notifications or notifications
responding to user input (unless the page is completely refreshing and bumping
the users focus back to the first element in the dom/tab order). If a Callout is
rendered after the initial render, screenreader users' focus may have already
passed this portion of the DOM and they will not know that the notification has
been rendered until they circle back to the beginning of the page.

This is the most passive notification component and is essentially just a styled
div. If you place actions or interactive elements within this component, place
an `aria-describedby` on the interactive element with a value that matches the
`title-id` attribute.

## Actionable

## Inline

## Toast

## Callout

## Component API

## `cds-actionable-notification`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## `cds-inline-notification`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## `cds-toast-notification`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## `cds-callout-notification`

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://web-components.carbondesignsystem.com)._

## CDN

This component is also available via CDN.

```html
// SPECIFIC VERSION (available starting v2.0.0)
<script type="module" src="https://1.www.s81c.com/common/carbon/web-components/version/v2.59.0-rc.0/notification.min.js"></script>
```

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/web-components/src/components/notification/notification.mdx).
