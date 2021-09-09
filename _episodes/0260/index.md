---
layout: default
date: 2021-09-01
number: 260
---

# Episode 260: Sep 1st, 2021

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2021-09-01)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0260.html)

## Topics
* Fixed the Joy of Coding Episode Guide theme that was broken due to a Jekyll Theme update that probably happened on GitHub's side of things
* [Bug 1724199](https://bugzilla.mozilla.org/show_bug.cgi?id=1724199) - 10.09 - 9.23% sessionrestore_no_auto_restore / sessionrestore_no_auto_restore + 1 more (Windows) regression on Tue August 3 2021
  - [Let's see](https://treeherder.mozilla.org/#/jobs?repo=try&revision=2406f69be8f65c5fe2702adca7a88c149825ffb0) if preloadedState is causing the issue. I will post the results in a comment in the bug.
* [Bug 1725276](https://bugzilla.mozilla.org/show_bug.cgi?id=1725276) - Intermittent docshell/test/browser/browser_TopLevelNavigationDelegate.js | Test timed out -
* Question time!
  - Have Firefox devs sent patches to Chromium and have Google devs sent patches over to Firefox?
    - Yes to both.
    - [Igalia](https://www.igalia.com/)
    - [WebRTC](https://webrtc.googlesource.com/) as well
  - What song (songs) has been playing in the back of your head lately?
    - Dinosaur Pile-up called 11:11
    - k.flay "Dating my Dad"
  - What in your life do you feel grateful for?
    - Being alive
    - Great family, great friends, great job that I enjoy, live in Canada
    - Small things: tea, coffee, tasty tap water (Toronto!), Toronto
      - Don Valley Parkway 
    - Good books, that I can read them
  - What do you value the most in a friendship and relationship?
    - Ease and fluidity of communication
    - Good humour
    - Trust
  - How would you go about debugging intermittent hangs in Firefox after its been on its own for a while? In the morning it is hanging, but was working when you left at night... and this happens not every day but some
    - The hang itself, at the point where you come back, may have enough information to be actionable. The thing to do is try to turn the hang into actionable data.
      - macOS and Linux, we want to crash intentionally
        - Get the Process ID of the parent process: `ps aux | grep firefox`
        - Crash using SIGABRT: `kill -SIGABRT <process ID>`, `kill -SIGABRT 1327`
      - Windows, crashintentionally.exe
        - https://releases.mozilla.org/pub/utilities/crashfirefox-intentionally/
        - Source: https://github.com/bsmedberg/crashfirefox-intentionally
      - https://firefox-source-docs.mozilla.org/performance/reportingaperformance_problem.html 

* [Rate this episode](https://forms.gle/xADFGN8CdFDm5uXM8)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Compiler Compiler](https://www.twitch.tv/codehag) live stream
* Try out Mozilla [VPN](https://vpn.mozilla.org/)
* How mconley uses [Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mikes Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* [Codetribute](https://codetribute.mozilla.org/) - Go here to find Mentored bugs to hack on, ie good for beginners
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
* [Codetribute](https://codetribute.mozilla.org/) - Help contribute to Firefox, good mentored bugs for You.
  - First, [Create](https://bugzilla.mozilla.org/createaccount.cgi) a Mozilla Bugzilla account.

