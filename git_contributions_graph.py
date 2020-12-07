#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

# get all folder path
# including itself floder
# check if exits .git floder
def get_all_floder():
    # change directory to repositories folder
    os.chdir('./repositories')
    cwd = os.getcwd()  # get current directory

    # get all subfolder
    subfolder_list = [os.path.join(cwd, d) for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]

    # filter git folder
    for subfolder in subfolder_list:
        if not '.git' in os.listdir(subfolder):
            subfolder_list.remove(subfolder)  # remove the folder not contain .git folder

    # print the number of repo
    print("<------find %d repositories------>" % len(subfolder_list))
    for subfolder in subfolder_list:
        print(subfolder)

    return subfolder_list


if __name__ == "__main__":
    # get all git folder in repositories folder
    all_git_folder = get_all_floder()





