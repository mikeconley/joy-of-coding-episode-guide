**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [Adso](https://github.com/mikeconley/joy-of-coding-episode-guide/tree/master/utils/adso)! Want to help me out? **Please help correct transcriptions** of episodes at [amara.org](http://amara.org)
    - [Here is a spreadsheet](https://docs.google.com/spreadsheets/d/1LiDWBkZ762LZQDYyFPmiXEGCJLT7cnLiAh3inehjdWc/edit?usp=sharing) with current auto-transcription state

**Today**

- Self-check: is everything working?
- Plug: [The Joy of Profiling!](https://air.mozilla.org/search/?ss=41)
    - https://docs.google.com/a/mozilla.com/forms/d/e/1FAIpQLSePiq1ifvrY6EzDowEdqKdb-tGGm-AvgG86ivU9ipv7FsggKQ/viewform
    - https://developer.mozilla.org/en-US/docs/Mozilla/Performance/Reporting_a_Performance_Problem
- **Tab warming Telemetry update**
    - [Spinner stats](https://mikeconley.github.io/bug1310250/)
    - [Telemetry probe to watch](https://telemetry.mozilla.org/new-pipeline/evo.html#!aggregates=median&cumulative=0&end_date=2018-03-11&keys=!__none__!__none__&max_channel_version=nightly%252F60&measure=FX_TAB_SWITCH_TOTAL_E10S_MS&min_channel_version=nightly%252F58&processType=*&product=Firefox&sanitize=1&sort_keys=submissions&start_date=2018-02-23&trim=0&use_submission_date=0)
- Update: [Bug 1445213 - 8.88 - 11.61% tabpaint (linux64, osx-10-10) regression on push 664c633802d4cd0e2c32a271a2d29107b5b43f38](https://bugzilla.mozilla.org/show_bug.cgi?id=1445213) - [Notes](https://www.evernote.com/l/AbKIJOgyOs9Ar46976BzTIVpOQKb0QWs2Gg)
    - We weren’t firing MozAfterPaint until the _next_ paint. A later patch to the Tab warming infrastructure fixed this.
- [Bug 1447326 - Tab warming Telemetry on warming state of tabs seems to be pretty wrong](https://bugzilla.mozilla.org/show_bug.cgi?id=1447326) - [Notes](https://www.evernote.com/l/AbLVTBpj80BHEZMqpn3bLMPp4Xz5o_CrT9Q)
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley #livehacking.**

**Rate this episode: https://goo.gl/forms/F9KNI52Ii2wpaiLI3**

**Chat**

- [IRC](https://wiki.mozilla.org/IRC)
- We're in [irc.mozilla.org](http://irc.mozilla.org) in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- I’ve also got my IRC client signed into the Twitch chat
- [This is a link to a web client that you can use to chat with me from your browser](https://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org)

**Links**

- [The Joy of Coding: Community-Run Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)
    - Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
    - [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [Facebook Page for The Joy of Coding](https://www.facebook.com/TheJoyOfCoding1/)
- [Solving Bugs with Sean Prashad](https://www.youtube.com/channel/UCRxijHyajcDWdjRK_9jmLYw)
- The Joy of Diagnosis!: https://www.youtube.com/watch?v=UL44ErfqJXs
- Livehacking on Air Mozilla: https://air.mozilla.org/channels/livehacking/
- [The Joy of Automation with Armen](https://www.youtube.com/channel/UCBgCmdvPaoYyha7JI33rfDQ)
- [I've been mirroring the episodes to YouTube](https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5)
- [The Joy of Illustrating - Episode 1](https://www.youtube.com/watch?v=5g82nBPNVbc) - Watch @mart3ll blow your mind with designs from the Mozilla Creative team!
- [Lost in Data](https://air.mozilla.org/lost-in-data-episode-1/) - sheriffing performance regressions in pushes for Firefox
- [The Hour of Design](https://www.youtube.com/watch?v=8_Ld4hOU1QU) - watch one of our designers demystify the design process!
- [Code Therapy with Danny O’Brien](https://www.youtube.com/channel/UCDShi-SQdFVRnQrMla9G_kQ)
- Watch a developer put together a Windows game from scratch (no third-part engines) - really great explanations: https://handmadehero.org/
- [/r/WatchPeopleCode](https://www.reddit.com/r/WatchPeopleCode) for more livehacking!
- [Watch @mrrrgn code to techno](https://www.youtube.com/channel/UC9ggHzjP5TepAxkrQyQCyJg)

**Glossary**

- BHR - “Background Hang Reporter”, a thing that records information about when Firefox performs poorly and sends it over Telemetry
- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)
- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- Deserialize - "turn a serialized object back into the complex object”
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc
- Regression - something that made behaviour worse rather than better. Regress means to “go backward”, more or less.

**Feedback**

- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on [irc.mozilla.org](http://irc.mozilla.org)
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)