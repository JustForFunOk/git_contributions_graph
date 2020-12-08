#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from datetime import date  # date
import time
import numpy as np
import re # re.search
import cv2

author_email_list = ['slgsunjian@163.com', 'slgsunjian@gmail.com', 'sunjian4@csvw.com']

tmp_file_name_list = []  # e.g. tmp_xxxxxx@xx.txt

tmp_store_folder = ""

date_string_list = []  # e.g. Date:   2020-04-09



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
    """
    the output format looks like this

    commit 5c6f14ea7a6de77efc4ab120b9d90035xxxx
    Author: xxx <xxxxx@xxx.com>
    Date:   2020-04-09

    commits xxxxx
    """
    os.chdir(git_folder)

    # get author commit and write to *.txt file
    for author_email in author_email_list:
        index = author_email_list.index(author_email)
        os.system("git log --author=%s --date=short > %s" %(author_email, tmp_file_name_list[index]))

def post_process_email():
    """
    remove '.com' postfix
    add 'tmp_' prefix
    """
    for email_addr in author_email_list:
        tmp_file_name = tmp_store_folder  + '/' + 'tmp_' + email_addr[:-4] + '.txt'
        tmp_file_name_list.append(tmp_file_name)
        print("%s >> %s" %(email_addr, tmp_file_name))

def get_date_lines():
    os.chdir(tmp_store_folder)

    for file in os.listdir(tmp_store_folder):
        print("start process %s" %file)
        fo = open(file,"r")
        for line in fo.readlines():
            if line.startswith("Date:"):
                date_string_list.append(line)
        fo.close()
        print("%s processed\n" %file)

def convert_statistic_to_color_level(date_statistic):
    # find the max number
    max_commit_cnt = np.max(date_statistic)

    # divide commits cnt into 4 level and level 0, 5 level in total
    level_step = round(max_commit_cnt / 4.0)
    if level_step < 1 :
        level_step = 1

    statistic_level = date_statistic.copy()
    cnt = 0
    for number in date_statistic:
        if number > 0 and number <= level_step :
            statistic_level[cnt] = 1
        elif number > level_step and number <= 2*level_step :
            statistic_level[cnt] = 2
        elif number > 2*level_step and number <= 3*level_step :
            statistic_level[cnt] = 3
        elif number > 3*level_step :
            statistic_level[cnt] = 4
        cnt += 1
    return statistic_level

def draw_calendar_graph(calendar_array):
    color_level = [[100, 100, 100],  # gray
                   [  0,   0,  60],
                   [  0,   0, 120],
                   [  0,   0, 180],
                   [  0,   0, 240]
                    ]

    # draw round rectangle with color level



def extract_date_info(year):
    # get the total days in one year
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    days_num = (end_date - start_date).days  # e.g. 2020 has 365 days

    date_statistic = np.zeros(days_num, dtype=np.intc)

    for date_string in date_string_list:
        # e.g. Date:   2020-04-09
        date_start_pos = re.search(r"\d", date_string).start()
        date_time = date_string[date_start_pos: -1]  # remove last \n
        date_time_obj = time.strptime(date_time, '%Y-%m-%d')
        # print(date_time_obj[0]) # year
        # print(date_time_obj[1]) # month
        # print(date_time_obj[2]) # day
        # get the day number between to date
        d = date(date_time_obj[0], date_time_obj[1], date_time_obj[2])
        days = (d - start_date).days
        date_statistic[days] += 1

    # including -1, 0, 1, 2, 3, 4
    statistic_level = convert_statistic_to_color_level(date_statistic)

    # add dummy  date
    # get the weekday of xxxx-1-1
    # 0 - monday
    # 5 - saturday
    # 6 - sunday
    weekday_1_1 = start_date.weekday()
    print("weekday_1_1 is %d \n" %weekday_1_1)

    # add prefix
    if weekday_1_1 < 6 :
        prefix_date = np.zeros(weekday_1_1+1, dtype=np.intc)
        for i in range(weekday_1_1+1):
            prefix_date[i] = -1
        tmp_date_statistic = np.append(prefix_date, statistic_level)

    # add postfix
    if np.size(tmp_date_statistic) /7 != 0:
        postfix_num = 7 - np.size(tmp_date_statistic) % 7
        postfix_date = np.zeros(postfix_num, dtype=np.intc)
        for i in range(postfix_num):
            postfix_date[i] = -1
        tmp_date_statistic = np.append(tmp_date_statistic, postfix_date)

    # reshape
    calendar_array =np.reshape(tmp_date_statistic, (-1, 7))

    # 2d array transposition
    calendar_array = np.transpose(calendar_array)
    # the 2D array of 2020 looks like
    '''
          0   1   2   x   x   x   54
    Sun  -1   x
    Mon  -1   x
    Tue  -1
    Wed   0
    Thu   0
    Fri   0
    Sat   0
    '''
    print(calendar_array)

    draw_calendar_graph(calendar_array)



    # init 2D array to store index of days
    # if days_num == 366 and weekday_1_1 == 6:
    #     week_num = 54
    # else :
    #     week_num = 53


    # calendar_array = np.zeros([week_num, 7])  # one week has 7 day

    # tmp_weekday = weekday_1_1
    # tmp_week = 0
    # # i start from 1
    # for i in range(1, days_num+1):
    #     if tmp_weekday > 6:
    #         tmp_week += 1
    #         tmp_weekday = 0
    #     calendar_array[tmp_week, tmp_weekday] = i
    #     tmp_weekday += 1
    #


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
    for git_folder in git_folder_list:
        print("start process [%s]" %git_folder)
        get_author_commits(git_folder)
        print("[%s] process finished\n" %git_folder)

    # process files
    # for every file
    # read file line by line
    # get the line start with 'Date'
    get_date_lines()
    print("get %d commits in total" %len(date_string_list))
    print("0: %s" %date_string_list[0])
    print("------")
    print("%d: %s\n" %(len(date_string_list)-1, date_string_list[len(date_string_list)-1]))

    extract_date_info(2020)



    # get time, paras time
    # from datetime import date
    # d0 = date(2008, 8, 18)
    # d1 = date(2008, 9, 26)
    # delta = d1 - d0
    # print(delta.days)
    # d0.weekday()


    # store times of time to array
    # resize to 2-D array


    # draw image with OpenCV








