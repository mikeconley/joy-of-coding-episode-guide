---
layout: default
date: 2021-10-27
number: 267
---

# Episode 267: Oct 27th, 2021

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2021-10-27)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0267.html)

## Topics
* [Bug 1736690](https://bugzilla.mozilla.org/show_bug.cgi?id=1736690) - Remove or update probes expiring in Firefox 96: pictureinpicture.most_concurrent_players
  - That was easy! Patch posted.
* r? means: request review from
* Mike looks at some of his Needinfos
* `mach try` can some times take time
* Mostly running Python-3.9
* about:memory can be a good place to see where the memory that Firefox uses goes
* [modelled vs modeled](https://wikidiff.com/modeled/modelled)
* Question time!
  - How is gBrowser and xpcom used? Can you talk about it too?
    - gBrowser
      - gBrowser is the name of the component in a Firefox browser window that manages tabs, and the underlying infrastructure for switching tabs, adding tabs, knowing about tab switches, etc.
      - [Light documentation](https://firefox-source-docs.mozilla.org/browser/base/tabbrowser/index.html)
      - gBrowser is a window-global instance of a component called tabbrowser
      - gBrowser is a pretty bad name for what it is. Could maybe be called gTabsManager or gBrowsersManager
      - <browser>, is similar to an <iframe>
      - g is for global, a is for argument, m is for method, s is for static, k is for global constant, ALL_CAPS for global constant
      - Firefox used to not have tabs! At some point in its lineage, Firefox didn't have tabs. It was one <browser> per window. gBrowser.
        - They kept the same name when adding tabs! I think this was to make it easier to support XUL add-ons that relied on touching gBrowser. The new gBrowser variable had the same interface as the old one but would forward calls to the currently selected <browser>.
      - [Source for reading](https://searchfox.org/mozilla-central/rev/f8576fec48d866c5f988baaf1fa8d2f8cce2a82f/browser/base/content/tabbrowser.js)
    - XPCOM
      - It's a very old Mozilla technology modeled after COM from Microsoft
      - Infrastructure for defining interfaces for components that are implementation-language agnostic
        - This means a component written in language A can in theory talk to a component written in language B by way of an interface defined in an (XP)IDL file (.idl)
      - The dream was that Mozilla-backed applications could be written in whatever language you wanted so long as it "supported XPCOM/XPConnect".
      - XPCOM components these days are written in C++, JavaScript or Rust
      - Registry of XPCOM components, and XPCOM component singletons ("services")
      - Cc (Components.classes), Ci (Components.interfaces)
      - let referrerInfo = Cc["@mozilla.org/referrer-info;1"].createInstance(Ci.nsIReferrerInfo);
      - deCOMtamination of the Mozilla source code
        - WebIDL Bindings (.webidl)
        - https://github.com/mdn/archived-content/tree/main/files/en-us/mozilla/tech/xpcom
  - Help us port documentation! [From here!](https://github.com/mdn/archived-content)
    - First find the documentation that you want to port in the GitHub repository
    - File a bug blocking [this bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1736613)
    - Follow these instructions to convert the document to an RST file
    - Use [this example](https://phabricator.services.mozilla.com/D121116) as a template
    - Post for review!
  - Can you explain the process of writing "These Weeks in Firefox" (from start to finish) ?
  - WebExtensions and how they interact with DocShells / BrowsingContexts
  - How a patch gets into Firefox, from start to finish!

* [Rate this episode](https://forms.gle/gxAQXX5ixFzUCSu47)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
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

