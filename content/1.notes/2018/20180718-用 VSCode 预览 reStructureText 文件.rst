用 VSCode 预览 reStructureText 文件
##################################################

:date: 2018-07-18 12:30
:author: Kaffa
:category: digital
:tags: VSCode, reStructureText
:slug: preview-restructuretext-file-in-vscode
:summary: 本文描述用 VSCode 预览 reStructureText 文件的配置办法


通识
====================

1. 得益于拥抱开源，微软 VSCode 成为了最热门的 IDE，广泛用于各种场景的编程，比如编辑 reStructureText 文件。

2. reStructureText 是 Python 官方文档的格式，属于 Sphinx 项目的一部分，Sphinx 是 Python 文档生成器。

3. 从 reStructureText 的文件格式 rst，方便转化为各种文件格式。

4. MS Code 自带 reStructureText 插件，类似于 Markdown，安装后可以用于预览 rst 格式。

5. 可安装后并不能直接预览，还需要配置一番，于是就有了下面的部分。


配置
===================
1. 依据 reStructureText 文档，先 pip 安装 doc8 和 sphinx

2. 再上 MSCode 配置::

    // Points to the doc8 exectuable.
    "restructuredtext.linter.executablePath": "doc8",
    // Extra arguments to doc8.
    "restructuredtext.linter.extraArgs": ["--max-line-length 1024"],
    // The full path of sphinx-build utility. This is an absolute path, and you can use ${workspaceRoot} to represent workspace root folder.
    "restructuredtext.sphinxBuildPath": "sphinx-build",
    // Flag to control whether text changed event triggers preview update.
    "restructuredtext.updateOnTextChanged": "true",

3. 在项目根目录下运行::

    sphinx-quickstart

一路回车下去，即生成了如下文件::

    _build
    _static
    _templates
    conf.py
    index.rst
    make.bat
    Makefile

此时可以通过 Ctrl+Shift+R 来预览了

4. 最后提供一份快速参考 sphinx-rest_



感谢阅读。

.. _sphinx-quickstart: http://www.pythondoc.com/sphinx/tutorial.html
.. _sphinx-rest: http://www.pythondoc.com/sphinx/rest.html
