解决 Obsidian 插件 Advanced Tables 不显示表格的问题
############################################################

:date: 2024-04-06 16:00
:author: Kaffa
:category: digital
:tags: obsidian
:slug: solution-to-obsidian-advanced-tables-not-display-problem
:summary: 本文提供 Obsidian 插件 Advanced Tables 表格不显示的解决办法
:image: /static/img/2024/hero.png

问题现象
====================

进入原先带有表格的文章时，表格数据不显示。

问题解决
====================

方法一. 放弃 Advanced Tables
----------------------------------------

Advanced Tables 大概是使用在 Obsidian 创立了一种新标记，标记指向一个表格，此表格的列定义和数据均保存在 SQLite 中。这种做法的弊端在于如果 SQLite 损坏，此目录下所有的数据可能难以恢复。

因此，我选择导出表格数据，采用原生格式表格插入原文。步骤如下：

1. 进入带有表格文章的仓库路径下，会发现 context.mdb 文件，虽然文件使用了 Microsoft Access 数据库的扩展名，但这文件其实是 SQLite 数据库，此时可以使用 SQLite 数据库客户端打开它（比如 Windows上的 heidisql）。
2. 其中有三个定义表 files、m_fields、m_schema，然后用文本编辑器打开文章，会发现指向的表格名。例如：![![我的目录/#^Table2]]，在这里“我的目录”即目录名，Table2 即表格名，我们可在 context.mdb 中找到同名表格，并导出其数据。如此，导出除 files、m_fields、m_schema 之外的所有数据，并在原文中插入。
3. 停用第三方插件 Advanced Tables，重启 Obsidian，检查所有表格数据。
4. 如果数据正常，则可以用文本编辑器打开含有表格的 md 文件，删除其中的类似 ![![我的目录/#^Table2]] 的表格标记。

方法二. 给开发者提交缺陷，并等待修复
----------------------------------------

很感慨的是，Windows 10 依然可以打开 Windows 3.1 版本的程序。

而作为应用软件的 Obsidian 和 Advanced Tables 居然产生了问题。

首先需定位问题的产生是因为升级了 Obsidian 还是升级了 Advanced Tables。

如果 Obsidian 的升级导致了第三方插件异常，可能是因为插件的接口有调整（这种可能性较低），另一个可能是插件的实现依赖了 Obsidian 的内部实现而不是接口。

搞清状况后，可以先提交 issue，如果有能力，可以下载源码进行修复并 PR 官方关闭 issue。
