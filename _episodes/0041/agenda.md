**Reminder - no plan survives breakfast.**

- <s>[**Bug 1238180**](https://bugzilla.mozilla.org/show_bug.cgi?id=1238180) - Unsafe CPOW usage in nsContextMenu.js, browser.js for pageInfo opened from context menu - [Notes](https://www.evernote.com/l/AbKW29OHINNCrIUxq0vSjvH7mxVK4oIMAEs) </s>
- <s>Writing an email to dev-platform, firefox-dev</s>
    - <s>In-browser unsafe CPOWs being outlawed except in add-on</s>
- <s>**Review**: [**Bug 1240750**](https://bugzilla.mozilla.org/show_bug.cgi?id=1240750) - [e10s] Fix and re-enable /layout/base/tests/browser_bug617076.js</s>
- [**Bug 1239533**](https://bugzilla.mozilla.org/show_bug.cgi?id=1239533) - [e10s] It's possible to accidentally get 2 visually selected tabs when opening tabs using window.open() - [Notes](https://www.evernote.com/l/AbKhY9jmWQhN7IAmVodmNXkV6iTic7G06no)
- **Review: [Bug 1237025](https://bugzilla.mozilla.org/show_bug.cgi?id=1237025)** - View Image Info context menu option uses unsafe cpows
- [**Bug 1182595**](https://bugzilla.mozilla.org/show_bug.cgi?id=1182595) - Make profile dumping work with e10s - [Notes](https://www.evernote.com/l/AbL6Q3uE4mpOWYg8NoXbSRee4BnQXkD-8M4)
- Continuing last week's - **Better Know a Gecko!**
    - Today’s piece of code is the async tab switcher for e10s: https://dxr.mozilla.org/mozilla-central/rev/e790bba372f14241addda469a4bdb7ab00786ab3/browser/base/content/tabbrowser.xml#3065 - [Notes](https://www.evernote.com/l/AbKPWoHTG_FDaLCwRgY4LFKbGJG51S5Zymk)
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**RATE THIS EPISODE:**  http://goo.gl/forms/Hwn4Nf6igf

**Chat**

- We're in irc.mozilla.org in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- [Here's a link to a web-based IRC client you can use.](http://client00.chat.mibbit.com/?server=irc.mozilla.org&channel=#livehacking)

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