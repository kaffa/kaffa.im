DB Service
##################################################

:date: 2024-07-03 12:00
:author: Kaffa
:category: software
:tags: database, windows-service
:slug: db-service
:summary: DB Service 是为了减少管理数据库时间而写的小脚本，此等工具在 AI 加持下，从以前的可能需要 16 hours，缩短为 2 hours。
:image: /static/img/2024/db-service.png

痛点
==========

本机安装了非常多的数据库服务以供开发和备份，每次需要启动和停止服务，操作比较费时间。

机器很少重装，本机安装过：

- PostgreSQL 9
- PostgreSQL 12
- PostgreSQL 15
- PostgreSQL 16
- MySQL 5.5
- MySQL 5.6
- MySQL 5.7
- MySQL 8.0
- MariaDB 10.2
- MariaDB 10.4
- MariaDB 10.5
- MariaDB 11.4

多个版本的服务中，不同时期的数据服务未作升级，也未迁移到一起。

数据库的趋势从最初的 MySQL 到后续的 MariaDB，现在发展最快的居然是 PostgreSQL，难道是因为菊厂的高斯或者一些 Serverless 用它的多。

OLAP 或者 OLTP 之争由来已久，在使用中体会 PostgreSQL 的复杂度明显高于 MySQL，而 MySQL 也几乎满足中小企业需求，而 PostgreSQL 更适合数据仓库、分析、批量运算，当然，用它作 Web 数据库也足够的，在数据量处于 1000w ~ 2000w 级别，同等数据和优化下，也许它还比 MySQL 更快。

解决
==========

用较少的依赖，在 AI 加持下，几小时自己写了一个管理这些数据库服务的管理器。

类似 Apache httpd 的那个，支持启动、停止、重启、启用、禁用等。

.. image:: /static/img/2024/db-service.png
    :alt: db service manager

Talk is cheap, show me the code: `db_service.py <https://github.com/kaffa/kaffa.im/blob/master/content/code/db_service.py>`_

状态变化后刷新，用处不大，后面有用再说。

确实，AI 帮助我更快的完成了这个工具，大约是十多年前，我使用 C# + WinForm 完成过一个也许更健壮的版本，这次是第二次实现，从以前的 16 hours 缩短为 2 hours，看来只要有经验，在 AI 的加持下，10x 程序员也许不容易得，但 2x 4x 8x 也是不难的。


价值
==========

写成 .cmd 文件，结合 `ALaunch <https://kaffa.im/alaunch-your-first-productivity-software>`_ 的以管理员启动，再配置一个热键，处理效率明显提升。

以前需要::

    ShowDesktop -> 右键点击我的电脑 -> G -> 服务 -> 按键按名称查找服务 -> 右键 -> 操作动作（启动 / 停止 / 重启）

现在简化为::

    快捷键 -> 选中要处理的服务 -> 点按钮操作

