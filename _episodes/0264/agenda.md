**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- https://blog.mozilla.org/attack-and-defense/2021/09/29/fixing-a-security-bug-by-changing-a-function-signature/
    
- Let's talk about BrowsingContexts! And DocShells!
    
    - [Site Isolation Architecture in Firefox](https://hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/)
        - Goes into detail about Meltdown / Spectre vulnerabilities
- Questions:
    
    - Yes I really get confused like how build system work. How they create binaries. And How do cpp gets build? The Firefox source seems to be a bit esoteric. It would be helpful like how jar.mn moz.build etc integrates together. Thanks.
        - moz.build are Python instructions that build dependency graphs that ultimately get fed into something like Makefile, and then we do a thing like \`make\`. moz.build helps define what gets packaged in omni.ja ("resources", JSMs)
        - jar.mn, which goes into more detail on HTML, XUL, CSS, JS what gets packaged in omni.ja
            - Go find your Firefox install folder
            - Find omni.ja
            - Copy it somewhere else on the file system (this is important - don't do the next step inside of the Firefox install folder)
            - Rename omni.ja to omni.zip
            - Unzip the file
    - Can you talk a bit about the history of the intro/outro jingle?
        - Jingle was written by my friend Barn, who is also the lead singer of my band
            - - [The Johnson Report bandcamp](https://thejohnsonreport.bandcamp.com/)
                - [Music videos](https://www.youtube.com/user/TheJohnsonReport)
                - [Barn's channel](https://www.youtube.com/user/HermitTheFraud/videos)
        - I had asked Barn for something like the hook from [the song "She Says What She Means" by the band Sloan](https://www.youtube.com/watch?v=fg3XlAgHpaI)
    - When you mentor someone, what does the process look like?
        - What does the mentee need? Some of them just need help getting started and finding work, getting set up.
        - Sometimes a person wants deeper insight into how things work, I can do one-on-ones explaining things, or might do a video or presentation about it
        - Career stuff. What does the person want out of their career? What is the shortest most practical line we can draw to get them there, and then let's put together a plan to get them on that line, and figure out how to measure how they're progressing.
    - If you had an extra hour of time each day, what would you spend it on? (What are some things you wish you had more time for?))
        - Reading
        - If I had a block of 3 hours every day to do whatever I wanted that didn't include maintenance things like doing laundry or taking care of the yard or cooking or cleaning... I would probably get better at drawing and painting using my new drawing tool... and maybe cartooning, and maybe I'd work on designing a point and click adventure game.
    - Have you ever considered switching to linux (eg. arch, etc. ?) - have you ever daily-driven some linux distro?
        - Knoppix was my first introduction to Linux (booted off of a CD)
        - Fedora
        - Ubuntu
- **No episode next week** due to unavoidable meetings. Sorry!
    
- Special shout out to "shittyskydiver" on YouTube

**[Rate this episode](https://forms.gle/ninYYnQ6tc4KDc6U6)**

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