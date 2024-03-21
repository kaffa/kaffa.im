从解决 libcurl 与 FreeBSD 13 兼容性问题中学到的
############################################################

:date: 2024-03-21 22:30
:author: Kaffa
:category: digital
:tags: libcurl, freebsd
:slug: learned-from-solving-compatibility-problem-of-libcurl-and-freebsd-12
:summary: 本文是解决 EverEdit 的 sftp 兼容性问题的反思。
:image: /static/img/2024/hero.png
:growth: 5

反思
====================

1. 问题发生概率是基本盘；

   列举客观事实，用概率否定非常低的可能；

2. 不厌其烦地尝试；

   每一次探索，都更接近真相；

3. 检查假设；

   如果依旧没有收获，可以返回出发点，检查假设。

**问题最终的解决是我错误的假设 sftp 是 EverEdit.exe 实现的，且EverEdit 目录下只有一个 libcurl。**


事因
====================

由于 Side Project 收尾，我关停了一台外网的服务器，将几个服务部署回内网。

服务架构调整后，我从 CentOS 转向了 FreeBSD 作个人服务器。

可从 Terminal ssh 上 FreeBSD sshd，而日常使用较多的 EverEdit 内置 sftp 却一直无法登录。

错误提示::

    [22:39:52]:Connected to xxx.xxx.xxx.xxx ...
    [22:39:53]:Failure establishing ssh session
    [22:39:53]:Closing connection 0


分析过程
====================

错误现象是，在建立与服务器连接时异常退出了。

1. 分析问题发生概率

   FreeBSD 13.2 有缺陷的概率趋近于 0；EverEdit 4 有缺陷的概率也不高，软件作者是长期主义且严谨的大牛。

   那么，我想问题可能出在 FreeBSD 与 EverEdit 兼容性上。

2. 询问软件作者

   作者的分析：可能是 curl 哪个地方的配置问题。

3. 检查 EverEdit 目录和 curl 官方

   我去到 EverEdit 目录，并查看了 curl 官方网站，也没有发现特别的配置。

4. 开始抓包分析

   使用 Wireshark 分别对 EverEdit 和 Terminal 发出的数据包进行抓取，但由于知识不足，分析过程很慢。

5. 怀疑 libcurl

   然后我在 EverEdit 目录看到了 libcurl

   我于是怀疑是 libcurl 所使用的证书不够新，于是更新了证书配置，结果问题依旧。

6. 暂时放弃。

   替换 libcurl.dll 后，问题依旧。

7. 返回思考假设。

   直到昨天，为优化 EverEdit 格式化代码的插件，我进入目录逐个查找。

   突然灵机一现。我发现在 EverEdit 的深层目录中 sftp 是以插件形式存在，且有一个独立的 libcurl。

   经过替换插件的 libcurl，和反复测试，问题完美解决。


最后就有了上述反思，以让我在今后解决此类问题上思路完整。


libcurl
====================

心目中有很多类似 curl 的 "Hero Softare"，如 OpenSSH、VIM、GCC，它们给与世界以选项，是美好世界拼图的一部分。
