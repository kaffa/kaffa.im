莫名解决局域网内 macOS 与 Windows 不能互访的问题
##################################################

:date: 2024-10-12 10:00
:author: Kaffa
:category: article
:tags: macOS,firewall
:slug: solution-for-macos-and-windows-cannot-communicate-on-a-lan
:summary: 本文
:image: /static/img/2024/hero.png
:brief: 被 macOS 和 Windows 突然不能互访的问题困扰多时，今天得以解决，但没有弄清原因，本文只是一个半成品，我也不清楚是怎么解决的。
:growth: 3


现象描述
==========

局域网中，通过路由器连接的 Windows 和 macOS 在某次 macOS 的系统升级后，就再也不能相互访问了，但奇怪的是，在 macOS 上通过桥接的虚拟机依然可以被 Windows 访问到，今天得空我解决了此问题。


现象一：在 macOS 上启动 Apache 或者 nginx，此时本机通过 http://127.0.0.1 可以打开测试网页，但 Windows 却不能。

现象二：Windows 无法 ping 通 macOS，macOS 却可以 ping 到 Windows。

解决思路
==========

现象二说明两者的网络是联通的，于是从 macOS 端着手，关闭防火墙，结果无法访问，又尝试关闭 Windows 端的防火墙，依然无法访问。

在 macOS 上尝试了使用 telnet 等工具测试，发现可以正常联通，但 Windows 上不行。

说明两者之间可能被什么挡住了，这莫名的暴躁，难道是小米路由器，难道是 ipv6，结果都排除了。

猜测：也许 macOS 端除了防火墙依然有什么进程在默默工作，经过回忆，我早期下载过一个叫做什么 cat 的 App，其中我开启过 macOS 的网络防火墙。

按照这个思路我下载了一堆防火墙：LuLu、Murus、Snail、Little Snitch 等，分别启动观察网络。

最终，一瞬间我发现网络似乎联通了， Windows 上可以访问 macOS 部署的所有服务。

经过又一阵子的排查，我发现退出 Murus 时，选择 Disable 就可以访问网络。

总结
==========

这真是一个诡异的现象，但通过 Murus 解决了，但我确实不知是怎样解决的。

这个阻挡网络的不是 macOS 自带的防火墙，是什么，我就没有时间研究了。

如果后续我知道的原理，我会来更新这篇文章。