**Reminder - no plan survives breakfast.**

![http://i.imgur.com/oYG9BSY.jpg](images/680d11ad9801e7f0a2fcee10cd62025c)

- Back from hiatus!
- Dedicated to killwill and Simon Gwerder who helped me clear up some logic last episode!
    - https://gist.github.com/anonymous/d4f864cd2e0662deacae
- **Reviewing!**
    - [Bug 653065](https://bugzilla.mozilla.org/show_bug.cgi?id=653065) - Make the lightweight theme web installer ready for e10s
    - [Bug 1178823](https://bugzilla.mozilla.org/show_bug.cgi?id=1178823) - Black screen on a machine that the sanity test failed to detect
- **Coding**
    - Bug [1181601](https://bugzilla.mozilla.org/show_bug.cgi?id=1181601) - Unable to receive messages from preloaded, remote newtab page - [Notes](https://www.evernote.com/l/AbK-tE-3WolLtrxbFOl71gcvpNTwN9Xxb24)
    - Bug [1146454](https://bugzilla.mozilla.org/show_bug.cgi?id=1146454) - Remove CPOW usage in printing - [Notes](https://www.evernote.com/l/AbIb1RPdh6lGGKhBjur3iWcsuM6NiKbT_1k)
- @mrrrgn hacks together a WebSocket server implementation in Go. To techno! https://www.youtube.com/watch?v=R2c-NpsWbiU
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**Chat**

- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- [Here's a link to a web-based IRC client you can use.](http://client00.chat.mibbit.com/?server=irc.mozilla.org&channel=#livehacking)

**Links**

- I've been mirroring the episodes to YouTube: https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5
- [Lost in Data](https://air.mozilla.org/lost-in-data-episode-1/) - sheriffing performance regressions in pushes for Firefox
- [The Hour of Design](https://www.youtube.com/watch?v=8_Ld4hOU1QU) - watch one of our designers demystify the design process!
- Watch @mrrrgn code to techno: https://www.youtube.com/channel/UC9ggHzjP5TepAxkrQyQCyJg
- That gist that killwill posted: https://gist.github.com/anonymous/d4f864cd2e0662deacae

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