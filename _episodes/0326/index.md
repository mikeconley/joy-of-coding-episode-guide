---
date: 2023-05-31
number: 326
---

# Episode 326: May 31st, 2023

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2023-05-31)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0326.html)

## Topics
* Firefox Translations!
  - [Metabug](https://bugzilla.mozilla.org/show_bug.cgi?id=971044) to file bugs against
  - [Training](https://github.com/mozilla/firefox-translations-training) pipeline
* Back to WindowsJumpList!
  - A lot of the complexity that we're dealing with architecturally is because we're trying to maintain the old backend while adding the new capability with a new backend, but the two backends share some infrastructure.
  -  What I want to do is determine if we can do a better job of separating out the jumplist backend by reading a pref at runtime and choosing the right implementation.
  - Rename nsIJumpListBuilder to nsILegacyJumpListBuilder
  - Add createLegacyJumpListBuilder to nsIWinTaskBar to use the old mechanism
  - Create a new nsIJumpListBuilder and implement it using the code we've got
  - Have createJumpListBuilder in nsIWinTaskBar use that
  - Update WindowsJumpLists to choose the right builder based on the pref and treat them correctly based on that pref.
* Let's work to retire the old migration wizard 

* [Rate this episode](https://forms.gle/bHrQLXo3eUym2mMc8)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

