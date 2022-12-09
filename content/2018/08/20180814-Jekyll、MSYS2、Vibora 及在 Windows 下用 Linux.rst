##################################################
Jekyll、MSYS2、Vibora 及在 Windows 下用 Linux
##################################################

:date: 2018-08-14 12:00
:author: Kaffa
:category: 随笔
:tags: 随笔, Essays, 技术, Technology, Windows, Linux, Jekyll, Ruby, MSYS2, Vibora, Cygwin, MinGW, Virtualpc, VMWare, Docker, MSYS, msysgit
:slug: jekyll-msys2-vibora-and-use-linux-on-windows
:summary: 本文聊聊 Jekyll、MSYS2、Vibora 及在 Windows 下用 Linux 的话题


故事
====================

故事开始于我需要在 Windows 下用 Jekyll 转化一篇 Markdown 的博文，于是在 Windows 下安装了 Jekyll，其中涉及一些 MSYS2 的安装坑。
接下来想到 MSYS2 其实可以解决 Vibora 的问题，于是将这两个过程中的难点记录一下，再谈谈在 Windows 下使用 Linux 的话题。

本文旨在为正使用 Windows 同时又想使用 Linux 功能的人列举一些可能的途径，本文适用于对 Windows 和 Linux 具备一定了解的人。
另有计划写 Windows、macOS、Linux 操作系统比较的博文，但本文的范围不涉及比较。


Widnows 下用 Jekyll
====================

Jekyll 依赖于 Ruby Runtime 和一些 Gem 包，而 Ruby Runtime 在 Windows 下推荐用于 RubyInstaller_，
某些 Gem 包需要本地编译，官方推荐 MSYS2_ 安装 Windows 上的编译工具链。
因为众所周知的原因，国内安装这些软件时也会遇到一些问题。下面叙述步骤并给予问题的解决办法。

安装 Ruby
--------------------
运行下载好的 RubyInstaller，基于少一层目录的原因，建议直接安装在根目录下，例如 ``C:\Ruby25\``，并将此目录加入安装目录到 PATH。在最后点击结束按钮后，会提示安装 MSYS2，它用来编译 Ruby 本地包，官方说它的下载由一个全球 CDN 提供，但它在国内的访问真是无力吐槽。

也许你等待龟速网络很久可以将 MSYS2 安装成功，也许你会遭遇反复失败，不知如何是好。但如果你需要使用 Jekyll，而它使用了本地二进制包，那么这个问题是无法跳过的。

安装 MSYS2 的小技巧
--------------------
如果你跳过了 MSYS2 安装，那么在后续的 gem install 时，会提示：

.. code-block:: batch

    MSYS2 could not be found. Please run 'ridk install' or download and install MSYS2 manually from https://msys2.github.io/

当你执行 ``ridk install`` 时，会显示下载 http://repo.msys2.org/distrib/x86_64/msys2-x86_64-20180531.exe 失败，我的解决办法是用迅雷下载 ``msys2-x86_64-20180531.exe``，并用 IIS 或 Apache 等服务器，在本地配置一个站点下载，这样做需要管理员权限修改 ``C:\Windows\System32\drivers\etc\hosts`` 文件，临时加入一行配置：

.. code-block:: batch

    127.0.0.1    repo.msys2.org

此时确保访问 http://127.0.0.1/distrib/x86_64/msys2-x86_64-20180531.exe 时可以正常下载。那么再次运行 ``ridk install`` 时，就会通过本机下载了。

然后，当 ``msys2-x86_64-20180531.exe`` 下载完毕时，需要及时把上述 hosts 配置行删除，因为本机并没有 ``repo.msys2.org`` 站点下的其他文件。


配置 MSYS2 镜像地址
--------------------

同时，为了 MSYS2 其他包方便下载，建议配置国内镜像，分别修改下面三个文件，在配置的最上加入 清华大学 与 中科大镜像地址

``C:\msys64\etc\pacman.d\mirrorlist.mingw64``

.. code-block:: batch

    ##
    ## 64-bit Mingw-w64 repository mirrorlist
    ##
    ## 清华大学软件镜像
    Server = https://mirrors.tuna.tsinghua.edu.cn/msys2/mingw/x86_64/
    ## 中科大镜像
    Server = http://mirrors.ustc.edu.cn/msys2/mingw/x86_64/

``C:\msys64\etc\pacman.d\mirrorlist.mingw32``

.. code-block:: batch

    ##
    ## 32-bit Mingw-w64 repository mirrorlist
    ##
    ## 清华大学软件镜像
    Server = https://mirrors.tuna.tsinghua.edu.cn/msys2/mingw/i686/
    ## 中科大镜像
    Server = http://mirrors.ustc.edu.cn/msys2/mingw/i686/

``C:\msys64\etc\pacman.d\mirrorlist.msys``

.. code-block:: batch

    ##
    ## MSYS2 repository mirrorlist
    ##
    ## 清华大学软件镜像
    Server = https://mirrors.tuna.tsinghua.edu.cn/msys2/msys/$arch/
    ## 中科大镜像
    Server = http://mirrors.ustc.edu.cn/msys2/msys/$arch/


如果你及时删除了 hosts 文件中的配置行，那么 NSYS2 即可以顺利完成安装。


测试 MSYS2 安装是否成功
----------------------------------------

可以再次运行 ``ridk install``，命令行会打开

.. code-block:: batch

    RubyInstaller2 for Windows

    1 - MSYS2 base installation
    2 - MSYS2 system update
    3 - MSYS2 and MINGW development toolchain

试试 1、2、3 三个选项，如果全部没有可更新项时，就证明 MSYS2 安装已经成功了。


配置 Gem 镜像地址
--------------------

对于有价值的开源技术，国内一般都进行了镜像，一般都建议直接使用国内镜像地址。运行下面命令配置镜像

.. code-block:: batch

    gem sources –r https://rubygems.org/   
    gem sources -a https://ruby.taobao.org/

运行下面命令查看，并更新

.. code-block:: batch

    gem sources -l
    gem update


安装 Jekyll
--------------------

下面是官方网站优雅的几行介绍

.. code-block:: batch

    ~ $ gem install bundler jekyll
    ~ $ jekyll new my-awesome-site
    ~ $ cd my-awesome-site
    ~/my-awesome-site $ bundle exec jekyll serve
    # => Now browse to http://localhost:4000

有了上面步骤的铺垫，至此，Jekyll 可以优雅的运行了。


关于 Ruby 的感叹
--------------------

十年前，曾在 Ruby 语言通过 Web 2.0 的需求爆发时，借 Web 敏捷框架 Rails 大红大紫了解过它，对这些年一直没有再有机会使用，如果没有 Rails，Ruby 就不会红，定位于 Python 和 Perl 之间，如今它也许会有所发展，但综合来看，都会逐渐变成先前使用了 RoR 公司的技术遗产，市场上 Ruby 的技术人员也会越来越少，加上它本身并未和现在大前端、移动互联网、大数据、云计算、人工智能、VR等任何一个热点沾边，也不具备后端编译语言的规模成本优势，从系统论视角思考，没有生态，就会走向低谷，但在它擅长的 Web 领域内，还是一种有智慧的解决方案。

相比来说，经常能先于时代的 Python 的好运气并不是偶然，因为重视科研领域，它借着大数据分析和人工智能一飞冲天，如今生态广阔的 Python，相比来说就有着更稳固的护城河，这种就好比持续增长的公司拥有的竞争优势一样，更值得长期看好。所以，下面就说说 Python Web Framework：Vibora


Widnows 下用 Vibora
====================

Vibora 性能闪瞎眼，为了不让 MSYS2 环境浪费，于是尝试是否可以通过 MSYS2 将它运行起来。


MSYS2 安装 python3
--------------------

首先，打开 MSYS2 运行 python 或 python3，提示

.. code-block:: batch

    -bash: python: 未找到命令
    -bash: python3: 未找到命令

于是我们需要在 MSYS2 中添加软件包，请出 pacman，它移植于著名 LFS ———— Arch Linux 发行版

首先，安装一些依赖和编译工具

.. code-block:: batch

    pacman --needed -Sy bash pacman pacman-mirrors msys2-runtime
    pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-gdb mingw-w64-x86_64-make tmux zsh git mingw64/mingw-w64-x86_64-cmake winpty
    pacman -S mingw-w64-x86_64-python3-bsddb3 mingw-w64-x86_64-gexiv2 mingw-w64-x86_64-ghostscript mingw-w64-x86_64-python3-cairo mingw-w64-x86_64-python3-gobject mingw-w64-x86_64-python3-icu mingw-w64-x86_64-iso-codes mingw-w64-x86_64-hunspell mingw-w64-x86_64-hunspell-en mingw-w64-x86_64-enchant


接下来安装 python3 和 pip3

.. code-block:: batch

    pacman -S mingw-w64-x86_64-python3 
    pacman -S python3-pip

此时 python3 和 pip3 已经安装，顺便把 pip3 升个级，最近它的版本号也像 Chrome 一样一发不可收拾。

.. code-block:: batch

    pip3 install --upgrade pip


MSYS2 安装 vibora
--------------------

再安装 vibora

.. code-block:: batch

    pip3 install vibora

提示错误：

.. code-block:: batch

    Running setup.py install for vibora ... error
    Complete output from command /usr/bin/python3 -u -c "import setuptools, toke                                            
    nize;__file__='/tmp/pip-install-rawskw89/vibora/setup.py';f=getattr(tokenize, 'o                                            
    pen', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile                                            
    (code, __file__, 'exec'))" install --record /tmp/pip-record-9rnpdvhe/install-rec                                            
    ord.txt --single-version-externally-managed --compile:

    ...

    unable to execute 'x86_64-pc-msys-gcc': No such file or directory
    error: command 'x86_64-pc-msys-gcc' failed with exit status 1

    ...

    Command "/usr/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-                                            
    install-rawskw89/vibora/setup.py';f=getattr(tokenize, 'open', open)(__file__);co                                            
    de=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec')                                            
    )" install --record /tmp/pip-record-9rnpdvhe/install-record.txt --single-version                                            
    -externally-managed --compile" failed with error code 1 in /tmp/pip-install-raws                                            
    kw89/vibora/


想来原因是 Vibora 依赖本地二进制程序进行异步通信。

再安装 x86_64-pc-msys-gcc

.. code-block:: batch

    pacman -S gcc

之后，再次运行 ``pip3 install vibora``，提示

.. code-block:: batch

    In file included from vibora/parsers/parser.c:4:0:
    /usr/include/python3.6m/Python.h:39:10: 致命错误：crypt.h：No such file or d                                            
    irectory
     #include <crypt.h>
              ^~~~~~~~~
    编译中断。
    error: command 'x86_64-pc-msys-gcc' failed with exit status 1

    ----------------------------------------
    Command "/usr/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-t22lx1u7/vibora/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-f8i8_k06/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-install-t22lx1u7/vibora/


StackOverflow 大法好，提示缺少的 头文件 crypt.h 在 libcrypt-devel 包中，于是再安装 x86_64-pc-msys-gcc

.. code-block:: batch

    pacman -S libcrypt-devel


第三次运行  ``pip3 install vibora`` 

.. code-block:: batch

    $ pip3 install vibora
    Collecting vibora
    Using cached https://files.pythonhosted.org/packages/1c/db/c42998b106b89d67ce0                                            fe256320454ca224e4d3d05f56dd518514a5b738c/vibora-0.0.6.tar.gz
    Requirement already satisfied: pendulum in /usr/lib/python3.6/site-packages (from vibora) (2.0.3)
    Requirement already satisfied: python-dateutil<3.0,>=2.6 in /usr/lib/python3.6/site-packages (from pendulum->vibora) (2.7.3)
    Requirement already satisfied: pytzdata>=2018.3 in /usr/lib/python3.6/site-packages (from pendulum->vibora) (2018.5)
    Requirement already satisfied: six>=1.5 in /usr/lib/python3.6/site-packages (from python-dateutil<3.0,>=2.6->pendulum->vibora) (1.10.0)
    Installing collected packages: vibora
    Running setup.py install for vibora ... done
    Successfully installed vibora-0.0.6

我的天，成功了！于是试了试官方 hello-world.py


运行 vibora hello world
----------------------------------------

.. code-block:: python

    from vibora import Vibora, Request
    from vibora.responses import JsonResponse

    app = Vibora()

    @app.route('/')
    async def home(request: Request):
        return JsonResponse({'hello': 'world'})

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=8000)

提示：

.. code-block:: batch

    xxx@yyyy MSYS /d/code/vibora
    $ python hello-world.py
    Traceback (most recent call last):
    File "hello-world.py", line 1, in <module>
        from vibora import Vibora, Request
    File "/usr/lib/python3.6/site-packages/vibora/__init__.py", line 7, in <module>
        from .server import *
    File "/usr/lib/python3.6/site-packages/vibora/server.py", line 11, in <module>
        from .workers.handler import RequestHandler
    File "/usr/lib/python3.6/site-packages/vibora/workers/handler.py", line 3, in <module>
        from socket import IPPROTO_TCP, TCP_NODELAY, SO_REUSEADDR, SOL_SOCKET, SO_REUSEPORT, socket
    ImportError: cannot import name 'SO_REUSEPORT'

google 错误提示，居然来到了 vibora-issues-106_，状态是关闭的，作者 @frnkvieira 说 @zzeric 已经修复，他已合入最新版，下面又有人要求打开这个 issues，说经过测试依然存在。

@zzeric_ 的解决办法是升级到 python 3.7.0，我个人认为这并非一个好的办法。
@danieldaeschle_ 的解决办法是 vibora-pull-157_ ，不过作者并未接受。

我暂时采用了 danieldaeschle_ 的方法修改，再次运行，提示：

.. code-block:: batch

    OSError: [Errno 112] Address already in use

不过，此时浏览器打开 http://localhost:8000 已经可以正常显示::

    {'hello': 'world'}

本文的第三部分，剩下的就是作个总结。


Windows 下用 Linux 的途径
========================================
* 虚拟机
    虚拟机是在物理宿主机上虚拟一台机器，再将 Linux 安装进去。Windows 平台的虚拟机软件也有不少选择，而且微软也内置了一种虚拟机 Hyper-V
* 类Linux / POSIX API 方案
    这类方案是在 Windows 核心上实现一种 类Linux / POSIX 标准的中间翻译层，要么对接到 Windows 原生动态链接库，要么对接到自带的库。
* Windows Subsystem for Linux
    这是基于市场博弈和市场的发展，微软官方基于 Hyper-V 给出了一个解决方案，这个方案可以从微软商店中下载 Linux，目前官方支持 5 种比较常见的发行版。

下面是我的一些理解

VirtualBox_
--------------------

在普通需求上，这是我最愿意使用的一种便携方案，比如国内银行的 usb key 只支持 Windows 时，使用虚拟机也是挺好的，适合个人。

VMWare_
--------------------

他们具备成熟的生产环境商业方案，但其实更适合开发环境和测试环境构建一套安全、灵活、可扩展的系统环境。但现在虚拟化的趋势中有所过气，XEN 算是 Linux 上对标的方案。但他们家显卡驱动实在不行。

Hyper-V_
--------------------

在虚拟微软自家系统旧版本时，这个是最佳方案，一些微软自家新技术，也是以此虚拟机发布的。

Docker_
--------------------

它不是虚拟机，但是目前很不错的容器虚拟化技术，但它需要 Widnows Pro 版本以上，且不能与 VirtualBox 和 VMWare 及一些 Android 模拟器共存。


Cygwin_ & MinGW_
--------------------
Cygwin 通过动态链接库 cygwin1.dll，提供一个 POSIX API 子集，编译出 Linux 下的程序通过这个库对接 Windows 底层动态链接库。

MinGW 是 GCC 在 Windows 的实现，通过编译器，把诸如 Linux 系统调用 如 fork 翻译成 Windows API 如 CreateProcess 这样。这种没有引入运行时的中间层，会比 Cygwin 更紧凑。
    
通俗的说 Cygwin 属于运行时适配，MinGW 属于编译时转化，从技术纯粹来说，我更喜欢 MinGW，但对于绝大多数小的程序，Cygwin 虽然多了中间层，但可移植性比 MinGW 强。

跨平台属于商业鸿沟，技术上也是一个复杂问题，之所以跨平台这个问题这么难，是因为平台差异导致的，比如可执行文件格式差异，Windows 是 PE 文件，Linux 是 ELF 文件，于是需要分别编译。


MSYS_ & MSYS2_
--------------------
MSYS 这个项目，由多年前的 MinGW 团队开始，并成为 Cygwin 的一个分支，一个从来没有跟上 Cygwin 发展的分支，目前已不活跃，如果有选择，请选择 MSYS2。

MSYS2 是 MSYS 的一个升级版，它集成了 pacman 和 Mingw-w64_ 的 Cygwin 升级版, 提供了 Bash 等 Linux 环境、版本控制软件（Git/hg）和 MinGW-w64 工具链。
它是由 mingw-builds 团队（也是MinGW-w64工具链的官方包装商）的 Alexey Pavlov 开发的一个项目，密切更新到最新的 Cygwin，使其不会过时。

MSYS2 不完全是基于 MinGW 的，至少其原生工具都是链接到自带的一套特定版本的 Cygwin DLL ，基本上只是用 libalpm 管理 MSYS2、MinGW-w64 和 MinGW 三个不同子系统的软件包。
Cygwin、MSYS 和 Git for Windows（前称 msysgit）里各有一套 Cygwin DLL 而且互不兼容，而 MinGW 那两个子系统都不需要链接到任何版本的 Cygwin DLL。


`Windows Subsystem for Linux`_
----------------------------------------
下载安装都很容易，可以在 Windows Store 下载，其中的坑在评论中都已解决。

* 用户可以使用 Linux 常见工具：grep, sed, awk, Bash, vim, emacs, tmux 等
* 可以支持很多运行时：Javascript/node.js, Ruby, Python, C/C++, C# & F#, Rust, Go
* 以及很多 Linux 的服务端软件：sshd, MySQL, Apache, lighttpd
* 还可以使用包管理器，如 apt-get 等
* 支持 Linux 和 Windows 程序的双向调用

我有安装过 WSL Ubuntu，其性能不高，图形包等并未尝试，相比虚拟机，觉得目前不具太大意义。


总结
========================================
总的来说，本文讲了 Windows 下用 Linux 的两个例子，再总结了一些 Windows 下 使用 Linux 的方法，整体内容很多。

最后来说，一个更好的方案可能是一台高配 macOS 运行 Parallels Desktop，再其中运行 Windows ;)

感谢阅读。

.. _`Ruby 官方`: https://www.ruby-lang.org
.. _`RubyInstaller`: https://rubyinstaller.org/
.. _`MSYS2`: http://www.msys2.org/
.. _`Jekyll`: https://jekyllrb.com/
.. _vibora-issues-106: https://github.com/vibora-io/vibora/issues/106
.. _zzeric: https://github.com/danieldaeschle
.. _danieldaeschle: https://github.com/danieldaeschle
.. _vibora-pull-157: https://github.com/vibora-io/vibora/pull/157 
.. _VirtualBox: https://www.virtualbox.org/
.. _VMWare: https://www.vmware.com/
.. _Hyper-V: https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
.. _Docker: https://www.docker.com/
.. _Cygwin: https://www.cygwin.com/
.. _MinGW: http://www.mingw.org/
.. _Mingw-w64: http://mingw-w64.org/
.. _MSYS: http://www.mingw.org/wiki/MSYS
.. _Windows Subsystem for Linux: https://docs.microsoft.com/en-us/windows/wsl/about