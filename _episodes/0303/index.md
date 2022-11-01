---
layout: default
date: 2022-10-19
number: 303
---

# Episode 303: Oct 19th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-10-19)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0303.html)

## Topics
* Rebase and resubmit a patch
* Drilling a "pilot hole" (this is a metaphor)
  - Investigate:
    - Using a reusable web component for our migration UI, the web component will be define in a ESM and will have some associated JSWindowActor glue to always be able to communicate back and forth with the parent process
    - Using a reusable document that can be loaded in a parent-process modal as well as a privileged about content process <xul:browser> / <iframe>.
      - Register an about: page that can be loaded by about:welcome in the privileged about content process
    - Having an build-time included document fragment in both places
      - Bookmark panel vs modal
* Pi-related episode for Episode 314? Maybe I'll eat pie that day... let me know what your thoughts are there.

* [Rate this episode](https://forms.gle/De7wVWyVwoZQT3td9)

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

