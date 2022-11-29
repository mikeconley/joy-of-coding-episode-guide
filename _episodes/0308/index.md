---
layout: default
date: 2022-11-23
number: 308
---

# Episode 308: Nov 23rd, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-11-23)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0308.html)

## Topics
* Extensions update
  - [firefox-dev mailing list that you can subscribe to](https://groups.google.com/g/firefox-dev)
    - [Blog post about MV3 and Unified Extensions](https://blog.mozilla.org/addons/2022/11/17/manifest-v3-signing-available-november-21-on-firefox-nightly/)
    - Follow [Planet](https://planet.mozilla.org/)
    - Follow [Planet@fossdon](https://fosstodon.org/@planetmozilla)
    - [Standards position](https://mozilla.github.io/standards-positions/)
    - [Privacy analysis of floc](https://blog.mozilla.org/en/privacy-security/privacy-analysis-of-floc/)

* Back to WindowsJumpLists!
  - Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
    - [x] Get rid of maxListItems, since it doesn't appear to be used
    - [x] Get rid of isListCommitted
    - [x] Make .available return a Promise
    - [x] Make abortListBuild return a Promise
    - [x] Make deleteActiveList return a Promise
    - [x] Make SetAppUserModelId return a Promise
    - [x] Add WebIDL for JumpListShortcutDescription and add populateJumpList method to JumpListBuilder.
    - [ ] Figure out how to make the above testable.
    - [ ] Make populateJumpList work to create jump list items all in one shot
    - [ ] Implement clearJumpList
    - [ ] See if the above works. If it does, get rid of old changes that we don't need and merge patches down
    - [ ] Update WindowsJumpList.jsm to use the new API instead of the old one.
    - [ ] Update WindowsJumpList.jsm to be simpler so that it doesn't try to do so much lazy stuff since now it's all off of the main thread
    - [ ] Remove the old implementation! Hooray!
    - [ ] Migrate off of dedicated lazy thread to background thread pool

* Question: How does the nightly blog schedule work, because sometimes there is a blog post every week and sometimes there is radio silence for a month, like right now.
  - [Blog](https://blog.nightly.mozilla.org/)
  - It's based on the [Firefox Desktop meeting](https://wiki.mozilla.org/Firefox/Meeting) that happens
  - That meeting happens (usually) every 2 weeks
  - 2 weeks ago, meeting was cancelled due to Low Meeting Week
  - Expect similar turbulence as we enter the holidays.

* [Rate this episode](https://forms.gle/sGFwWopvHzb3fszb6)

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

