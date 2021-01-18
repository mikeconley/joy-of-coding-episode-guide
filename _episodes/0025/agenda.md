**Reminder - no plan survives breakfast.**

- Upcoming break! Next episode will be the last for a few weeks. Gone for August 26th, September 2nd, and September 9th. **Back on the 16th!**
- Coding:
    - [**Bug 1193838**](https://bugzilla.mozilla.org/show_bug.cgi?id=1193838) - Make it possible to gather profiles from processes that have exited. [Notes](https://www.evernote.com/l/AbIApW1ezr1EN6XRU4jlbLho0cizUJv0d0w)
    - [**Bug 1109714**](https://bugzilla.mozilla.org/show_bug.cgi?id=1109714) - Handle anonymous XUL feed subscriber UI in e10s. [Notes](https://www.evernote.com/l/AbLur1fChGtE2rpKDlWnjTQpZ5sVg7t1xaI)
- Reviewed:
    - [**Bug 1175940**](https://bugzilla.mozilla.org/show_bug.cgi?id=1175940) - TabChild::RecvUIResolutionChanged can be really slow when switching tabs
- Ricardo is up next with Episode 7 of The Hour of Design! https://www.youtube.com/watch?v=k5kLKN0U-QU
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