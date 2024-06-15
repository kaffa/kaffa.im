清除 Microsoft Edge 自动跳转 https 的缓存
##################################################

:date: 2024-06-09 12:00
:author: Kaffa
:category: digital
:tags: Edge
:slug: clear-the-301-automatic-redirection-to-https-cache-of-microsoft-edge
:summary: 在配置 nginx 反代过程中，发现了 Edge 浏览器会缓存某个网址的 301 或 https 跳转，本文提供了清除该缓存的解决办法。

问题现象
==========

在配置 nginx 反向代理过程中，发现 Microsoft Edge 浏览器似乎缓存了网址的 http 习惯。

举例来说：对于 www.kaffa.im，如果访问过 https://www.kaffa.im 成功后，即使服务器取消了 https 访问，只提供 http 服务，当访问 http://www.kaffa.im 时，浏览器并不请求 80 端口的 http 服务，而是根据缓存继续会请求 443 端口的 https 服务。

由于很早之前第一次发现是在 Edge 中，本想写一篇吐槽微软对于这事处理的傲慢态度，今天又在豆包 AI 中询问了此事的翻译，结果豆包好像非常捍卫微软的品牌声誉似的，说这并不是微软的傲慢，而是出于安全考虑，这种回答还真是让我非常吃惊。

我仔细阅读了关于这个问题源头的一些对话：

1. https://issues.chromium.org/issues/41266980
2. https://learn.microsoft.com/en-us/answers/questions/988950/edge-redirecting-http-to-https

问题解决
==========


方法一
----------

这个方法较为推荐，一般人不知道，是一种“隐藏 Feature”。在 Edge 里按下 F12，打开 Microsoft Edge DevTools，然后鼠标左键长按在浏览器工具栏上的刷新按钮上，大约1秒后，按钮下方会出现下拉菜单，最后的菜单项是“清空缓存并进行硬刷新”，点击它，即会清空关于 https 或 301 永久跳转的缓存。

方法二
----------

这个方法可能会不太好，因为它的粒度不够。在 Edge 浏览器中，按下 Ctrl + Shift + Del 调出对话框，清除过去一小时的缓存。（如果上次服务是在很久以前，那么这个办法将无效。）

其它没有作用或失效的处理办法
------------------------------

* edge://flags/#edge-automatic-https

这个选项已经没有了。

* edge://net-internals/#hsts

这个处理无效。

* edge://settings/searchFilters

这个处理无效。


更进一步
==========

这个问题刨根问底，答案在 Chromium 源码逻辑里。

但我时间资源有限，如果某位有闲有兴趣的专业程序员擅长这块，还望不吝分享和指正。