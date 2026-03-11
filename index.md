---
layout: homepage
---

## The Joy of Coding: Episode Guide

The Joy of Coding is a livehacking stream that I do weekly on Wednesday's at 1PM
ET.

You can find all of the past episodes here on [Air Mozilla][airmo] and search for
Joy of Coding or [YouTube][youtube].

One of my viewers had the brilliant idea of making it possible to have an episode
guide to accompany and complement the "agenda" that I normally lay out
beforehand. This is very similar to how [handmadehero.org][handmadehero]'s
[episode guide][handmadehero-guide] works.

So that's what this is! Still early days, but hopefully we can make this thing
work properly. Or it'll fail miserably, who knows? No plan survives breakfast.

## Search Transcripts

<link href="{{ site.baseurl }}/pagefind/pagefind-ui.css" rel="stylesheet">
<style>
:root {
  --pagefind-ui-primary: #0066cc;
  --pagefind-ui-text: inherit;
  --pagefind-ui-background: inherit;
  --pagefind-ui-border: #ffeb9b;
  --pagefind-ui-tag: #111111;
  --pagefind-ui-border-width: 1px;
  --pagefind-ui-border-radius: 4px;
  --pagefind-ui-image-background: #ffffff;
  --pagefind-ui-image-border: #dddddd;
  --pagefind-ui-font: inherit;
}
.pagefind-ui__search-input::placeholder {
    opacity: 0.7 !important;
}
</style>
<script src="{{ site.baseurl }}/pagefind/pagefind-ui.js"></script>

<div id="search"></div>

<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        new PagefindUI({
            element: "#search",
            showSubResults: true,
            excerptLength: 30,
            baseUrl: "{{ site.baseurl }}"
        });
    });
</script>

[airmo]: https://air.mozilla.org/
[contribute]: CONTRIBUTING.md
[handmadehero]: https://handmadehero.org
[handmadehero-guide]: https://hero.handmade.network/episodes
[youtube]: https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5
