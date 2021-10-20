---
layout: default
date: 2021-09-15
number: 262
---

# Episode 262: Sep 15th, 2021

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2021-09-15)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0262.html)

## Topics
* [Bug 1707582](https://bugzilla.mozilla.org/show_bug.cgi?id=1707582) - Bug 1707582 - Intermittent /modules/test/browser/browser_UsageTelemetry_interaction.js | Expected to see the correct value for bookmark-item in bookmarks_bar. - "undefined" == 1 - JS frame :: /browser/modules/test/browser/browser_UsageTelemetry_interaction.js :: assert
* Fixed the Joy of Coding Episode Guide theme that was broken due to a Jekyll Theme update that probably happened on GitHub's side of things
* [Bug 1724199](https://bugzilla.mozilla.org/show_bug.cgi?id=1724199) - 10.09 - 9.23% sessionrestore_no_auto_restore / sessionrestore_no_auto_restore + 1 more (Windows) regression on Tue August 3 2021
  - [Let's see](https://treeherder.mozilla.org/#/jobs?repo=try&revision=2406f69be8f65c5fe2702adca7a88c149825ffb0) if preloadedState is causing the issue. I will post the results in a comment in the bug.
* [Bug 1725276](https://bugzilla.mozilla.org/show_bug.cgi?id=1725276) - Intermittent docshell/test/browser/browser_TopLevelNavigationDelegate.js | Test timed out -
* The orange color in Treeherder is intermittent test failure
* Shippable builds has gone through PGO - Profile Guided Optimization - which is a step that binaries go through before being shipped to users
* Plug for [Replay](https://www.replay.io) - Your time travel debugger for JavaScript
* [Let's look at a memory report](https://bugzilla.mozilla.org/show_bug.cgi?id=1619772)
* [Let's bump some probe expiries](https://bugzilla.mozilla.org/show_bug.cgi?id=1730042)
  - [And here](https://bugzilla.mozilla.org/show_bug.cgi?id=1730041)
* Question time!
  - What are your thoughts on Proton redesign?
    - I like it!
  - When I was tinkering with Firefox I found a way to zoom text only: Menu Bar -> View -> Zoom -> Zoom text only. I find it extremely useful. Is there a reason why this could not be additionally accessed using "Zoom controls" or activated with some shortcut? + What is the process for deciding which items to select in menu bars/toolboxes?
  - Have you ever read a book on e-ink paper?
    - Yes
    - I have a Kobo
    - Margaret Atwood's Oryx and Crake
  - Some companies/teams once in a while have a time period when they focus solely on fixing bugs - what do you think about this approach? have you ever discussed this with your colleagues?
    - Yes, I like this approach. We do this approach! It's a great way to fix papercuts and also to pay down technical debt.

* [Rate this episode](https://forms.gle/SSpT4vYSGYM6vAWU9)

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

