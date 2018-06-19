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

#### 4、启动本地服务
进入项目根目录，执行命令：

```python manage.py runserver```

## 目录大纲
01.什么是Django
	- Django是Python Web框架
	- Django的特点
	- 安装Python3
	- 安装Django2.0 

02.入门仪式：Hello World
	- 创建Django项目
	- 在网页打出"Hello, world"
	- 初步介绍urls路由
	- 创建超级管理员，进入后台管理界面
    
(完善中...)

## 注意
我后面会继续把其他代码和说明补充完整。
admin后台用户名是ysh，密码是test123456
