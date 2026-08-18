---
date: 2022-10-19
number: 303
---

# Episode 303: Oct 19th, 2022

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2022-10-19)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0303.html)

## Topics
* Rebase and resubmit a patch
* Drilling a "pilot hole" (this is a metaphor)
  - Investigate:
    - Using a reusable web component for our migration UI, the web component will be define in a ESM and will have some associated JSWindowActor glue to always be able to communicate back and forth with the parent process
    - Using a reusable document that can be loaded in a parent-process modal as well as a privileged about content process <xul:browser> / <iframe>.
      - Register an about: page that can be loaded by about:welcome in the privileged about content process
    - Having an build-time included document fragment in both places
      - Bookmark panel vs modal
* Pi-related episode for Episode 314? Maybe I'll eat pie that day... let me know what your thoughts are there.

* [Rate this episode](https://forms.gle/De7wVWyVwoZQT3td9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

