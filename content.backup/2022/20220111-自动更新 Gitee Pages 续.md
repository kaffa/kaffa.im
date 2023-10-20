Title: 自动更新 Gitee Pages 续
Date: 2022-01-11 12:00
Modified: 2022-01-11 12:00
Category: 随笔
Tags: 随笔, Essays, 博客, My Blog, 技术, Technology, Gitee Pages, PlayWright
Slug: update-gitee-pages-with-playwright-2
Authors: Kaffa
Summary: 2021年提供了一段 Python 代码解决免费 Gitee Pages 服务无法自动刷新的问题，这篇中随 PlayWright API 的更新相应更新了代码。


## 更新 Gitee Pages 静态站点的 Python 代码

    from playwright.sync_api import sync_playwright

    USERNAME = 'YOUR_USERNAME'
    PASSWORD = 'YOUR_PASSWORD'
    GITEE_PAGES_URL = 'https://gitee.com/kaffa/kaffa/pages'


    def main():
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto('https://gitee.com/login')
            page.click('input[name="user[login]"]');
            page.fill('input[name="user[login]"]', USERNAME);
            page.click('input[name="user[login]"]');
            page.fill('input[name="user[password]"]', PASSWORD);
            page.click("input[value='登 录']")
            page.wait_for_timeout(5000)
            page.goto(GITEE_PAGES_URL)
            page.on("dialog", lambda dialog: dialog.accept())
            page.click(".update_deploy")
            page.wait_for_selector('span:text("已开启 Gitee Pages 服务")', timeout=60 * 1000, state='visible')
            #browser.close()


    if __name__ == '__main__':
        main()


## 感谢 [chinabiue][2] 同学指正

2021年[提供了一段 Python 代码][3]解决免费 Gitee Pages 服务无法自动刷新的问题，由于目前 PlayWright API 的 API 命名由 Camel 变为了小写下划线，[chinabiue][2] 指出之前的代码出现报错，本文中一起修正了。以下是记录的过程。


以下是更新过程，个人的 pypi 源是使用的 douban。


    C:\WINDOWS\system32>pip install playwright --upgrade
    Looking in indexes: http://pypi.douban.com/simple
    Requirement already satisfied: playwright in c:\python39\lib\site-packages (0.171.1)
    Collecting playwright
      Downloading http://pypi.doubanio.com/packages/42/60/917ecb1a27bed6f13925df7c032efea2bba5e1e6b848812273dc2d361636/playwright-1.17.2-py3-none-win_amd64.whl (27.5 MB)
        |████████████████████████████████| 27.5 MB 6.8 MB/s
    Requirement already satisfied: pyee>=8.0.1 in c:\python39\lib\site-packages (from playwright) (8.1.0)
    Collecting websockets>=8.1
      Downloading http://pypi.doubanio.com/packages/43/5f/b237bebc4c483a17c2a2104fdcc2ed4322ac7fcb067917714b366480ce56/websockets-10.1-cp39-cp39-win_amd64.whl (97 kB)
        |████████████████████████████████| 97 kB 1.1 MB/s
    Collecting greenlet>=1.0.0
      Downloading http://pypi.doubanio.com/packages/bb/7b/2ac66aa5f9b7e07d62cd6c2c95d44036b609bda80e8739202e3551ee7bf3/greenlet-1.1.2-cp39-cp39-win_amd64.whl (101 kB)
        |████████████████████████████████| 101 kB 3.2 MB/s
    Installing collected packages: websockets, greenlet, playwright
      Attempting uninstall: greenlet
        Found existing installation: greenlet 1.0a1
        Uninstalling greenlet-1.0a1:
          Successfully uninstalled greenlet-1.0a1
      Attempting uninstall: playwright
        Found existing installation: playwright 0.171.1
        Uninstalling playwright-0.171.1:
          Successfully uninstalled playwright-0.171.1
    Successfully installed greenlet-1.1.2 playwright-1.17.2 websockets-10.1
    WARNING: You are using pip version 21.0.1; however, version 21.3.1 is available.
    You should consider upgrading via the 'c:\python39\python.exe -m pip install --upgrade pip' command.


    ╔═════════════════════════════════════════════════════════════════════════╗
    ║ Looks like Playwright Test or Playwright was just installed or updated. ║
    ║ Please run the following command to download new browsers:              ║
    ║                                                                         ║
    ║     playwright install                                                  ║
    ║                                                                         ║
    ║ <3 Playwright Team                                                      ║
    ╚═════════════════════════════════════════════════════════════════════════╝

    C:\WINDOWS\system32>playwright install
    Removing unused browser at C:\Users\USERNAME\AppData\Local\ms-playwright\chromium-833159
    Removing unused browser at C:\Users\USERNAME\AppData\Local\ms-playwright\firefox-1221
    Removing unused browser at C:\Users\USERNAME\AppData\Local\ms-playwright\webkit-1402
    Downloading Playwright build of chromium v939194 - 101.8 Mb [====================] 100% 0.0s
    Playwright build of chromium v939194 downloaded to C:\Users\USERNAME\AppData\Local\ms-playwright\chromium-939194
    Downloading Playwright build of ffmpeg v1006 - 1.4 Mb [====================] 100% 0.0s
    Playwright build of ffmpeg v1006 downloaded to C:\Users\USERNAME\AppData\Local\ms-playwright\ffmpeg-1006
    Downloading Playwright build of firefox v1304 - 74.2 Mb [====================] 100% 0.0s
    Playwright build of firefox v1304 downloaded to C:\Users\USERNAME\AppData\Local\ms-playwright\firefox-1304
    Downloading Playwright build of webkit v1578 - 41.3 Mb [====================] 100% 0.0s
    Playwright build of webkit v1578 downloaded to C:\Users\USERNAME\AppData\Local\ms-playwright\webkit-1578


感谢阅读。如果上述内容和代码片段对你有帮助，可通过以下二维码请杯咖啡。

![我的赞赏码](https://kaffa.im/img/reward.png "我的赞赏码")


[1]: https://kaffa.im/img/reward.png
[2]: https://github.com/chinabiue
[3]: https://kaffa.im/update-gitee-pages-with-playwright.html