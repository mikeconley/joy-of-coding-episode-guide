---
layout: default
date: 2023-03-22
number: 319
---

# Episode 319: Mar 22nd, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-03-22)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0319.html)

## Topics
* New Migration Wizard - Sneak peek - by setting browser.migrate.content-modal.enabled to true in about:config. No need to restart. 
  - [Bug 1529276](https://bugzilla.mozilla.org/show_bug.cgi?id=1529276) - resource:///modules/WindowsJumpLists.jsm still does main thread I/O
* Still hacking on WindowsJumpLists!
  - Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
    - [x] Get rid of maxListItems, since it doesn't appear to be used
    - [x] Get rid of isListCommitted
    - [x] Make .available return a Promise
    - [x] Make abortListBuild return a Promise
    - [x] Make deleteActiveList return a Promise
    - [x] Make SetAppUserModelId return a Promise
    - [x] Add WebIDL for JumpListShortcutDescription and add populateJumpList method to JumpListBuilder.
    - [x] Custom List (this is the Frequently Visited stuff) - Frequent is ENABLED by default - Recent is DISABLED by default - Don't need separators
    - [x] Tasks
    - [x] Update methods so that tasks and custom lists are added in the same method call. So a single populate method that takes something like... (taskDescriptions, customTitle, customListDescriptions)
    - [x] Finish the URL removal thing. Basically, if an item was removed via the shell, the next call to AppendCategory cannot include that item with the same display name - the next call needs to display something else entirely.
    - [x] Implement clearJumpList (it's called deleteActiveList)
    - [x] Handle the URL removal case
    - [x] Handle re-entry to buildList
    - [x] What was with that NS_ERROR_FAILURE we saw after caling .update() not long after startup?
    - [x] See how Thunderbird uses JumpListBuilder in case there are things we need to support there.
      - [x] It's a simple usage. They don't have any custom items. We should support the no-custom-items case.
    - [x] How about private browsing windows? How do the icon caches work for those? How do the built lists work for those?
    - [x] Make our approach preffable. Put all the old stuff back (gulp), and update WindowsJumpList to use the new mechanism on a pref.
    - [ ] Figure out how to make the above testable. Then write tests.
      - [ ] Let's update WinTaskbar to have a new method that can be accessed from native code (so not through XPCOM), called, like, DoCreateJumpListBuilder or something. Have it take an argument that is a reference to something that implements a JumpListManager interface. Have JumpListBuilder move that thing to the background thread - the background thread owns it. Then, in our tests, have our GTest call DoCreateJumpListBuilder, passing it something that mocks out JumpListManager. And then call it's populateJumpList method for testing.

* Next week, I am travelling and won't be able to stream! Sorry!
* [Rate this episode](https://forms.gle/j8giTgUbTM5NMXgL6)

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

