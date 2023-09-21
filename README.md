# 监测github项目自动更新

## 参考文章
- Python监控Github项目更新并自动下载：https://mp.weixin.qq.com/s/6TpCFPbd-Uqwo9TovblH5w
- Github API: https://docs.github.com/en/rest?apiVersion=2022-11-28
- 从Github存储库上次更新文件时获取：https://qa.1r1g.com/sf/ask/3513596901/
- PyGithub: https://github.com/PyGithub/PyGithub

## 测试流程
- 建立两个项目，一个做老项目，一个做新项目
- 在老项目下，在libs文件夹下放入old文件
- 在新项目下，在libs文件夹下对old文件进行修改并提交修改，commit到github
- 在老项目下，运行supervisor.py
- 观察老项目下，是否将github项目的libs文件夹下新文件拉取了下来存到了new文件夹