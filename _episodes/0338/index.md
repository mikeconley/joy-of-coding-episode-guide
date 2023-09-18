---
layout: default
date: 2023-09-13
number: 338
---

# Episode 338: Sep 13th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-09-13)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0338.html)

## Topics
* [Faster Vue.js execution](https://hacks.mozilla.org/2023/09/faster-vue-js-execution-in-firefox/) in Firefox
* Quick pivot - fixing a thing in the migration wizard: [Bug 1852973](https://bugzilla.mozilla.org/show_bug.cgi?id=1852973)
* [Writing good commit messages](https://reviewboard.notion.site/Writing-Good-Change-Descriptions-10529e7c207743fa8ca90153d4b21fea)
* Back to WindowsJumpLists
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
  - [x] Investigate shutdown crashes by adding MOZ_ASSERT(mThread == PR_GetCurrentThread()); basically everywhere. Especially at shutdown.
    - [x] I KNOW WHAT"S HAPPENING. The JumpListBuilder is created on the main thread. That class creates a LazyIdleThread (mIOThread) which is responsible for instantiating the JumpListBackend (aka the NativeJumpListBackend). BUT GUESS WHAT: A LazyIdleThread will shut itself down after a period of inactivity - that's part of how it works! That means that when it comes time to shutting everything down, we're asking a LazyIdleThread to destroy the JumpListBackend which might not be the same thread that created it, thus hitting our assertion! What we might need to do is to either, 1: destroy the JumpListBackend anytime the LazyIdleThread is shut down. 2: move the JumpListBackend destruction responsibility to the main thread.
    - [x] Nika suggests using NS_INLINE_DECL_REFCOUNTING_ONEVENTTARGET
  - [x] After doing a removal, I saw a NSERRORUNEXPECTED, and then an NSERRORFAILURE for each subsequent update. Why is that?
    - [x] We need to ask Windows for the set of URLs to remove before we query Places and populate with the new list. That means adding a new function.
  - [ ] Write a GTest for the JumpListBuilder
    - [x] SetAppId
    - [x] CheckForRemovals
      - [x] Need to get the JS string[] thing out and compare! Fun!
        - [x] Make WaitForResolver::SpinUntilResolved return resolve JSValue
    - [ ] PopulateJumpList
      - [x] Uh... how come when I pass in empty arrays it's still returning NS_OK? Whattttttt is happening?
        - [x] This is fine because we can pass empty arrays to clear out the jump list! The only rule that seems to be enforced is that a custom string must be supplied if and custom tasks are supplied.
      - [x] Figure out how to convert our description objects into JS Values. There might be helpers for this via [DictionaryBase](https://searchfox.org/mozilla-central/rev/e7b8d13b7513b6fbd97d69e882d7faeed05309d0/dom/bindings/ToJSValue.h#283-289)
      - [ ] Write a new kind of matcher to match against the ShellLink that has been passed to AddUserTasks and compare it to the WindowsJumpListShortcutDescription!
      - [ ] Maybe all of our mocks should be StrictMocks?
  - [ ] Write a front-end test that registers a fake nsIWinTaskbar or otherwise produces a fake nsIJumpListBuilder to make sure it gets passed the right things.
    - [ ] Make a note to migrate the new jump list builder off of the dedicated lazy thread and use the IO thread pool instead.

* [Rate this episode](https://forms.gle/g3G2T9vuetweJgZRA)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
* [npb hacks](https://www.twitch.tv/BackToTheCode) on the SpiderMonkey JS engine
* [Compiler Compiler](https://www.twitch.tv/codehag) live stream
* Try out Mozilla [VPN](https://vpn.mozilla.org/)
* How mconley uses [Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mike's Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
* [Codetribute](https://codetribute.mozilla.org/) - Help contribute to Firefox, good mentored bugs for You.
  - First, [Create](https://bugzilla.mozilla.org/createaccount.cgi) a Mozilla Bugzilla account.

