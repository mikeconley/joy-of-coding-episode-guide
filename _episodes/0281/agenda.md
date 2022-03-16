**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

## **Today**

- Are you Canadian? [Then consider donating to the Ukraine Humanitarian Crisis Appeal](https://donate.redcross.ca/page/100227/donate/1?_ga=2.69967120.1415423639.1645826820-1854297146.1645826820&_gl=1*zqfv37*_ga*MTg1NDI5NzE0Ni4xNjQ1ODI2ODIw*_ga_376D8LHM0R*MTY0NTgyNjgxOS4xLjEuMTY0NTgyNjk1OS4w)
- [New MDN!](https://hacks.mozilla.org/2022/03/a-new-year-a-new-mdn/)
- [Bug 1756123 - 4.39 - 0.14% tart / tart (Windows) regression on Fri February 11 2022](https://bugzilla.mozilla.org/show_bug.cgi?id=1756123)
    - Conclusion: WONTFIX
- [Bug 1550453 - Picture-In-Picture: toggle icon's display place should be customizable](https://bugzilla.mozilla.org/show_bug.cgi?id=1550453)
    - Duplicate of bug [1680885](https://bugzilla.mozilla.org/show_bug.cgi?id=1680885)
- [Bug 1756235 - Logspam during crashtest runs: JavaScript error: resource://gre/modules/URLQueryStrippingListService.jsm, line 90: TypeError: can't access property "removeEventListener", Services.cpmm.sharedData is null](https://bugzilla.mozilla.org/show_bug.cgi?id=1756235)
    - Commented!
- Intermittent failure talk
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
            
    - [Bug 1712012 - Intermittent TEST-UNEXPECTED-TIMEOUT | browser/base/content/test/webrtc/browser\_devices\_get\_user\_media\_unprompted\_access.js | application timed out after 370 seconds with no output](https://bugzilla.mozilla.org/show_bug.cgi?id=1712012)

**[Rate this episode](https://forms.gle/7ShpaeGnymXAfBrh9)**

**Chat**

- [Join us in the Livehacking room on Mozilla’s Matrix instance!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist) Here’s [documentation on how to join](https://wiki.mozilla.org/Matrix). I’m only sorta monitoring the Twitch chat. A bot will try to bridge Matrix and Twitch (joc-bridgebot).

**Links**

- [nbp hacks on the SpiderMonkey JS engine](https://www.twitch.tv/BackToTheCode)
- [Alessandro Castellani has been streaming himself livehacking on Thunderbird](https://www.youtube.com/c/AlessandroCastellani/videos)
- [emilio hacks on Firefox!](https://www.youtube.com/channel/UCYbsdvH4_52BFAijFVgYGgA)
- [Compiler Compiler - watch a Mozilla engineer hack on the SpiderMonkey JavaScript engine!](https://www.twitch.tv/codehag)
- [How mconley uses Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
- [Fission](https://wiki.mozilla.org/Project_Fission) \- what is it, and how does it work?
- [Andreas Kling hacks on a custom browser engine for a hand-rolled OS called SerenityOS](https://www.youtube.com/playlist?list=PLMOpZvQB55be0Nfytz9q2KC_drvoKtkpS)
- [The Joy of Coding: Community-Run Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)
    - Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
    - [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [Check out Josh Marinacci](https://twitter.com/joshmarinacci) hacking on [Firefox Reality, our nascent VR browser](https://www.twitch.tv/joshmarinacci)!
- [I've been mirroring the episodes to YouTube](https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5)
- [Code Therapy with Danny O’Brien](https://www.youtube.com/channel/UCDShi-SQdFVRnQrMla9G_kQ)
- Watch a developer put together a Windows game from scratch (no third-part engines) - really great explanations: https://handmadehero.org/
- [/r/WatchPeopleCode](https://www.reddit.com/r/WatchPeopleCode) for more livehacking!

**Glossary**

- BHR - “Background Hang Reporter”, a thing that records information about when Firefox performs poorly and sends it over Telemetry
- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)
- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- Deserialize - "turn a serialized object back into the complex object”
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc
- Regression - something that made behaviour worse rather than better. Regress means to “go backward”, more or less.
- l10n - localization
- a11y - accessibility
- i18n - internationalization
- k8s - kubernetes

**Feedback**

- [@mconley@mastodon.social on Mastodon](https://mastodon.social/@mconley)
- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on [irc.mozilla.org](http://irc.mozilla.org/)
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)
- mconley at mozilla dot com