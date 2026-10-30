---
date: 2022-10-05
number: 301
airmozilla: https://mzl.la/joy-of-coding-2022-10-05
agenda: https://mikeconley.ca/joc/agendas/Episode-0301.html
rating: https://forms.gle/uC3CYi14o93cAGA16
---

## Topics

- Thunderbird patch from Episode 300 was merged!
- Masterwayz!
- Let's review [D158655](https://phabricator.services.mozilla.com/D158655)
  - [Are we ESMified yet?](https://spidermonkey.dev/areweesmifiedyet/)
- Let's keep going with the WindowsJumpList stuff!
- Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
  - [x] Get rid of maxListItems, since it doesn't appear to be used
  - [x] Get rid of isListCommitted
  - [x] Make .available return a Promise
  - [x] Make abortListBuild return a Promise
  - [x] Make deleteActiveList return a Promise
  - [x] Make SetAppUserModelId return a Promise
  - [ ] Make addListToBuild return a Promise
  - [ ] Make commitListBuild return a Promise instead of using that old callback mechanism
  - [ ] Update all of the callers of the above methods!
  - [ ] Remove locks and monitors
  - [ ] Migrate off of dedicated lazy thread to background thread pool
