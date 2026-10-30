---
date: 2022-08-24
number: 298
airmozilla: https://mzl.la/joy-of-coding-2022-08-24
agenda: https://mikeconley.ca/joc/agendas/Episode-0298.html
rating: https://forms.gle/Hn9zuXR8Hav1Sg49A
---

## Topics

- Code review: [D155448](https://phabricator.services.mozilla.com/D155448)
- Let's try to make the WindowsJumpList stuff happen off of the main thread! Exciting!
  - This may or may not actually contribute to the permanent private browsing thing we've been looking at, but it's righteous work because of the placement it has in the hang stats list (currently #4!)
  - Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
    - [x] Get rid of maxListItems, since it doesn't appear to be used
    - [x] Get rid of isListCommitted
    - [x] Make .available return a Promise
    - [x] Make abortListBuild return a Promise
    - [x] Make SetAppUserModelId return a Promise
    - [ ] Make addListToBuild return a Promise
    - [ ] Make commitListBuild return a Promise instead of using that old callback mechanism
    - [ ] Make deleteActiveList return a Promise
    - [ ] Update all of the callers of the above methods!
    - [ ] Remove locks and monitors
    - [ ] Migrate off of dedicated lazy thread to background thread pool
