---
layout: default
date: 2020-03-25
number: 209
---

# Episode 209: Mar 25th, 2020

## Links
* [Watch this episode on Air Mozilla](https://air.mozilla.org/event-redirect/366241/)
* [Evernote Agenda](https://www.evernote.com/shard/s434/client/snv?noteGuid=0e9fa569-c955-4782-8545-9f2af2c05d3c&noteKey=dfd61e2d88f359bf&sn=https%3A%2F%2Fwww.evernote.com%2Fshard%2Fs434%2Fsh%2F0e9fa569-c955-4782-8545-9f2af2c05d3c%2Fdfd61e2d88f359bf&title=March%2B25th%252C%2B2020%2B-%2BEpisode%2B209)

## Topics
* Pandemic edition! Mike is streaming from home! Let's hope the wifi holds out (It did!)
* Background [music](https://freemusicarchive.org/music/Broke_For_Free/Leaf)
* [Bug 1184701](https://bugzilla.mozilla.org/show_bug.cgi?id=1184701) - PageThumbsProtocol (moz-page-thumb://) does not work in the content process - [Notes](https://www.evernote.com/l/AbLH7ey0w7FPe71-bQhj8TPpdm3sG2YjKSg)
* [Bug 1614502](https://bugzilla.mozilla.org/show_bug.cgi?id=1614502) - Add a mechanism for producing a static version of about:home periodically that can be cached for startup.
* Applying a 2 year old patch can be tricky
* To help reproduce a Performance issue (around 1h41 in this episode):
  - Get a copy of [Nightly](https://www.mozilla.org/en-US/firefox/channel/desktop/#nightly)
  - If you can reproduce the issue, visit [Profiler](https://profiler.firefox.com)
  - Then press the "Enable Profiler Menu Button" that should put a stopwatch in your toolbar
  - Press the stopwatch icon, then "Start recording"
  - Then do what causes the performance issue
  - When you have had the problem, press the Capture button in the Stopwatch
  - After a while that will show you a site from https://profiler.firefox.com that is very ... colorful
  - If you then want to submit this capture, press the green Publish button in the right corner.
  - Then submit a but with the link or contact Mike somehow, this makes it easier for them profile the issue
* To help reproduce a memory issue, you can do so via the Profiler aswell, but that is experimental for now
  - Instead go to : about:memory in nightly or Release
  - Then press the Measure button to the left
  - Then press Measure and save to save the output and share with Mike/Mozilla via either a bug or somehow

* [Rate this episode](https://forms.gle/rQNxxCCbKTxVdj9i7)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mikes Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* [Codetribute](https://codetribute.mozilla.org/) - Go here to find Mentored bugs to hack on, ie good for beginners
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
