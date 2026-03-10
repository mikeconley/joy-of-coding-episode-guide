---
layout: default
date: 2025-12-10
number: 422
---

# Episode 422: Dec 10th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-12-10)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0422.html)

## Topics
* ![Alt text](https://mikeconley.ca/joc/agendas/images/bd6f8274570d4c35a8b34f5871010b55 "keanu code 422")
  - https://www.keanu.codes/?code=422
  - Brought to you by HTTP code 422
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/422
* Q: "My release version of private browsing was updated with this about:config variable: browser.privatebrowsing.felt-privacy-v1 I was a little surprised as it isn't default in nightly yet... Just from looking at Bugzilla it is hard to see initial bugs and what stage feature rollouts and trials are at. Can you give some pointers?"
* Let's keep going with the holepunching thing!
  - Tests
    - Tests for the AboutNewTabComponentRegistry
    - Tests for the ExternalComponentsFeed
    - Tests for the ExternalComponentWrapper
    - Test for the search component registration, to make sure it's happening
  -  Potentially rename #verifyConfiguration to #validateConfiguration, and have it actually do something (in this case, just make sure another SEARCH component wasn't already registered)
  - Update JSDoc comments
  - [x] Determine if ExternalComponents.refresh is being called at the right time
    - Right now, it seems to be called too frequently, and I think we're not using Redux correctly.
  - Think through the error/setError state for ExternalComponentWrapper
  - Add some initial documentation!
* Next week is the last stream for 2025, the "holiday" stream! And then I'm off for 2 weeks for holidays!
* TODO: Find the bug that flips the pref by default, and attach it to this agenda

* [Rate this episode](https://forms.gle/HapPSJ5yU8SQct5p7)

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

