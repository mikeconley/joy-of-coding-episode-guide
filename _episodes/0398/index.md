---
date: 2025-04-16
number: 398
---

# Episode 398: Apr 16th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-04-16)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0398.html)

## Topics
* Updating the episode guide
* Let's keep going with our Rust component for FilterAdult
  - https://github.com/mozilla/application-services/
  - Write a tool that can take a list of base64 encoded md5 hashes and produce a .rs file that has those hashes defined as raw bytes, and can be linked into the library
  - Modify that tool afterwards to also accept a list of base domain strings rather than base64 encoded md5 hashes, so that we can easily update the list
    - Make it possible for the tool to merely accept additions, or to fully overwrite
      - Maybe removals too?
  - Design and write the library. It should ideally just expose the following functions:
    - isAdultURL function
    - addDomainToListForTesting
    - removeDomainFromListForTesting
  - Our utility can use relevancy components "generate-test-data" utility as an example to work from
  - For next time:
    - Read in the .mjs file, strip out what we don't need, and then convert each string into the byte representation to generate the Rust file that we need.
    - Import that Rust file into import-site-list
*  ./import-site-list --from-filteradult-mjs=<path> ./import-site-list --add=<path> ./import-site-list --remove=<path> ./import-site-list --replace=<path>

* [Rate this episode](https://forms.gle/pTVA361bbFFMqbq4A)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

