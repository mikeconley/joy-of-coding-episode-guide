**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- [Bug 1707582 - Intermittent /modules/test/browser/browser\_UsageTelemetry\_interaction.js | Expected to see the correct value for bookmark-item in bookmarks\_bar. - "undefined" == 1 - JS frame :: /browser/modules/test/browser/browser\_UsageTelemetry_interaction.js :: assert](https://bugzilla.mozilla.org/show_bug.cgi?id=1707582)
- Plug for Replay (https://www.replay.io/)
- [Let's look at a memory report](https://bugzilla.mozilla.org/show_bug.cgi?id=1619772)
- [Let's bump some probe expiries](https://bugzilla.mozilla.org/show_bug.cgi?id=1730042)
    - [And here](https://bugzilla.mozilla.org/show_bug.cgi?id=1730041)
- Questions:
    - What are your thoughts on Proton redesign?
        - I like it!
    - When I was tinkering with Firefox I found a way to zoom text only: Menu Bar -> View -> Zoom -> Zoom text only. I find it extremely useful. Is there a reason why this could not be additionally accessed using "Zoom controls" or activated with some shortcut? + What is the process for deciding which items to select in menu bars/toolboxes?
    - Have you ever read a book on e-ink paper?
        - Yes
        - I have a Kobo
        - Margaret Atwood's Oryx and Crake
    - Some companies/teams once in a while have a time period when they focus solely on fixing bugs - what do you think about this approach? have you ever discussed this with your colleagues?
        - Yes, I like this approach. We do this approach! It's a great way to fix papercuts and also to pay down technical debt.

**[Rate this episode](https://forms.gle/SSpT4vYSGYM6vAWU9)**

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