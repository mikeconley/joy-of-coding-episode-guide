**Reminder - no plan survives breakfast.**

- Back from holiday! Not sure if you saw last week's episode, but it's [here](https://air.mozilla.org/the-joy-of-coding-mconley-livehacks-on-firefox-episode-16-2/).
- [Sound effects!](https://github.com/mikeconley/wacky-morning-dj) Hopefully not annoying, but let me know.
- OS X printing!
    - [Bug 1091112 - Print dialog doesn't get focus automatically, if e10s is enabled](https://bugzilla.mozilla.org/show_bug.cgi?id=1091112) - [Notes](https://www.evernote.com/l/AbI7nTQXK7BC46pLTwYTI2MFzgXVLTPkpPQ)
    - Fixed and landed! \o/
- [**Bug 1116188** - [e10s] Stop using sync messages for Gecko profiler](https://bugzilla.mozilla.org/show_bug.cgi?id=1116188https://bugzilla.mozilla.org/show_bug.cgi?id=1116188) - [Notes](https://www.evernote.com/l/AbLGLra4sjRNx4SsKStgW41ZRsZ1TeEp_Xo)
- [**Bug 1170488** - Click-to-Play for Adobe Flash not working when loading video not directly](https://bugzilla.mozilla.org/show_bug.cgi?id=1170488https://bugzilla.mozilla.org/show_bug.cgi?id=1170488)
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**Chat**

- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- [Here's a link to a web-based IRC client you can use.](http://client00.chat.mibbit.com/?server=irc.mozilla.org&channel=#livehacking)

**Links**

- I've been mirroring the episodes to YouTube: https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5
- [Lost in Data](https://air.mozilla.org/lost-in-data-episode-1/) - sheriffing performance regressions in pushes for Firefox
- [The Hour of Design](https://www.youtube.com/watch?v=VgzydofdJbw) - watch one of our designers demystify the design process!

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