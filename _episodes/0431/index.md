---
layout: default
date: 2026-02-25
number: 431
---

# Episode 431: Feb 25th, 2026

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2026-02-25)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0431.html)

## Topics
* ![Alt text](https://mikeconley.ca/joc/agendas/images/6b2852e03a62474293c223c1c94a3205 "keanu code 431")
  - https://www.keanu.codes/?code=431
  - Brought to you by HTTP code 431
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/431
* Today will be a slightly shorter episode.
* No episode next week!
* Is it cleaner to just create a specialized protocol handler for cached newtab resources in this configuration?
```HTML
* Add a moz-newtab-cached protocol handler that can run in the privileged about content process.
* It's job will be to get a remote stream from the parent for script, or for styles.
* When the parent receives the request, the parent will get the hash value from prefs.
* Will retrieve the cache entry for the particular resource - like, moz-newtab-cached://script.js - and check that the hash matches the expectation. If not, blow away all caches, fallback to streaming out the packaged script.
* After retrieving the stream, kick off a DeferredTask that will eventually kick a check to see
* if we need to refresh the cache. Once that fires, check RemoteSettings to see if the hash and/or version has changed.
* If the hash and/or version has changed, download them and stream them into the cache:
* Writing to the cache. When it's time to write to the cache:
  - Recreate the entries for script and styles, and hold onto the new references.
  - Write the new hash into prefs.
  - Set the metadata to include the hash and version numbers.
  - Begin streaming, this puts the entries into WRITING mode.
  - Parallel stream scripts and styles into the cache output streams
    - If either fail, doom the cache entry. Clear the pref value for the hash. Try again later.
* moz-newtab-cached protocol has one job: get a remote stream from the parent that will either pull from the valid cache entry OR will fallback to the built-in one. Which means that we have a bit of separation here:
* moz-newtab-cached protocol handler is the "read-only" parts here. It just knows how to read from the cache. It does not know how to write to it. It knows how to fall back.
* The other part is the business around noticing that a newtab loaded, and kicking off the DeferredTask to maybe write an update to the cache.
```

* [Rate this episode](https://forms.gle/ZkVYmmZskFNaaNFV7)

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

