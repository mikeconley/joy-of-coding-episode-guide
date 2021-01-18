**Reminder - no plan survives breakfast.**

- Hopefully I’m continuing the trend of recording these things correctly!
    - Self-note: Is my Mic on?
- I’m boosting my font size. Let me know if there are other places I should bump sizes.
- **Need to test to see if you can see what I’m typing at the bottom of my screen**
- **Update: [Bug 1251032](https://bugzilla.mozilla.org/show_bug.cgi?id=1251032)** - Have ContentParent send RenderFrameInfo down when responding to the CreateWindow sync message - [Notes](https://www.evernote.com/l/AbJ6DxvNwlpDYZONrjBuddJP072OGQTVrW4)
    - Turns out I had to move some stuff around!
    - This landed this morning - already seeing some payoff:
        - Linux 64: [https://treeherder.mozilla.org/perf.html#/graphs?timerange=7776000&series=%5Bmozilla-inbound,c1b1c708a4991e8bfbcfed312c14b840ba1ac87a,1%5D&series=%5Bmozilla-inbound,29c253bef49b44be88ba4cf244e66d20ee02934c,1%5D&zoom=1458567595165.6978,1459956430000,205.0724416539289,411.5941807843637]()
        - OS X 10.10: [https://treeherder.mozilla.org/perf.html#/graphs?series=%5Bmozilla-inbound,83892f58324732a38c5aefbe7fa251143d4cf7bb,1%5D&series=%5Bmozilla-inbound,22aef36b0aaa84b17d6c6781de4187e18c59a7f2,1%5D]()
        - Windows 8 64: [https://treeherder.mozilla.org/perf.html#/graphs?series=%5Bmozilla-inbound,6b31d18100b143c31595be90e6f8bb46b64bb31b,1%5D&series=%5Bmozilla-inbound,15399aeb472c4e091d5b5f74acc7a5ad3344b2c5,1%5D]()
- **[Bug 1258465](https://bugzilla.mozilla.org/show_bug.cgi?id=1258465)** - Only nsIWebBrowserFocus->activate a TabChild once it has composited - [Notes](https://bugzilla.mozilla.org/show_bug.cgi?id=1258465)
- **[Bug 1261842](https://bugzilla.mozilla.org/show_bug.cgi?id=1261842)** - Make initial browser remote sooner if we're defaulting to using remote tabs - [Notes](https://www.evernote.com/l/AbJAn7bfId9NvYOpy1Oh2eXPQX481M7Y27k)
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley or Richard in #livehacking.**

**RATE THIS EPISODE: **http://goo.gl/forms/NHG3JlqeAh

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

- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)
- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc"
- Deserialize - "turn a serialized object back into the complex object"

**Feedback**

- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on irc.mozilla.org
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)