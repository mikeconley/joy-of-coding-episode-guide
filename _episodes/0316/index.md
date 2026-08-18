---
date: 2023-02-15
number: 316
---

# Episode 316: Feb 15th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-02-15)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0316.html)

## Topics
* [Bug 1529276](https://bugzilla.mozilla.org/show_bug.cgi?id=1529276) - resource:///modules/WindowsJumpLists.jsm still does main thread I/O
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
    - [ ] Handle the URL removal case
    - [ ] Handle re-entry to buildList
    - [ ] What was with that NSERRORFAILURE we saw after caling .update() not long after startup?
    - [ ] How about private browsing windows? How do the icon caches work for those? How do the built lists work for those?
    - [ ] See how Thunderbird uses JumpListBuilder in case there are things we need to support there.
    - [ ] Figure out how to make the above testable. Then write tests.
      - [ ] Let's update WinTaskbar to have a new method that can be accessed from native code (so not through XPCOM), called, like, DoCreateJumpListBuilder or something. Have it take an argument that is a reference to something that implements a JumpListManager interface. Have JumpListBuilder move that thing to the background thread - the background thread owns it. Then, in our tests, have our GTest call DoCreateJumpListBuilder, passing it something that mocks out JumpListManager. And then call it's populateJumpList method for testing.
    - [ ] Make our approach preffable. Put all the old stuff back (gulp), and update WindowsJumpList to use the new mechanism on a pref.
* [Thunderbird's upcoming re-theme!](https://blog.thunderbird.net/2023/02/thunderbird-115-supernova-preview-the-new-folder-pane/)

* [Rate this episode](https://forms.gle/xJKmY3CwVPDeveRq6)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

