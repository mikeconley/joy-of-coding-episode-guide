---
layout: default
date: 2025-08-20
number: 414
---

# Episode 414: Aug 20th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-08-20)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0414.html)

## Topics
* ![Alt text](https://mikeconley.ca/joc/agendas/images/23f4022ac0c84e4eb7903704898bcdf7 "keanu code 414")
  - https://www.keanu.codes/?code=414
  - 414 - URI Too Long
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/414
* New Tab trainhop readyness tool
  - Overarching goal: a tool that can be used by an Eng, PM, TPM to assess the viability of the most recent revision (or a specific revision) of the newtab code in mozilla-central (or main) to train-hop to Beta and / or Release.
    - Train-hop compatibility state from CI
      - Displays train-hop compatibility meta bug stats, and reminds users when a compatibility shim can be removed.
    - Localization state (are the strings displayed by default localized in all of the supported locales? If not, which locales are localized and which are not)?
      - I want to know if the en-US newtab.ftl is different from the one included in the XPI, because this means that the localizations need to be updated before a train-hop can possibly proceed.
    - Glean / Metrics state to see if runtime metrics or pings need to be generated.
    - Existing experiments and rollouts on each channel, including existing train-hop jobs
    - Version number of what's in main and display it
      - Since right now we bump the version number manually, we should also check deployments to see if the major and minor version numbers match with a deployment, which indicates that a minor version bump is necessary.
      - Nightly: 144.0.0
      - Beta and Release: 144.0.20250820.0800
      - Then bump Nightly to 144.1.0
  - I want this to be a web-based tool that I can deploy on, say, GitHub pages. I want it to have no server component, I want it to be a normal webpage that uses JS to query Taskcluster and Firefox Nightly repository to produce its report. And then maybe cache the results locally (since once you've checked a particular revision, the results are not going to change).
  - User story: Amy wants to know if the current codebase on the top of Firefox's main repository is ready for doing a train-hop. She loads the web-based tool, which automatically queries the most recent merge commit to main to assess its readyness. Amy gets an easy to read report which allows her to know if there's any work to do to make New Tab more ready to do a train-hop (for example, updating strings, regenerating runtime metrics, fixing train-hop compatibility problems, etc). She realizes that there is some work to do before New Tab can be train-hopped, so she goes and files some bugs to make that happen.
  - TODO
    - Query GitHub for the most recent revision SHA.
      - http "https://api.github.com/repos/mozilla-firefox/firefox/commits?sha=main&perpage=1&page=1"
    - Check to see if the Mercurial mapping is in the local cache.
      - If not, ask [this tool](https://bugzilla.mozilla.org/show_bug.cgi?id=1963822#c3) for a mapping to the Mercurial SHA
    - Use the Mercurial SHA and ask Taskcluster JS library for train-hop job status
      - Hit https://treeherder.mozilla.org/api/project/mozilla-central/push/?full=true&count=10&revision=[Mercurial SHA] to get back job description
      - Extract push id from description (it's the id value), and then request all jobs
      - Query https://treeherder.mozilla.org/api/jobs/?pushid=[push id]&jobgroupsymbol=nt-trainhop
      - That should give us the pass/fail on the trainhop jobs. Check for repeat platforms to detect intermittents.
    - Get newtab.ftl last changed date from GitHub
    - Get webext-glue/locales/en-US/newtab.ftl last changed date from GitHub
    - Get locales-report.json from GitHub
    - Use jq-web library (https://github.com/fiatjaf/jq-web) to query Experimenter for active deploys, rollouts and experiments.

* [Rate this episode](https://forms.gle/PAKbxoJrc85e5Zjq8)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
* [npb hacks](https://www.twitch.tv/BackToTheCode) on the SpiderMonkey JS engine
* [Compiler Compiler](https://www.twitch.tv/codehag) live stream
* Try out Mozilla [VPN](https://vpn.mozilla.org/)
* How mconley uses [Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mike's Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
* [Codetribute](https://codetribute.mozilla.org/) - Help contribute to Firefox, good mentored bugs for You.
  - First, [Create](https://bugzilla.mozilla.org/createaccount.cgi) a Mozilla Bugzilla account.

