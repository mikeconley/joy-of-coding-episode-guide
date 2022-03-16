**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- [Bug 1736690 - Remove or update probes expiring in Firefox 96: pictureinpicture.most\_concurrent\_players](https://bugzilla.mozilla.org/show_bug.cgi?id=1736690)
    - That was easy! Patch posted.
- Questions:
    - How is gBrowser and xpcom used? Can you talk about it too?
        - `gBrowser`
            - `gBrowser` is the name of the component in a Firefox browser window that manages tabs, and the underlying infrastructure for switching tabs, adding tabs, knowing about tab switches, etc.
            - [Light documentation](https://firefox-source-docs.mozilla.org/browser/base/tabbrowser/index.html)
            - `gBrowser` is a window-global instance of a component called tabbrowser
            - `gBrowser` is a pretty bad name for what it is. Could maybe be called `gTabsManager` or `gBrowsersManager`
            - `<browser>`, is similar to an `<iframe>`
            - `g` is for global, `a` is for argument, `m` is for method, `s` is for static, `k` is for global constant, ALL_CAPS for global constant
            - Firefox used to not have tabs! At some point in its lineage, Firefox didn't have tabs. It was one `<browser>` per window. `gBrowser`.
                - They kept the same name when adding tabs! I think this was to make it easier to support XUL add-ons that relied on touching `gBrowser`. The new `gBrowser` variable had the same interface as the old one but would forward calls to the currently selected `<browser>`.
            - [Source for reading](https://searchfox.org/mozilla-central/rev/f8576fec48d866c5f988baaf1fa8d2f8cce2a82f/browser/base/content/tabbrowser.js)
        - XPCOM
            - It's a very old Mozilla technology modeled after COM from Microsoft
            - Infrastructure for defining interfaces for components that are implementation-language agnostic
                - This means a component written in language A can in theory talk to a component written in language B by way of an interface defined in an (XP)IDL file (.idl)
            - The dream was that Mozilla-backed applications could be written in whatever language you wanted so long as it "supported XPCOM/XPConnect".
            - XPCOM components these days are written in C++, JavaScript or Rust
            - Registry of XPCOM components, and XPCOM component singletons ("services")
            - Cc (`Components.classes`), `Ci` (`Components.interfaces`)
            -     let referrerInfo = Cc["@mozilla.org/referrer-info;1"].createInstance(Ci.nsIReferrerInfo);
            - deCOMtamination of the Mozilla source code
                - WebIDL Bindings (.webidl)
                - https://github.com/mdn/archived-content/tree/main/files/en-us/mozilla/tech/xpcom
        - [Help us port documentation! From here!](https://github.com/mdn/archived-content)
            - First find the documentation that you want to port in the GitHub repository
            - File a bug blocking [this bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1736613)
            - Follow these instructions to convert the document to an RST file
            - [Use this example as a template](https://phabricator.services.mozilla.com/D121116)
            - Post for review!
    - Can you explain the process of writing "These Weeks in Firefox" (from start to finish) ?
    - WebExtensions and how they interact with DocShells / BrowsingContexts
    - How a patch gets into Firefox, from start to finish!



        

**[Rate this episode](https://www.example.com)**

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