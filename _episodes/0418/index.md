---
layout: default
date: 2025-10-29
number: 418
---

# Episode 418: Oct 29th, 2025

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2025-10-29)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0418.html)

## Topics
* Sorry for the delays!
  - More travel coming soon though...
* ![Alt text](https://mikeconley.ca/joc/agendas/images/709d846bd7c54d23b8057994de48ec64 "keanu code 418")
  - https://www.keanu.codes/?code=418 - mikes favourite
  - Brought to you by HTTP code 418
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/418
* Previewing split view!
  - browser.tabs.splitView.enabled
* Testing a punch out of a hole for newtab
  - nsICategoryManager
  - Hand-off Search Component
    - Has a SearchComponents.manifest
    - category browser-newtab-ui-component moz-src:///browser/components/search/ContentSearchUINewTabComponent.sys.mjs ContentSearchUINewTabComponent.definition
    - ContentSearchUINewTabComponent.sys.mjs
      - const ContentSearchNewTabUIComponent { definition() { return { type: NewTabUIComponent.TYPE_SEARCH, scripts: [dependencies, and script that defines moz-search-input], markup: { tagName: "moz-search-input", attrs: { } }, } } }
    - Something that reads from the category manager on initialization, also adds observers for "xpcom-category-entry-added" and "xpcom-category-entry-removed", and on initialization OR when the category in question (browser-newtab-ui-component) changes, we reconstruct the list of components
    - Potentially reuse CatManListenerManager, which does the above (but we need to recompute the categories on notifications)
    - Interestingly, the CategoryManager has its entries populated from manifest files for each process, meaning that we'd get build-time registration for free in the privileged about content process. What we wouldn't get is dynamic registration and unregistration
    - Have the backend newtab code iterate the relevant categories, and get the return values for each entry in the category, and then to sort them by type.
      - This will then create a structure which can be send down in the state object that each New Tab receives - A class (or component?) will be responsible for parsing that structure and holding it per page - Yes, it's awkward that each instance of newtab has one of these, but that's already a problem with the state object - The Search.jsx component will get the definition for the lone "search" item in the registry. When it finds it, it will insert the script and insert a web component (React, Lit, vanilla) that is responsible for adding stylesheet dependencies within its shadow dom or via CSS modules.
        - I need to start an Engineering Design document to start shopping around with these ideas, at least show Gijs and Scott, but probably a bunch of others as well.
        - File a bug to get rid of non-handoff behaviour to simplify Search.jsx and contentSearchUI
* Reviewing?

* [Rate this episode](https://forms.gle/Qn3SPSzPmqW13qpt9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
* [npb hacks](https://www.twitch.tv/BackToTheCode) on the SpiderMonkey JS engine
* [Compiler Compiler](https://www.twitch.tv/codehag) live stream
* Try out Mozilla [VPN](https://vpn.mozilla.org/)
* How mconley uses [Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mike's Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
* [Codetribute](https://codetribute.mozilla.org/) - Help contribute to Firefox, good mentored bugs for You.
  - First, [Create](https://bugzilla.mozilla.org/createaccount.cgi) a Mozilla Bugzilla account.

