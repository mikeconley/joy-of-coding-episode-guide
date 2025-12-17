**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

* 414 keanu.codes
	* ![28a3ea8e5ff19a0b79bf96f9ff1b57aa.png](images/23f4022ac0c84e4eb7903704898bcdf7)
	* https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/414
* New Tab trainhop readyness tool
	* Overarching goal: a tool that can be used by an Eng, PM, TPM to assess the viability of the most recent revision (or a specific revision) of the newtab code in mozilla-central (or main) to train-hop to Beta and / or Release.
		* Train-hop compatibility state from CI
			* Displays train-hop compatibility meta bug stats, and reminds users when a compatibility shim can be removed.
		* Localization state (are the strings displayed by default localized in all of the supported locales? If not, which locales are localized and which are not)?
			* I want to know if the en-US newtab.ftl is different from the one included in the XPI, because this means that the localizations need to be updated before a train-hop can possibly proceed.
		* Glean / Metrics state to see if runtime metrics or pings need to be generated.
		* Existing experiments and rollouts on each channel, including existing train-hop jobs
		* Version number of what's in main and display it
			* Since right now we bump the version number manually, we should also check deployments to see if the major and minor version numbers match with a deployment, which indicates that a minor version bump is necessary.
			* Nightly: 144.0.0
			* Beta and Release: 144.0.20250820.0800
			* Then bump Nightly to 144.1.0
	* I want this to be a web-based tool that I can deploy on, say, GitHub pages. I want it to have _no server component_, I want it to be a normal webpage that uses JS to query Taskcluster and Firefox Nightly repository to produce its report. And then maybe cache the results locally (since once you've checked a particular revision, the results are not going to change).
	* User story: Amy wants to know if the current codebase on the top of Firefox's main repository is ready for doing a train-hop. She loads the web-based tool, which automatically queries the most recent merge commit to main to assess its readyness. Amy gets an easy to read report which allows her to know if there's any work to do to make New Tab _more_ ready to do a train-hop (for example, updating strings, regenerating runtime metrics, fixing train-hop compatibility problems, etc). She realizes that there is some work to do before New Tab can be train-hopped, so she goes and files some bugs to make that happen.
	* TODO
		* Query GitHub for the most recent revision SHA.
			* http "https://api.github.com/repos/mozilla-firefox/firefox/commits?sha=main&per_page=1&page=1"
		* Check to see if the Mercurial mapping is in the local cache.
			* If not, ask [this tool](https://bugzilla.mozilla.org/show_bug.cgi?id=1963822#c3) for a mapping to the Mercurial SHA
		* Use the Mercurial SHA and ask Taskcluster JS library for train-hop job status
			* Hit https://treeherder.mozilla.org/api/project/mozilla-central/push/?full=true&count=10&revision=[Mercurial SHA] to get back job description
			* Extract push id from description (it's the id value), and then request all jobs
			* Query https://treeherder.mozilla.org/api/jobs/?push_id=[push id]&job_group_symbol=nt-trainhop
			* That should give us the pass/fail on the trainhop jobs. Check for repeat platforms to detect intermittents.
		* Get newtab.ftl last changed date from GitHub
		* Get webext-glue/locales/en-US/newtab.ftl last changed date from GitHub
		* Get locales-report.json from GitHub
		* Use jq-web library (https://github.com/fiatjaf/jq-web) to query Experimenter for active deploys, rollouts and experiments.

**[Rate this episode](https://forms.gle/PAKbxoJrc85e5Zjq8)**

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