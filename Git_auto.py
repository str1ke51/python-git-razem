#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:33:08 2022

@author: MyszekAI
"""
import os
import sys

arvg = sys.argv[1:]

if  len(arvg) == 3:
    url_git_repo = arvg[0].replace("https://", "")
    username     = arvg[1]
    token        = arvg[2]
    
elif len(arvg) == 1:
    if arvg[0].lower() in ("help","-h","--help",'pomoc'):
        print("pomoc")
    
       
print(f"\n{'url:':<7}",url_git_repo)
print("-"*(len(url_git_repo)+8))
print(f"{'user:':<7}",username)
print("-"*(len(username)+8))
print(f"{'token:':<7}",token)
print("-"*(len(token)+8))






# url_git_repo = 'https://github.com/MyszekAI/desktop-tutorial.git'.replace("https://", "")
# username     = "MyszekAI"
# token        = "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"

line_number = 0
with open(os.path.expanduser(".git/config"),"r") as config:
    list_line = list(config)
    
    for i in range(0,len(list_line)):
        if "\turl = " in list_line[i]:
            line_number = i

list_line[line_number] = f"\turl = https://{username}:{token}@{url_git_repo}"

os.system("rm -f .git/config")
with open(os.path.expanduser(".git/config"),"a") as config_save:
    
    for j in range(0,len(list_line)):
        if list_line[j] != "\n":
            print(list_line[j].replace("\n",""),file=config_save)
