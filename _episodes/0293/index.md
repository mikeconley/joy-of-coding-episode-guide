---
layout: default
date: 2022-07-06
number: 293
---

# Episode 293: Jul 6st, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-07-06)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0293.html)

## Topics
* [Bug 1778204](https://bugzilla.mozilla.org/show_bug.cgi?id=1778204) - LightweightThemeChild doesn't call update() for non-sidebar parent process documents
* Only 7 episodes until Episode 300! Any more ideas on what to do for 300? Let me know in the [Rate this episode](https://forms.gle/n8FbeWEDFtmfnExQ9) form!
* Question time!

  - Could you please give an overview of the reason for the functional split between bugzilla, phabricator, jira. Also, should mozilla's jira be publicly accessible, there are links from bugzilla to both but it seems only phabricator are public?
    - JIRA is good as a project management tool. It is less good as a bug tracker. It is much worse as a tool for doing development in the open, since we (Mozilla) have to pay a seat license per user for our instance.
    - Bugzilla is a free, open-source bug tracker tool. A very good, very powerful bug tracking tool. But a pretty bad project management tool.
    - We have a tool that glues Bugzilla and JIRA together. When you file a bug in Bugzilla for a project that's using JIRA for Project Management, a JIRA ticket is automatically created that mirrors the Bugzilla bug. And they stay in sync.
      - That way, project management / product management get their fun and fancy reports and can do prioritization and see the big picture.
      - Engineering gets to do the development in Bugzilla in the open (presuming the bugs are not marked confidential for security, privacy or partnership reasons)
    - Differential is an open-source code review tool that's part of the Phabricator suite of developer tools. It's another set of tools that tries to be everything for everyone, but we just use the code review part for the most part (there are some other bits that we use, but mainly we just use Differential which is for code review)
    - Bugzilla integrates with Differential and moz-phab knows how to talk to both
    - Bugzilla <-> Phabricator (via moz-phab) that's for code review!
    - Bugzilla <-> JIRA (via background JIRA sync thing) that's for project management
    - Bugzilla is for open development
    - JIRA is for project management / reporting, etc.
  - When is it enough to just restart the browser and when does "mach build faster" need to be run?
    - This is a great question and not immediately obvious, and I can't actually say if I know for certain.
    - It's going be different from platform to platform, actually - since, I think, on some platforms the way that symlinks work is different from others. And symlinking is kind of the magic that's making it so that you don't need to run `./mach build faster`. What `./mach build faster` does is repackages a bunch of files into a directory that's then read by the firefox binary at runtime... and sometimes we can get away with symlinking instead of repackaging. Sometimes not though! Specifically, for pre-processed files. Anything that has #ifdef in it, or needs to run some extra build-time step, we have to invoke that build-time step.
    - If you're not sure, try it! Make a change in a file, and restart the browser (or sometimes, reload the page!) and see if the change is there. If not, then try `./mach build faster`. Or, if you're feeling adventurous, try `./mach watch`, which will do the `./mach build faster` for you in the background.
    - [JoC ep 190](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/fd3591f6f7d79786d9c1b152ec43e7ab7cacf47b/_episodes/0190/index.md)
  - When do you need to rebuild when running tests and when not?
    - If you've made binary changes, or need to run a build-time step (like pre-processing...) then you need to rebuild.
    - I've noticed that when changing just test files, you don't need to run `./mach build` at all when modifying the test. You can just modify the test file, and then re-run the test.
  - What is the easiest way to figure out which try jobs should get run to get maximum confidence?
    - `./mach try auto`

* [Rate this episode]( https://forms.gle/n8FbeWEDFtmfnExQ9)

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

