> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/Tabs/Tabs.mdx

# Tabs

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/Tabs)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/tabs/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/tabs/accessibility)

## Table of Contents

- [Overview](#overview)
  - [Line Tabs](#line-tabs)
  - [Contained Tabs](#contained-tabs)
  - [Contained Full Width](#contained-full-width)
  - [Contained With Icons](#contained-with-icons)
  - [Contained With Second Labels](#contained-with-second-labels)
  - [Contained With Second Labels and Icons](#contained-with-second-labels-and-icons)
  - [Icon Tabs Only](#icon-tabs-only)
  - [Dismissable Tabs](#dismissable-tabs)
  - [Manual](#manual)
  - [Skeleton](#skeleton)
  - [With Icons](#with-icons)
  - [Vertical tabs](#vertical-tabs)
  - [Tab - tab activation modes](#tab---tab-activation-modes)
  - [Tabs and the Grid - fullWidth prop](#tabs-and-the-grid---fullwidth-prop)
- [V11](#v11)
  - [Tabs composition](#tabs-composition)
  - [Various updates](#various-updates)
  - [Max width](#max-width)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

Use tabs to allow users to navigate easily between views within the same
context. Tabs are now more composable, meaning that you have more flexibility in
what is in rendered inside of `Tab` and `TabPanel`.

### Line Tabs

```jsx
<Grid condensed>
  <Column lg={16} md={8} sm={4}>
    <Tabs>
      <TabList aria-label="List of tabs" contained fullWidth>
        <Tab>Tab Label 1</Tab>
        <Tab>Tab Label 2</Tab>
        <Tab disabled>Tab Label 3</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Tab Panel 1</TabPanel>
        <TabPanel>Tab Panel 2</TabPanel>
        <TabPanel>Tab Panel 3</TabPanel>
      </TabPanels>
    </Tabs>
  </Column>
</Grid>
```

Using the `fullWidth` prop alone within a `Grid` makes it so that the `Tabs`
container aligns to the `Grid`, but not the individual `Tab` items; to have each
individual `Tab` take up exactly one or many columns within the `Grid`, you must
specify the number of columns as a multiple of the number of `Tab` items within
the `TabList`.

For example, to have 5 tabs and each tab span exactly two columns:

```jsx
<Grid condensed>
  <Column lg={10}>
    <Tabs>
      <TabList aria-label="List of tabs" contained fullWidth>
        <Tab>Tab Label 1</Tab>
        <Tab>Tab Label 2</Tab>
        <Tab disabled>Tab Label 3</Tab>
        <Tab>Tab Label 4</Tab>
        <Tab>Tab Label 5</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Tab Panel 1</TabPanel>
        <TabPanel>Tab Panel 2</TabPanel>
        <TabPanel>Tab Panel 3</TabPanel>
        <TabPanel>Tab Panel 4</TabPanel>
        <TabPanel>Tab Panel 5</TabPanel>
      </TabPanels>
    </Tabs>
  </Column>
</Grid>
```

Or, to have 5 tabs and each tab span exactly three columns:

```jsx
<Grid condensed>
  <Column lg={15}>
    <Tabs>
      <TabList aria-label="List of tabs" contained fullWidth>
        <Tab>Tab Label 1</Tab>
        <Tab>Tab Label 2</Tab>
        <Tab disabled>Tab Label 3</Tab>
        <Tab>Tab Label 4</Tab>
        <Tab>Tab Label 5</Tab>
      </TabList>
      <TabPanels>
        <TabPanel>Tab Panel 1</TabPanel>
        <TabPanel>Tab Panel 2</TabPanel>
        <TabPanel>Tab Panel 3</TabPanel>
        <TabPanel>Tab Panel 4</TabPanel>
        <TabPanel>Tab Panel 5</TabPanel>
      </TabPanels>
    </Tabs>
  </Column>
</Grid>
```

## V11

### Tabs composition

Tabs got a big revamp in v11! Tabs are now more composable than ever before,
meaning that you have the flexibility and control on your end to make them look
and act how you want. The biggest difference is that the Tab label and the Tab
content are now separate components.

Example of Tabs in v10:

```js
<Tabs>
  <Tab label="Tab label 1">
    <p>Content for first tab goes here.</p>
  </Tab>
  <Tab label="Tab label 2">
    <p>Content for second tab goes here.</p>
  </Tab>
  <Tab label="Tab label 3" disabled>
    <p>Content for third tab goes here.</p>
  </Tab>
  <Tab
    label="Tab label 4 shows truncation"
    title="Tab label 4 shows truncation">
    <p>Content for fourth tab goes here.</p>
  </Tab>
</Tabs>
```

Those same Tabs, now in v11:

```js
<Tabs>
  <TabList>
    <Tab>Tab Label 1</Tab>
    <Tab>Tab Label 2</Tab>
    <Tab disabled>Tab Label 3</Tab>
    <Tab title="Tab Label 4 shows truncation">Tab Label 4 shows truncation</Tab>
  </TabList>
  <TabPanels>
    <TabPanel>Content for first tab goes here.</TabPanel>
    <TabPanel>Content for second tab goes here.</TabPanel>
    <TabPanel>Content for third tab goes here.</TabPanel>
    <TabPanel>Content for fourth tab goes here.</TabPanel>
  </TabPanels>
</Tabs>
```

### Various updates

All the same functionality for Tabs is available in v11 and more! Below are the
minor tweaks in naming or implementation.

- the `type` prop is deprecated. Both "container" and "default" tabs still exist
  but now can be called by adding the prop `contained` to the `TabList`. See the
  above "Contained Tabs" for an example.
- Default tabs are now referred to as line tabs in our documentation here and on
  our website.
- `hidden` prop is no longer needed with the new composable Tabs. You have full
  control over tab content and when it's hidden through the `TabPanel` and
  `TabPanels` components.
- `selected` prop is now named `selectedIndex`.
- `tabContentClassName` is no longer needed. `TabPanel` (equivalent to tab
  content) takes in a className prop on its outermost node.
- For `Tab`, `label` is no longer needed. `children` of `Tab` are now the label.
- Due to its composability, `renderAnchor`, `renderButton`, `renderContent` are
  no longer needed on `Tab`.
- `selected` on `Tab` is deprecated in favor or `selectedIndex`, now placed on
  `Tabs` instead.
- Because `renderButton` is no longer needed, the associated `tabIndex` prop has
  also been deprecated.

### Max width

In V11, tabs no longer have a max-width property set. Which means a tab title
can span as wide as its title is long. To override this behavior, you may use
some style rules:

```css
.cds--tabs__nav-link {
  max-width: 10rem;
}
```

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/Tabs/Tabs.mdx).
