---
layout: default
date: 2023-08-09
number: 335
---

# Episode 335: Aug 9th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-08-09)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0335.html)

## Topics
* No episodes for the next two weeks due to travel!
* Feedback:
  - Q: If you want to be as sure as possible when filing a bug, if it is a security related bug or not. How would you think about that?
    - https://www.mozilla.org/en-US/security/bug-bounty/
  - After all of this Windows JumpList work is merged and riding the rails to release I think it may be interesting to have a bit of a recap on all the pieces of work you did during all these episodes. Doesn't have to necessarily take up a full episode but maybe it could? 🤷‍♂️
    - I think this is a great idea. This whole project has taken about a year at this point, more or less (we've come and go from the project a bit). I think a recap would be really useful.

* WindowsJumpLists! <b>Let's keep going!</b>
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
  - [x] Investigate shutdown crashes by adding MOZ_ASSERT(mThread == PR_GetCurrentThread()); basically everywhere. Especially at shutdown.
    - [x] I KNOW WHAT"S HAPPENING. The JumpListBuilder is created on the main thread. That class creates a LazyIdleThread (mIOThread) which is responsible for instantiating the JumpListBackend (aka the NativeJumpListBackend). BUT GUESS WHAT: A LazyIdleThread will shut itself down after a period of inactivity - that's part of how it works! That means that when it comes time to shutting everything down, we're asking a LazyIdleThread to destroy the JumpListBackend which might not be the same thread that created it, thus hitting our assertion! What we might need to do is to either, 1: destroy the JumpListBackend anytime the LazyIdleThread is shut down. 2: move the JumpListBackend destruction responsibility to the main thread.
    - [x] Nika suggests using NS_INLINE_DECL_REFCOUNTING_ONEVENTTARGET
  - [x] After doing a removal, I saw a NSERRORUNEXPECTED, and then an NSERRORFAILURE for each subsequent update. Why is that?
    - [x] We need to ask Windows for the set of URLs to remove before we query Places and populate with the new list. That means adding a new function.
  - [ ] Write a gtest for the JumpListBuilder
  - [ ] Write a front-end test that registers a fake nsIWinTaskbar or otherwise produces a fake nsIJumpListBuilder to make sure it gets passed the right things.
  - [ ] Make a note to migrate the new jump list builder off of the dedicated lazy thread and use the IO thread pool instead.

* [Rate this episode](https://forms.gle/NAZ6G6gDjkbKAAKH8)

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

