---
layout: default
date: 2021-11-03
number: 268
---

# Episode 268: Nov 3rd, 2021

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2021-11-03)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0268.html)

## Topics
* Episode naming!
* Better mic settings, hopefully. More dynamic compression!
* Needinfos:
  - [Bug 1706981](https://bugzilla.mozilla.org/show_bug.cgi?id=1706981) - Bookmarks Menu Toolbar button submenu items have incorrectly placed chevron on Windows
  - [Bug 1707279](https://bugzilla.mozilla.org/show_bug.cgi?id=1707279) - picture-in-picture control do not always disappear
    - [Getting set up](https://firefox-source-docs.mozilla.org/setup/index.html)
    - [Contributor](https://firefox-source-docs.mozilla.org/contributing/contribution_quickref.html) quick reference. You can submit patches using either Mercurial or Git!
    - [Guide](https://firefox-source-docs.mozilla.org/setup/index.html) on building Firefox
* [Good first bugs](https://codetribute.mozilla.org/)
* Shirshak55 gets assigned their 1st PiP bug

* Question time!
  - Where do Services.wm.functions exist?
    - The properties for Services.jsm are defined using `jsname` in the `components.conf` file when registering XPCOM components statically at build time.
    - Services.wm points to [nsWindowMediator](https://searchfox.org/mozilla-central/rev/1e7f7235cf822e79cd79ba9e200329ede3d37925/xpfe/appshell/nsWindowMediator.cpp) which implements the [nsIWindowMediator](https://searchfox.org/mozilla-central/rev/1e7f7235cf822e79cd79ba9e200329ede3d37925/xpfe/appshell/nsIWindowMediator.idl) interface
  - Also when i receive a warning on the browser toolbox is there any way to know from which path it comes (I mean stack trace)?
    - It depends. If the warning passed an Error, then you get it for free. Otherwise, it will only show you the filename and line number where the warning was logged, and from there you could attach a breakpoint and wait to hit it again.
  - I would be interested in a write-up about your stream setup / equipment
    - Covered somewhat in [Episode 109](https://www.youtube.com/watch?v=0K-hPyqOyL0)
  - Can you explain the process of writing "These Weeks in Firefox" (from start to finish) ?
    - https://wiki.mozilla.org/Firefox/Meeting
    - During the meeting, we take notes as updates are given.
    - After the meeting, a few of us stick around to rewrite the meeting notes into something more palatable
    - We put developer-centric things in "Below the fold" - this doesn't make the cut to the blog, but goes to the firefox-dev mailing list
    - We then post to firefox-dev and the blog. Done!
  - WebExtensions and how they interact with DocShells / BrowsingContexts
    - Next episode. Promise.
  - How a patch gets into Firefox, from start to finish!
    - Next episode. Promise.
  - I have been watching your videos for about two years now. I'm curious if you know who smurfd is. Have you ever met?
    - No! Have never met. Don't know where they are. Don't know who they are. But they're great.
      - And i can unfortunately not remember how or when i found JOC. I suspect it was either from planet.mozilla.org or via twitter. Always thought of it as, if you had a good tv show you could contribute to, would you not do that? /smurfd
  - Read anything interesting lately?
    - After the Flood by Margaret Atwood (MaddAddam trilogy)
    - Hands on Rust
      - Cracked the cover, started reading, looks good, haven't gotten into the meat of it yet. Maybe over the winter holidays, when I have some real focus time.
    - https://www.mozilla.org/en-US/firefox/94.0/releasenotes/
    - https://wiki.mozilla.org/ProjectFission
    - [VPN!](https://www.mozilla.org/en-US/products/vpn/) Give it a shot!

* [Rate this episode](https://forms.gle/iEq2Eq6s4zWEC66g7)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
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

