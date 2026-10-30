---
date: 2026-07-15
number: 443
airmozilla: https://mzl.la/joy-of-coding-2026-07-15
agenda: https://mikeconley.ca/joc/agendas/Episode-0443.html
rating: https://forms.gle/xL8n3xeo8HNGNtnL9
---

## Topics

- Phew, turbulent few weeks! But I'm back!
- Where were we? Oh yeah, cropped labels.
  - WebIDL that is ChromeOnly exposed that allows a caller to enable center cropping behaviour
  - nsCSSFrameConstructor, I wanted check for that usage rather than merely checking the system principal
  - moz-label:
    - Add a new observed attribute called "enable-center-crop" that will, if set to true, call the WebIDL function to set the state of center cropping behavior
    - Will also ensure that the `value` attribute is set, and the textContent is cleared out (or will warn if there are child elements and bail out!)
    - Have CSS applied automatically with `enable-center-crop` that sets text-wrap: nowrap
