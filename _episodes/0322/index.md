---
date: 2023-04-19
number: 322
---

# Episode 322: Apr 19th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-04-19)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0322.html)

## Topics
* TODO: Hunt down race bug for "Pin to Toolbar"
  - Smurfd found this one: [Bug 1712729](https://bugzilla.mozilla.org/show_bug.cgi?id=1712729)
  - Done: [Bug 1828966](https://bugzilla.mozilla.org/show_bug.cgi?id=1828966) - Pin to Toolbar context menu item is sometimes out of sync
* [Bug 1828738](https://bugzilla.mozilla.org/show_bug.cgi?id=1828738) - Make it possible for about:welcome to open an FxA sign-in flow that closes itself after sign-in completes
  - https://developer.mozilla.org/en-US/docs/Web/API/AbortController/AbortController
  - Hypotheses
    - I'm adding a progress listener to the wrong browser
      - <b>aukras saves the day</b> by helping Mike realize that he's added the progress listener to the wrong browser (it was being added to the about:welcome browser, and not the fxaBrowser!)
      - The FxA browser does not accept progress listeners for some reason
      - The progress listener is misconfigured

* [Rate this episode](https://forms.gle/TbkDQtnAaSn5kt9C9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

