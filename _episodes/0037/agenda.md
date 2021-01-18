**Reminder - no plan survives breakfast.**

- **Update: [Bug 1177310](https://bugzilla.mozilla.org/show_bug.cgi?id=1177310)** - [e10s] Stop using CPOWs on application shutdown - [Notes](https://www.evernote.com/l/AbJXQWjJUQlD2atc5e2ob8QQ1PiB0ogbOl0)
    - Blocked on review
- **Update: [Bug 1227444](https://bugzilla.mozilla.org/show_bug.cgi?id=1227444)** - "Restore Previous Session" opens duplicate window - [Notes](https://www.evernote.com/l/AbK2ivLgvAxGQaUp96tg5lwYDfnDjttEhF4)
    - Fixed!
- [**Bug 1225921**](https://bugzilla.mozilla.org/show_bug.cgi?id=1225921) - Async tab and window flushing may make it possible to accidentally save tabs we want to forget - [Notes](https://www.evernote.com/l/AbKZwm2xv5NJq6mXo3sVvrS-XyVTOadjuE4)
- [**Bug 1195295**](https://bugzilla.mozilla.org/show_bug.cgi?id=1195295) - content-sessionStore.js sends a sync message to the parent in SyncHandler.init - [Notes](https://www.evernote.com/l/AbIDZA7wgGFIMaKU4DP_WvBL3oY-IAXJDUU)
- [**Bug 1226333**](https://bugzilla.mozilla.org/show_bug.cgi?id=1226333) - Add tests for async window flushing - [Notes](https://www.evernote.com/l/AbJFmQEL6BRNp7qyfVmQSx_P_HqItlgLEBw)
- [**Bug 1221846**](https://bugzilla.mozilla.org/show_bug.cgi?id=1221846) - Get Task Tracer working on desktop - [Notes](https://www.evernote.com/l/AbJ7J4czEutGQpQPxQUMqMedXvmz_rZXVxI)
- Subscribe to The Joy of Coding in iTunes or Kodi: [(L)](https://air.mozilla.org/feed/itunes/livehacking)https://air.mozilla.org/feed/itunes/livehacking
- [The Joy of Illustrating - Episode 1](https://www.youtube.com/watch?v=5g82nBPNVbc)
- No livestream next week, but hopefully an episode!
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**Chat**

- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- [Here's a link to a web-based IRC client you can use.](http://client00.chat.mibbit.com/?server=irc.mozilla.org&channel=#livehacking)

**Links**

- Livehacking on Air Mozilla: https://air.mozilla.org/channels/livehacking/
- I've been mirroring the episodes to YouTube: https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5
- [Lost in Data](https://air.mozilla.org/lost-in-data-episode-1/) - sheriffing performance regressions in pushes for Firefox
- [The Hour of Design](https://www.youtube.com/watch?v=8_Ld4hOU1QU) - watch one of our designers demystify the design process!
- Watch @mrrrgn code to techno: https://www.youtube.com/channel/UC9ggHzjP5TepAxkrQyQCyJg
- M8 bugs: https://bugzilla.mozilla.org/buglist.cgi?quicksearch=cf_tracking_e10s%3Am8%2B&list_id=12396117

**Glossary**

- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- [nsISHEntry](https://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHEntry.idl?from=nsISHEntry.idl#1) - a "session history entry". This is what powers the back and forward buttons and history for each browser tab. [Documentation.](https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsISHEntry)
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc"
- Deserialize - "turn a serialized object back into the complex object"
- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)

**Feedback**

- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on irc.mozilla.org
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)