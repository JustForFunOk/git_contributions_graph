# Git Contributions Graph Generator

## Why this project?

use this project your can merge all your git commit contributions(maybe including Github, GitLab, Bitbucket) into one graph.

## How it works

* local repositories
* git log --author=xxxx --all
* opencv draw graph

## Usage


1. clone this repository to `git_contributions_graph` folder
    ``` shell
    git clone git@github.com:JustForFunOk/git_contributions_graph.git
    cd git_contributions_graph/
    ```

1. copy (or create link) all your repositories to `git_contributions_graph/repositories/` folder

1. input all your email address to `author_email_list`  in git_contributions_graph.py line 11

1. change `dest_year` in line 12

1. run scripts
    ``` shell
    ./git_contributions_graph.py
    ```

1. save image using `save` button

1. press `Esc` to exit