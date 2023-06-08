---
layout: default
date: 2023-06-07
number: 327
---

# Episode 327: Jun 7th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-06-07)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0327.html)

## Topics
* WindowsJumpLists! Let's gooooo!
  - A lot of the complexity that we're dealing with architecturally is because we're trying to maintain the old backend while adding the new capability with a new backend, but the two backends share some infrastructure.
  - What I want to do is determine if we can do a better job of separating out the jumplist backend by reading a pref at runtime and choosing the right implementation.
* TODO
  - [x] Rename nsIJumpListBuilder to nsILegacyJumpListBuilder
  - [x] Add createLegacyJumpListBuilder to nsIWinTaskBar to use the old mechanism
  - [x] Update WindowsJumpList to use the legacy interface
  - [x] Create a new nsIJumpListBuilder
  - [ ] Populate nsIJumpListBuilder using the code we developed in the previous iteration
  - [ ] Have createJumpListBuilder in nsIWinTaskBar use that
  - [ ] Update WindowsJumpLists to choose the right builder based on the pref and treat them correctly based on that pref.

* [Rate this episode](https://forms.gle/CCcpZn82xDPMaH3e7)

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

