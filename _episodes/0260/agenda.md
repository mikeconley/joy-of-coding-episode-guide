**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- Fixed the Joy of Coding Episode Guide theme that was broken due to a Jekyll Theme update that probably happened on GitHub's side of things
- [Bug 1724199 - 10.09 - 9.23% sessionrestore\_no\_auto\_restore / sessionrestore\_no\_auto\_restore + 1 more (Windows) regression on Tue August 3 2021](https://bugzilla.mozilla.org/show_bug.cgi?id=1724199)
    - [Let's see if preloadedState is causing the issue](https://treeherder.mozilla.org/#/jobs?repo=try&revision=2406f69be8f65c5fe2702adca7a88c149825ffb0). I will post the results in a comment in the bug.
- [Bug 1725276 - Intermittent docshell/test/browser/browser_TopLevelNavigationDelegate.js | Test timed out -](https://bugzilla.mozilla.org/show_bug.cgi?id=1725276)
    
-  Questions:
    - Have Firefox devs sent patches to Chromium and have Google devs sent patches over to Firefox?
        - Yes to both.
        - [Igalia](https://www.igalia.com/)
        - [WebRTC](https://webrtc.googlesource.com) as well
    - What song (songs) has been playing in the back of your head lately?
        - Dinosaur Pile-up called 11:11
        - k.flay "Dating my Dad"
    - What in your life do you feel grateful for?
        - Being alive
        - Great family, great friends, great job that I enjoy, live in Canada
        - Small things: tea, coffee, tasty tap water (Toronto!), Toronto
            - Don Valley Parkway 
        - Good books, that I can read them
    - What do you value the most in a friendship and relationship?
        - Ease and fluidity of communication
        - Good humour
        - Trust
    - How would you go about debugging intermittent hangs in Firefox after its been on its own for a while? In the morning it is hanging, but was working when you left at night... and this happens not every day but some
        - The hang itself, at the point where you come back, may have enough information to be actionable. The thing to do is try to turn the hang into actionable data.
        - macOS and Linux, we want to crash intentionally
            - Get the Process ID of the parent process (`ps aux | grep firefox`)
            - Crash using SIGABRT: `kill -SIGABRT <process ID>`, `kill -SIGABRT 1327`
		- Windows, crashintentionally.exe
			- https://releases.mozilla.org/pub/utilities/crashfirefox-intentionally/
			- Source: https://github.com/bsmedberg/crashfirefox-intentionally
		- https://firefox-source-docs.mozilla.org/performance/reporting_a_performance_problem.html
		- 
            

**[Rate this episode](https://forms.gle/xADFGN8CdFDm5uXM8)**

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