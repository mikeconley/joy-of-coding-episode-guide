---
date: 2022-10-12
number: 302
airmozilla: https://mzl.la/joy-of-coding-2022-10-12
agenda: https://mikeconley.ca/joc/agendas/Episode-0302.html
rating: https://forms.gle/jFQ1xLiJ5unBatWR7
---

## Topics

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
- [WebIDL documentation](https://firefox-source-docs.mozilla.org/dom/webIdlBindings/index.html)
