# Django2.0视频教程的代码
![Python3.x](https://img.shields.io/badge/Python-3.x-519dd9.svg)
![Django2.x](https://img.shields.io/badge/Django-2.x-519dd9.svg)

**版权声明：该套教程版权是作者（杨仕航）所有，侵权必究。这套教程我没有在淘宝等任何地方售卖。**

该git项目是Django2.0视频教程对应每节课的代码。为了查看方便，对应章节代码在对应文件夹中。<br>
Django2.0视频教程地址：https://space.bilibili.com/252028233/#/channel/detail?cid=28138

## 如何使用
该git项目主要是提供一个可对照的代码给大家。每个文件夹对应每节课的代码。<br>
大家自己一定要先把代码敲一遍，消化理解，以加深印象。

#### 1、Python
Django是Python的一种web框架，需要Python才可使用。<br>
本教程使用Python3.6的版本录制，建议使用Python3.x最新版本。<br>
可打开[Python官网](https://www.python.org/downloads/)下载并安装。

#### 2、虚拟环境
本课程用virtualenv，你也可以使用其他虚拟环境管理Python库。

#### 3、一键安装库（包含Django）
每次课的代码文件夹都有一个requirments.txt文件。该文件是记录所使用库的信息。可利用该文件直接一键安装所有库。<br>
启动虚拟环境之后（若有使用虚拟环境的的话），进入requirments.txt所在的目录，执行命令：<br>
```pip install -r requirements.txt```

#### 4、从第21节开始需要创建缓存表
从“第21节 热门阅读博客排行及缓存提速”开始使用到缓存功能，需要执行命令：```python manage.py createcachetable``` 创建缓存表。<br>
若没有执行该命令，可能会出现**“no such table: my_cache_table”**的错误。

#### 5、从第36节开始使用MySQL数据库，需要安装的mysqlclient库
由于从第36节开始使用MySQL数据库，需要的mysqlclient库先用pip install mysqlclient安装。不行的话，打开[https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)下载mysqlclient的whl包，再用pip安装这个whl包。

#### 6、启动本地服务
进入项目根目录，执行命令：```python manage.py runserver```<br>
<b>admin后台用户名是ysh，密码是test123456</b>

## 教程目录
### 第1部分 Django基本认识
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

### 第3部分 学习更丰富的知识
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
    
### 第5部分 提升用户体验
    42.阶段性总结和后续开发
    43.用QQ登录到我们的网站
    44.站内消息通知
    45.站内简单搜索
    46.完结，新的开始

### 番外篇
    番外篇：在pythonanywhere部署Django
    番外篇：在Windows部署Django
    番外篇：外键那些事儿
    番外篇：Django admin全面汉化

## 交流
**学习交流QQ群：701914136**<br>
**公众号：再敲一行代码**<br>
![image](https://github.com/HaddyYang/django2.0-course/blob/master/weixin_mp_qrcode.jpg)

## 助学云
助学云是我一个粉丝创建，专门为学习时候的我们提供实惠的云服务器。他理念打动了我。<br/>
![理念和价值](https://zqyhdm.com/static/zhuxuecloud_wx.png)<br/>
![助学云QQ群：921547003](https://zqyhdm.com/static/zhuxuecloud.png)<br/>
助学云的服务器（最低配置）我试用过，质量不错。
