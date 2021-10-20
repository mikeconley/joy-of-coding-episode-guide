---
layout: default
date: 2021-09-29
number: 264
---

# Episode 264: Sep 29th, 2021

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2021-09-29)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0264.html)

## Topics
* [Fixing a security bug blog](https://blog.mozilla.org/attack-and-defense/2021/09/29/fixing-a-security-bug-by-changing-a-function-signature/)
* Let's talk about BrowsingContexts! And DocShells!
  - [Site Isolation Architecture in Firefox](https://hacks.mozilla.org/2021/05/introducing-firefox-new-site-isolation-security-architecture/)
    - Goes into detail about Meltdown / Spectre vulnerabilities
* No episode next week due to unavoidable meetings. Sorry!
* Special shout out to "shittyskydiver" on YouTube
* Question time!
  - Yes I really get confused like how build system work. How they create binaries. And How do cpp gets build? The Firefox source seems to be a bit esoteric. It would be helpful like how jar.mn moz.build etc integrates together. Thanks.
    - moz.build are Python instructions that build dependency graphs that ultimately get fed into something like Makefile, and then we do a thing like `make`. moz.build helps define what gets packaged in omni.ja ("resources", JSMs)
    - jar.mn, which goes into more detail on HTML, XUL, CSS, JS what gets packaged in omni.ja
      - Go find your Firefox install folder
      - Find omni.ja
      - Copy it somewhere else on the file system (this is important - don't do the next step inside of the Firefox install folder)
      - Rename omni.ja to omni.zip
      - Unzip the file
  - Can you talk a bit about the history of the intro/outro jingle?
    - Jingle was written by my friend Barn, who is also the lead singer of my band - - [The Johnson Report bandcamp](https://thejohnsonreport.bandcamp.com/) - [Music videos](https://www.youtube.com/user/TheJohnsonReport) - [Barn's channel](https://www.youtube.com/user/HermitTheFraud/videos)
    - I had asked Barn for something like the hook from the song "[She Says What She Means](https://www.youtube.com/watch?v=fg3XlAgHpaI)" by the band Sloan
  - When you mentor someone, what does the process look like?
    - What does the mentee need? Some of them just need help getting started and finding work, getting set up.
    - Sometimes a person wants deeper insight into how things work, I can do one-on-ones explaining things, or might do a video or presentation about it
    - Career stuff. What does the person want out of their career? What is the shortest most practical line we can draw to get them there, and then let's put together a plan to get them on that line, and figure out how to measure how they're progressing.
  - If you had an extra hour of time each day, what would you spend it on? (What are some things you wish you had more time for?))
    - Reading
    - If I had a block of 3 hours every day to do whatever I wanted that didn't include maintenance things like doing laundry or taking care of the yard or cooking or cleaning... I would probably get better at drawing and painting using my new drawing tool... and maybe cartooning, and maybe I'd work on designing a point and click adventure game.
  - Have you ever considered switching to linux (eg. arch, etc. ?) - have you ever daily-driven some linux distro?
    - Knoppix was my first introduction to Linux (booted off of a CD)
    - Fedora
    - Ubuntu

* [Rate this episode](https://forms.gle/ninYYnQ6tc4KDc6U6)

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

