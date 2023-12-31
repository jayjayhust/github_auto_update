import requests
import time
import os
from datetime import datetime, timedelta

from github import Github
g = Github()
repo = g.get_repo("jayjayhust/github_auto_update")
print("repo.name:", repo.name)
commits = repo.get_commits(path='libs/test.py')  # 获取单文件的commit信息
print("commits.totalCount:", commits.totalCount)
if commits.totalCount:
    print("commits[0].commit.committer.date:", commits[0].commit.committer.date + timedelta(hours=8))  # 形如：2023-09-21 07:06:04

# https://github.com/facebookresearch/fastText的api地址为：https://api.github.com/repos/facebookresearch/fastText
api_url = "https://api.github.com/repos/jayjayhust/github_auto_update/%s"  # https://api.github.com/repos/用户名/库名
download_url = "https://github.com/%s/archive/master.zip"

def get_FileModifyTime(path):
    d = {}  # 字典
    files= os.listdir(path)
    # 得到文件夹下的所有文件名称
    s = []  # list
    for file in files:
        # 遍历文件夹
        t = os.path.getmtime(path + file)  # 获取时间，形如：1695279853.7023084
        d[file] = t
    return d

import requests
import time
def is_old(old_time, name):
    l_commits = repo.get_commits(path = 'libs/' + name)  # 获取单文件的commit信息
    if l_commits.totalCount:
        # 获取文件单文件最后的commit的时间信息
        l_new_time = time.mktime(time.strptime(str(l_commits[l_commits.totalCount - 1].commit.committer.date + timedelta(hours=8)), "%Y-%m-%d %H:%M:%S"))
        if l_new_time > old_time:  # github仓库的更新时间大于本地时间（要考虑时差，本地是北京时间，github是格林尼治时间？）
            old_time = l_new_time
            return True
        else:
            return False

import requests
def download_newfile(name):
    # 请求链接后保存到变量r中
    with open("new/" + name, 'wb') as f:  # 自动下载得到的文件放置在new文件夹中
        # r.content写入至文件
        f.write(repo.get_contents('./libs/' + name, ref='main').decoded_content)

files = get_FileModifyTime('./libs/')  # 获取./libs文件夹下的所有文件信息（字典格式：文件与更新时间键值对）
# 遍历所有文件，检测是否有新文件
for i in files:
    print(i, files[i])
    # name = i.split('.')[0].replace('_', '/')  # 
    old = is_old(files[i], i)
    if old:
        download_newfile(i)  # 从github上下载文件