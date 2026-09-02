---
date: 2026-06-17
number: 441
---

# Episode 441: Jun 17th, 2026

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2026-06-17)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0441.html)

## Topics
* Lots of episode guide pull requests to merge in!
* Let's work on center crop for moz-label
  - FIRST, let us actually see if xul:label cannot be used. If it CAN be used, then this work is not necessary for the project
    - No, cannot use xul:label in HTML documents, as suspected.
  - We will re-implement XUL-style center cropping but for moz-label, with a special property or some special mechanism in `moz-label` to indicate to the engine to use center crop.
    - Must have `value` and crop="center" set to work
    - Getting and setting textContent directly will forward to value in this configuration
    - Multiple text child nodes is not allowed in this configuration, and will warn / bail out of cropping.
  - We're going to be re-using much of the XUL center cropping stuff, and all of the l10n problems it entails
  - We must guarantee a single text node as the child of moz-label

* [Rate this episode](https://forms.gle/Gs5BCiJP8RnTsFZBA)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

