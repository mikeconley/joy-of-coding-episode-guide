---
date: 2024-07-10
number: 372
airmozilla: https://mzl.la/joy-of-coding-2024-07-10
agenda: https://mikeconley.ca/joc/agendas/Episode-0372.html
rating: https://forms.gle/jofrxntMCEzqUWta6
---

## Topics

- Finishing up [Bug 1906739](https://bugzilla.mozilla.org/show_bug.cgi?id=1906739) - Implement scheduled backups CTA and restore your data sections in backup-settings
  - We need tests!
    - Test that when backups are disabled:
      - We show the CTA
      - The "Restore" section has the right strings
    - Test that when backups enabled:
      - We do not show the CTA
      - The "Restore" section has the right strings
- File a bug for a backup still being displayed as existing after having disabled backups and restarting
  - Done, and we posted a patch!
  - [Bug 1907136](https://bugzilla.mozilla.org/show_bug.cgi?id=1907136)
  - [D216201](https://phabricator.services.mozilla.com/D216201)
