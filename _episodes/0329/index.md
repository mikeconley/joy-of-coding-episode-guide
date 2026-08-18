---
date: 2023-06-21
number: 329
---

# Episode 329: Jun 21st, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-06-21)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0329.html)

## Topics
* Volume control in Picture-in-Picture! That's in Nightly right now, might roll out to users in Firefox 116.
* Firefox release info - [What train is it now](https://whattrainisitnow.com/)
  - If you want to hear more about our release model and how "the trains" work, check out [Episode 270](https://www.youtube.com/watch?v=YwfCI1xqBpM), around 44m20s in
* WindowsJumpLists! Let's keep going!
  - A lot of the complexity that we're dealing with architecturally is because we're trying to maintain the old backend while adding the new capability with a new backend, but the two backends share some infrastructure.
  - What I want to do is determine if we can do a better job of separating out the jumplist backend by reading a pref at runtime and choosing the right implementation.
* TODO
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

* [Rate this episode](https://forms.gle/d7VRh19tf2Zgad467)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

