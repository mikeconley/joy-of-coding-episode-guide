**Reminder - no plan survives breakfast.**

- **Hopefully I'm recording this!**
- I've been bad at keeping up my blog lately. I swear I'll get better soon-ish, just lots of other things on my plate right now.
- Review:
    - [**Bug 1134585**](https://bugzilla.mozilla.org/show_bug.cgi?id=1134585) - [e10s] "View Selection/MathML Source" in remote browser causes unsafe CPOW usage warning
- Coding:
    - [**Bug 1145916**](https://bugzilla.mozilla.org/show_bug.cgi?id=1145916) - printing multiple copies doesn't work with e10s - [Notes](https://www.evernote.com/l/AbJC1TPsiKBMJ7VRvR2WB5R3f8Olp4zWxrk)
    - [**Bug 1141337**](https://bugzilla.mozilla.org/show_bug.cgi?id=1141337) - [e10s] "Save Page|Frame As..." in remote browser causes unsafe CPOW usage warnings - [Notes](https://www.evernote.com/l/AbJC1TPsiKBMJ7VRvR2WB5R3f8Olp4zWxrk)
    - [**Bug 1175645**](https://bugzilla.mozilla.org/show_bug.cgi?id=1175645) - Printing stops working on a particular tab (probably e10s) - [Notes](https://www.evernote.com/l/AbIDTkDNMj5NSrYLa5SXJqmmIOJXCWfb2WM)
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**Chat**

- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- [Here's a link to a web-based IRC client you can use.](http://client00.chat.mibbit.com/?server=irc.mozilla.org&channel=#livehacking)

**Links**

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