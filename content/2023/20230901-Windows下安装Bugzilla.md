Title: 在 Windows 上安装 Bugzilla
Date: 2023-09-01 22:24
Modified: 2023-09-01 22:24
Category: 随笔
Tags: 随笔, Essays, Bugzilla
Slug: bugzilla-installation-on-windows
Authors: Kaffa
Summary: 记录在 Windows 上安装 Bugzilla 的过程


## 有关 Bugzilla 的回忆

曾在 15 年前和 6 个朋友一起协同开发时，我安装过 Bugzilla。缺陷管理，最早在腾讯的开发组使用的是禅道，后来其他部门开发了TAPD，我大约是看到ZQ大妈介绍的在金山公司使用的 Bugzilla 分支。
那是的版本大约是 2 或 3，鬼知道当年是如何在 Windows 下安装好 Bugzilla 的，印象中安装有一些错误，但不影响最终的使用。

那时候的互联网还不那么快，但也还没有墙，只知道软件协同开发需要使用缺陷管理工具，在当时是相当先进的思想。

大约在 bugzilla 中管理了几十个缺陷，缺陷的流转也是挺自然的，可谓一用就会。在好来，由于我们需要引入异地协同开发，而我们的 Bugzilla 部署在本机，最后大家还是觉得用一张 Excel 飞来飞去比较轻便。好在组内沟通不太频繁，要不使用一张 Excel 来维护缺陷，就是一个噩梦。


## 再装 Bugzilla

由于自己有开发两个产品，看到 Bugzilla 已经更新到 5，之前和朋友提起过 Perl，说 Perl 的软件，我还是很喜欢的，比如 Bugzilla 和 MovableTyp。

可能比较怀旧，于是重新又在本机安装了新版的 Bugzilla，配置的地址是 http://bugs.k.com/，准备在产品中用起来。

安装过程是按官方文档的，由于本机已经安装了 Apache 和 MariaDB，所以只需要安装 Perl 和 配置 Apache CGI

Perl 是使用的 Strawberry 发行版。

Apache 使用的 2.4 ，个人习惯配置一个 v-hosts 节点。

```ini
<VirtualHost *:80>
    ServerAdmin     admin@l.com
    DocumentRoot    "d:/web/bugzilla"
    ServerName      bugs.k.com
    ErrorLog        "d:/logs/bugs.l.com-error.log"
    CustomLog       "d:/logs/bugs.l.com-access.log" common
    Alias "/bugzilla/" "d:/web/bugzilla/"
    AddHandler cgi-script .cgi
    ScriptInterpreterSource Registry-Strict 
    <Directory "d:/web/bugzilla">
        ScriptInterpreterSource Registry-Strict
        Options +ExecCGI +FollowSymLinks
        DirectoryIndex index.html index.cgi 
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

其余的注册表配置

```TEXT
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\.cgi\Shell\ExecCGI\Command]
@="C:\\Strawberry\\perl\\bin\\perl.exe -T"
```


安装过程按文档一切都很顺利。
