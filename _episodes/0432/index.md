---
date: 2026-03-11
number: 432
airmozilla: https://mzl.la/joy-of-coding-2026-03-11
agenda: https://mikeconley.ca/joc/agendas/Episode-0432.html
rating: https://forms.gle/uxusn4rxdiKjL6Ki9
---

## Topics

- No HTTP error code 432 in the standard
- Let's get the episode guide up-to-date!
  - Also I can talk about the local search engine thing
- Let's clean up our new implementation for the newtab remote renderer coordinator, do proper version checks, and add the DeferredTask for updating from RemoteSettings.
  - [x] Use Services.vc.compare to compare version numbers to always ensure that the highest version number wins between bundled and cached renderer
  - [x] Add a DeferredTask mechanism to update from RemoteSettings
- TODO:
  - Post Episode 423 to YouTube. It's missing!
