## 1st time, do : 
Create github account via browser and http://www.github.com

Fork mikes repo from https://github.com/mikeconley/joy-of-coding-episode-guide

When you are in your Forked copy, press the Clone or download green button on github.
Press Use SSH and copy the git@ url

Clone main repo 
$ git clone git@github.com:<user>/joy-of-coding-episode-guide.git

Change into new project directory
$ cd joy-of-coding-episode-guide

Connect your local repo to the upstream repo
$ git remote add upstream git@github.com:mikeconley/joy-of-coding-episode-guide.git

Checkout the Master branch
$ git checkout master

$ git pull upstream master && git push origin master

 
## Every other time, do :_

Change to the project directory
$ cd joy-of-coding-episode-guide

$ git pull origin master

$ git pull upstream master

Create a new branch named like episode1234
$ git checkout -b episodeBranch

# Do work...

Add the newly created folder and README.md file, and then update the index.
$ git add episode-0123

Commit the changes
$ git commit -m 'new episodes'

Push your commit to the remote master branch
$  git push -u origin episodeBranch

In your browser, visit https://github.com/mikeconley/joy-of-coding-episode-guide
Press Compare & pull request

