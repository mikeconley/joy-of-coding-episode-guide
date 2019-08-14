## How to Contribute

### Getting Started

1. If you don't already have a GitHub account, head over to
   [their website][gh] to create one.
2. [Create a fork and clone a copy][fork]

If you're new to Git, here's some resources to help you:

* https://learngitbranching.js.org/
* https://github.com/jlord/git-it-electron#what-to-install

### Add a new episode

0. Go to your project directory

   ```
   cd /path/to/joy-of-coding-episode-guide
   ```
0. Update your master branch
   
   ```
   git pull upstream master
   ```
0. Create a new branch (e.g add-episode-1234)

   ```
   git checkout -b add-episode-1234
   ```
0. Create a new folder in the `_episodes` folder. The name of your folder should
   be composed of 4 digits (e.g 1234 for the episode 1234).
0. Create an `index.md` file inside your newly created folder.
0. Copy and paste the following template inside the `index.md` file.

   ```
   ---
   layout: default
   date: YYYY-MM-DD
   number: 1234
   ---
   
   ## Episode 1234: MMM DD, YYYY

   ### Links
   
   ### Topics
   
   ### Other
   ```
0. Edit your `index.md` as needed. You can look other episodes' files to see an
   example.
0. Save your changes to your fork
   
   ```
   git add 1234
   git commit -m "add episode 1234
   git push origin add-episode-1234
   ```
0. [Open a Pull Request][pr] and wait for Mike to merge it.

### Run a copy of the website locally

0. [Install Jekyll][jekyll-doc]
0. Go to your project directory

   ```
   cd /path/to/joy-of-coding-episode-guide
   ```
0. Install the dependencies 

   ```
   bundle install --path vendor/bundle
   ```
0. Run Jekyll

   ```
   bundle exec jekyll serve
   ```

[fork]: https://help.github.com/en/articles/fork-a-repo
[gh]: https://github.com
[jekyll-doc]: https://jekyllrb.com/docs/
[pr]: https://help.github.com/en/articles/creating-a-pull-request-from-a-fork
