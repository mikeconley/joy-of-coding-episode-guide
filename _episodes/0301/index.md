---
layout: default
date: 2022-10-05
number: 301
---

# Episode 301: Oct 5th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-10-05)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0301.html)

## Topics
* Thunderbird patch from Episode 300 was merged!
* Masterwayz!
* Let's review [D158655](https://phabricator.services.mozilla.com/D158655)
  - [Are we ESMified yet?](https://spidermonkey.dev/areweesmifiedyet/)
* Let's keep going with the WindowsJumpList stuff!
* Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
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

* [Rate this episode](https://forms.gle/uC3CYi14o93cAGA16)

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

