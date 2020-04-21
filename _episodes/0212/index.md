---
layout: default
date: 2020-04-15
number: 212
---

# Episode 212: Apr 15th, 2020

## Links
* [Watch this episode on Air Mozilla](https://air.mozilla.org/event-redirect/367425/)
* [Evernote Agenda](https://www.evernote.com/shard/s434/client/snv?noteGuid=54443a75-c002-475d-81c7-b998bda7a34f&noteKey=b2c8d358c366484e&sn=https%3A%2F%2Fwww.evernote.com%2Fshard%2Fs434%2Fsh%2F54443a75-c002-475d-81c7-b998bda7a34f%2Fb2c8d358c366484e&title=April%2B15th%252C%2B2020%2B-%2BEpisode%2B212)

## Topics
* Pandemic edition! Mike is streaming from home! Let's hope the wifi holds out
* Background [music](https://freemusicarchive.org/music/Broke_For_Free/Petal)
* [Bug 1630234](https://bugzilla.mozilla.org/show_bug.cgi?id=1630234) - About:newtab does not maintain the scroll position after navigating back to the page - [Notes](https://www.evernote.com/l/AbIdnKfcU55Crbvs2mH5Ysin-kPmufiV4rQ)
* Bisect
  - ./mach mozregression --launch 2019-01-01    (check wether this has your bug or not)
  - if it did not, you can "mark" it as a good build : ./mach mozregression --good 2019-01-01   (again mark it as good) 
    it will then stop your browser, download a new snapshot, and you write wether its a good or bad build. Repeat until your window of when the bug appeared is so small its easy to find what revision it might have been introduced in.
* Was using the Browser Toolbox to debug the problem
* Getting started [Contributing](https://codetribute.mozilla.org/) to Mozilla
  - you can if you want, use Git to contribute to Mozilla aswell as Mercurial

* [Rate this episode](https://forms.gle/apF6hWYmKwiPbmPr7)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mikes Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* [Codetribute](https://codetribute.mozilla.org/) - Go here to find Mentored bugs to hack on, ie good for beginners
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
