**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- Episode naming!
- Better mic settings, hopefully. More dynamic compression!
- Needinfos:
    - [Bug 1706981 - Bookmarks Menu Toolbar button submenu items have incorrectly placed chevron on Windows](https://bugzilla.mozilla.org/show_bug.cgi?id=1706981)
    - [Bug 1707279 - picture-in-picture control do not always disappear](https://bugzilla.mozilla.org/show_bug.cgi?id=1707279)
        - [Getting set up](https://firefox-source-docs.mozilla.org/setup/index.html)
        - [Contributor quick reference. You can submit patches using either Mercurial or Git!](https://firefox-source-docs.mozilla.org/contributing/contribution_quickref.html)
        - [Guide on building Firefox](https://firefox-source-docs.mozilla.org/setup/index.html)
- https://codetribute.mozilla.org/
- Questions:
    - Where do Services.wm.functions exist?
        - The properties for Services.jsm are defined using \`js_name\` in the \`components.conf\` file when registering XPCOM components statically at build time.
        - Services.wm points to [nsWindowMediator](https://searchfox.org/mozilla-central/rev/1e7f7235cf822e79cd79ba9e200329ede3d37925/xpfe/appshell/nsWindowMediator.cpp) which implements the [nsIWindowMediator](https://searchfox.org/mozilla-central/rev/1e7f7235cf822e79cd79ba9e200329ede3d37925/xpfe/appshell/nsIWindowMediator.idl) interface
    - Also when i receive a warning on the browser toolbox is there any way to know from which path it comes (I mean stack trace)?
        - It depends. If the warning passed an Error, then you get it for free. Otherwise, it will only show you the filename and line number where the warning was logged, and from there you could attach a breakpoint and wait to hit it again.
    - I would be interested in a write-up about your stream setup / equipment
        - Covered somewhat in \[Episode 109\](https://www.youtube.com/watch?v=0K-hPyqOyL0)
    - Can you explain the process of writing "These Weeks in Firefox" (from start to finish) ?
        - https://wiki.mozilla.org/Firefox/Meeting
        - During the meeting, we take notes as updates are given.
        - After the meeting, a few of us stick around to rewrite the meeting notes into something more palatable
        - We put developer-centric things in "Below the fold" - this doesn't make the cut to the blog, but goes to the firefox-dev mailing list
        - We then post to firefox-dev and the blog. Done!
    - WebExtensions and how they interact with DocShells / BrowsingContexts
        - Next episode. Promise.
    - How a patch gets into Firefox, from start to finish!
        - Next episode. Promise.
    - I have been watching your videos for about two years now. I'm curious if you know who smurfd is. Have you ever met?
        - No! Have never met. Don't know where they are. Don't know who they are. But they're great.
    - Read anything interesting lately?
        - After the Flood by Margaret Atwood (MaddAddam trilogy)
        - Hands on Rust
            - Cracked the cover, started reading, looks good, haven't gotten into the meat of it yet. Maybe over the winter holidays, when I have some real focus time.
        - https://www.mozilla.org/en-US/firefox/94.0/releasenotes/
            - https://wiki.mozilla.org/Project_Fission
            - [VPN! Give it a shot!](https://www.mozilla.org/en-US/products/vpn/)

**[Rate this episode](https://forms.gle/iEq2Eq6s4zWEC66g7)**

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