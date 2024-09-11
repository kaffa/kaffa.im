给网站增加了 DIŸgöd 的 follow（Description 方式）
##################################################

:date: 2024-09-09 15:30
:author: Kaffa
:category: website
:tags: follow, DIYgod
:slug: add-diygod-follow-claim
:summary: 本文的主要目的是给 follow 增加 claim。
:description: 本文的主要目的是给 follow 增加 claim。follow 是 DIYgod 出的关于 RSS 的新产品，其中整合了 RSSHub 和 Web3 的内容，产品都是联合在一起的。

为什么我写了好几篇
========================================

为 follow 增加 claim 的方式有三种，我最初选择使用方式一，但增加 Content 后无效，经思考，估计方式一不支持 Atom 格式 Feed（个人猜测）。


为 follow 增加 claim 的方式
========================================

follow.is 是 DIYgod 的新产品，其中可以 Claim 一个 Feed 为自己的，据说为 follow 增加 claim 后可以支持打赏。

增加方式有三种：

1. Content

   在 Feed 最新内容中增加如下文字::

       This message is used to verify that this feed (feedId:41342818708527123) belongs to me (userId:41447029693323264). Join me in enjoying RSS on the next generation information browser https://follow.is.

2. Description

   在 Feed 的 xml 文件中，增加 Description 标签，内容如下::

      <description>feedId:41342818708527123+userId:41447029693323264</description>

3. 在 Feed 中增加如下内容::

    <follow_challenge>
       <feedId>41342818708527123</feedId>
       <userId>41447029693323264</userId>
    </follow_challenge>


Pelican 增加 claim 的方式
========================================

由于 Pelican 实现 Feed 的方式是采用 Django 的 `feedgenerator <https://github.com/django/django/blob/main/django/utils/feedgenerator.py>`_ 工具库（依赖一个成熟项目的组件是非常聪明的做法）。经查看源码，发现 feedgenerator 支持新增节点，但不太支持修改 Feed 节点，于是，对于此场景较好的方式是手动搞定，搞定方式嘛，新增一个 Pelican Plugin 来处理或者新增一个后处理步骤（比如一个脚本），在其中处理一下 Feed 的 XML 文件内容即可，原理都差不多，采用 Pelican Plugin 方式的好处是可以较方便获取文件路径。

`Pelican 实现 claim 插件源码 <https://github.com/kaffa/kaffa.im/blob/master/plugins/followclaim/>`_\