#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import urllib.parse
import os
import sys

AUTHOR = 'Kaffa'
AUTHOR_NAME = '昆'
MANTRA = 'Kunnect Adventures & Fun'
AUTHOR_INTRO = '「探索」人生，共享「意趣」，主研方向是「软件研发 + 技术管理」和「业务数字化」，有兴趣或有反馈请点击菜单项的关于。'

SITENAME = 'Kaffa.im'
SITESUBTITLE = ''  # 'Kunnect Adventures & Fun'
SITEURL = 'https://kaffa.im'
TIMEZONE = 'Asia/Shanghai'

GITHUB_URL = 'http://github.com/kaffa/'

PATH = 'content'
OUTPUT_PATH = 'docs/'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %a'
DEFAULT_LANG = 'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Paul Graham', 'http://paulgraham.com'),
         ('Guido van Rossum', 'https://gvanrossum.github.io/'),
         ("Kaffa.im", 'https://kaffa.im'),
         ("Coffee's", 'https://coffees.app'),
         ('论道', 'https://lundao.pub/'),)

# Social widget
SOCIAL = (('My GitHub', 'https://github.com/kaffa'),)

DEFAULT_PAGINATION = 6

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
    #'statics',
    #'minify'
    #'gravatar',
    #'ace_editor'
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

# plugin: plantuml
PLANTUML = {
    'java_path': r'C:\Java\jdk-11.0.11\bin\java.exe',
    'plantuml_jar_path': r'D:\soft\plantuml-jar-gplv2-1.2023.7\plantuml.jar',
    'uml_image_folder': r'/static/img/'

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


COLORFUL_SITENAME ='''<
    span style="color:#52A2C6">褪</span><
    span style="color:#6791BC">色</span><
    span style="color:#7C80B2">的</span><
    span style="color:#916FA8">抽</span><
    span style="color:#A65E9E">象</span>'''

# My Data
AVATAR_URL = 'https://avatars.githubusercontent.com/u/4386281?v=4'

# mailto
mailto_email = urllib.parse.quote('admin@kaffa.im')
mailto_subject = urllib.parse.quote('网站反馈')
mailto_body = urllib.parse.quote('提示：可反馈“在什么场景下，做什么操作时，遇到什么问题。”')
mailto = f'mailto:{mailto_email}?subject={mailto_subject}&body={mailto_body}'

# menu
MENUITEMS = (
    ("首页", "/", (
        ("项目", "/category/project.html"),
    )),
    ("笔记", "/", (
        ("网站", "/category/website.html"),
        ("-", ""),
        ("读书", "/category/reading.html"),
        ("-", ""),
        ("数智", "/category/digital.html")
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
        #("-", ""),
        #("店", "/category/shop/"),
        #("食", "/category/food/"),
        ("-", ""),
        ("物", "/category/things.html"),
    )),
    ("关于", "/", (
        ("站长", "/pages/about.html"),
        ("联系我", "/pages/contact.html"),
        ("-", ""),
        ("网站反馈", mailto),
    )),
)

CATEGORY_DICT = {
    'website': '网站', 'reading': '读书', 'digital': '数智',
    'article': '文章', 'project': '项目', 'software': '软件', 'book-list': '书单', 'weekly': '周报',
    'book': '书', 'movie': '影', 'music': '音', 'things': '物'
}

CATEGORY_MOMENTS_DICT = {
    'project': '启动一个项目',

    'website': '记录一条笔记',
    'reading': '记录一条笔记',
    'digital': '记录一条笔记',

    'article': '创作一篇文章',
    'software': '编写一个软件',
    'book-list': '精选一款书单',
    'weekly': '汇报一次周报',

    'book': '阅读一本书籍',
    'movie': '观赏一部电影',
    'music': '收藏一首音乐',
    'things': '标记一个物品',

    'links': '添加一条友链'
}

JAVASCRIPT_HEAD = ''
JAVASCRIPT_FOOT = ''

sys.path.append(os.curdir)
import projects
PROJECTS = projects.get_list()

import friends
FRIENDS = friends.get_list()
pass

