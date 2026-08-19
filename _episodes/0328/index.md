---
date: 2023-06-14
number: 328
---

# Episode 328: Jun 14th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-06-14)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0328.html)

## Topics
* WindowsJumpLists! Let's keep going!
* TODO
  - [x] Rename nsIJumpListBuilder to nsILegacyJumpListBuilder
  - [x] Add createLegacyJumpListBuilder to nsIWinTaskBar to use the old mechanism
  - [x] Update WindowsJumpList to use the legacy interface
  - [x] Create a new nsIJumpListBuilder
  - [ ] Populate nsIJumpListBuilder using the code we developed in the previous iteration
  - [ ] Have createJumpListBuilder in nsIWinTaskBar use that
  - [ ] Update WindowsJumpLists to choose the right builder based on the pref and treat them correctly based on that pref.
  - [ ] Make a note to migrate the new jump list builder off of the dedicated lazy thread and use the IO thread pool instead.

* [Rate this episode](https://forms.gle/nMqrbrnvApSBUDns9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

