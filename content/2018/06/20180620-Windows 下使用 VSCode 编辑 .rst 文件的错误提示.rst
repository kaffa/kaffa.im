##################################################
Windows 下使用 VSCode 编辑 \*.rst 文件的错误提示
##################################################

:date: 2018-06-20 02:52
:author: Kaffa
:category: 随笔
:tags: 随笔, Essays, 技术, Technology, VSCode, reStructuredText, rst
:slug: vscode-restructuredtext
:summary: 本文提供消除 Windows 下使用 VSCode 编辑 \*.rst 文件的错误提示的方法

问题出现的场景
===================

1. 使用 VSCode 编辑 \*.rst 文件时，会提示安装 doc8 ，于是使用 pip 安装 doc8，执行::

    pip install doc8

2. 重新打开文件，全文会出现两条警告 D002 和 D004，如下::

    'D002 Trailing whitespace'
    'D004 Found literal carriage return'

D002 信息按字面意思是行尾有空格，稍作思考，感觉可能和 Windows 的换行符 CRLF 有关，
于是点击 VSCode 状态栏，修改 ``CRLF`` 为 ``LF``，之后错误提示消失。请参考：issues-84_

3. 又产生新的警告 D001，如下::

    'D001 Line Too Long'

在 issues-83_ 中给的解决方法是，在 VSCode 的用户配置中提供一个更大的行宽度值。
于是 ``Ctrl + P``，选择 ``Preferences: Open Settings``，在 ``User Settings`` 标签页，
也就是 ``C:\Users\username\AppData\Roaming\Code\User\settings.json`` 文件加入如下配置::

    "restructuredtext.linter.extraArgs": [
        "--max-line-length 80"
    ]

我的理解是，这个最大行宽在 \*.rst 文件中不建议设置太大，大约每行最多 80 个字符就差不多了，
这个和可维护性代码的最佳实践是一致的。


感谢观阅，如果您觉得有用，可以扫我的赞赏码，鼓励一杯咖啡。

.. image:: https://kaffa.im/img/reward.png
    :alt: 我的赞赏码

.. _issues-83: https://github.com/vscode-restructuredtext/vscode-restructuredtext/issues/83
.. _issues-84: https://github.com/vscode-restructuredtext/vscode-restructuredtext/issues/84

