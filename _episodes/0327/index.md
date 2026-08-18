---
date: 2023-06-07
number: 327
---

# Episode 327: Jun 7th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-06-07)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0327.html)

## Topics
* WindowsJumpLists! Let's gooooo!
  - A lot of the complexity that we're dealing with architecturally is because we're trying to maintain the old backend while adding the new capability with a new backend, but the two backends share some infrastructure.
  - What I want to do is determine if we can do a better job of separating out the jumplist backend by reading a pref at runtime and choosing the right implementation.
* TODO
  - [x] Rename nsIJumpListBuilder to nsILegacyJumpListBuilder
  - [x] Add createLegacyJumpListBuilder to nsIWinTaskBar to use the old mechanism
  - [x] Update WindowsJumpList to use the legacy interface
  - [x] Create a new nsIJumpListBuilder
  - [ ] Populate nsIJumpListBuilder using the code we developed in the previous iteration
  - [ ] Have createJumpListBuilder in nsIWinTaskBar use that
  - [ ] Update WindowsJumpLists to choose the right builder based on the pref and treat them correctly based on that pref.

* [Rate this episode](https://forms.gle/CCcpZn82xDPMaH3e7)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

