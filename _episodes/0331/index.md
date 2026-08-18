---
date: 2023-07-05
number: 331
---

# Episode 331: Jul 5th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-07-05)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0331.html)

## Topics
* [m/firefox](https://fedia.io/m/firefox)
* [Main-thread disc access](https://mikeconley.ca/blog/2019/05/16/a-few-words-on-main-thread-disk-access-for-general-audiences/)
* WindowsJumpLists! Let's keep going!
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
    - [x] Update WindowsJumpLists to choose the right builder based on the pref and treat them correctly based on that pref.
  - [x] Why aren't the favicons working?
    - [x] It was always this way - there's a moment in time, right after the page visits, where the favicon hasn't yet been written to disk, but after it has been, the favicon becomes present. Usually the update immediately after.
  - [ ] Investigate shutdown crashes by adding MOZ_ASSERT(mThread == PR_GetCurrentThread()); basically everywhere. Especially at shutdown.
    - [ ] I KNOW WHAT"S HAPPENING. The JumpListBuilder is created on the main thread. That class creates a LazyIdleThread (mIOThread) which is responsible for instantiating the JumpListBackend (aka the NativeJumpListBackend). BUT GUESS WHAT: A LazyIdleThread will shut itself down after a period of inactivity - that's part of how it works! That means that when it comes time to shutting everything down, we're asking a LazyIdleThread to destroy the JumpListBackend which might not be the same thread that created it, thus hitting our assertion! What we might need to do is to either, 1: destroy the JumpListBackend anytime the LazyIdleThread is shut down. 2: move the JumpListBackend destruction responsibility to the main thread.
  - [ ] After doing a removal, I saw a NSERRORUNEXPECTED, and then an NSERRORFAILURE for each subsequent update. Why is that?
  - [ ] Write a gtest for the JumpListBuilder
  - [ ] Write a front-end test that registers a fake nsIWinTaskbar or otherwise produces a fake nsIJumpListBuilder to make sure it gets passed the right things.
  - [ ] Make a note to migrate the new jump list builder off of the dedicated lazy thread and use the IO thread pool instead.

* [Rate this episode](https://forms.gle/2QaZ19cexzKw6ao18)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

