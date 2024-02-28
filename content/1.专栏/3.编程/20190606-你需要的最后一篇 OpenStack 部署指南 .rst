悟了，你所需要的最后一篇部署指南
##################################################################

:date: 2019-06-06 12:00
:modified: 2024-02-28 12:00
:author: Kaffa
:category: programming
:tags: Installation and Deployment Guide, OpenStack
:slug: the-last-installation-and-deployment-guide-you-need
:summary: 这篇是在约5年前我在朋友的公司为客户部署一套 OpenStack 时的笔记，五年后，我在修改中删除了 80% 内容，这就是技术文档。
:image: /static/img/2024/markus-winkler-92HqQ0ZvKDA-unsplash.png

图片版权备注
==================================================

.. raw:: html

    Photo by <a href="https://unsplash.com/@markuswinkler?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Markus Winkler</a> on <a href="https://unsplash.com/photos/white-paper-on-brown-folder-beside-silver-key-92HqQ0ZvKDA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

题记
==============================

|    如果你爱一个人，送他去部署 OpenStack，因为那里是天堂；
|    如果你恨一个人，送他去部署 OpenStack，因为那里是地狱。

.. image:: https://kaffa.im/img/2019/openstack-logo.png
    :alt: OpenStack

OpenStack 是在一个「帐篷」下的相互协同的开源软件组合。

如果你成功的部署并使用它，则可以赋予你私有云的管理能力。

如果你用尽各种办法部署 OpenStack，遇到了各种障碍，还没放弃搜索，那我希望你搜索到此篇。

我将在此篇传授你『万物部署指南』，the last guides you need.

说「最后一篇」的底气是什么？
==============================

:strike:`因为这个部署方式是相当清晰的、各个击破的、非常详尽的，它记录了每一个步骤，经过了反复测试，甚至修正了官方部署中的瑕疵。所以敢说：按此部署，一定成功。`

.. role:: strike
    :class: strike

如果你没有成功，\ :strike:`还可在本文回复留言，我会来答疑，`\ 请继续阅读。

OpenStack 部署步骤
==============================

.. image:: https://kaffa.im/img/2024/openstack-installation.png
    :alt: OpenStack 2023.2


目的和范围
------------------------------

本节讲述 OpenStack 次新版 Rocky 在 CentOS 上的最小化多节点部署过程。

部署完成后经优化，即可用于生产。

在 CentOS 上部署 OpenStack，可选途径有多种，你会看到不同的做法，但不经过测试，你并不知道哪一种可以成功。

次新版 Rocky 已历时考验，软硬件环境，所有的程序、数据库、配置、都是确定的。

提示：部署过程细节非常多，分清节点的同时，还有很多初看类似之处，但细节不同，需谨慎细心。


:strike:`知识准备`
------------------------------

（以下删除 1000 字）

:strike:`硬件准备`
------------------------------

（以下删除 2000 字）

:strike:`环境部署`
------------------------------

（以下删除 3000 字）

:strike:`软件部署`
------------------------------

（以下删除 6000 字）

如果你认真的，正在部署 OpenStack，请看完下段内容离开这里：

- DevStack：官方文档，经过了20多个版本，已经相当完善，必读。
- RDOProject Packstack：相对最容易，耗时最少，用于验证为目的。
- RDOProject TripleO Quickstart：复杂，文档也不够好，没有人可以一次成功。
- kolla-ansible：容器部署简化了部署，但减低了可调试性，如果你想定制一下，你将面对一个复杂性陷阱。

\ **上面的时效已过，最佳途径请\ `跳转官方 <https://docs.openstack.org/2023.2/install/>`_\ 。**\

痛点：OpenStack 为啥安装不好
====================================================

为什么你遵循的 OpenStack 指南，无法真正让你安装好 OpenStack，因为它们：

* 没教你准备硬件
* 缺少软硬件环境说明
* 未标注软件前置依赖
* 未指明软件版本
* 运行命令没指明运行目录
* 运行命令未记录必要的回显
* 没有指明命令运行的节点

:strike:`本文这些都做了，所以会有些长。但我进行分节和编号，你随时可以知道你进行到了哪里。`

2024年2月28日，呕心沥血的权威「安装指南」，为什么失效了？
============================================================

Because of 刻舟求剑。

软件有生命周期，软件文档是一种正在生长的生命。

OpenStack 版本按 26 个字母进化（如今已不够用，换成了年份）。

书籍写作者部署时，按其中的某个版本教授。

书付梓时，软件已然又 build 了 1000 次，bug fix 500 次。

作者在卖的书上写着：「后生，你的疑问请书上见。」你以为部署成功就在书看完后。

实际上你会发现你继续在失败，还得网上最新文档见。

这就是技术写作和出版的痛点。通用的，不好写；时效有限的，不好卖。

步骤流程没有想象的重要，重要的是避坑指南和经验。

这就是 OpenStack 的多种部署看起来都那么不聪明的样子，像极了盲人摸象。

验证式部署、单节点部署、大规模部署、容器式部署？

都是鸡肋。不是想的太简单，就是做的太复杂。

万物部署指南
==========================

看到此的，我想说的是，也许真有『万物部署指南』一样的法宝：

1. 法宝一：一手文档。永远优先使用官方文档，如果官方文档出错，则推进官方改正，若不能改，请改换软件。
2. 法宝二：自知之明。跟随官方文档不奏效的原因，80% 概率是由于，思维和知识中至少其一不到位。

没啥能多说的，唯有多踩坑，到后面会悟了，笨方法就是大智慧。



.. image:: https://kaffa.im/img/reward.png
    :alt: 谢谢心累的你，您请随意~

末了，如果你觉得本文还算有点用，:strike:`别`\ 扫我的赞赏码


