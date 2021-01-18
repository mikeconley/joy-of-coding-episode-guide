**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [Adso](https://github.com/mikeconley/joy-of-coding-episode-guide/tree/master/utils/adso)! Want to help me out? **Please help correct transcriptions** of episodes at [amara.org](http://amara.org)
    - [Here is a spreadsheet](https://docs.google.com/spreadsheets/d/1LiDWBkZ762LZQDYyFPmiXEGCJLT7cnLiAh3inehjdWc/edit?usp=sharing) with current auto-transcription state

**Today**

- Self-check: is everything working?
- Attempt to reproduce and (if reproducible) file the about:printpreview bug that I noticed during the stream

    1. Create a session with a single window and tab pointed at http://i.imgur.com/lmzNpx7.png

    2. Shut down the browser

    3. Start the browser and restore session automatically, so we have a single tab pointed at http://i.imgur.com/lmzNpx7.png

    4. ???

- [Bug 1478112 - Sort out how to best call `this._getSwitcher().requestTab` and `this.updateCurrentBrowser` during tabpanels selectedIndex change](https://bugzilla.mozilla.org/show_bug.cgi?id=1478112) - [Notes](https://www.evernote.com/l/AbIx170GaO1AC7jA1tqCEhqVpo_7PLhXW0A)
    - Quick plug - JS time travel debugging AKA Project Delorean AKA WebReplay: https://twitter.com/digitarald/status/1026887071955181569
        - devtools.recordreplay.enabled
        - Windows support bug: https://bugzilla.mozilla.org/show_bug.cgi?id=1310271
    - Weak Memory ordering bug blog post: https://robert.ocallahan.org/2018/08/for-first-time-in-my-life-i-tracked.html

    -

- [Bug 1481466 - Themes are incorrectly displayed in preview mode](https://bugzilla.mozilla.org/show_bug.cgi?id=1481466) - [Notes](https://www.evernote.com/l/AbIQURQhNG9AJJbyt6TToWfhHK8_YttMLyA)
- Episode 150
    - Got ideas? Submit them in the Episode Rating form!
    - AMA
    - Work on some kind of user voted bug?
    - Build a WebExtension to do something from scratch?
    - Explore some other Mozilla project?
    - Explore a non-Mozilla project and try to understand it?
    - Explain some part of the codebase?
    - Normal episode? (But wear a funny hat)?
- **Not going to be streaming next week!**
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley #livehacking.**

**Rate this episode: https://goo.gl/forms/royiLYnHOetbyYC32**

**Chat**

- [IRC](https://wiki.mozilla.org/IRC)
- We're in [irc.mozilla.org](http://irc.mozilla.org) in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- I’ve also got my IRC client signed into the Twitch chat
- [This is a link to a web client that you can use to chat with me from your browser](https://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org)

**Links**

- [The Joy of Coding: Community-Run Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)
    - Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
    - [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [Check out my colleague Josh Marinacci](https://twitter.com/joshmarinacci) hacking on [Firefox Reality, our nascent VR browser](https://www.twitch.tv/joshmarinacci)!
- [Les Orchard hacks on Firefox Color](https://www.twitch.tv/lmorchard/videos/all)
- [Solving Bugs with Sean Prashad](https://www.youtube.com/channel/UCRxijHyajcDWdjRK_9jmLYw)
- The Joy of Diagnosis!: https://www.youtube.com/watch?v=UL44ErfqJXs
- [The Joy of Automation with Armen](https://www.youtube.com/channel/UCBgCmdvPaoYyha7JI33rfDQ)
- [I've been mirroring the episodes to YouTube](https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5)
- [The Joy of Illustrating - Episode 1](https://www.youtube.com/watch?v=5g82nBPNVbc) - Watch @mart3ll blow your mind with designs from the Mozilla Creative team!
- [Lost in Data](https://air.mozilla.org/lost-in-data-episode-1/) - sheriffing performance regressions in pushes for Firefox
- [The Hour of Design](https://www.youtube.com/watch?v=8_Ld4hOU1QU) - watch one of our designers demystify the design process!
- [Code Therapy with Danny O’Brien](https://www.youtube.com/channel/UCDShi-SQdFVRnQrMla9G_kQ)
- Watch a developer put together a Windows game from scratch (no third-part engines) - really great explanations: https://handmadehero.org/
- [/r/WatchPeopleCode](https://www.reddit.com/r/WatchPeopleCode) for more livehacking!
- [Watch @mrrrgn code to techno](https://www.youtube.com/channel/UC9ggHzjP5TepAxkrQyQCyJg)

**Glossary**

- BHR - “Background Hang Reporter”, a thing that records information about when Firefox performs poorly and sends it over Telemetry
- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)
- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- Deserialize - "turn a serialized object back into the complex object”
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc
- Regression - something that made behaviour worse rather than better. Regress means to “go backward”, more or less.

**Feedback**

- [@mconley@mastodon.social on Mastodon](https://mastodon.social/@mconley)
- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on [irc.mozilla.org](http://irc.mozilla.org)
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)