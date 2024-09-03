import os
import sys
import MySQLdb


class Friend:
    ID = 0
    Name = ''
    URL = ''


def get_list():
    return [
        {
            'ID': 1,
            'Name': '槿呈Goidea',
            'URL': 'https://justgoidea.com/',
            'Intro': '读书｜新知｜生活禅',
            'Owner': '槿呈Goidea',
            'Icon': 'https://justgoidea.com/icon.svg',
            'Email': 'me@hhzz.top',
        }, {
            'ID': 2,
            'Name': '欧雷流',
            'URL': 'https://ourai.ws/',
            'Intro': '我叫欧雷，是一个出生于上世纪 80 年代的理想主义叛逆青年。喜欢日本，热爱咖啡，善于总结。这里有我对技术和语言的研究，也有对世界和生活的思考。',
            'Owner': '欧雷',
            'Icon': 'https://ourai.ws/assets/avatars/ourai-100px-3bcaa1cb0c7fa0547d15622572d74a8bbc98a5f62e4920ecddb72ca95e505d17.jpg',
            'Email': ''
        }, {
            'ID': 3,
            'Name': '雅余',
            'URL': 'https://yayu.net/',
            'Intro': '一位爱喝咖啡的产品经理曾经是位设计师，偶尔捣腾代码，不玩摄影的时候也泡泡工夫茶。',
            'Owner': '晨间风、Jeff',
            'Icon': 'https://yayu.net/wp-content/themes/yayu/assets/images/logo.png',
            'Email': 'hi@yayu.net',
        }, {
            'ID': 4,
            'Name': '非理勿试',
            'URL': 'https://www.ntiy.com/',
            'Intro': '“Never Try It Yourself”，记录、分享、学习',
            'Owner': 'Soulizer、欧阳桂花、谢让',
            'Icon': '/static/img/2024/ntiy_logo_o.png',
            'Email': 'collect@live.com',
        }, {
            'ID': 5,
            'Name': '有思想的芦苇',
            'URL': 'https://thinking-reed.cn/',
            'Intro': "我是一名正在川渝地区某高校攻读人工智能方向的研究生，喜欢编程，技术，哲学，心理学，期待与您交朋友!",
            'Owner': '芦苇',
            'Icon': 'https://thinking-reed.cn/images/avatar.png',
            'Email': '',
        }, {
            'ID': 6,
            'Name': '印记',
            'URL': 'https://yinji.org/',
            'Intro': '君子可内敛不可懦弱，面不公可起而论之',
            'Owner': 'Bruce，Blogger/摄影爱好者/数码发烧友',
            'Icon': 'https://huhexian.s3.bitiful.net/2023/12/23/3b83cc067b2c3f1e45807dfdeb66e0c0.webp',
            'Email': 'huhexian0206@gmail.com',
        }, {
            'ID': 7,
            'Name': '陈仓颉',
            'URL': 'https://imzm.im/',
            'Intro': '以有涯随无涯',
            'Owner': '陈仓颉',
            'Icon': 'https://imzm.im/wp-content/uploads/2023/05/logo50px.png',
            'Email': 'zm.rayme@gmail.com',
        }, {
            'ID': 8,
            'Name': '松易涅的写作分享站',
            'URL': 'https://www.sungyinieh.com/flinks',
            'Intro': '回顾历史，审视当下，期盼未来',
            'Owner': '松易涅',
            'Icon': 'https://avatars.githubusercontent.com/u/115633657?u=6bb5bee98c33bbd8d80a0e3ea0308d716504de33&v=4',
            'Email': 'mail@songyinie.com',
        }, {
            'ID': 9,
            'Name': '七仔的博客',
            'URL': 'https://www.baby7blog.com',
            'Intro': '主要记录自己在写程序过程中的发现、问题、成果',
            'Owner': '七仔',
            'Icon': 'https://www.baby7blog.com/favicon.ico',
        }, {
            'ID': 10,
            'Name': '浪海导航',
            'URL': 'https://www.langhai.net/',
            'Intro': '收录各种类型的博客',
            'Owner': '浪海导航',
            'Icon': 'https://www.langhai.net/assets/images/langhai-logo.png',
            'Email': '676558206@qq.com'
        }, {
            'ID': 11,
            'Name': '清阳livingWithFCS',
            'URL': 'https://conge.livingwithfcs.org/',
            'Intro': '记录读过的书和跑过的路。',
            'Owner': 'Conge',
            'Icon': 'https://conge.livingwithfcs.org/favicon.ico',
            'Email': ''
        }, {
            'ID': 12,
            'Name': '@1900\'Blog',
            'URL': 'https://1900.live/',
            'Intro': 'All work and no play makes Jack a dull boy。',
            'Owner': '1900',
            'Icon': 'https://cdn.1900.live/20190640/ico.png',
            'Email': ''
        }, {
            'ID': 13,
            'Name': '拾月',
            'URL': 'https://www.skyue.com/',
            'Intro': '日常关注互联网、软件应用居多，也喜欢股票投资、社科历史。执着于掌控自己的数据，self-host 爱好者。',
            'Owner': 'SKYue',
            'Icon': 'https://www.skyue.com/favicon.ico',
            'Email': 'skyue.hu@gmail.com'
        }, {
            'ID': 14,
            'Name': '啤酒加冰',
            'URL': 'http://teddy.bell.cf/',
            'Intro': '一个技术宅的日常',
            'Owner': '',
            'Icon': '/static/img/2024/teddy-logo.jpg',
            'Email': 'Teddy Bell'
        }
    ]
