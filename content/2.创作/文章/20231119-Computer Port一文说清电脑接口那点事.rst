Computer Port 一文说清电脑接口
############################################################

:date: 2023-11-19 13:05
:author: Kaffa
:category: article
:tags: Computer Port, USB, Type-C, HDMI, DisplayPort
:slug: computer-port-in-a-nutshell
:summary: 从使用者角度梳理电脑接口，将散落各处的信息合并到一篇文章中，避开技术细节，只介绍作为普通使用者需要了解的信息。
:image: /static/img/2023/about-kaffa.png


接口 Port
====================

在过去二十五年中，我接触到的 Port 主要指三种东西：

- 电脑接口
- Tcp/Udp 端口：这个将在 `「TCP / UPD Port」 </computer-port-in-a-nutshell.html>`_ 一文中描述
- MacPorts，一个开源社区驱动的实现将开源软件编译安装到 Mac 操作系统的项目。

本文梳理的属于电脑接口。


数码真香，连接真烦
====================

相较于真香的数码设备，将它们连接起来对很多人来说都是焦虑的事。 ⎛ -᷄ ᴥ -᷅ ⎞೯

苹果公司当时激进地取消线缆，整合接口，广泛使用无线通讯技术属于值得点赞的创新。

人的感觉实在是太驽钝，感受不到空气中广泛漂浮的震动的电磁波所携带的信息，这才让无线通讯技术有了改进空间。

然后，在很多需要大量数据通讯的场景下，还是不得不通过线缆作为信息和能量的介质。

在这所有的线缆中，通用连接线缆似乎快统一为 USB Type-C 了，但这是一种理想情况。

事实上，未来依然还是会有不止一二三种选择。


电话线接口和网线接口
----------------------------------------

开始讲接口时，需要有几个概念。公头、母头。

公头会插入母头，母头是插座。

用来传输信息的接口，公头是水晶头，一般人只需要了解两种：

* 电话线口：RJ11，可以连接固定电话和 Moden（猫），现在大多用不着了，国内改为了光线。
* 网口：RJ45，一般人见的最多的就是网口，连接的主要有「五类线」和「六类线」，六更好一点，支持千兆。

这两种接口看起来很相似，但网口更宽一点，看图就懂。

.. image:: https://kaffa.im/static/img/2023/rj45-rj11.png
    :alt: RJ45 和 RJ11 头

USB 接口
----------------------------------------

USB 是一种接口标准，主要用来传输电流和数据，对于本文发布日的人来说，不差钱尽量买 USB4。

USB 是一种综合接口，所以电流、视数据频、音频数据、文件数据等都不在话下。

.. class:: table is-bordered

    +----------------------------------------------+----------+------------------+--------------+
    | 标准                                         | 发布日期 | 最大电压电流支持 | 最大传输速率 |
    +==============================================+==========+==================+==============+
    | USB 1.0                                      | 1996.01  | 5V / 500mA       | 1.5 Mbps     |
    +----------------------------------------------+----------+------------------+--------------+
    | USB 1.1                                      | 1998.09  | 5V / 500mA       | 12 Mbps      |
    +----------------------------------------------+----------+------------------+--------------+
    | USB 2.0                                      | 2000.04  | 5V / 500mA       | 480 Mbps     |
    +----------------------------------------------+----------+------------------+--------------+
    | USB 3.0 --> USB 3.1 Gen1 --> USB 3.2 Gen1    | 2008.11  | 5V / 900mA       | 5 Gbps       |
    +----------------------------------------------+----------+------------------+--------------+
    | USB 3.1 --> USB 3.1 Gen2 --> USB 3.2 Gen2 x1 | 2013.07  | 20V / 5A         | 10 Mbps      |
    +----------------------------------------------+----------+------------------+--------------+
    | USB 3.2 -->                  USB 3.2 Gen2 x2 | 2017.09  | 20V / 5A         | 20 Mbps      |
    +----------------------------------------------+----------+------------------+--------------+
    | USB4                                         | 2019.09  | 20V / 5A         | 40 Mbps      |
    +----------------------------------------------+----------+------------------+--------------+

在 USB 标准之下，还有厂商的接口规格，大家常说的 Type-C，就是 USB 的一种类型，目前有大一统的趋势。

.. image:: https://kaffa.im/static/img/2023/usb-type-c.webp
    :alt: USB Type-C

如果是从业者，可能还需要了解 USB Type-A、USB Type-B，主要用于一些大的移动硬盘，打印机之类。

.. image:: https://kaffa.im/static/img/2023/usb-type-a-usb-type-b.webp
    :alt: USB Type-A and USB Type-B

从接口尺寸来说，还可以分为 USB / Mini USB / Micro USB，见到了就知道了。

.. image:: https://kaffa.im/static/img/2023/usb-mini-a-usb-mini-b.webp
    :alt: USB Mini A and USB Mini B

.. image:: https://kaffa.im/static/img/2023/usb-micro-a-usb-micro-b.webp
    :alt: USB Micro A and USB Micro B

USB 接口相关的接口标准和连接器
----------------------------------------

* Thunderbolt 接口标准：Intel 和 Apple，最新是第 4 代：

1. Thunderbolt-1
2. Thunderbolt-2
3. Thunderbolt-3
4. Thunderbolt-4

* Lightning(闪电) 连接器：源自 Apple，如从 iPhone 5 到 iPhone 14 使用的充电和数据连接线，从 iPhone 15 开始，已改为USB Type-C。


视频接口
----------------------------------------

现存接口主要有：VGA、DVI、HDMI、DP，VGA 和 DVI 已属于过去，未来主要是 HDMI 和 DP，且是 USB Type-C 形态。

.. class:: table is-bordered

    +-----------------------------------------------------------+--------+
    | 图片                                                      | 类型   |
    +===========================================================+========+
    |.. image:: https://kaffa.im/static/img/2023/dp-port.png    | DP     |
    |    :alt: DP                                               |        |
    +-----------------------------------------------------------+--------+
    |.. image:: https://kaffa.im/static/img/2023/hdmi-port.png  | HDMI   |
    |    :alt: HDMI                                             |        |
    +-----------------------------------------------------------+--------+
    |.. image:: https://kaffa.im/static/img/2023/dvi-port.png   | DVI    |
    |    :alt: DVI                                              |        |
    +-----------------------------------------------------------+--------+
    |.. image:: https://kaffa.im/static/img/2023/vga-port.png   | VGA    |
    |    :alt: VGA                                              |        |
    +-----------------------------------------------------------+--------+

支持视频的现代接口主要有HDMI，和后来居上的更开放的接口DP(DisplayPort)，主要版本如下

* DisplayPort / Mini DisplayPort

  * DisplayPort 1.2
  * DisplayPort 1.4
* HDMI

  * HDMI 1
  * HDMI 2

值得一提的是 Thunderbolt 接口，也逐步演化为 USB Type-C 形态：

1. Thunderbolt-1：Mini DisplayPort 集成
2. Thunderbolt-2：Mini DisplayPort 集成
3. Thunderbolt-3：USB Type-C 结合，集成供电
4. Thunderbolt-4：USB Type-C 结合，集成供电


音频
--------------------

不使用 HI-FI，音频相对简单，3.5mm接口与蓝牙4、5.0、5.1

还有一种最老式的三色 AV 线，常用在老式游戏设备和老式电视机的连接上。

如下图第二排后两张所示：

.. image:: https://kaffa.im/static/img/2023/av-port.jpg
    :alt: AV


电源
--------------------

一般使用厂商的原配线缆接口。

现在通用的是 USB4 Type-C。


结论
====================

可以看出，使用常规数码设备，未来 USB4 将是最通用的接口，只需随身携带这一种线，就是 USB4 Type-C。

或者期待基础科学能有新的突破，让无线充电技术还有新的发展。

世界上有那么多种类的连接线、连接器件，并不是因为无法设计为统一，而是商业目的。

所以对于新的专业设备，研发厂商需要获得创新红利，在商业目的驱使下，总会使用专有技术，专有线是永远不会消失的。

事物的演化是类似的，而为和跟进者PK、在将饱和的市场中竞争，或者触及垄断，专有技术又会逐步兼容开放技术。


如何确定两台设备用什么连接线
========================================

**方法就是查询产品的规格文档(specifications)，通过网站或者网店客服联系到厂家，拿到产品规格。**

事出我为我的 DELL XPS 购买了新外接显示器，为确定笔记本外接显示器时需使用和可使用什么线缆，特地梳理了现有的接口。

如果将此问题抽象化，可以表述为，为确定两台设备可以使用什么连接，需要分别查询设备A和设备B的接口规格，如果规格相同，则可以直接使用对等线缆连接，如果规格不同，则需要在市场上寻找连接线。

在我的例子中，我分别寻找了 XPS 和 HKC 支持的协议标准和接口规格

1. XPS NoteBook：`Dell 服务支持站 <https://www.dell.com/support/home/zh-cn/>`_ 查询笔记本规格 PDF 文件，其中有记录笔记本接口的详细说明。查询出支持 HDMI 1.4 port 和 Thunderbolt 3 port with PowerShare（USB Type-C），详细规格是 USB 3.1 Gen 2 + DisplayPort 1.2 + PowerShare(USB-C)

2. HKC Display：支持 HDMI1、HDMI2、DP 1.2

由此我们可以确定为使用为 DisplayPort 1.2 标准相互连接，需要一条支持 Thunderbolt 3 的 USB Type-C 转 DP 1.2 的线。

经查询，国内有很多厂商都做：

* `优籁特 <http://www.ult-unite.com/>`_
* `达而稳 <http://www.dorewin.cn/>`_
* 优联

在海外 Google 一下，发现 Dell 自己也做

* `绿联 <https://www.lulian.cn/>`_
* `海倍思 <http://cn.hagibis.com.cn/>`_
* `Anker <https://www.anker.com/>`_
* `Baseus <https://www.baseus.com/>`_
* `Belkin <https://www.belkin.com/>`_

可以说，上述品牌的都可以，只是有些擅长设计、有些侧重品牌营销、有些是源头工厂。

参考
==========

1. Thunderbolt: https://www.intel.com/content/www/us/en/architecture-and-technology/thunderbolt/overview.html
2. Thunderbolt Wiki: https://en.wikipedia.org/wiki/Thunderbolt_(interface)
3. Lightning Wiki: https://en.wikipedia.org/wiki/Lightning_(connector)
4. HDMI: https://www.hdmi.org/
5. DisplayPort: https://www.displayport.org/
6. DisplayPort Wiki: https://en.wikipedia.org/wiki/DisplayPort
