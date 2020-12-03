##################################################
在 Linux 上安装 VSCode 遇到的问题和解决思路
##################################################

:date: 2018-07-05 12:30
:author: Kaffa
:category: 随笔
:tags: 随笔, Essays, 技术, Technology, CentOS, VSCode, Linux
:slug: install-vscode-on-linux-error
:summary: 本文描述在 Linux 上安装 VSCode 遇到的问题和解决思路


为什么在 Linux 上安装 VSCode？
========================================

近期计划使用搭建 telegram bot，了解原理后，发现是基本的 http 开发。

计划使用轻量级 Web 框架，就项目需求来说，选择 Python 微框架 或 Go 语言比较适宜，加上前不久了解到类似 Flask_ 的框架 Vibora_，其官方介绍中的性能基准测试结果惊人难以置信，于是选择尝试，饶有兴致运行官方 hello world

.. code-block:: python

    from vibora import Vibora, Response

    app = Vibora()

    @app.route('/')
    async def home():
        return Response(b'Hello world')

    if __name__ == '__main__':
        app.run(debug=True)

却发现无法在 Windows 下运行，提示::

    Traceback (most recent call last):
    File "test_vibora.py", line 1, in <module>
        from vibora import Vibora, JsonResponse
    File "C:\Python36\lib\site-packages\vibora\__init__.py", line 7, in <module>
        from .server import *
    File "C:\Python36\lib\site-packages\vibora\server.py", line 5, in <module>
        from signal import pause
    ImportError: cannot import name 'pause'

查看源代码，是因为 vibora 使用了 Linux signal 的原因，看来，虽然其文档中称支持 Windows 是其目标，但目前还不支持。

由于服务器是 CentOS，于是选择在本地虚机装上桌面，直接采用 VSCode 或 PyCharm 进行开发调试。


遇到的问题
===================
按照微软官方 `VSCode 的 Linux 安装帮助`，本应该四个命令就可以搞定::

    sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
    sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
    yum check-update
    sudo yum install code

可是在执行最后一个命令时，出现了一系列的 404 错误，安装终止了，提示::

    Error downloading packages:  libXScrnSaver-1.2.2-6.1.el7.x86_64

看样子是因为VSCode所依赖的某个软件包，提示资源不存在，yum 命令没能下载成功。


解决思路
===================
笼统的说，之前写过一篇 `解决编程领域难题的有效方法`_，提到 StackOverflow，但此问题并不能很直接搜索到解决思路，所以只能自己思考。

按照 yum 的提示去对应 `CentOS 7`_ 目录才发现，原来是 `CentOS 7.5.1804`_ 到 Main Line 版本了。

于是这个包依赖问题可以从 `CentOS 7.4.1708 readme`_ 得到解答，即 `升级 CentOS 7.4 到 CentOS 7.5`_。

升级完成后，再次运行 ``sudo yum install code``，即成功。


感谢观阅，如果您觉得有用，可以扫我的赞赏码，鼓励一杯咖啡。

.. image:: https://kaffa.im/img/reward.png
    :alt: 我的赞赏码



.. _Flask: http://flask.pocoo.org/
.. _Vibora: https://vibora.io/
.. _VSCode 的 Linux 安装帮助: https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions
.. _Python Web Frameworks: https://wiki.python.org/moin/WebFrameworks
.. _解决编程领域难题的有效方法: http://kaffa.im/the-effective-way-to-find-answers-to-programming-questions.html
.. _CentOS 7: http://mirror.centos.org/centos-7/
.. _CentOS 7.4.1708 readme: http://mirror.centos.org/centos-7/7.4.1708/readme
.. _CentOS 7.5.1804: http://mirror.centos.org/centos-7/7.5.1804/
.. _CentOS Mirrors: https://www.centos.org/download/mirrors/
.. _升级 CentOS 7.4 到 CentOS 7.5: https://kaffa.im/update-centos-linux-kernel/


