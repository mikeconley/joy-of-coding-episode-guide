---
layout: default
date: 2024-04-10
number: 362
---

# Episode 362: Apr 10th, 2024

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2024-04-10)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0362.html)

## Topics
* WindowsJumpList favicon stuff!
  - We need tests
    - We have added a new method called obtainAndCacheFaviconAsync on nsIJumpListBuilder
    - The expectation is that we should be able to use this method to asynchronously clone a favicon from the Favicon Database to our disk cache for Jump List, and that this can happen off of the main thread, and that we get the path back if it exists or an non-success result code in the event that the favicon is not in the database or some other error occurs.
      - Test 1: Insert a favicon into the favicon database. Ensure that the jump list cache path is empty. Use the obtainAndCacheFaviconAsync method to get its cache path. Ensure that the file exists. Delete the file as clean up.
      - Test 2: Try to get a favicon that we know _doesn't_ exist in the favicon database, ensure that obtainAndCacheFaviconAsync rejects with a particular result code.
      - Test 3: Obtain and cache the same favicon multiple times should result in use not actually writing a new favicon, but instead returning the path to an existing favicon that has not expired.
      - Test 4: Test expiring a favicon. Artificially change the lastModifiedTime of the file so that it is expired, and ensure that it gets overwritten.
    - Cleanups
      - Add documentation to nsIJumpListBuilder for a new method
    - The patches are a little messy, and could be broken up better <-- "a refactor"

* Questions:
  - I'm seeing you doing special builds (thunderbird, debug, etc). I'm really curious where and how this is working. How do mach knows what folders/files it needs to use, override (in the case of Thunderbird), etc. I guess I'm intrigued in the build system in general but the question above didn't seem to be covered in the Firefox docs.That could be interesting to have a 5min crash course on that if/when you're stuck waiting for a build to finish :)
    - [mozconfigwrapper](https://pypi.org/project/mozconfigwrapper/)
    - https://firefox-source-docs.mozilla.org/build/buildsystem/mozconfigs.html
    - https://firefox-source-docs.mozilla.org/build/buildsystem/mozbuild-files.html
  - "I wanted follow the STR for the bug 1889455 you created today.
    But am currently getting this output in my console:
    buildList failed: NSERRORUNEXPECTED: WindowsJumpLists.sys.mjs:281:15 buildList resource:///modules/WindowsJumpLists.sys.mjs:281
    My assumption is there is a problem with the large number of URIsToRemove i previously specified ""right click jump list, remove from this list""
    As i don't believe there is a GUI method to undo this list, could you please demonstrate the sqlite command syntax (terminal or powershell) so that it can be cleared for an existing profile and avoid having to create a brand new firefox profile? thanks for the streams"
    - const { WinTaskbarJumpList } = ChromeUtils.importESModule( "resource:///modules/WindowsJumpLists.sys.mjs" );
    - WinTaskbarJumpList.update()

* [Rate this episode](https://forms.gle/wNVrp498YkmsArqd7)

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

