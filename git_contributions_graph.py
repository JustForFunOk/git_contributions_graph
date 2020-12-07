#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

author_email_list = ['slgsunjian@163.com', 'slgsunjian@gmail.com', 'sunjian4@csvw.com']

post_process_author_email_list = []

tmp_store_folder = ""

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
    print("<------end of repositories------>\n")

    return subfolder_list


def get_author_commits(repo_path):
    os.chdir(git_folder)

    # get author commit write to *.txt file
    # for author_email in author_email_list:
    #     os.system("git log --author=%s --date=short > " %author_email %)

def post_process_email():
    """
    remove '.com' postfix
    add 'tmp_' prefix
    """
    for email_addr in author_email_list:
        tmp_email_addr = 'tmp_' + email_addr[:-4]
        post_process_author_email_list.append(tmp_email_addr)
        print("%s >> %s" %(email_addr, tmp_email_addr))


if __name__ == "__main__":
    # init
    # init the position of tmp file
    cwd = os.getcwd()
    tmp_store_folder = os.path.join(cwd, 'tmp')
    print("tmp file store in [%s] \n" %tmp_store_folder)

    # deal with email format to store file with email filename
    print("<------start process email address------>")
    post_process_email()
    print("<------process email address finished------>\n")

    # get all git folder in repositories folder
    git_folder_list = get_all_floder()

    # deal with every repository
    all_commits_list = []
    # for git_folder in git_folder_list:
        # print("\nstart process [%s]" %git_folder)
        # get_author_commits(git_folder)
        # print("[%s] process finished\n" %git_folder)

    print(all_commits_list)




