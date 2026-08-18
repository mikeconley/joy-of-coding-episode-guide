---
date: 2025-03-19
number: 396
---

# Episode 396: Mar 19th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-03-19)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0396.html)

## Topics
* Custom backgrounds
  - browser.newtabpage.activity-stream.newtabWallpapers.customWallpaper.enabled
* Slow Git autocomplete on zsh? Here's the dealio: https://superuser.com/questions/458906/zsh-tab-completion-of-git-commands-is-very-slow-how-can-i-turn-it-off
* Figure out failure and re-land CustomizableUI patches
* More Rust component planning
  - Write a tool that can take a list of base64 encoded md5 hashes and produce a .rs file that has those hashes defined as raw bytes, and can be linked into the library
  - Modify that tool afterwards to also accept a list of base domain strings rather than base64 encoded md5 hashes, so that we can easily update the list
  - Design and write the library. It should ideally just expose the following functions:
    - isAdultURL function
    - addDomainToListForTesting
    - removeDomainFromListForTesting
  - Our utility can use relevancy components "generate-test-data" utility as an example to work from
* Next time: maybe let's learn jj together
  - https://steveklabnik.github.io/jujutsu-tutorial/introduction/introduction.html

* [Rate this episode](https://forms.gle/iurnbvQjc19qC2hT7)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

