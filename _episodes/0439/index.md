---
layout: default
date: 2026-05-06
number: 439
---

# Episode 439: May 6th, 2026

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2026-05-06)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0439.html)

## Topics
* Q:
  "missed the submission window, so here is my question again:
  There was a regression on 10th April 2026 breaking the functionality of middle clicking the "Go to the address in Location Bar" arrow button to open the address in a new tab.

  however the bug mozregession provides is not public, and it's title does not make sense related to the regression:

  2026-04-14T18:40:43.437000: INFO : Narrowed integration regression window from [aee77767, 602084a8] (4 builds) to [e41f1f9a, 602084a8] (2 builds) (~1 steps left)
  2026-04-14T18:40:43.473000: DEBUG : Starting merge handling...
  2026-04-14T18:40:43.476000: DEBUG : Using url: https://hg.mozilla.org/integration/autoland/json-pushes?changeset=602084a80545c3aa2879ec54585f298966b00839&full=1
  2026-04-14T18:40:43.480000: DEBUG : redo: attempt 1/3
  2026-04-14T18:40:43.482000: DEBUG : redo: retry: calling _default_get with args: ('https://hg.mozilla.org/integration/autoland/json-pushes?changeset=602084a80545c3aa2879ec54585f298966b00839&full=1',), kwargs: {}, attempt #1
  2026-04-14T18:40:43.488000: DEBUG : urllib3.connectionpool: Resetting dropped connection: hg.mozilla.org
  2026-04-14T18:40:44.270000: DEBUG : urllib3.connectionpool: https://hg.mozilla.org:443 "GET /integration/autoland/json-pushes?changeset=602084a80545c3aa2879ec54585f298966b00839&full=1 HTTP/1.1" 302 0
  2026-04-14T18:40:45.446000: DEBUG : urllib3.connectionpool: https://hg-edge.mozilla.org:443 "GET /integration/autoland/json-pushes?changeset=602084a80545c3aa2879ec54585f298966b00839&full=1 HTTP/1.1" 200 None
  2026-04-14T18:40:45.482000: DEBUG : Found commit message:
  Revert "Bug 2029066 - Remove Sinking of Live instructions. r=iain" for causing spidermonkey build bustages at Sink.cpp

  This reverts commit dcb553336bdbc8a96073e287127b82eb5144d8aa.

  2026-04-14T18:40:45.488000: DEBUG : Did not find a branch, checking all integration branches
  2026-04-14T18:40:45.492000: INFO : The bisection is done.
  2026-04-14T18:40:45.496000: INFO : Stopped

  there is a similar "Bug 2033231 - Middle clicking alternate engines no longer perform a search on the current search bar text in a new tab" but the dates don't match and the issue isn't fixed in current Nightly.

  I assume this regression isn't an intended change but I can't tell without seeing the regressor bug.
  I used the functionality as a workaround for what has caused internal Mozilla debate: 724239, 776167, 1415136
  and there is still inconsistent behaviour between about:newtab, about:blank and about:privatebrowsing"
  - This bug: https://bugzilla.mozilla.org/show_bug.cgi?id=2037361, which is assigned (as of this writing, an hour ago!)
* [Query](https://bugzilla.mozilla.org/buglist.cgi?quicksearch=keyword%3Aregressionwindow-wanted&list_id=17963114) for finding regressionwindow-wanted bugs
  - ./mach mozregression to find the regressor
* Let's solve a mystery!
  - Where are those spans going? Where is the progress going?!
    - Our self-closing tags were confusing things. Got rid of them!
  - Build fluent migration for the strings we moved
    - Still to do
  - Fix button styling to match existing button behaviour
    - Done
* TODO:
  - Talk to emilio about center cropping support in CSS for privileged markup / layout
  - Factor out download item UI into a reusable Lit element

* [Rate this episode](https://forms.gle/G82dS9igNarahUgi9)

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

