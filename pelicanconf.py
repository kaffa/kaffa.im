#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import inspect
import urllib.parse
import os
import sys
from functools import partial
sys.path.append(os.curdir)
import projects
import friends


AUTHOR = 'Kaffa'
AUTHOR_NAME = 'Kaffa'
SITENAME = '<span class="is-italic author_name">Kaffa</span>.im'
SITESUBTITLE = ''  # 'Kunnect Adventures & Fun'

MANTRA = '<span class="has-text-grey is-size-6"><span class="is-italic author_name">K</span>unnect</span>'\
         '<sup class="has-text-grey is-size-7">'\
         '  <span class="is-italic author_name">a</span>dventures & <span class="is-italic author_name">f</span>un'\
         '</sup>'
AUTHOR_INTRO = '「探索」人生，共享「意趣」。'  # 专注「软件研发」吧和「业务数字化」。

SITEURL = 'https://kaffa.im'
TIMEZONE = 'Asia/Shanghai'

GITHUB_URL = 'http://github.com/kaffa/'

PATH = 'content'
OUTPUT_PATH = 'docs/'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %a'
DEFAULT_LANG = 'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    {'group': '数字花园', 'items': (
        ('仿生猫不会梦见电子猫粮', 'https://jefftay.com/'),)},
    {'group': '收录', 'items': (
        ('十年之约', 'https://www.foreverblog.cn'),
        ('BlogFinder', 'https://bf.zzxworld.com'),
        ('个站商店', 'https://storeweb.cn/'),
        ('博客志', 'http://www.jetli.com.cn'),
        ('积薪', 'https://firewood.news'),
        ('博客圈', 'https://bkq.net.cn/'),)},
    {'group': '链接', 'items': (
        ('Paul Graham', 'http://paulgraham.com'),
        ('Guido van Rossum', 'https://gvanrossum.github.io/'),
        ("Coffee's", 'https://coffees.app'),
        ('论道', 'https://lundao.pub/'),)},
]
# Social widget
SOCIAL = (('My GitHub', 'https://github.com/kaffa'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# 20190518 添加
DISPLAY_CATEGORIES_ON_MENU = False

# 20230913 添加
# 20231019 修改
DISPLAY_PAGES_ON_MENU = False

# THEME = "D:/code/github/kaffa/kaffa.github.io/themes/pelican-octopress-theme-cn"
THEME = "D:/code/github/kaffa/kaffa.github.io/themes/pelican-kaffa-theme"
THEME_STATIC_DIR = 'static'

STATIC_PATHS = ['static']
EXTRA_PATH_METADATA = {
    'static/favicon/favicon.ico': {'path': 'favicon.ico'},
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
}
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'sitemap',
    'plantuml',
    'featured_image',
    'kaffapod'
    # 'statics',
    # 'minify'
    # 'gravatar',
    # 'ace_editor'
]

# plugin: sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    'exclude': [
        'tag/',
        'category/'
    ]
}

# plugin: kaffapod
KAFFAPOD = {
    # SQLite 数据库相对 PATH 目录的路径
    'db_path': r'\db\0.db',
    # img 本地目录
    'img_folder': os.path.join(os.path.dirname(inspect.getfile(inspect.currentframe())), PATH, THEME_STATIC_DIR, 'img'),
    # img 相对目录，用于 web 拼接
    'img_relative_folder': '/static/img/'
}

JINJA_FILTERS = {
    'sort_by_article_count': partial(sorted, key=lambda tag: len(tag[1]), reverse=True)
}


# plugin: plantuml
PLANTUML = {
    'java_path': r'C:\Java\jdk-11.0.11\bin\java.exe',
    'plantuml_jar_path': r'D:\soft\plantuml-jar-gplv2-1.2023.7\plantuml.jar',
    'uml_image_folder': '/static/img/'
}

# plugin: ace_editor
ACE_EDITOR_PLUGIN = {
    'ACE_EDITOR_THEME': 'chrome',
    'ACE_EDITOR_SCROLL_TOP_MARGIN': 0,
    'ACE_EDITOR_MAXLINES': 50,
    'ACE_EDITOR_READONLY': True,
    'ACE_EDITOR_AUTOSCROLL': True,
    'ACE_EDITOR_SHOW_INVISIBLE': True
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': False,
            'use_pygments': True
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# plugin: minify
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

COLORFUL_SITENAME = '''<
    span style="color:#52A2C6">褪</span><
    span style="color:#6791BC">色</span><
    span style="color:#7C80B2">的</span><
    span style="color:#916FA8">抽</span><
    span style="color:#A65E9E">象</span>'''

# My Data
AVATAR_URL = 'https://kaffa.im/static/img/kaffa-avatar.png' #'https://avatars.githubusercontent.com/u/4386281?v=4'

# mailto
mailto_email = urllib.parse.quote('admin@kaffa.im')
mailto_subject = urllib.parse.quote('网站反馈')
mailto_body = urllib.parse.quote('提示：可反馈“在什么场景下，做什么操作时，遇到什么问题。”')
mailto = f'mailto:{mailto_email}?subject={mailto_subject}&body={mailto_body}'

# menu
MENUITEMS = (
    ("专栏", "/", (
        ("项目", "/category/project.html"),
        ("-", ""),
        ("研发", "/category/development.html"),
        ("编程", "/category/programming.html"),
    )),
    ("笔记", "/", (
        ("网站", "/category/website.html"),
        ("-", ""),
        ("阅读", "/category/reading.html"),
        ("-", ""),
        ("数智", "/category/digital.html"),
        ("-", ""),
        ("言论", "/category/words.html")
    )),
    ("创作", "/", (
        ("文章", "/category/article.html"),
        ("-", ""),
        ("软件", "/category/software.html"),
        ("-", ""),
        ("书单", "/category/book-list.html"),
        ("-", ""),
        ("周报", "/category/weekly.html"),
    )),
    ("我的", "/", (
        ("书", "/category/book.html"),
        ("影", "/category/movie.html"),
        ("音", "/category/music.html"),
        # ("-", ""),
        # ("店", "/category/shop/"),
        # ("食", "/category/food/"),
        ("-", ""),
        ("物", "/category/things.html"),
    )),
    ("关于", "/", (
        ("站长", "/pages/about.html"),
        ("网站", "/pages/about-website.html"),
        ("联系我", "/pages/contact.html"),
        ("-", ""),
        ("网站反馈", mailto),
    )),
)

CATEGORY_DICT = {
    'project': {'name': '项目', 'moment': '启动一个项目'},
    'development': {'name': '研发', 'moment': '记录一篇随笔'},
    'programming': {'name': '编程', 'moment': '记录一篇随笔'},

    'website': {'name': '网站', 'moment': '记录一条笔记'},
    'reading': {'name': '读书', 'moment': '记录一条笔记'},
    'digital': {'name': '数智', 'moment': '记录一条笔记'},
    'words': {'name': '言论', 'moment': '记录一条言论'},

    'article': {'name': '文章', 'moment': '创作一篇文章'},
    'software': {'name': '软件', 'moment': '记录一个软件'},
    'book-list': {'name': '书单', 'moment': '精选一款书单'},
    'weekly': {'name': '周报', 'moment': '汇报一次周报'},

    'book': {'name': '书', 'moment': '阅读一本书籍'},
    'movie': {'name': '影', 'moment': '观赏一部电影'},
    'music': {'name': '音', 'moment': '收藏一首音乐'},
    'things': {'name': '物', 'moment': '标记一个物品'},
}

GROWTH_DICT = {
    '1': {'img': 'seedling.svg', 'title': '幼苗'},
    '3': {'img': 'budding.svg', 'title': '发育中...'},
    '5': {'img': 'evergreen.svg', 'title': '常青树'},
}

JAVASCRIPT_HEAD = ''
JAVASCRIPT_FOOT = ''

PROJECTS = projects.get_list()
FRIENDS = friends.get_list()
