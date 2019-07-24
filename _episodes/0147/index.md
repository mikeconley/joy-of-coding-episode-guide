---
layout: default
date: 2018-08-15
number: 147
---

# Episode 147: August 15th, 2018

## Links
* [Watch this episode on new Air Mozilla](https://onlinexperiences.com/Launch/Event.htm?ShowKey=44908&DisplayItem=E300281)
* [Evernote Agenda](https://www.evernote.com/shard/s434/sh/17032b66-7d06-4c72-b0f2-98a128b53c30/90e3a50671e12aa7)

## Shoutouts
* [Les Orchard](https://www.twitch.tv/lmorchard/videos/all) Hacks on [Firefox Color](https://color.firefox.com)
* [Josh Marinacci](https://twitter.com/joshmarinacci) Hacks on [Firefox Reallity](https://www.twitch.tv/joshmarinacci)

## Topics
* [Mikes Firefox Color Theme](https://color.firefox.com/?theme=XQAAAAL0AAAAAAAAAABBqYhm849SCiazH1KEGccwS-xNVAVPvKGAiNxTtah5dSzAMY7NzGmHfkUxcNIrZ_wYPN9WEZbZAy4tRvZRuWYQhm80LcQZZTOdLhL5yc7pW2Zj4dNy6LgWfK7PFe8TDkw1-5Ob20-NiTi_Ryu2oBEpvJE9kFK2BHbPc4QaRiB6f2FsJmxcKUXEwRtl6AfcsSppjNaoAS-qGvdPPLLUM-H46onWPoZjwmLc3wocjn4JOxhB8oQZuvjGCv9UEEAA)
* Attempt to reproduce and (if reproducible) file the about:printpreview bug that I noticed during the stream
  1. Create a session with a single window and tab pointed at http://i.imgur.com/lmzNpx7.png
  2. Shut down the browser
  3. Start the browser and restore session automatically, so we have a single tab pointed at http://i.imgur.com/lmzNpx7.png
  4. Earlier noticed a about:printpreview  tab[0].content.location  but not this time....
* [Bug 1478112](https://bugzilla.mozilla.org/show_bug.cgi?id=1478112) - Sort out how to best call `this._getSwitcher().requestTab` and `this.updateCurrentBrowser` during tabpanels selectedIndex change
* [JS Time travel debugging](https://twitter.com/digitarald/status/1026887071955181569) AKA Project Delorean AKA WebReplay
   1. flip about:config switch : devtools.recordreplay.enabled
   2. Windows support [Bug1310271](https://bugzilla.mozilla.org/show_bug.cgi?id=1310271)
* [Bug 1481466](https://bugzilla.mozilla.org/show_bug.cgi?id=1481466) - Themes are incorrectly displayed in preview mode

## Episode 150 ideas?!
* Got ideas? Submit them in the Episode Rating form!
* AMA
* Work on some kind of user voted bug?
* Build a WebExtension to do something from scratch?
* Explore some other Mozilla project?
* Explore a non-Mozilla project and try to understand it?
* Explain some part of the codebase?
* Normal episode? (But wear a funny hat)?
