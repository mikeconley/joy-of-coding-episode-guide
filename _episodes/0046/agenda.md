**Reminder - no plan survives breakfast.**

- Hopefully I’m continuing the trend of recording these things correctly!
    - Self-note: Is my Mic on?
- **Updates**
    - [**Bug 1246291**](https://bugzilla.mozilla.org/show_bug.cgi?id=1246291) - [e10s] about:preferences#advanced - "Warn me when websites try to redirect or reload the page" doesn't allow redirects - [Notes](https://www.evernote.com/l/AbIQV2xXDY1CMpKPvFpjfOkbTVD97L-rliQ)
        - Fixed and landed! I went with the solution we originally settled on last episode.
    - [**Bug 1248599**](https://bugzilla.mozilla.org/show_bug.cgi?id=1248599) - [e10s] The user is not automatically signed into the Firefox account after resetting the password - [Notes](https://www.evernote.com/l/AbIRby4TJg1KWbE8GaydZRBWF9R2GcoKjww)
        - Never got into this last week, but this got fixed.
    - [**Bug 1182595**](https://bugzilla.mozilla.org/show_bug.cgi?id=1182595) - Make profile dumping work with e10s - [Notes](https://www.evernote.com/l/AbL6Q3uE4mpOWYg8NoXbSRee4BnQXkD-8M4)
        - I’ve got the initial patch up for review!
    - content-sessionStore.js test failure. [Notes for content-sessionStore.js](https://www.evernote.com/l/AbIDZA7wgGFIMaKU4DP_WvBL3oY-IAXJDUU)
        - Oh man, what a garbage fire. But it’s landed!
- One of the lovely people who rated last weeks episode reminded me about THE HOUR OF DESIGN by ricardo! Check it out!
    - [(L)](https://www.youtube.com/channel/UC9MJ2wGfJ_7mbLN6rXjWztA?app=desktop)https://www.youtube.com/channel/UC9MJ2wGfJ_7mbLN6rXjWztA?app=desktop
- [**Bug 1174770**](https://bugzilla.mozilla.org/show_bug.cgi?id=1174770) - tpaint regressions (3%-33%) in e10s mode compared to non-e10s mode - [Notes](https://www.evernote.com/l/AbJg4IIy14ZLfqiuN0gdG8L89gmUJTnmuEM)
    - Let’s look at some profiles: [https://treeherder.mozilla.org/#/jobs?repo=try&revision=7bacdebeffc6&selectedJob=17130143]()
- Reviews!
    - [(L)](https://bugzilla.mozilla.org/show_bug.cgi?id=1088710)https://bugzilla.mozilla.org/show_bug.cgi?id=1088710
    - https://bugzilla.mozilla.org/show_bug.cgi?id=1245891
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**RATE THIS EPISODE: **http://goo.gl/forms/MMT8eAnrO7

**Chat**

- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- [Here's a link to a web-based IRC client you can use.]()

**Links**

- Livehacking on Air Mozilla: https://air.mozilla.org/channels/livehacking/
- I've been mirroring the episodes to YouTube: [(L)](https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5)https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5
- [The Joy of Illustrating - Episode 1](https://www.youtube.com/watch?v=5g82nBPNVbc) - Watch @mart3ll blow your mind with designs from the Mozilla Creative team!
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