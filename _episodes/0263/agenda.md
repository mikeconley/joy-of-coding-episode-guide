**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- New toy to show off!
    - Wacom Cintiq 16
- [Bug 1730039 - Remove or update probes expiring in Firefox 95: pictureinpicture.*](https://bugzilla.mozilla.org/show_bug.cgi?id=1730039)
    - [Lean data practices](https://www.mozilla.org/en-US/about/policy/lean-data/)
- [Bug 1730042 - Remove or update probes expiring in Firefox 95: browser.startup.abouthome\_cache\_*](https://bugzilla.mozilla.org/show_bug.cgi?id=1730042)
- [Bug 1730041 - Remove or update probes expiring in Firefox 95: FX\_TAB\_CLOSE_*](https://bugzilla.mozilla.org/show_bug.cgi?id=1730041)
- [Bug 1619772 - Memory leak after long work](https://bugzilla.mozilla.org/show_bug.cgi?id=1619772)
    - [Dark matter detector](https://firefox-source-docs.mozilla.org/xpcom/dmd.html)
- Questions:
    - 1\. Picture-in-Picture: Current way to see all available control options is to visit https://support.mozilla.org/en-US/kb/about-picture-picture-firefox#w_keyboard-shortcuts. Would it be possible to add a small button (perhaps only when using PIP for the first time), which could expand to show all available shortcuts or maybe direct user to this page?
        - The general keyboard shortcut problem in Firefox
        - [Shortcut HUD](https://bugzilla.mozilla.org/show_bug.cgi?id=492557)
            - Problem: keyboard shortcuts are not all registered in one place!
        - Picture-in-Picture
            - Build up Site-specific video adapters
            - Exposing more controls on the player window
            - Have tooltips on those controls for the keyboard shortcuts
    - 2\. Are there any newsletters that you are subscribed to? (for example I read Thomas Frank's Tuesday Tools and Tips)
        - No. I don't have any that I'm subscribed to.
        - I do write "These Weeks in Firefox", so if you want to check that out, [here it is](https://blog.nightly.mozilla.org/)
    - 3\. When it comes to planning (daily, events) - do you use a traditional calendar, a digital calendar or something else?
        - I use a combination of Google Calendar, Rememberthemilk, for work stuff I'll set needinfos on myself in Bugzilla.

**[Rate this episode](https://forms.gle/tQRJeoBX5e4MRCsm9)**

**Chat**

- [Join us in the Livehacking room on Mozilla’s Matrix instance!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist) Here’s [documentation on how to join](https://wiki.mozilla.org/Matrix). I’m only sorta monitoring the Twitch chat. A bot will try to bridge Matrix and Twitch (joc-bridgebot).

**Links**

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