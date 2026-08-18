---
date: 2025-08-27
number: 415
---

# Episode 415: Aug 27th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-08-27)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0415.html)

## Topics
* ![Alt text](https://mikeconley.ca/joc/agendas/images/b08ff93f94c44aed9186a23c6cf575f9 "keanu code 415")
  - https://www.keanu.codes/?code=415
  - 415 - Unsupported Media Type
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/415
* Sections in the US!
* The widgets on Beta and Nightly
* Fairly gnarly toolbar bug - 142.0.1 went out today.
* Let's keep going with the tool we wrote! I made some changes. I've copied over the TODOs from last week.
* TODO:
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

* [Rate this episode](https://forms.gle/JPF5hBvf4xJbMUSz5)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

