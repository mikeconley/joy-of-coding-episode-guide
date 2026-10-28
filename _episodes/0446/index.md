---
date: 2026-08-12
number: 446
---

# Episode 446: Aug 12th, 2026

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2026-08-12)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0446.html)

## Topics
* Let's look at what it took to get the moz-label working like we wanted
* Now let's write some tests!
  - InspectorUtils.getChildrenForNode($0, true, false)[1]
  - ^-- where \$0 is the label element
  - Let's write a mochitest-chrome test that checks that center cropping actually works
    - dom/html/test/forms/testchromelabelcentercropping.html
      - We expect center cropping to work when crop="center" and value="some string" and text-wrap: no-wrap and max-width applied.
  - Let's write a mochitest-plain test that checks that center cropping does not work for plain HTML documents
    - dom/html/test/forms/testcontentlabelnocenter_cropping.html
      - We expect NO center cropping when crop="center" and value="some string" and text-wrap: no-wrap and max-width applied.

* [Rate this episode](https://forms.gle/kKAy3aHUYeq7jMqm6)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

