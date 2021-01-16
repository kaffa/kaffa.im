#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kaffa'
SITENAME = '褪色的抽象'
SITESUBTITLE = "Kaffa's blog"
SITEURL = 'https://kaffa.im'

PATH = 'content'
OUTPUT_PATH = 'docs/'

TIMEZONE = 'Asia/Shanghai'
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
         ("Kaffa", 'https://kaffa.im'),
         ("Coffee's", 'https://coffees.app'),
         ('论道', 'https://lundao.pub/'),)

# Social widget
SOCIAL = (('My GitHub', 'https://github.com/kaffa'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# 菜单
MENUITEMS = (
    ("首页", "/"),
    ("随笔", "/category/sui-bi.html"),
    ("阅读", "/category/yue-du.html"),
    ("人文", "/category/ren-wen.html"),
    ("自然", "/category/zi-ran.html"),
    ("日志", "/category/ri-zhi.html"),
)
# 添加 20190518
DISPLAY_CATEGORIES_ON_MENU = False


THEME = "E:/code/github/kaffa/kaffa.github.io/themes/pelican-octopress-theme-cn"

STATIC_PATHS = [
    'js',
    'css',
    'img',
    'extra/CNAME',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
FAVICON_FILENAME = 'favicon.ico'

PLUGIN_PATHS = ['E:/code/kaffa.im/plugins/']
PLUGINS = [
    'sitemap',
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

# plugin: ace_editor
ACE_EDITOR_PLUGIN = {
    'ACE_EDITOR_THEME': 'chrome',
    'ACE_EDITOR_SCROLL_TOP_MARGIN': 0,
    'ACE_EDITOR_MAXLINES': 50,
    'ACE_EDITOR_READONLY': True,
    'ACE_EDITOR_AUTOSCROLL': True,
    'ACE_EDITOR_SHOW_INVISIBLE': True
}
# MARKDOWN = {
#     'markdown.extensions.codehilite': {
#         'css_class': 'literal-block',
#         'linenums': True,
#         'use_pygments': True
#     }
# }
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