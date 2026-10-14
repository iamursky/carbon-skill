> Source: https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/TextArea/TextArea.mdx

# TextArea

[Source code](https://github.com/carbon-design-system/carbon/tree/main/packages/react/src/components/TextArea)
&nbsp;|&nbsp;
[Usage guidelines](https://carbondesignsystem.com/components/text-input/usage/#text-area)
&nbsp;|&nbsp;
[Accessibility](https://www.carbondesignsystem.com/components/text-input/accessibility)

## Table of Contents

- [Overview](#overview)
- [Skeleton](#skeleton)
- [AI Label](#ai-label)
- [Translations](#translations)
- [Component API](#component-api)
- [Feedback](#feedback)

## Overview

## Skeleton

## AI Label

## Translations

When `maxCount` is set, `TextArea` announces the remaining characters or words
to screen readers as the value approaches the limit. When `enableCounter` is
also set, the limit is exposed as the accessible description of the
`<textarea>`. These strings can be translated with `translateWithId`. The
function receives a translation ID and an object with `count` and `maxCount`,
and must return the translated string. Use `count` to select the correct plural
form. The `counterMode` prop determines whether the `characters` or `words` IDs
are used.

```jsx
const translations = {
  'carbon.text-area.counter.characters.remaining': ({ count }) =>
    count === 1 ? '1 caractère restant.' : `${count} caractères restants.`,
  'carbon.text-area.counter.characters.max-reached': () =>
    'Nombre maximal de caractères atteint.',
  'carbon.text-area.counter.characters.limit': ({ maxCount }) =>
    `Limite de ${maxCount} caractères`,
  // ... `words` IDs when `counterMode="word"`
};

<TextArea
  id="text-area"
  labelText="Label"
  enableCounter
  maxCount={500}
  translateWithId={(id, args) => translations[id](https://github.com/carbon-design-system/carbon/blob/main/packages/react/src/components/TextArea/args)}
/>;
```

| Translation ID                                    | Default                                          | `count`              |
| ------------------------------------------------- | ------------------------------------------------ | -------------------- |
| `carbon.text-area.counter.characters.remaining`   | `1 character left.` / `{count} characters left.` | Remaining characters |
| `carbon.text-area.counter.characters.max-reached` | `Maximum characters reached.`                    | `maxCount`           |
| `carbon.text-area.counter.characters.limit`       | `Character limit {maxCount}`                     | `maxCount`           |
| `carbon.text-area.counter.words.remaining`        | `1 word left.` / `{count} words left.`           | Remaining words      |
| `carbon.text-area.counter.words.max-reached`      | `Maximum words reached.`                         | `maxCount`           |
| `carbon.text-area.counter.words.limit`            | `Word limit {maxCount}`                          | `maxCount`           |

## Component API

_The full props/attributes table is generated from the component source. See the **Source code** link at the top of this page, or the live API table in [Storybook](https://react.carbondesignsystem.com)._

## Feedback

Help us improve this component by providing feedback, asking questions on Slack,
or updating this file on
[GitHub](https://github.com/carbon-design-system/carbon/edit/main/packages/react/src/components/TextArea/TextArea.mdx).
