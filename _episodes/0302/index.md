---
layout: default
date: 2022-10-12
number: 302
---

# Episode 302: Oct 12th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-10-12)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0302.html)

## Topics
* Today - Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
  - [x] Get rid of maxListItems, since it doesn't appear to be used
  - [x] Get rid of isListCommitted
  - [x] Make .available return a Promise
  - [x] Make abortListBuild return a Promise
  - [x] Make SetAppUserModelId return a Promise
  - [ ] Add WebIDL for JumpListShortcutDescription and add populateJumpList method to JumpListBuilder. 
  - [ ] Figure out how to make the above testable.
  - [ ] Make addListToBuild return a Promise
  - [ ] Make commitListBuild return a Promise instead of using that old callback mechanism
  - [ ] Make deleteActiveList return a Promise
  - [ ] Update all of the callers of the above methods!
  - [ ] Remove locks and monitors
  - [ ] Migrate off of dedicated lazy thread to background thread pool
* [WebIDL documentation](https://firefox-source-docs.mozilla.org/dom/webIdlBindings/index.html)

* [Rate this episode](https://forms.gle/jFQ1xLiJ5unBatWR7)

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

