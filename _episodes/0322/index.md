---
layout: default
date: 2023-04-19
number: 322
---

# Episode 322: Apr 19th, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-04-19)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0322.html)

## Topics
* TODO: Hunt down race bug for "Pin to Toolbar"
  - Smurfd found this one: [Bug 1712729](https://bugzilla.mozilla.org/show_bug.cgi?id=1712729)
  - Done: [Bug 1828966](https://bugzilla.mozilla.org/show_bug.cgi?id=1828966) - Pin to Toolbar context menu item is sometimes out of sync
* [Bug 1828738](https://bugzilla.mozilla.org/show_bug.cgi?id=1828738) - Make it possible for about:welcome to open an FxA sign-in flow that closes itself after sign-in completes
  - https://developer.mozilla.org/en-US/docs/Web/API/AbortController/AbortController
  - Hypotheses
    - I'm adding a progress listener to the wrong browser
      - <b>aukras saves the day</b> by helping Mike realize that he's added the progress listener to the wrong browser (it was being added to the about:welcome browser, and not the fxaBrowser!)
      - The FxA browser does not accept progress listeners for some reason
      - The progress listener is misconfigured

* [Rate this episode](https://forms.gle/TbkDQtnAaSn5kt9C9)

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

