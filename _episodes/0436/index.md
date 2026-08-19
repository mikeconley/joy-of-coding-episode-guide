---
date: 2026-04-08
number: 436
---

# Episode 436: Apr 8th, 2026

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2026-04-08)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0436.html)

## Topics
* Attempt to re-land https://lando.moz.tools/D291881/
* Work on downloads sidebar
  - We'll create a simple version of Downloads in Firefox View, with a shared base component
    - Then the FxView and Sidebar variants inherit from that shared base component
      - Don't actually worry about FxView, but have the base component none-the-less.
    - We'd have a version of the list that lists the items
            ![Alt text](https://mikeconley.ca/joc/agendas/images/690e243b256c4c0e8e96727ee9b17230 "list")
    - See if we can factor out the existing download panel item UI into a domain-specific reusable component that can be used in different contexts (primarily, I'm aiming for this to be storybook-able)
      - window
        - DownloadsPanel
        - DownloadsView (added as a listener to DownloadsCommon)
          - DownloadsViewItem represents a download, and hears about updates
    - How do we make Downloads View UI storybook compatible?
      - Doesn't necessarily mean the first step is converting to Lit! The first step is perhaps to not use XUL.
      - Convert richlistitem to moz-richlistitem HTML element
        - Do this next week (I should clear this with the ReComp team)
      - Convert richlistbox to moz-richlistbox HTML element
        - Probably slightly easier than moz-richlistitem (clear this with ReComp team)
      - Convert DownloadsViewItem to use HTML elements

* [Rate this episode](https://forms.gle/i4GLysR896eP24FDA)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

