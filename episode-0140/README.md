# Episode 140: May 23th, 2018

## Links
* [Watch this episode on air mozilla](https://air.mozilla.org/the-joy-of-coding-episode-140/)
* [Evernote Agenda](https://www.evernote.com/l/AbIWbCcjmGVEBahV0XAzixQhYuOz13rtjf8)
* [Adso!](https://github.com/mikeconley/joy-of-coding-episode-guide/tree/master/utils/adso) Want to help me out? Please help correct transcriptions of episodes at [Amara](https://amara.org)
    * [Here is a spreadsheet](https://docs.google.com/spreadsheets/d/1LiDWBkZ762LZQDYyFPmiXEGCJLT7cnLiAh3inehjdWc/edit#gid=0) with current auto-transcription state

## Topics

* Updated: [Bug 1176019](https://bugzilla.mozilla.org/show_bug.cgi?id=1176019) - [e10s] Keep around the layer tree for tabs on a LRU basis
    * This landed! And will hopefully make things faster!
* [Bug 1458375](https://bugzilla.mozilla.org/show_bug.cgi?id=1458375) - Remove empty binding & investigate the performance gain caused by it
    * Still an issue, perf tried locally
* [Bug 1457276](https://bugzilla.mozilla.org/show_bug.cgi?id=1457276) - TabChild::RecvRenderLayers often results in two consecutive paints
    * Maybe make use of dthayer’s work?
