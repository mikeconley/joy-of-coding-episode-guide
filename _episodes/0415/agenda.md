**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- keanu.codes:
    - ![423cda9800316a7e622b5dff580060bf.png](images/b08ff93f94c44aed9186a23c6cf575f9)
    - [Error code 415](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/415) on MDN
- Sections in the US!
- The widgets on Beta and Nightly
- Fairly gnarly toolbar bug - 142.0.1 went out today.
- Let's keep going with the tool we wrote! I made some changes. I've copied over the TODOs from last week.
- TODO
    - Query GitHub for the most recent revision SHA.
        - http "https://api.github.com/repos/mozilla-firefox/firefox/commits?sha=main&per_page=1&page=1"
    - Check to see if the Mercurial mapping is in the local cache.
        - If not, ask [this tool](https://bugzilla.mozilla.org/show_bug.cgi?id=1963822#c3) for a mapping to the Mercurial SHA
    - Use the Mercurial SHA and ask Taskcluster JS library for train-hop job status
        - Hit [https://treeherder.mozilla.org/api/project/mozilla-central/push/?full=true&count=10&revision=\\](https://treeherder.mozilla.org/api/project/mozilla-central/push/?full=true&count=10&revision=%5C)\[Mercurial SHA\] to get back job description
        - Extract push id from description (it's the id value), and then request all jobs
        - Query [https://treeherder.mozilla.org/api/jobs/?push_id=\\](https://treeherder.mozilla.org/api/jobs/?push_id=%5C)\[push id\]&job_group_symbol=nt-trainhop
        - That should give us the pass/fail on the trainhop jobs. Check for repeat platforms to detect intermittents.
    - Get newtab.ftl last changed date from GitHub
    - Get webext-glue/locales/en-US/newtab.ftl last changed date from GitHub
    - Get locales-report.json from GitHub
    - Use jq-web library (https://github.com/fiatjaf/jq-web) to query Experimenter for active deploys, rollouts and experiments.

**[Rate this episode](https://forms.gle/JPF5hBvf4xJbMUSz5)**

**Chat**

- [Join us in the Livehacking room on Mozilla’s Matrix instance!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist) Here’s [documentation on how to join](https://wiki.mozilla.org/Matrix). I’m only sorta monitoring the Twitch chat. A bot will try to bridge Matrix and Twitch (joc-bridgebot).

**Links**

- [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
- [nbp hacks on the SpiderMonkey JS engine](https://www.twitch.tv/BackToTheCode)
- [Alessandro Castellani has been streaming himself livehacking on Thunderbird](https://www.youtube.com/c/AlessandroCastellani/videos)
- [emilio hacks on Firefox!](https://www.youtube.com/channel/UCYbsdvH4_52BFAijFVgYGgA)
- [Compiler Compiler - watch a Mozilla engineer hack on the SpiderMonkey JavaScript engine!](https://www.twitch.tv/codehag)
- [How mconley uses Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
- [Andreas Kling hacks on a custom browser engine for a hand-rolled OS called SerenityOS](https://www.youtube.com/playlist?list=PLMOpZvQB55be0Nfytz9q2KC_drvoKtkpS)
- [The Joy of Coding: Community-Run Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)
    - Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
    - [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
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

- [@mconley@mozilla.social on Mastodon](https://mozilla.social/@mconley)
- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- You can chat with me on [Matrix](https://wiki.mozilla.org/Matrix) at @mconley:mozilla.org
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)
- mconley at mozilla dot com