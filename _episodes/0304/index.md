---
layout: default
date: 2022-10-26
number: 304
---

# Episode 304: Oct 26th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-10-26)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0304.html)

## Topics
* A very spoooOOOOOooky episode!
* Let's get back to the WindowsJumpList stuff.
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
* Question:
  - I have many preferences in about:config that start with "services.sync.prefs.sync-seen.". I know these have to do with syncing prefs, but I don't remember the "-seen" part. What does the -seen mean? is it new?
    - [Bug 1731249#c13](https://bugzilla.mozilla.org/show_bug.cgi?id=1731249#c13)

* [Rate this episode](https://forms.gle/AkEuwQuRZGmXp7xs9)

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

