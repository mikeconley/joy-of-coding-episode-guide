---
layout: default
date: 2022-08-17
number: 297
---

# Episode 297: Aug 17th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-08-17)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0297.html)

## Topics
* [Mozilla Connect](https://connect.mozilla.org/)
* First, let's see what it takes to not coalesce items in the Windows Task Tray
  - Because ultimately, that might be the most sensible solution - each profile is mapped to a different spot on the tray.
  - This appears to be how Chromium does it - they're setting a AppUserModelID per profile
  - It turns out we've got a mechanism to do this already. It got added back in bug 577867 but it appears to only work for private browsing windows.
  - mconley to talk to Priv/Sec teams to figure out what's going on with the AUMID stuff. 
* Let's try to make the WindowsJumpList stuff happen off of the main thread! Exciting!
  - This may or may not actually contribute to the permanent private browsing thing we've been looking at, but it's righteous work because of the placement it has in the hang stats list (currently #4!)
  - Goal: I want the JumpListManager to only ever be accessed off of the main thread, so that the main thread in the parent process never has to await a lock.
    - [x] Get rid of maxListItems, since it doesn't appear to be used
    - [x] Get rid of isListCommitted
    - [ ] Make .available return a Promise
    - [ ] Make abortListBuild return a Promise
    - [ ] Make SetAppUserModelId return a Promise
    - [ ] Make addListToBuild return a Promise
    - [ ] Make commitListBuild return a Promise instead of using that old callback mechanism
    - [ ] Make deleteActiveList return a Promise
    - [ ] Update all of the callers of the above methods!
    - [ ] Remove locks and monitors
    - [ ] Migrate off of dedicated lazy thread to background thread pool
  - Goal: I want to make AddListToBuild do most of its work off of the main thread

* [Rate this episode](https://forms.gle/4oTFrM2UzReEp8BE9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
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

