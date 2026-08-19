---
date: 2023-01-25
number: 313
---

# Episode 313: Jan 25th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-01-25)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0313.html)

## Topics
* Still hacking on WindowsJumpLists!
  - Let's try to get something to show up!
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
    - [ ] Update methods so that tasks and custom lists are added in the same method call. So a single populate method that takes something like... (taskDescriptions, customTitle, customListDescriptions)
    - [ ] Finish the URL removal thing. Basically, if an item was removed via the shell, the next call to AppendCategory cannot include that item with the same display name - the next call needs to display something else entirely.
    - [ ] Figure out how to make the above testable. Then write tests.
    - [x] Implement clearJumpList (it's called deleteActiveList)
    - [ ] See if the above works. If it does, get rid of old changes that we don't need and merge patches down
    - [ ] Update WindowsJumpList.jsm to use the new API instead of the old one.
    - [ ] Update WindowsJumpList.jsm to be simpler so that it doesn't try to do so much lazy stuff since now it's all off of the main thread
    - [ ] Remove the old implementation! Hooray!
    - [ ] Migrate off of dedicated lazy thread to background thread pool

* [Rate this episode](https://forms.gle/kUwBNR7s5m9fifMY9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

