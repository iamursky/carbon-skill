> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/StructuredList/StructuredList.mdx

# StructuredList

export const structuredListDefs = [
  `const prefix = 'cds';`,
  `const selectionRows = [
  { environment: 'Production', region: 'Frankfurt', purpose: 'Runs customer-facing services' },
  { environment: 'Staging', region: 'Dallas', purpose: 'Validates releases before deployment' },
  { environment: 'Development', region: 'London', purpose: 'Supports feature development and integration' },
  { environment: 'Disaster recovery', region: 'Sydney', purpose: 'Provides a standby recovery environment' },
];`,
  `const structuredListBodyRowGenerator = (numRows) => {
  return selectionRows.slice(0, numRows).map((row, i) => (
    <StructuredListRow key={\`row-\${i}\`} id={\`row-\${i}\`}>
      <StructuredListCell>{row.environment}</StructuredListCell>
      <StructuredListCell>{row.region}</StructuredListCell>
      <StructuredListCell>{row.purpose}</StructuredListCell>
      <StructuredListInput
        id={\`row-\${i}\`}
        value={\`row-\${i}\`}
        title={\`row-\${i}\`}
        name="row-0"
        aria-label={\`row-\${i}\`}
      />
      <StructuredListCell>
        <CheckmarkFilled
          className={\`\${prefix}--structured-list-svg\`}
          aria-label="select an option">
          <title>select an option</title>
        </CheckmarkFilled>
      </StructuredListCell>
    </StructuredListRow>
  ));
};`,
];

# StructuredList

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/StructuredList)
&nbsp;|&nbsp;
[Usage guidelines](https://www.carbondesignsystem.com/components/structured-list/usage)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/structured-list/accessibility)

## Table of Contents

- [StructuredList](#structuredList)
  - [Overview](#overview)
  - [Skeleton](#skeleton)
  - [Initial Row Selection](#initial-row-selection)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

## Skeleton

## Initial Row Selection

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/StructuredList/StructuredList.mdx).
