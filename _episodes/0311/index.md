---
layout: default
date: 2023-01-11
number: 311
---

# Episode 311: Jan 11th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-01-11)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0311.html)

## Topics
* Reviewing a patch for [Danny Colin!](https://bugzilla.mozilla.org/show_bug.cgi?id=1316727)
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

* Question: "What is easiest way to succeed with applying an old patch, bump it to tip and deal with merge conflicts? To handle review feedback. Is it best to apply somewhere close in the Mercurial tree where it was committed?"
  - Answer: It's best if you can take advantage of the VCS's smarts when reviving an old patch. moz-phab patch XYZ --apply-to here just uses the patch command under the hood to apply the patch directly. Rebase the old patch from where it was onto the tip. That will take advantage of what the VCS knows about what has happened since that commit was made.

* [Rate this episode](https://forms.gle/zenyCRvp5YH1Ukfr8)

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

