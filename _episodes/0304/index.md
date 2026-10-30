---
date: 2022-10-26
number: 304
airmozilla: https://mzl.la/joy-of-coding-2022-10-26
agenda: https://mikeconley.ca/joc/agendas/Episode-0304.html
rating: https://forms.gle/AkEuwQuRZGmXp7xs9
---

## Topics

- A very spoooOOOOOooky episode!
- Let's get back to the WindowsJumpList stuff.
- Today - Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
  - [x] Get rid of maxListItems, since it doesn't appear to be used
  - [x] Get rid of isListCommitted
  - [x] Make .available return a Promise
  - [x] Make abortListBuild return a Promise
  - [x] Make SetAppUserModelId return a Promise
  - [ ] Add WebIDL for JumpListShortcutDescription and add populateJumpList method to JumpListBuilder.
  - [ ] Figure out how to make the above testable.
  - [ ] Make addListToBuild return a Promise
  - [ ] Make commitListBuild return a Promise instead of using that old callback mechanism
  - [ ] Make deleteActiveList return a Promise
  - [ ] Update all of the callers of the above methods!
  - [ ] Remove locks and monitors
  - [ ] Migrate off of dedicated lazy thread to background thread pool
- Question:
  - I have many preferences in about:config that start with "services.sync.prefs.sync-seen.". I know these have to do with syncing prefs, but I don't remember the "-seen" part. What does the -seen mean? is it new?
    - [Bug 1731249#c13](https://bugzilla.mozilla.org/show_bug.cgi?id=1731249#c13)
