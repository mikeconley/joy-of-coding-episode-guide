---
layout: default
date: 2022-02-09
number: 278
---

# Episode 278: Feb 9th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-02-09)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0278.html)

## Topics
* How to debug Firefox's native code on macOS (lldb), then Linux (gdb), then Windows (Visual Studio)!
  - Optimized builds, unoptimized / debug builds, artifact builds
    - Why can't we do native code debugging of artifact builds?
      - [Configure Build Options](https://firefox-source-docs.mozilla.org/setup/configuring_build_options.html)
  - Attaching to a running instance of Firefox
    - https://lldb.llvm.org/use/map.html
    - MOZ_DEBUG_CHILD_PROCESS=1
    - https://rr-project.org/
    - https://pernos.co/
    - Attaching to the parent process
      - Windows: The Launcher Process
        - https://bugzilla.mozilla.org/showbug.cgi?id=1495040
        - MOZ_DEBUG_BROWSERPAUSE=15
    - Attaching to the content process

* [Rate this episode](https://forms.gle/xnGneA1xnB2uM5u46)

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

