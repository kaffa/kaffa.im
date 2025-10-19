上 NextCloud，一站搞定个人数据同步
####################################################################################################

:date: 2025-10-19 22:52
:author: Kaffa
:category: digital
:tags: NextCloud,WebDAV,Obsidian,Remotely Save,Joplin
:slug: nextcloud-one-stop-personal-data-sync
:summary: 本文记录了我的个人数据同步的选择，使用 NextCloud 解决个人数据同步。


个人数据同步需求
====================

1. 个人数据能完全个人控制；
2. 个人数据能实现跨平台的多端同步。
3. Obsidian 作为知识库，能实现同步。

解决方案
====================

手动安装 NextCloud，实现个人数据同步。主要过程还是 LAMP 技术栈：

1. 选择 Ubuntu 系统
2. 在 Ubuntu 上安装 Apache 2
3. 在 Ubuntu 上安装 MySQL/MariaDB
4. 在 Ubuntu 上安装 PHP 8.3
5. 使 LAMP 栈配合运行起来
6. 在 Apache 配置文件中，增加该站点配置，重启 Apache
7. 创建 数据库，并准备好数据库名、用户名和密码
8. 输入站点 URL，输入刚才的数据库信息，进行安装。


WebDAV
====================

由于 NextCloud 提供了 WebDAV 服务，因此基于 WebDAV 进行文件同步的常见服务都可以寄生于此。

1. Obsidian：可利用 Remotely Save 插件，配置 WebDAV 的 URL、用户名、密码，实现同步；
2. Joplin：如果希望自己掌握自己的数据，可以使用开源且注重安全的笔记软件。在前期的选型中，有 AnyType、Joplin、Logseq、Trilium Notes 等入我法眼，在目前的工作中，以金融为主，因此没有选择非常 Geek 的 Trilium Notes。


主要参考
====================

`官方文档 <https://docs.nextcloud.com/server/latest/admin_manual/installation/index.html>`_

遇到的问题记录
====================

1. Config 文件，不能 Copy config.sample.php 文件，而只需要从其中复制需要修改的项。

2. "Temporary directory /tmp/nextcloudtemp is not present or writable"

使用下面的命令，增加临时目录权限::

    sudo mkdir -p /tmp/nextcloudtemp
    sudo chown -R www-data:www-data /tmp/nextcloudtemp
    sudo chmod 755 /tmp/nextcloudtemp


3. "Call to undefined function Sabre\\\\HTTP\\\\mb_check_encoding()"

安装 php-mbstring 扩展，类似的还有 GD 库::

    sudo apt-get install php8.3-mbstring


4. 看起来您正在尝试重新安装您的 Nextcloud。但您的 config 文件夹中没有 CAN_INSTALL 文件。请在您的 config 文件夹中创建 CAN_INSTALL 文件以继续。

这个问题似乎是在重新修改了 config.php 文件，加入了 index.php 的省略造成的，解决方式为，重新安装一次全新包，另一个可能的原因可能是下载插件时产生的。

