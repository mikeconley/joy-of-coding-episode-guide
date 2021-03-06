**Reminder - no plan survives breakfast.**

- Self-check: is everything working?
- [Episode guide](https://github.com/mikeconley/joy-of-coding-episode-guide)
    - Feel free to send pull requests!
- [Bug 1356271 - add a test to measure how many layout flushes it takes for a simple location bar search](https://bugzilla.mozilla.org/show_bug.cgi?id=1356271) - [Notes](https://www.evernote.com/l/AbLNjyGtSjtNapUXbs0AfSGQGbp017bMKfY)
    - Landed! And stuck!
- Things related to reflow tests!
    - [Bug 1349555 - Make tabs rectangular (remove tab curve)](https://bugzilla.mozilla.org/show_bug.cgi?id=1349555)
        - Investigated and figured out why the tests were failing (some reflow stack signatures just changed)
    - [Bug 1363485 - Move the Back, Forward, Reload and Stop buttons outside of the location bar container to the start of the toolbar along with the Home button](https://bugzilla.mozilla.org/show_bug.cgi?id=1363485)
        - Tested UK92’s patch to ensure that URL bar reflows got fixed
- [Bug 1355426 - When closing tabs, select the next tab before working on closing the tab](https://bugzilla.mozilla.org/show_bug.cgi?id=1355426) - [Notes](https://www.evernote.com/l/AbJNfWX4y3xPRp3SltRyh9XSn8730sfL57c)
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley #livehacking.**

**Rate this episode:** https://goo.gl/forms/IIiIHFdu72mDk1xM2

**Chat**

- [IRC](https://wiki.mozilla.org/IRC)
- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- I’ve also got my IRC client signed into the Twitch chat
- [This is a link to a web client that you can use to chat with me from your browser](https://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org)

**Links**

- [Facebook Page for The Joy of Coding](https://www.facebook.com/TheJoyOfCoding1/)
- The Joy of Diagnosis!: https://www.youtube.com/watch?v=UL44ErfqJXs
- Livehacking on Air Mozilla: https://air.mozilla.org/channels/livehacking/
- [The Joy of Automation with Armen](https://www.youtube.com/channel/UCBgCmdvPaoYyha7JI33rfDQ)
- I've been mirroring the episodes to YouTube: https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5
- [The Joy of Illustrating - Episode 1](https://www.youtube.com/watch?v=5g82nBPNVbc) - Watch @mart3ll blow your mind with designs from the Mozilla Creative team!
- [Lost in Data](https://air.mozilla.org/lost-in-data-episode-1/) - sheriffing performance regressions in pushes for Firefox
- [The Hour of Design](https://www.youtube.com/watch?v=8_Ld4hOU1QU) - watch one of our designers demystify the design process!
- [Code Therapy with Danny O’Brien](https://www.youtube.com/channel/UCDShi-SQdFVRnQrMla9G_kQ)
- Watch a developer put together a Windows game from scratch (no third-part engines) - really great explanations: https://handmadehero.org/
- [/r/WatchPeopleCode](https://www.reddit.com/r/WatchPeopleCode) for more livehacking!
- Watch @mrrrgn code to techno: https://www.youtube.com/channel/UC9ggHzjP5TepAxkrQyQCyJg
- M8 bugs: https://bugzilla.mozilla.org/buglist.cgi?quicksearch=cf_tracking_e10s%3Am8%2B&list_id=12396117

**Glossary**

- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)
- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc"
- Deserialize - "turn a serialized object back into the complex object”
- BHR - “Background Hang Reporter”, a thing that records information about when Firefox performs poorly and sends it over Telemetry

**Feedback**

- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on irc.mozilla.org
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)