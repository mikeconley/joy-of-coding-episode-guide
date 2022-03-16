**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- Exploring about:unloads
    - [aboutUnloads.js](https://searchfox.org/mozilla-central/source/browser/components/tabunloader/content) 
    - [aboutUnloads.html](https://searchfox.org/mozilla-central/rev/a166f59fba89fc70ebfab287f4edb8e05ed4f6da/browser/components/tabunloader/content/aboutUnloads.html)
    - Part of Firefox :: Tabbed Browser in Bugzilla
    - Maybe fact: URLs is a subset of URIs
        - URI: "about:home", "about:about", "viewsource:https://google.ca", "https://mikeconley.ca"
            - about:unloads
        - URLs: "https://mikeconley.ca", "https://example.com", "http://badssl.com"
            - chrome://version
- OpenSearch:
    - https://developer.mozilla.org/en-US/docs/Web/OpenSearch
- [Bug 1674827 - Re-enable startup\_about\_home\_paint\_cached Talos test](https://bugzilla.mozilla.org/show_bug.cgi?id=1674827)
    - https://mikeconley.ca/blog/2020/07/13/improving-firefox-startup-time-with-the-abouthome-startup-cache/
- Feedback:
    - People are digging the questions. Going to keep doing that. Thanks for the feedback!
- Questions:
    - As a normal user: What other products of Mozilla (e.g. Pocket, Mozilla VPN, Firefox Relay, Thunderbird) do you use on a daily basis? What are the features of Firefox you can't live without (e.g. Containers, Picture-in-Picture etc.)?
        
        - Firefox
            - Picture-in-Picture
            - uBlock Origin
            - AwesomeBar
            - Tabs!
            - Password generation
            - Knowing that it's got my interests at heart
        - Mozilla VPN
        - Pocket
        - Thunderbird on one of my desktop machines
        - Fenix
        - Have used Relay in the past, but don't often create aliases
        - Lockwise
    - Can you describe your day of work? (eg. do you have special time to read emails, bugzilla, catch up with slack/matrix, etc.) - what changes when you work on a bigger project vs during a normal day?
        
        - Every day is different, because (at least at this point in my career), I get roped into lots of different meetings.
        - Try to have concentrated blocks of working time
        - The first thing I do in the morning, is go through what happened since the last time I was around.
        - Look at my calendar for the day, look at my task list, and then try to plan a route
    - Can you walk us through your previous jobs? (some general things, interesting stories etc.) - how do they differ from your current job?
        
        - Dishwasher
        - Music store clerk, guitar lesson teacher
        - Quality assurance clerk at a salvage firm
        - Greenhouse, lifting, moving, planting, watering, pruning, etc.
        - Gardener
        - Web application developer for a school board
        - TA
        - Mozilla (contractor)
        - Mozilla (full time)
    - Have you ever made / co-developed add-ons, or is it not your cup of tea?
        
        - MyQOnly
        - [Balcony](https://github.com/mikeconley/balcony/)

**[Rate this episode](https://forms.gle/p537sYotHfqzvTdG7)**

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