##################################################
升级 CentOS Linux Kernel
##################################################

:date: 2018-07-06 13:00
:author: Kaffa
:category: 随笔
:tags: 随笔, Essays, 技术, Technology, CentOS, Linux Kernel
:slug: update-centos-linux-kernel
:summary: 本文描述升级 CentOS Linux Kernel 的方法

升级 CentOS Linux Kernel 的方法
======================================

升级命令::

    yum clean all
    yum update

查看 Kernel 版本命令::

    cat /etc/redhat-release

升级前::

    CentOS Linux release 7.4.1708 (Core)

升级后::

    CentOS Linux release 7.5.1804 (Core)


升级 CentOS Linux Kernel 后要做的事
======================================

升级完成后，我的开机菜单变成了::

    CentOS Linux (3.10.0-862.6.3.e17.x86_64) 7 (Core)
    CentOS Linux (3.10.0-693.21.1.e17.x86_64) 7 (Core)
    CentOS Linux (3.10.0-693.e17.x86_64) 7 (Core)
    CentOS Linux (0-rescue-4a8a974112aw410ea531fd24c60220bf) 7 (Core)

可以看到多出了一个选项外，依然包括旧版本 Kernel，少数几个也不妨碍什么，只是多占用一点硬盘空间。

如果想清理，可以先查看待删除的内核，命令如下::

    rpm -qa | grep kernel

再删除旧版本的内核包::

    yum autoremove kernel-.el7.x86_64


闲话几句
===========

1. Linux Kernel_ 即操作系统核心软件。有数据表示50%+的互联网服务器是 Linux，加上移动时代的 Android 占据半壁江山。可以这么说，*一半以上大部分计算设备内都运行了一份 Linux 核心*。
2. 论贡献，豪不夸张，这个由神级人物 Linus Torvalds 领导开发了27年的软件，是现代文明的重度的坚实依赖，它是实用者的胜利，也是 Linus Torvalds 价值观的成功检验；
3. Linux 的历史和文化值得慢慢了解、品位和思考，但现在大多情况下，云端机器 Linux 内核都是 3.x 版本，是不用升级的，除非你知道为什么要升级，或者你认为升级内核不重启机器的能力确实很酷；
4. 在国内，除非天时地利人和，研究 Linux Kernel 并没什么太多商业价值，只是领域情怀或“我乐意”；
5. https://www.elrepo.org 和 https://kernelnewbies.org 可能对你有用。



感谢阅读。

.. _Kernel: https://www.kernel.org/

