---
layout: default
date: 2022-04-06
number: 285
---

# Episode 285: Apr 6th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-04-06)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0285.html)

## Topics
* Let's review a patch!
  - [D142898](https://phabricator.services.mozilla.com/D142898)
* Let's go through some needinfos!
  - [Bug 1755547](https://bugzilla.mozilla.org/show_bug.cgi?id=1755547) - LoadType not set on SessionHistoryInfo when handling `pushState`
* [Bug 1756878](https://bugzilla.mozilla.org/show_bug.cgi?id=1756878) - Add a linting rule for mochitest.ini / browser.ini / chrome.ini files to ensure tests are in alphabetical order

Question time:
* Hey, have i dreamt or have you said you use a site called Roll20? Seems as of late it is not working so good with Webcams and Firefox. Was thinking of filing a bug for it but not sure how to give a good bug report. I can see my camera, but my friends cant see my camera... and i cant see theirs if they use firefox. but if they use say Chrome i can see them but they cant see me until i switch to chrome? br smurfd
  - It sounds like we're having trouble sending a feed... or, the correct camera device isn't being used.
  - How to file a good bug for this:
    - https://webcompat.com/
    - Describe the steps to reproduce

* In JoC 237 you reviewed a MSU Capstone patch for:
  [Bug 1678390](https://bugzil.la/1678390) - Prevent Picture-in-Picture windows from opening on top of one another
  - Bug patches subsequently failed to land and i thought it would be interesting to revisit, with an overview post-mortem of what can cause a submitted patch to fail autoland?
  - summary of patch behaviour from the episode:
    - start with pip window1 which has left-top xy coordinate
    - try to fit pip window2 to the left/right/above/below of window1
    - if there is enough room, then use this optimal side-by-side placement for window2.
    - if there is not enough room (e.g. window1 fills majority of screen), then the episode mentioned adding an xy offset to window2, so there is still a fix for the 100% overlap of current behaviour.
    - i assume like "cascade" i.e. https://www.tenforums.com/tutorials/78477-cascade-windows-windows-10-a.html
  - Hopefully you could either propose a fix to the patch, or alternatively add a comment to the bug indicating a likely method needed for it to be fixed by a future assignee?

* Next week: Maybe back in the office to stream?!

* [Rate this episode](https://forms.gle/B4UQBg7c3RKF3ZBU8)

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

