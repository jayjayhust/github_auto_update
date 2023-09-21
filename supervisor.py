import requests
import time
import os

api_url = "https://api.github.com/repos/%s"
download_url = "https://github.com/%s/archive/master.zip"

def get_FileModifyTime(path):
    d = {}  # 字典
    files= os.listdir(path)
    # 得到文件夹下的所有文件名称
    s = []  # list
    for file in files:
        # 遍历文件夹
        t = os.path.getmtime(path + file)
        d[file] = t
    return d

import requests
import time
def is_old(old_time, name):
    # name：xxx/xxx
    all_info = requests.get(api_url % name).json()
    new_time = time.mktime(time.strptime(all_info["updated_at"], "%Y-%m-%dT%H:%M:%SZ"))
    if not old_time:
        old_time = all_info["updated_at"]
    print(new_time, old_time)
    if new_time > old_time:
        old_time = new_time
        return True
    else:
        return False

import requests
def download_newfile(name):
    # name：xxx/xxx
    r = requests.get(download_url % name) 
    # 请求链接后保存到变量r中
    name = name.replace('/', '_') + '.zip'
    with open("new/" + name, 'wb') as f:  # 自动下载得到的文件放置在new文件夹中
        # r.content写入至文件
        f.write(r.content)

files = get_FileModifyTime('./libs/')  # 获取./libs文件夹下的所有文件信息（字典格式）
for i in files:
    print(i, files[i])
    name = i.split('.')[0].replace('_', '/')  # 
    old = is_old(files[i], name)
    if old:
        download_newfile(name)