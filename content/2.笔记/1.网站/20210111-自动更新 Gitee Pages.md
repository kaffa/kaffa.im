Title: 自动更新 Gitee Pages
Date: 2021-01-11 12:00
Modified: 2021-01-11 12:00
Category: website
Tags: Gitee Pages, PlayWright
Slug: update-gitee-pages-with-playwright
Authors: Kaffa
Summary: 本文提供一段 Python 代码，用来解决免费 Gitee Pages 服务无法自动刷新。
 
## 2022-01-11 更新

本文写于2021年1月11日，PlayWright 当时的版本是 0.171.1，本文代码已不适用最新版 PlayWright，获取新版代码，请移步《20220111-自动更新 Gitee Pages 续》。

## 更新 Gitee Pages 静态站点

由于在 Gitee Pages 备份了个人博客，但免费用户 Gitee Pages 服务不能像 Github Pages 一样自动发布，
网上有利用 Github Action 实现的现成解决方案，但刷新 Gitee Pages 是点击按钮的简单任务，不如自己搞定。

## Python 代码

    import time
    from playwright import sync_playwright

    USERNAME = 'YOUR_USERNAME'
    PASSWORD = 'YOUR_PASSWORD'
    GITEE_PAGES_URL = 'https://gitee.com/kaffa/kaffa/pages'
    
    
    def main():
        with sync_playwright() as p:
            for browser_type in [p.chromium]:
                browser = browser_type.launch(headless=False)
                page = browser.newPage()
                page.goto('https://gitee.com/login')
                page.click('input[name="user[login]"]');
                page.fill('input[name="user[login]"]', USERNAME);
                page.click('input[name="user[login]"]');
                page.fill('input[name="user[password]"]', PASSWORD);
                page.click("input[value='登 录']")
                time.sleep(3)
                page.goto(GITEE_PAGES_URL)
                page.on("dialog", lambda dialog: dialog.accept())
                page.click(".update_deploy")
                page.waitForSelector('span:text("已开启 Gitee Pages 服务")', timeout=60 * 1000, state='visible')
                browser.close()
    
    if __name__ == '__main__':
        main()


## 代码说明

从编程角度上，实现 Git Push 完后自动更新 Gitee Pages，需要当 Git Push 完成时发送消息，消息订阅方接收到该息后执行更新操作。
现实中这些通常由持续集成（CI）服务器来做，但 Gitee 的持续集成服务 Gitee Go 是收费服务。

不如换个思路，即提交 Github 和 Gitee 完成后，追加一次点击 Gitee Pages 更新按钮的操作，该操作最后是客户端发出一个 Http Post 请求，
复杂而不好的办法是直接构造该请求的数据，但为实现“一次编写，一直运行”，也为防止点按钮时还做了什么其它较风骚的操作，
这里选择使用了 Headless Testing 的方法。

这条道路主流是沿着 Selenium -> Puppeteer -> PlayWright 进行的，特别是 PlayWright 团队，原先就是从 Google 的 Puppeteer 
转到 [Microsoft PlayWright][6]，毕竟，能把创造和改造的轮子从 Chrome 扩展到 Firefox 到 Webkit 谁不想呢？

说回 Headless Testing，这种方式没有直接发送 Http Post 请求迅速，但需要维护代码的可能性低，且更易维护。对个人来说，
启动时把 headless 参数改为 True，多等十秒问题也不大。

代码中有两点值得一提：

1. ```page.waitForSelector``` 方法，文档的第二个参数，在 node.js 语法中是传入 Object，但在 Python 中的用法是多个参数，
这一点上由于 Python 版的 PlayWright 文档不详细，需在 PyCharm 中按 Ctrl 看源码提示才能看到；
2. ```page.on("dialog", lambda dialog: dialog.accept())``` 表示在 alert 弹出框上点击确定。

其余代码直白到十岁小友也可看懂，不再解释。

### 搜索关键字和延伸

[Gitee Pages][2], [PlayWright][3], [playwright-python][4], [Headless Testing][5]  


感谢阅读。如果上述内容和代码片段对你有帮助，请扫描二维码打赏一杯咖啡。

![我的赞赏码](https://kaffa.im/static/img/reward.png "我的赞赏码")

[1]: https://kaffa.im/static/img/reward.png
[2]: https://gitee.com/help/articles/4136
[3]: https://playwright.dev/
[4]: https://github.com/microsoft/playwright-python
[5]: https://headlesstesting.com/ 
[6]: https://www.infoq.com/news/2020/01/playwright-browser-automation/
