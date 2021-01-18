**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [Adso](https://github.com/mikeconley/joy-of-coding-episode-guide/tree/master/utils/adso)! Want to help me out? Please help correct transcriptions of episodes at [amara.org](http://amara.org)
    - [Here is a spreadsheet](https://docs.google.com/spreadsheets/d/1LiDWBkZ762LZQDYyFPmiXEGCJLT7cnLiAh3inehjdWc/edit?usp=sharing) with current auto-transcription state

**Today**

- Self-check: is everything working?
- [Bug 1434376 - Make BrowserUtils.promiseReflowed and BrowserUtils.promiseLayoutFlushed more reliable](https://bugzilla.mozilla.org/show_bug.cgi?id=1434376) - [Notes](https://www.evernote.com/l/AbJHAjbrrXJAoK83dubONe7hlXKsaXrT-A4)
    - Update: **This landed! \o/**
- [Bug 1432509 - Short tab-switch spinners displayed when switching to a tab that is still warming but not yet rendered.](https://bugzilla.mozilla.org/show_bug.cgi?id=1432509)
    - Update: **Figured out the issue! This is fixed! \o/**
    - Going to turn on tab warming early in the 61 cycle. You can try it now by flipping browser.tabs.remote.warmup.enabled to true
    - https://mikeconley.ca/blog/2018/01/11/making-tab-switching-faster-in-firefox-with-tab-warming/
- [Bug 1358719 - 1.26ms uninterruptible reflow at PT__updateChevronTimerCallback@chrome://browser/content/places/browserPlacesViews.js:1205:22](https://bugzilla.mozilla.org/show_bug.cgi?id=1358719) - [Notes](https://www.evernote.com/l/AbKSVSA6xJNAubfPmTiLGAEV7GX6FjGo3rA)
    - https://developer.mozilla.org/en-US/Firefox/Performance_best_practices_for_Firefox_fe_engineers
- For **kelvinstro**: https://www.joshmatthews.net/bugsahoy/?
    - https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Build_Instructions/Simple_Firefox_build
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley #livehacking.**

**Rate this episode: https://goo.gl/forms/RUm4F3UfFxnnDhRD3**

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