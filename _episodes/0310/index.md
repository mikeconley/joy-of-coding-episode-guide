---
date: 2022-12-21
number: 310
---

# Episode 310: Dec 21st, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-12-21)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0310.html)

## Topics
* [News](https://blog.mozilla.org/en/mozilla/mozilla-launch-fediverse-instance-social-media-alternative/): Mozilla and the Fediverse
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
    - [ ] Tasks
    - [ ] Figure out how to make the above testable.
    - [ ] Make populateJumpList work to create jump list items all in one shot
    - [ ] Implement clearJumpList
    - [ ] See if the above works. If it does, get rid of old changes that we don't need and merge patches down
    - [ ] Update WindowsJumpList.jsm to use the new API instead of the old one.
    - [ ] Update WindowsJumpList.jsm to be simpler so that it doesn't try to do so much lazy stuff since now it's all off of the main thread
    - [ ] Remove the old implementation! Hooray!
    - [ ] Migrate off of dedicated lazy thread to background thread pool
* Let's look at [Delores](https://github.com/grumpygamer/DeloresDev/) for fun to close out the year!
  - [Frank Cifaldi](https://www.youtube.com/watch?v=ikaqus5_QIg) from the Video Game History Foundation talks to Ron Gilbert about Monkey Island and shows off some of the source code and tools used to make the game work!
  - [delores dev](https://grumpygamer.com/delores_dev)
* Questions:
  - "What is easiest way to succeed with applying an old patch, bump it to tip and deal with merge conflicts? To handle review feedback. Is it best to apply somewhere close in the Mercurial tree where it was committed?"

* [Rate this episode](https://forms.gle/aWjmGDYu3hqjaS577)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

