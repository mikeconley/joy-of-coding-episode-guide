---
date: 2022-08-31
number: 299
---

# Episode 299: Aug 31th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-08-31)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0299.html)

## Topics
* Next week is Episode 300!
  - I'm going to see if I can contribute a fix to Thunderbird!
    - I started as a contractor working on Thunderbird for a subsidiary of Mozilla called Mozilla Messaging
    - MZLA Technologies now runs Thunderbird
  - Failing that, in anticipation for the upcoming Monkey Island game, I thought we could examine the [ScummVM](https://www.scummvm.org/) [implementation](https://github.com/scummvm/scummvm) of the SCUMM engine!
* No episodes on September 21st or September 28th due to travel
* Let's [review a patch!](https://phabricator.services.mozilla.com/D144711)
* Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
    - [x] Get rid of maxListItems, since it doesn't appear to be used
    - [x] Get rid of isListCommitted
    - [x] Make .available return a Promise
    - [x] Make abortListBuild return a Promise
    - [x] Make deleteActiveList return a Promise
    - [ ] Make SetAppUserModelId return a Promise
    - [ ] Make addListToBuild return a Promise
    - [ ] Make commitListBuild return a Promise instead of using that old callback mechanism
    - [ ] Update all of the callers of the above methods!
    - [ ] Remove locks and monitors
    - [ ] Migrate off of dedicated lazy thread to background thread pool

* [Rate this episode](https://forms.gle/ZLfhcDHnDcexXwjj7)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

