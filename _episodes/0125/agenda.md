**Reminder - no plan survives breakfast.**

**Happy New Year!**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- Self-check: is everything working?
    - Hopefully my audio is sync’d up! I think the new mic is causing slight lag.
- Beard video: https://air.mozilla.org/the-joy-of-profiling-episode-17/
- Update: [Bug 1397426 - Make tab browser warming API not set the docshell to be active](https://bugzilla.mozilla.org/show_bug.cgi?id=1397426) - [Notes](https://www.evernote.com/l/AbLOfT-bJURAxqXAs4fqUdsjcLctLBSSubI)
    - Landed! Just some follow-up stuff to land now to take care of a perma-spinner on new tabs / windows opened from content.
    - browser.tabs.remote.warmup.enabled
- [Bug 1423208 - Permanent tabswitch spinners when opening some links in new tabs with tab warming enabled](https://bugzilla.mozilla.org/show_bug.cgi?id=1423208) - [Notes](https://www.evernote.com/l/AbK9q__zcQlF3YZtvgwpijMQy7wLuyjydD8)
    - Addressed comments, and going to land this.
- [Bug 888784 - FormHistory.jsm migration and DB creation should be off the main thread](https://bugzilla.mozilla.org/show_bug.cgi?id=888784) - [Notes](https://www.evernote.com/l/AbImEKYlZg1D4op6mBAA6Q832PGjbjBGQOo)
- Subscribe to The Joy of Coding in iTunes or Kodi: https://air.mozilla.org/feed/itunes/livehacking
- **We'd love for other people in the Mozilla community to start livehacking! Come talk to mconley #livehacking.**

**Rate this episode: https://goo.gl/forms/XgnMg7qf2ExyxG423**

**Notes**
Synchronous vs. Asynchronous

smurfd asks: mconley|livehacking: hey, your were touching a subject id like to ask a follow up on... async calls vs sync calls ... its basicly just that async calls handles if the function is called from several threads, and manages the callbacks right?

function addTwo(num) {
  return num + 2;
}

let x = addTwo(2);
console.log(x);
// x == 4

Synchronous => “immediately”. This function returns a result immediately.

function addTwoIn1Sec(num, callback) {
  setTimeout(() => {
    callback(num + 2);
  }, 1000);
}

let x = addTwoIn1Sec(2);
console.log(x);
// x == undefined

addTwoIn1Sec(2, result => {
  console.log(result);
  // 4 (after 1 second has elapsed)
});

let p = new Promise((resolve, reject) => {
  // Does stuff probably asynchronously
  ...
  setTimeout(resolve, 5000);
});

// Option 1
p.then(() => {
  console.log(“Done!”);
});

// Option 2
async function() {
  await p;
  console.log(“Done!”);
}

**
**
**Chat**

- [IRC](https://wiki.mozilla.org/IRC)
- We're in [irc.mozilla.org](http://irc.mozilla.org) in [#livehacking](http://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org).
- I’ve also got my IRC client signed into the Twitch chat
- [This is a link to a web client that you can use to chat with me from your browser](https://client00.chat.mibbit.com/?channel=%23livehacking&server=irc.mozilla.org)

**Links**

- [The Joy of Coding: Community-Run Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)
    - Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
    - [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [Facebook Page for The Joy of Coding](https://www.facebook.com/TheJoyOfCoding1/)
- The Joy of Diagnosis!: https://www.youtube.com/watch?v=UL44ErfqJXs
- Livehacking on Air Mozilla: https://air.mozilla.org/channels/livehacking/
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

- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- mconley in IRC on [irc.mozilla.org](http://irc.mozilla.org)
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)