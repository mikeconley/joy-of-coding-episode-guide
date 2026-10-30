---
date: 2024-02-28
number: 357
airmozilla: https://mzl.la/joy-of-coding-2024-02-28
agenda: https://mikeconley.ca/joc/agendas/Episode-0357.html
rating: https://forms.gle/39DE99HJ4oYXeMJ57
---

## Topics

- Jump List stuff
  - Beta got the green light! Looks like we're shipping to release!
  - Made some forward progress with some fairly rube-goldbergy architecture to marshall stuff between io thread, favicon service and the main thread. But we got something that ultimately builds. But crashed when used. Trying to use a nsMainThreadPtrHandle instead because maybe that's better. ?! Could really use some help, maybe from our Media team which definitely uses MozPromises a lot.
    - TODO: Talk to Media team about the right way of doing this.
