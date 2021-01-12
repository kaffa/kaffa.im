Title: 自动更新 Gitee Pages
Date: 2021-01-11 12:00
Modified: 2021-01-11 12:00
Category: 随笔
Tags: 随笔, Essays, 技术, Technology, Gitee Pages，PlayWright
Slug: update-gitee-pages-with-playwright
Authors: Kaffa
Summary: 本文提供一段 Python 代码，用来解决免费 Gitee Pages 服务无法自动刷新。
 

## 更新 Gitee Pages 静态站点

由于在 Gitee Pages 备份了个人博客，但免费用户 Gitee Pages 服务不能像 Github Pages 一样自动发布，
网上有利用 Github Action 实现的现成解决方案，但刷新 Gitee Pages 是点击按钮的简单任务，不如自己搞定。


## Python 代码

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
                browser.close()
    
    
    if __name__ == '__main__':
        main()


## 说明

实现自动更新，本质上只是发出一个 Http 请求，但不知是否有其他保护，
为“一次编写，一直运行”，这里使用了来自微软的类似 Selenium 的 PlayWright 库，
这种方式没有直接发送 Http Post 请求快，但需要维护的可能性低，且更易维护。
这句 ```page.on("dialog", lambda dialog: dialog.accept())``` 表示弹出框点击确定，
其余代码直白到十岁小友也可看懂，不再解释。

### 搜索关键字

[Gitee Pages][2], [PlayWright][3], [playwright-python][4]


感谢阅读。

[1]: https://kaffa.im/img/reward.png
[2]: https://gitee.com/help/articles/4136
[3]: https://playwright.dev/
[4]: https://github.com/microsoft/playwright-python 
