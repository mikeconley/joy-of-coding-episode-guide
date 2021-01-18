**Reminder - no plan survives breakfast.**

- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- I've been mirroring the episodes to YouTube: https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5
- View Source and Save As bugs both have r+ - waiting on waiting on [that cache key thing](https://bugzilla.mozilla.org/show_bug.cgi?id=1156493) to land.

-

    - [Bug 1025146 - Never load the source off of the network when viewing source](https://bugzilla.mozilla.org/show_bug.cgi?id=1025146%20) - [Notes](https://www.evernote.com/l/AbKJ3Z1m90ZLuZuThyXIsGaLuRi-dHUmETg)
    - [Bug 1128050 - [e10s] Save page as... doesn't always load from cache](https://bugzilla.mozilla.org/show_bug.cgi?id=1128050) - [Notes](https://www.evernote.com/l/AbLmzz8TYLVM-YOL4c2mwjwqwov9VYz87uM)
- Today, I'm hoping to focus on (yet another) printing bug - this time for OS X.

-

    - [Bug 1091112 - Print dialog doesn't get focus automatically, if e10s is enabled](https://bugzilla.mozilla.org/show_bug.cgi?id=1091112) - [Notes](https://www.evernote.com/l/AbI7nTQXK7BC46pLTwYTI2MFzgXVLTPkpPQ)
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**Glossary**

- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- [nsISHEntry](https://dxr.mozilla.org/mozilla-central/source/docshell/shistory/public/nsISHEntry.idl?from=nsISHEntry.idl#1) - a "session history entry". This is what powers the back and forward buttons and history for each browser tab. [Documentation.](https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsISHEntry)
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc"
- Deserialize - "turn a serialized object back into the complex object"
- e10s - short for Electrolysis, which is the multi-process Firefox project

**Feedback**

- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on irc.mozilla.org
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)