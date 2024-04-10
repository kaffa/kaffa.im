Caffeine
##################################################

:date: 2024-04-10 13:00
:author: Kaffa
:category: software
:tags: tiddlywiki
:slug: caffeine
:summary: Caffeine 能帮助你更快使用 tiddlywiki 单文件保存方案。
:image: /static/img/caffeine.svg


痛点
==========

进入数字花园的软件选型，我选择跟随，当我面前有 tiddlywiki 资深用户 Leslie 的数字花园\ `MemEx <https://note.justgoidea.com/>`_\ 和仓颉哥数字花园\ `仿生猫不会梦见电子猫粮 <https://jefftay.com/>`_\ 作为例子时，这块是作为 KN 的一个发布目标，所以需要先亲自实践。

论 tiddlywiki 持久化方案，唯免费香，我选择单文件和 GitHub 托管，它的工作流是：

1. 打开网址 https://coffees.app/ ，编写条目，完成编写条目时，点击保存，一个名为 tiddlywiki.html 的文件会被保存到当前用户的下载目录中。
2. 将 tiddlywiki.html 复制到本地 github 目录中覆盖 index.html。
3. 提交目录到 github。

此处的痛点是，每次都做类似的事挺麻烦。

Caffeine
====================

我编写了一个脚本用来处理这种无聊的操作，简化了流程。

说明
--------------------

本软件适用于 Windows 下使用 TiddlyWiki Single File + Github Pages 使用。它与 aio.cmd 一起使用实现写作保存后自动推送 GitHub。

使用方法
--------------------

在保存 TiddlyWiki 条目之前，先打开命令行，进入 TiddlyWiki 目录，再运行脚本 `caffeine.py`。例如：

::

    cd /d d:/your-tiddlywiki-folder/
    python caffeine.py

默认路径
--------------------

下载目录是浏览器下载目录，也可以通过命令行参数在运行时指定：

::

    python caffeine.py /path-to-your-downloaded-tiddlywiki.html-file


macOS
--------------------

它很容易移植到 macOS 因为它使用 watchdog。



其余的也不用多说了，`源码 <https://github.com/kaffa/coffees/blob/main/caffeine.py>`_ 面前，了无秘密，我在 Windows 上编写的，但其实非常容易也移植到 macOS 使用。