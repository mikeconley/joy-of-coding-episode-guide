**Reminder - no plan survives breakfast.**

- Hopefully I’m continuing the trend of recording these things correctly!
    - Self-note: Is my Mic on?
- **Update:**
    - **[Bug 1254865](https://bugzilla.mozilla.org/show_bug.cgi?id=1254865)** - remote-browser.xml's browser-child.js should not send a sync message on load - [Notes](https://www.evernote.com/l/AbIvaW7WBtxOG6FLb865cwyLjE4S2uxFyo8)
    - Great success!
- **[Bug 1251032](https://bugzilla.mozilla.org/show_bug.cgi?id=1251032)** - Have ContentParent send RenderFrameInfo down when responding to the CreateWindow sync message - [Notes](https://www.evernote.com/l/AbJ6DxvNwlpDYZONrjBuddJP072OGQTVrW4)
- **Reviews:**
    - [Bug 1260360](https://bugzilla.mozilla.org/show_bug.cgi?id=1260360) - Session Restore needs to honor "Clear history when Firefox closes -> Cookies" in a clean shut-down
    - [Bug 1164931](https://bugzilla.mozilla.org/show_bug.cgi?id=1164931) - The e10s slow script notification bar keeps spontaneously disappearing and reappearing in cycles.
    - <s>[Bug 1164286](https://bugzilla.mozilla.org/show_bug.cgi?id=1164286) - The page load stop and refresh buttons do nothing when the E10S slow script dialog is being shown.</s>
    - <s>[Bug 1186029](https://bugzilla.mozilla.org/show_bug.cgi?id=1186029) - Need e10s tests for accessibility</s>
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**RATE THIS EPISODE: **http://goo.gl/forms/8rSgqqkVho

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