---
date: 2022-02-09
number: 278
airmozilla: https://mzl.la/joy-of-coding-2022-02-09
agenda: https://mikeconley.ca/joc/agendas/Episode-0278.html
rating: https://forms.gle/xnGneA1xnB2uM5u46
---

## Topics

- How to debug Firefox's native code on macOS (lldb), then Linux (gdb), then Windows (Visual Studio)!
  - Optimized builds, unoptimized / debug builds, artifact builds
    - Why can't we do native code debugging of artifact builds?
      - [Configure Build Options](https://firefox-source-docs.mozilla.org/setup/configuring_build_options.html)
  - Attaching to a running instance of Firefox
    - https://lldb.llvm.org/use/map.html
    - MOZ_DEBUG_CHILD_PROCESS=1
    - https://rr-project.org/
    - https://pernos.co/
    - Attaching to the parent process
      - Windows: The Launcher Process
        - https://bugzilla.mozilla.org/showbug.cgi?id=1495040
        - MOZ_DEBUG_BROWSERPAUSE=15
    - Attaching to the content process
