---
layout: default
date: 2023-07-26
number: 333
---

# Episode 333: Jul 26th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-07-26)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0333.html)

## Topics
* Episode Guide!!
* [sdk's patch to add tooltips to the All Tabs menu panel](https://phabricator.services.mozilla.com/D183102)
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
  - [ ] Let's update WinTaskbar to have a new method that can be accessed from native code (so not through XPCOM), called, like, DoCreateJumpListBuilder or something. Have it take an argument that is a reference to something that implements a JumpListManager interface. Have JumpListBuilder move that thing to the background thread - the background thread owns it. Then, in our tests, have our GTest call DoCreateJumpListBuilder, passing it something that mocks out JumpListManager. And then call it's populateJumpList method for testing.

 (abstract) class JumpListBackend HRESULT BeginList HRESULT AddUserTasks HRESULT AppendCategory HRESULT CommitList

// Two implementations: // 1: "Real" one that wraps one of these things: RefPtr jumpListMgr; HRESULT hr = ::CoCreateInstance( CLSIDDestinationList, nullptr, CLSCTXINPROCSERVER, IIDICustomDestinationList, getter_AddRefs(jumpListMgr));

// 2: "Fake" one that allows us to interrogate it for things it has been passed, for testing. class MockJumpListManager HRESULT BeginList(outparam maxitems and outparam IObjectArray) Wants to be prepared to provide an outparam which is an IObjectArray. We can do that by creating an empty collection, or a collection that returns ShellLinks. HRESULT AddUserTasks(collection) Takes an array of tasks and returns an HRESULT. We can then examine what was passed. HRESULT AppendCategory(string, collection) Takes a string and collection for the custom list. HRESULT CommitList Just returns an HRESULT.

* [Rate this episode](https://forms.gle/9H7fhG69rdGg4Cx98)

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

