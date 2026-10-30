---
date: 2023-06-28
number: 330
airmozilla: https://mzl.la/joy-of-coding-2023-06-28
agenda: https://mikeconley.ca/joc/agendas/Episode-0330.html
rating: https://forms.gle/tgSHNtwTJ4FhTmRa8
---

## Topics

- Reviewing [D180514](https://phabricator.services.mozilla.com/D180514)
- WindowsJumpLists! Let's keep going!
- TODO
  - [x] Rename nsIJumpListBuilder to nsILegacyJumpListBuilder
  - [x] Add createLegacyJumpListBuilder to nsIWinTaskBar to use the old mechanism
  - [x] Update WindowsJumpList to use the legacy interface
  - [x] Create a new nsIJumpListBuilder
  - [x] Document NativeJumpListBackend
  - [x] Populate nsIJumpListBuilder using the code we developed in the previous iteration
  - [x] Have createJumpListBuilder in nsIWinTaskBar use that
  - [x] Figure out why the JumpListBuilder isn't returning the URLs of the previous
    - [x] It's working! It's just that you have to remember to actually remove the item for it to show up in the list.
  - [ ] Update WindowsJumpLists to choose the right builder based on the pref and treat them correctly based on that pref.
  - [ ] Write a gtest for the JumpListBuilder
  - [ ] Write a front-end test that registers a fake nsIWinTaskbar or otherwise produces a fake nsIJumpListBuilder to make sure it gets passed the right things.
  - [ ] Make a note to migrate the new jump list builder off of the dedicated lazy thread and use the IO thread pool instead.
- Tim Schafer interview with [Cressup](https://www.twitch.tv/videos/1857329968)
- [https://mikeconley.github.io/documents/HowmconleyusesMercurialforMozillacode](https://mikeconley.github.io/documents/how_mconley_uses_Mercurial_for_Mozilla_code)
