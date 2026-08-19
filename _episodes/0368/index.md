---
date: 2024-06-12
number: 368
---

# Episode 368: Jun 12th, 2024

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2024-06-12)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0368.html)

## Topics
* Commandeer, add some changes to, and then land a colleagues patch
* Solve a WindowsJumpList favicon test failure
* And then hopefully reland!
* ...And then land the legacy backend removal patches
* Maybe some tests for the backup scheduler
  - Test that initBackupScheduler registers an idle callback
  - Test that uninitBackupScheduler unregisters an idle callback
  - Test that observing the "idle" notification calls onIdle
  - Test that observing the "quit-application-granted" notification calls uninitBackupScheduler
  - Test that calling onIdle and a backup has never occurred causes a backup to get scheduled
  - Test that calling onIdle and a backup has occurred recently does not cause a backup to get scheduled
  - Test that calling onIdle and a backup has occurred, but after the threshold does cause a backup to get scheduled
  - Test that calling onIdle and a backup occurred in the future somehow causes a backup to get scheduled

* [Rate this episode](https://forms.gle/xGBNun9gsjsDvhqD8)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

