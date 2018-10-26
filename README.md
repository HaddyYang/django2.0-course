# Django2.0视频教程的代码
![Python](https://img.shields.io/badge/Python-3.x-519dd9.svg)
![Django](https://img.shields.io/badge/Django-2.x-519dd9.svg)

该git项目是Django2.0视频教程对应章节的代码，为了查看方便，对应章节代码在对应文件夹中。

Django2.0视频教程地址：https://space.bilibili.com/252028233/#/channel/detail?cid=28138

## 如何使用
该git项目主要是提供一个可对照的代码给大家。大家一定要先照着视频把代码敲一遍，以加深印象。

每个文件夹对应每节课的代码。

#### 1、Python
Django是Python的一种web框架，需要Python才可使用。本教程使用Python3.6的版本录制，建议使用Python3.x最新版本。可打开[Python官网](https://www.python.org/downloads/)下载并安装。

#### 2、虚拟环境
本课程用virtualenv，你也可以使用其他虚拟环境管理Python库。

#### 3、一键安装库
每次课的代码文件夹都有一个requirments.txt文件。该文件是记录所使用库的信息。可利用该文件直接一键安装所有库。

启动虚拟环境之后（若有使用虚拟环境的的话），进入requirments.txt所在的目录，执行命令：

```pip install -r requirements.txt```

#### 4、第36节需要安装的mysqlclient库
第36节需要的mysqlclient库先用pip install mysqlclient安装。不行的话，打开[https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)下载mysqlclient的whl包，再用pip安装这个whl包。

#### 5、启动本地服务
进入项目根目录，执行命令：```python manage.py runserver```


## 教程目录
### 第1部分 Django基础
    01.什么是Django
    02.入门仪式：Hello World
    03.Django基本应用结构
    04.使用模版显示内容
    05.定制后台和修改模型


### 第2部分 以实际项目带动学习
    06.开始完整制作网站
    07.构建个人博客网站
    08.常用的模版标签和过滤器
    09.模版嵌套
    10.使用CSS美化页面
    11.CSS框架协助前端布局
    12.Bootstrap响应式布局
    13.分页和shell命令行模式
    14.优化分页展示
    15.上下篇博客和按月分类
    16.博客分类统计
    17.博客后台富文本编辑


### 第3部分 Django进阶内容
    18.博客阅读简单计数
    19.博客阅读计数优化
    20.阅读计数统计和显示
    21.热门阅读博客排行及缓存提速
    22.评论功能设计和用户登录
    23.html表单提交评论
    24.使用Django Form表单
    25.富文本编辑和ajax提交评论
    26.回复功能设计和树结构
    27.获取评论数和细节处理
    28.用所学知识实现点赞功能
    29.完善点赞功能
    30.导航栏添加用户操作
    31.自定义用户模型
    32.修改用户信息
    33.发挥邮箱作用
    34.评论发送邮件通知


### 第4部分 网站部署
    35.部署准备（一）：Git
    36.部署准备（二）：MySQL
    37.部署准备（三）：服务器
    38.用Apache+mod_wsgi部署
    39.用Nginx+uWSGI部署
    40.部署配置清单
    41.域名、备案和https
    (未完待续...)

## 注意
我后面会继续把其他代码和说明补充完整。
其中，第5节到第17节之前的代码我没有保留，我正在重新补上中 :)

admin后台用户名是ysh，密码是test123456
