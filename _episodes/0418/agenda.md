**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- Sorry for the delays!
    - More travel coming soon though...
- HTTP code 418 - this is one of my favourites.
    - ![26410633c625e8e7f923f8173de2d55a.png](images/709d846bd7c54d23b8057994de48ec64)
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/418
- Previewing split view!
    - `browser.tabs.splitView.enabled`
- Testing a punch out of a hole for newtab
    - nsICategoryManager
    - Hand-off Search Component
        - Has a SearchComponents.manifest
        - `category browser-newtab-ui-component moz-src:///browser/components/search/ContentSearchUINewTabComponent.sys.mjs ContentSearchUINewTabComponent.definition`
        - ContentSearchUINewTabComponent.sys.mjs
            - ```
                   const ContentSearchNewTabUIComponent {
                     definition() {
			           return {
	                  	   type: NewTabUIComponent.TYPE_SEARCH,
	                  	   scripts: [dependencies, and script that defines moz-search-input],
	                  	   markup: {
				             tagName: "moz-search-input",
						     attrs: {
						     }
				           },
				       }
                     }
                   }
                ```
        - Something that reads from the category manager on initialization, also adds observers for `"xpcom-category-entry-added"` and `"xpcom-category-entry-removed"`, and on initialization OR when the category in question (`browser-newtab-ui-component`) changes, we reconstruct the list of components
		- Potentially reuse CatManListenerManager, which does the above (but we need to recompute the categories on notifications)
	    -  Interestingly, the CategoryManager has its entries populated from manifest files *for each process*, meaning that we'd get build-time registration _for free_ in the privileged about content process. What we wouldn't get is *dynamic* registration and unregistration
        - Have the backend newtab code iterate the relevant categories, and get the return values for each entry in the category, and then to sort them by type.
			- This will then create a structure which can be send down in the state object that each New Tab receives
				 - A class (or component?) will be responsible for parsing that structure and holding it per page
				 - Yes, it's awkward that each instance of newtab has one of these, but that's already a problem with the state object
				 - The Search.jsx component will get the definition for the lone "search" item in the registry. When it finds it, it will insert the script and insert a web component (React, Lit, vanilla) that is responsible for adding stylesheet dependencies within its shadow dom or via CSS modules.
		 - I need to start an Engineering Design document to start shopping around with these ideas, at _least_ show Gijs and Scott, but probably a bunch of others as well.
	     - File a bug to get rid of non-handoff behaviour to simplify Search.jsx and contentSearchUI
		  - 
- Reviewing?

**[Rate this episode](https://forms.gle/Qn3SPSzPmqW13qpt9)**

**Chat**

- [Join us in the Livehacking room on Mozilla’s Matrix instance!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist) Here’s [documentation on how to join](https://wiki.mozilla.org/Matrix). I’m only sorta monitoring the Twitch chat. A bot will try to bridge Matrix and Twitch (joc-bridgebot).

**Links**

- [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
- [nbp hacks on the SpiderMonkey JS engine](https://www.twitch.tv/BackToTheCode)
- [Alessandro Castellani has been streaming himself livehacking on Thunderbird](https://www.youtube.com/c/AlessandroCastellani/videos)
- [emilio hacks on Firefox!](https://www.youtube.com/channel/UCYbsdvH4_52BFAijFVgYGgA)
- [Compiler Compiler - watch a Mozilla engineer hack on the SpiderMonkey JavaScript engine!](https://www.twitch.tv/codehag)
- [How mconley uses Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
- [Andreas Kling hacks on a custom browser engine for a hand-rolled OS called SerenityOS](https://www.youtube.com/playlist?list=PLMOpZvQB55be0Nfytz9q2KC_drvoKtkpS)
- [The Joy of Coding: Community-Run Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)
    - Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
    - [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [I've been mirroring the episodes to YouTube](https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5)
- [Code Therapy with Danny O’Brien](https://www.youtube.com/channel/UCDShi-SQdFVRnQrMla9G_kQ)
- Watch a developer put together a Windows game from scratch (no third-part engines) - really great explanations: https://handmadehero.org/
- [/r/WatchPeopleCode](https://www.reddit.com/r/WatchPeopleCode) for more livehacking!

**Glossary**

- BHR - “Background Hang Reporter”, a thing that records information about when Firefox performs poorly and sends it over Telemetry
- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)
- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- Deserialize - "turn a serialized object back into the complex object”
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc
- Regression - something that made behaviour worse rather than better. Regress means to “go backward”, more or less.
- l10n - localization
- a11y - accessibility
- i18n - internationalization
- k8s - kubernetes

**Feedback**

- [@mconley@mozilla.social on Mastodon](https://mozilla.social/@mconley)
- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- You can chat with me on [Matrix](https://wiki.mozilla.org/Matrix) at @mconley:mozilla.org
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)
- mconley at mozilla dot com