---
date: 2022-11-30
number: 309
airmozilla: https://mzl.la/joy-of-coding-2022-11-30
agenda: https://mikeconley.ca/joc/agendas/Episode-0309.html
rating: https://forms.gle/4yWxPMt4PtXTPDy76
---

## Topics

- Migrator reusable component infrastructure is being added in [this patch](https://phabricator.services.mozilla.com/D162623)
- Still hacking on WindowsJumpLists!
  - Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
    - [x] Get rid of maxListItems, since it doesn't appear to be used
    - [x] Get rid of isListCommitted
    - [x] Make .available return a Promise
    - [x] Make abortListBuild return a Promise
    - [x] Make deleteActiveList return a Promise
    - [x] Make SetAppUserModelId return a Promise
    - [x] Add WebIDL for JumpListShortcutDescription and add populateJumpList method to JumpListBuilder.
    - [ ]
      - [ ] Custom List (this is the Frequently Visited stuff)
      - [ ] Frequent is ENABLED by default
      - [ ] Recent is DISABLED by default
      - [ ] Don't need separators
        - [ ] Tasks
    - [ ] Figure out how to make the above testable.
    - [ ] Make populateJumpList work to create jump list items all in one shot
    - [ ] Implement clearJumpList
    - [ ] See if the above works. If it does, get rid of old changes that we don't need and merge patches down
    - [ ] Update WindowsJumpList.jsm to use the new API instead of the old one.
    - [ ] Update WindowsJumpList.jsm to be simpler so that it doesn't try to do so much lazy stuff since now it's all off of the main thread
    - [ ] Remove the old implementation! Hooray!
    - [ ] Migrate off of dedicated lazy thread to background thread pool
- Question: When will WebGPU be available in the main release?
  - [This](https://bugzilla.mozilla.org/show_bug.cgi?id=1746245) is the bug to enable it in Nightly
- No episode next week!
