---
layout: default
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

## Other
* [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
* [npb hacks](https://www.twitch.tv/BackToTheCode) on the SpiderMonkey JS engine
* [Compiler Compiler](https://www.twitch.tv/codehag) live stream
* Try out Mozilla [VPN](https://vpn.mozilla.org/)
* How mconley uses [Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mike's Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
* [Codetribute](https://codetribute.mozilla.org/) - Help contribute to Firefox, good mentored bugs for You.
  - First, [Create](https://bugzilla.mozilla.org/createaccount.cgi) a Mozilla Bugzilla account.

