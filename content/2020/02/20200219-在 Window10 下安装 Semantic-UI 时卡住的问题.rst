解决在 Window10 下安装 Semantic-UI 时卡住的问题
##################################################################

:date: 2020-02-19 12:00
:author: Kaffa
:category: 随笔
:tags: 随笔, Essays, 技术, Technology, Semantic-UI, nodejs
:slug: install-semantic-ui-on-windows-10
:summary: 本文帮助读者解决在 Windows 10 下安装 Semantic-UI 时，遇到 Creating src/theme.config 卡住的问题。



问题概述
=============

`Semantic-UI`_ 是一种纯前端 UI 的开发包，国内 OSChina 应该是就是用它的。根据官方文档进行起步安装，如果操作系统是 Windows 10 ，可能会在执行 ``npm install semantic-ui --save`` 时卡住。

解决办法
=============

将 nodejs 版本降级到 v10.1.0，旧版本下载地址在：https://nodejs.org/dist/v10.1.0/，如果当前版本是解压安装的，可简单下载解压替换即可。

然后清理一下未完成的 Semantic-UI 安装的文件，再次安装即可解决。

解决办法二
=============

可试试 `Fomantic-UI`_ 。


感谢阅读。

.. _`Semantic-UI`: https://semantic-ui.com/introduction/getting-started.html
.. _`Fomantic-UI`: https://github.com/fomantic/Fomantic-UI
.. _`issues 6641`: https://github.com/Semantic-Org/Semantic-UI/issues/6641
