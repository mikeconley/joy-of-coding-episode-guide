**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

* Vertical tabs stuff!
	* Close buttons on vertical tabs
	* Keyboard shortcut for vertical tabs
		* Ctrl-Z on macOS
		* Alt+Ctrl+Z on Linux and Windows
	* Looks like it _might_ ride out as an option in Firefox 136 (March?): https://bugzilla.mozilla.org/show_bug.cgi?id=1936379
* Continuing to document CustomizableUI!
* What to do for the 400th episode??!
	* Do a SPICY HACKING EPISODE. This is where I work on code while eating _very spicy_ food on a regular interval (10 minutes per wing or something)
	* We can examine some video game source code
	* We could try to fix a Thunderbird bug
	* We could try to fix the oldest possible Firefox bug during the episode (so find a really old bug, try to fix it in a one-shot)
	* Write a simple add-on to do... something
	* Try to do something with AI? How would we feel about that?
		* We could write a tool that tries to pipe the transcript of past episodes into an LLM to produce video title suggestions.
		* Revive Adso, and attempt to hand-roll our own captions using newer models
	* Try to write... something in Rust?... I've done this before, but we could try again. Try to port a JS module to Rust for use with application-services.

**[Rate this episode](https://forms.gle/3q8bPY4XkzcTTuXx6)**

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