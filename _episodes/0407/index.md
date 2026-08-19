---
date: 2025-06-25
number: 407
---

# Episode 407: Jun 25th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-06-25)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0407.html)

## Topics
* Fix Opera migrator
  - https://bugzilla.mozilla.org/show_bug.cgi?id=1971702
* New Tab messaging plumbing?
  - The issue is that NewTabMessage knows that it has sent a particular newtab an instruction to show a message in the past, but doesn't actually know if it's visible or not. It may have already been dismissed by the user.
  - What I think we should do is have the MessageWrapper send an action to the parent if a message is shown, and if a message is dimissed. The parent will maintain a WeakSet of elements that are showing messages. On a message shown, it'll add to the set. On message dimissed or newtab unload, it'll remove from the set.
  - When it comes time to check if a message is visible on the current selected browser, merely check if it's in the set O(1).
* New Tab image performance optimization, if we have time

* [Rate this episode](https://forms.gle/vVF2WCw6hsJxnwY79)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

