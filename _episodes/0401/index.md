---
layout: default
date: 2025-05-14
number: 401
---

# Episode 401: May 14th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-05-14)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0401.html)

## Topics
* No episode next week
* Question: Not a serious question, but Can you make a fun video whenever you are freee about Reviewing and Explaining how old swf shockwave flash games worked , why swf was banned later from the Internet.
  - Flash ran as an NPAPI plugin in the browser: Netscape Plugin API
    - Homestarrunner.com
    - YouTube
  - Macromedia: Shockwave Flash
  - Bought by Adobe
  - 2008 is the year that the Apple iPhone is revealed
    - No plugins for the web browser (Safari). No NPAPI.
  - https://ruffle.rs/
* For implementing filter in filter_adult - I actually don't think I want to do this. I don't think I want to force the embedders to use a particular class right now - specifically on desktop, because it seems to be used to passing raw objects around with URL properties and just being a bit loose-y goose-y... I don't want to (yet) disturb that. I'm trying to avoid fixing the world. For now, what I'll do is implement filter in the wrapper module which will simply delegate the set lookup to the Rust module.

* [Rate this episode](https://forms.gle/PtsWa9MFzW4G5Pdr6)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
* [npb hacks](https://www.twitch.tv/BackToTheCode) on the SpiderMonkey JS engine
* [Compiler Compiler](https://www.twitch.tv/codehag) live stream
* Try out Mozilla [VPN](https://vpn.mozilla.org/)
* How mconley uses [Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mike's Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
* [Codetribute](https://codetribute.mozilla.org/) - Help contribute to Firefox, good mentored bugs for You.
  - First, [Create](https://bugzilla.mozilla.org/createaccount.cgi) a Mozilla Bugzilla account.

