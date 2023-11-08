Title: VSCode Insert Filename
Date: 2019-07-23 12:00
Modified: 2023-11-08 15:00
Category: software
Tags: VSCode, VSCode Extension, vsce, Visual Studio Marketplace
Slug: vscode-extension-insert-filename
Authors: Kaffa
Summary: 本文是我为讲解如何发布 VSCode 扩展到 Visual Studio Marketplace 而编写的插件VSCode Insert Filename，通过本文你将学会创作和发布 VSCode 扩展的步骤和方法。


![编写 VSCode 插件](https://kaffa.im/static/img/2019/create-vscode-extension.png "编写 VSCode 插件")

## 假设

假设你熟悉 node.js 和 npm 工具，用过 Git，并懂点 JavaScript，那么本文将一步步教你编写一个 VSCode 扩展，并发布到微软 Visual Studio Marketplace。

## 概述

VSCode 已是免费文本编辑器/IDE的王者，但其文本闪改能力还是不如一些老牌文本编辑器，比如 EverEdit 与 EmEditor，但它免费呀，所以，用它用它用它。

在文本中插入文件名是个常用场景，比如编辑本文时，第一行就会用到，笔者在 EverEdit 和 EmEditor 中编写过脚本插件，基本都只需要一个文件和几行脚本代码。

考虑到 VSCode 有一个全球生态，那么 Visual Studio Marketplace 中是否能找到一个类似的插件呢，答案是：没有。于是，我们做一个呗。

![If not me, who? If not now, when?](https://kaffa.im/static/img/2019/if-not-me-who-if-not-now-when.png "If not me, 
who? If not now, when?")

在 VSCode 关于中，我们可以看到它的技术栈如下，其插件采用 JavaScript 或 TypeScript 编写。

* Electron: 4.2.5
* Chrome: 69.0.3497.128
* Node.js: 10.11.0
* V8: 6.9.427.31-electron.0

## 具体步骤

1、假设你已安装 node.js 和 git

2、如果你没有用过 Yeoman 脚手架工具，那么现在正是时候，装上它

`npm install -g yo generator-code`

3、利用 Yeoman 建立项目框架

`yo code`

<pre>
    # ? What type of extension do you want to create? New Extension (TypeScript)
    # ? What's the name of your extension? insert-filename
    ### Press <Enter> to choose default for all options below ###
    # ? What's the identifier of your extension? insert-filename
    # ? What's the description of your extension?
    # ? Initialize a git repository? Yes
    # ? Which package manager to use? npm
</pre>

扩展项目就创建好了，下一步，让我们运行起来。

4、执行

`code ./insert-filename`

再按 `F5` 运行，这时，VSCode 会启动一个新窗口，这个窗口中 Yeoman 脚手架项目 insert-filename 已经加载了插件。

5、让我们按下 `Ctrl + Shift + P`，输入 `insert-filename`，可以看到这条命令，回车后应该可以看到一条 Hello World！的信息在 VSCode 的右下角弹出来。

6、接着，我们便可以开始编写插入文件名的代码了，还可以调试哟！让我们打开 `src/extension.ts` 文件。为便于理解，请参阅中文注释。
<pre>
    import { commands, workspace, window, ExtensionContext } from 'vscode';

    // 在所有选区中插入文件名
    function replaceEditorSelection() {
        const editor = window.activeTextEditor;
        if (editor === undefined) {
            return;
        }
        const selections = editor.selections;
        editor.edit((editBuilder) => {
        selections.forEach((selection) => {
            let url = editor.document.fileName;
            let urlFormatted = url.replace(/\\/g, '/');
            let lastPart = urlFormatted.split('/').pop() || '';
            editBuilder.replace(selection, '');
            editBuilder.insert(selection.active, lastPart);
        });
        );
    }

    // 插件激活
    export function activate(context: ExtensionContext) {
        console.log('Congratulations, your extension "Insert Filename" is now active!');
        // 注册一条命令
        let disposable = commands.registerCommand('extension.insertFilename', () => replaceEditorSelection());

        context.subscriptions.push(disposable);
    }

    // 插件待用
    export function deactivate() {
        console.log('Your extension "Insert Filename" is now inactive!');
    }
</pre>

7、其次，最重要的是编辑 package.json 文件，最重要的 contributes 配置，以下配置分别在命令、编辑器右键菜单上注册了此命令，并设置其快捷键。

<pre>
    "contributes": {
        "commands": [
            {
                "command": "extension.insertFilename",
                "title": "Insert Filename"
            }
        ],
        "menus": {
            "editor/context": [
                {
                    "command": "extension.insertFilename",
                    "group": "extension@1"
                }
            ]
        },
        "keybindings": [
            {
                "command": "extension.insertFilename",
                "key": "ctrl+alt+i",
                "mac": "shift+cmd+i",
                "when": "editorTextFocus"
            }
        ]
    }
</pre>

8、更详细的代码和配置文件请移步 GitHub 仓库：[vscode-insert-filename 插件源码][3] 。

## 编译发布

到目前为止，我们的测试都是直接运行插件，现在让我们对项目进行编译，得到 insert-filename-0.0.2.vsix 文件，就可以进行发布了。

9、为编译插件，我们需要下载微软 VSCode Extension 工具：vsce

`npm install -g vsce`

10、安装完毕后，让我们执行如下指令进行编译

`vsce package`

11、编译成功后，项目目录中会得到 insert-filename-0.0.2.vsix 文件，再运行如下命令发布

`vsce publish`

不出意料，你会得到 401 错误，是因为向微软市场发布这个插件，需要一个 [Azure DevOps][4] 账号，你可以用一个 Microsoft 账号登录跳转注册 [Azure DevOps][4] 即可。

接下来，我们不用创建项目，直接在右上角个人头像菜单 `Security` 中创建一个 Personal Access Tokens，选项如下，先点击 `Show all scopes`

* Organization：All accessible organization
* Scopes: Marketplace 中的 Acquire and Manage

再点击 `Create` 按钮，生成成功后，点击 `Copy`，**注意**：这个Token只会在这个时候出现一次，所以，你得找一个不会忘记的地方记录下来。

再执行此命令，将其中的 kaffa 换成你的 id，输入刚才创建的 Token

`vsce create-publisher kaffa`

12、发布

`vsce publish`

到这里，我们的插件就发布成功了，过几分钟，就可以官网看到你的插件了，并可以在 VSCode 插件中搜索了，记得做一些关键字 SEO，并升级一下版本。

## 总结

本插件发布在 [Visual Studio Marketplace][4]，欢迎下载使用。

祝各位读者读完本文，能顺利安装、编写、编译、发布你的插件，如果在具体步骤中遇到问题，请回复和留言。

感谢观阅！

本站所有写作都是免费的，如果您觉得有用，可以微信扫赞微微鼓励！

![我的赞赏码](https://kaffa.im/static/img/reward.png "一杯咖啡吸取太阳能量")

[1]: https://kaffa.im/static/img/reward.png
[2]: http://www.everedit.net/
[3]: https://github.com/kaffa/vscode-insert-filename
[4]: https://marketplace.visualstudio.com/items?itemName=kaffa.insert-filename
[5]: https://aka.ms/SignupAzureDevOps
