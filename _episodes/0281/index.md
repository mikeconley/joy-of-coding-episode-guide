---
layout: default
date: 2022-03-02
number: 281
---

# Episode 281: Mar 2nd, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-03-02)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0281.html)

## Topics
* Are you Canadian? [Then consider donating to the Ukraine Humanitarian Crisis Appeal](https://donate.redcross.ca/page/100227/donate/1?_ga=2.69967120.1415423639.1645826820-1854297146.1645826820&_gl=1*zqfv37*_ga*MTg1NDI5NzE0Ni4xNjQ1ODI2ODIw*_ga_376D8LHM0R*MTY0NTgyNjgxOS4xLjEuMTY0NTgyNjk1OS4w)
* [New MDN!](https://hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/)
* [Bug 1756123](https://bugzilla.mozilla.org/show_bug.cgi?id=1756123) - 4.39 - 0.14% tart / tart (Windows) regression on Fri February 11 2022
  - Conclusion: WONTFIX
* [Bug 1550453](https://bugzilla.mozilla.org/show_bug.cgi?id=1550453) - Picture-In-Picture: toggle icon's display place should be customizable
  - Duplicate of [Bug 1680885](https://bugzilla.mozilla.org/show_bug.cgi?id=1680885)
* [Bug 1756235](https://bugzilla.mozilla.org/show_bug.cgi?id=1756235) - Logspam during crashtest runs: JavaScript error: resource://gre/modules/URLQueryStrippingListService.jsm, line 90: TypeError: can't access property "removeEventListener", Services.cpmm.sharedData is null
  - Commented!

* Intermittent failure talk
  - What is an Intermittent Test Failure?
    - (Mike gives his sloppy definition in the video)
  - Mike's guide to dealing with intermittent test failures
    - If you can, get it to reproduce locally!
    - Look at the platform it failed on. Do you have access to it?
    - See if you can reproduce it on that platform! Chances are, if it's restricted to a particular platform, you have a better chance of reproducing it there.
      - Reproducing using:
        - verify
        - chaos mode
        - --start-at / --end-at
        - Or a mixture of the above
  - [Bug 1712012](https://bugzilla.mozilla.org/show_bug.cgi?id=1712012) - Intermittent TEST-UNEXPECTED-TIMEOUT | browser/base/content/test/webrtc/browser_devices_get_user_media_unprompted_access.js | application timed out after 370 seconds with no output

* [Rate this episode](https://forms.gle/7ShpaeGnymXAfBrh9)

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

