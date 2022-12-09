###################################
为 GitHub Pages 站点添加独立域名
###################################

:date: 2018-06-19 17:17
:author: Kaffa
:category: 日志
:tags: 随笔, Essays, 博客, Blog, 自定义域名, Technology, Custom Domain, GitHub Pages, CNAME
:slug: custom-domain-of-github-pages-site
:summary: 本文记录为 GitHub Pages 站点添加独立域名的步骤和遇到的问题

添加独立域名的步骤
===================

1. 注册一个域名

选择你喜欢的域名商注册一个域名。
例如，我注册的是 kaffa.im

2. 域名解析

在域名配置中添加一条 CNAME 记录。
例如，将 kaffa.im 指向 kaffa.github.io，此时，访问 kaffa.im 会得到 Github 反馈的 404 错误页面

3. 添加 CNAME 文件

在 Github 仓库 master 的根目录下添加一个名称为 **CNAME** 的文件，文件内容为你注册的域名。
例如，在 kaffa.github.io 仓库 master 的根目录新建一个 `CNAME`_ 文件，文件内容为 kaffa.im，刷新刚才的 404 页面即打开了原先的 kaffa.github.io 站点


感谢阅读。

.. _CNAME: https://github.com/kaffa/kaffa.github.io/blob/master/CNAME


