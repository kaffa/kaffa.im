##################################################
Windows 下安装 Wechaty 的注意点(keng)
##################################################

:date: 2018-07-17 12:00
:author: Kaffa
:category: 随笔
:tags: 随笔, Essays, 技术, Technology, Wechaty, Node, Node.js
:slug: install-wechaty-on-windows
:summary: 本文描述 Windows 下安装 Wechaty 的注意点(keng)

摘要
======================================

本文对于在 Windows 下安装 Wechaty_ 的坑作个临时记录，但其中涉及的处理方式随着项目的升级或依赖软件的升级可能会变得不再需要。


说明
======================================

升级到 Node 10
    与 node 有关的问题，那可能是因为 node 没有升级到 10 以上的版本，解决办法是在 nodejs.org 官方下载 10 以上的新版本。

安装 Python 2.7
    因为 node-gyp 依赖 Python 2.7 和 windows-build-tools，node 在安装中多采用源代码编译安装，这种的好处是跨平台。
    安装好 Python 2.7 以后，需要设置环境变量
    PYTHON=c:\\Python27\\python.exe

文本二维码
    QR 在移动世界盛行，但 Windows 依然缺少官方提供的文本二维码方案，控制台的文本二维码支持的不好，启动二维码以后，也许格式错乱无法扫描，此时可以复制张贴到记事本中，采用合适的等宽字体进行 **反选** 扫描登录。

puppeteer
    puppeteer 是 Google Chrome？

ts-node
    如果采用 TypeScript 版本的 Wechaty，那么 ts-node 的路径在 wechaty\\node_modules\\.bin\\ts-node 下。

docker Wechaty
    如果使用 docker 版本的 Wechaty，那么需要升级 Windows 到 Proffesional 版。


吐槽
===========
- 一般生产推荐使用 LTS 版本的 node ，可能很多人都不会安装 node 最新版，所以此处算是一坑，官方虽有提示，但不够醒目；

- 已经 2018 年了，大部分库都用 six 支持了 Python 2 和 3 版本，很多人都转到 Python 3.6+，对于安装时出现 Python 相关的错误时，可能不会想到是 node-gyp 依赖 Python 2.7 的原因。


感谢阅读。

.. _Wechaty: https://github.com/Chatie/wechaty
.. _node-gyp: https://www.npmjs.com/package/node-gyp
.. _puppeteer: https://github.com/GoogleChrome/puppeteer
.. _windows-build-tools: https://www.npmjs.com/package/windows-build-tools
