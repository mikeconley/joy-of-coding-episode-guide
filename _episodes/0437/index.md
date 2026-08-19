---
date: 2026-04-15
number: 437
---

# Episode 437: Apr 15th, 2026

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2026-04-15)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0437.html)

## Topics
* Work on downloads sidebar
* We'll create a simple version of Downloads in Firefox View, with a shared base component
* Then the FxView and Sidebar variants inherit from that shared base component
* Don't actually worry about FxView, but have the base component none-the-less.
* We'd have a version of the list that lists the items
* ![Alt text](https://mikeconley.ca/joc/agendas/images/690e243b256c4c0e8e96727ee9b17230 "list")
* See if we can factor out the existing download panel item UI into a domain-specific reusable component that can be used in different contexts (primarily, I'm aiming for this to be storybook-able)
* window
* DownloadsPanel
* DownloadsView (added as a listener to DownloadsCommon)
* DownloadsViewItem represents a download, and hears about updates
* How do we make Downloads View UI storybook compatible?
* Doesn't necessarily mean the first step is converting to Lit! The first step is perhaps to not use XUL.
* Convert richlistitem to moz-richlistitem HTML element
* ~~Do this next week (I should clear this with the ReComp team)~~  <-- don't need to do this first
* Convert richlistbox to moz-richlistbox HTML element
* ~~Probably slightly easier than moz-richlistitem (clear this with ReComp team)~~ <-- don't need to do this second
* Convert DownloadsViewItem to use HTML elements <-- let's do this!
* The ReComp team suggested a different approach, which is to make the DownloadsViewItem to use HTML elements AND to make sure it's agnostic / not bound to richlistitem / richlistbox. The upshot meaning we can continue using it, but don't need to do the richlistitem/richlistbox conversion.
* We'll use moz-box-group instead, and see what gaps we find. The multi-select gap is an obvious one, but that might be acceptable to start.

* [Rate this episode](https://forms.gle/zE1h7DG4t5x58RtF9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

