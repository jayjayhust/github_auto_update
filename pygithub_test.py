from github import Github
import time

g = Github()
repo = g.get_repo("jayjayhust/github_auto_update")
print("repo.name:", repo.name)
commits = repo.get_commits(path='libs/test.py')  # 获取单文件的commit信息
print("commits.totalCount:", commits.totalCount)
if commits.totalCount:
    print("commits[0].commit.committer.date:", commits[0].commit.committer.date)  # 形如：2023-09-21 07:06:04
    new_time = time.mktime(time.strptime(str(commits[0].commit.committer.date), "%Y-%m-%d %H:%M:%S")) 
    print("time after convert", new_time)  # 转换成形如：形如：1695279853.7023084

# 从github上下载文件
with open("new/" + 'test.py', 'wb') as f:  # 自动下载得到的文件放置在new文件夹中
    # r.content写入至文件
    f.write(repo.get_contents('./libs/test.py', ref='main').decoded_content)  # https://stackoverflow.com/questions/70678117/python-downloading-a-yaml-file-from-github-using-pygithub-get-contents-and-try

