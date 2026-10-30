---
date: 2022-08-31
number: 299
airmozilla: https://mzl.la/joy-of-coding-2022-08-31
agenda: https://mikeconley.ca/joc/agendas/Episode-0299.html
rating: https://forms.gle/ZLfhcDHnDcexXwjj7
---

## Topics

- Next week is Episode 300!
  - I'm going to see if I can contribute a fix to Thunderbird!
    - I started as a contractor working on Thunderbird for a subsidiary of Mozilla called Mozilla Messaging
    - MZLA Technologies now runs Thunderbird
  - Failing that, in anticipation for the upcoming Monkey Island game, I thought we could examine the [ScummVM](https://www.scummvm.org/) [implementation](https://github.com/scummvm/scummvm) of the SCUMM engine!
- No episodes on September 21st or September 28th due to travel
- Let's [review a patch!](https://phabricator.services.mozilla.com/D144711)
- Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
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
