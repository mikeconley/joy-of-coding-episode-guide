**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

- WindowsJumpList favicon stuff!
    - We need tests
        - We have added a new method called obtainAndCacheFaviconAsync on nsIJumpListBuilder
        - The expectation is that we should be able to use this method to asynchronously clone a favicon from the Favicon Database to our disk cache for Jump List, and that this can happen off of the main thread, and that we get the path back if it exists or an non-success result code in the event that the favicon is not in the database or some other error occurs.
            - Test 1: Insert a favicon into the favicon database. Ensure that the jump list cache path is empty. Use the obtainAndCacheFaviconAsync method to get its cache path. Ensure that the file exists. Delete the file as clean up.
            - Test 2: Try to get a favicon that we know \_doesn't_ exist in the favicon database, ensure that obtainAndCacheFaviconAsync rejects with a particular result code.
            - Test 3: Obtain and cache the same favicon multiple times should result in use not actually writing a new favicon, but instead returning the path to an existing favicon that has not expired.
            - Test 4: Test expiring a favicon. Artificially change the lastModifiedTime of the file so that it is expired, and ensure that it gets overwritten.
    - Cleanups
        - Add documentation to nsIJumpListBuilder for a new method
    - The patches are a little messy, and could be broken up better <-- "a refactor"
-  Questions:
    - I'm seeing you doing special builds (thunderbird, debug, etc). I'm really curious where and how this is working. How do mach knows what folders/files it needs to use, override (in the case of Thunderbird), etc. I guess I'm intrigued in the build system in general but the question above didn't seem to be covered in the Firefox docs.That could be interesting to have a 5min crash course on that if/when you're stuck waiting for a build to finish :)
        - [mozconfigwrapper](https://pypi.org/project/mozconfigwrapper/)
        - https://firefox-source-docs.mozilla.org/build/buildsystem/mozconfigs.html
        - https://firefox-source-docs.mozilla.org/build/buildsystem/mozbuild-files.html
    - "I wanted follow the STR for the bug 1889455 you created today.  
        But am currently getting this output in my console:  
        buildList failed: NS_ERROR_UNEXPECTED: `WindowsJumpLists.sys.mjs:281:15 buildList resource:///modules/WindowsJumpLists.sys.mjs:281`  
        My assumption is there is a problem with the large number of URIsToRemove i previously specified ""right click jump list, remove from this list""  
        As i don't believe there is a GUI method to undo this list, could you please demonstrate the sqlite command syntax (terminal or powershell) so that it can be cleared for an existing profile and avoid having to create a brand new firefox profile? thanks for the streams"
		- `const { WinTaskbarJumpList } = ChromeUtils.importESModule(
  "resource:///modules/WindowsJumpLists.sys.mjs"
);`
        - `WinTaskbarJumpList.update()`
        

**[Rate this episode](https://forms.gle/wNVrp498YkmsArqd7)**

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