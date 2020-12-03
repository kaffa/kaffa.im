##################################################
Windows 下 Node 的路径配置
##################################################

:date: 2018-08-06 22:00
:author: Kaffa
:category: 随笔
:tags: 随笔, Essays, 技术, Technology, Node, Node.js, Windows, Path
:slug: config-nodejs-path-in-windows
:summary: 本文描述 Windows 下 nodejs 的路径配置问题，也涉及 Windows 路径的说明


在 Windows 下安装 nodejs
============================

1. 浏览器打开 nodejs 官方网站 https://nodejs.org/，选择 LTS 或者 Current 版本。

2. 用下载软件（如迅雷）下载目前的最新版 ``https://nodejs.org/dist/v10.8.0/node-v10.8.0-x64.msi``，下载到本地后，双击安装。

3. 个人推荐将运行时安装在根路径下，因为当需要进入运行时目录查看时，每次会比进入 Program Files 少进一层，这样可以节省时间。我的安装目录是 ``C:\nodejs``


在 Windows 下配置 nodejs
============================

1. 至此 nodejs 就已经安装好了，其中 npm 是 nodejs 的包管理器，此时已经在 ``C:\nodejs\node_modules\npm`` 之下

2. 然后在 Windows 下 nodejs 还需要配置两个重要的路径：

一个是 node_global，这个目录用来放全局安装命令 ``npm install [PACKAGE_NAME] -g`` 安装的包，通常将很多基础的共用包可以安装到这个目录，例如 nw

一个是 node_cache，这个目录是 node 缓存

我们用 ``npm install [PACKAGE_NAME]`` 命令安装的内容，会安装在每个目录下，这就是 node 来管理依赖的方式。

运行下面命令::

    C:\>cd nodejs
    C:\nodejs>mkdir node_global
    C:\nodejs>mkdir node_cache
    C:\nodejs>npm config set prefix "C:\nodejs\node_global"
    C:\nodejs>npm config set cache "C:\nodejs\node_cache"

3. 配置环境变量 ``NODE_PATH=C:\nodejs\``

4. 在 PATH 中 加入 ``%NODE_PATH%`` 和 ``%NODE_PATH%\node_global``，顺便推荐使用 `Rapid Environment Editor`_

5. 至此，Windows 下的 nodejs 配置完毕


补充说明
============================

本文推荐的路径是最简单的方法，下面对 Windows 路径本身的机制加以说明::

    1. 应用数据全局目录：C:\ProgramData\
    2. 应用数据用户目录：C:\Users\USER_NAME\AppData\Roaming\
    3. 用户根目录：C:\Users\USER_NAME\
    4. 64位程序目录：C:\Program Files\，非管理员权限不可写
    5. 32位程序目录：C:\Program Files (x86)\，非管理员权限不可写

如果 npm 出现警告 ``Missing write access``，接着出现错误 ``npm ERR! code ENOENT``，则和上述权限有关，这里的 ENOENT 是 Error NO ENTry 的意思::

    pm WARN checkPermissions Missing write access 
    ...
    npm ERR! code ENOENT
    npm ERR! errno -2
    npm ERR! syscall access
    npm ERR! enoent ENOENT: no such file or directory, access '/usr/local/lib/node_modules/webpack/node_modules/[XXX]'
    npm ERR! enoent This is related to npm not being able to find a file.
    npm ERR! enoent

如果忘记将 nodejs 放入PATH，那么可能会出现以下错误提示，因为程序调用 node 时， Windows 找不到 node.exe 或 node.cmd 或 node.bat::

    'node' 不是内部或外部命令，也不是可运行的程序或批处理文件


另外，当然也可以参考官方文档 npm-folders_，但可能有更新不及时，node 社区还年轻且贡献者有很多个人，有时并不太照顾 Windows 平台，这点不比 python 社区发展了那么久，且那么多机构贡献者。

感谢观阅，如果您觉得有用，可以扫我的赞赏码，鼓励一杯咖啡。

.. image:: https://kaffa.im/img/reward.png
    :alt: 我的赞赏码

.. _npm-folders: https://docs.npmjs.com/files/folders
.. _Rapid Environment Editor: https://www.rapidee.com