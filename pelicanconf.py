#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kaffa'
SITENAME = 'Kaffa.im'
COLORFUL_SITENAME = '''<span style="color:#52A2C6">褪</span><span style="color:#6791BC">色</span><span style="color:#7C80B2">的</span><span style="color:#916FA8">抽</span><span style="color:#A65E9E">象</span>'''
SITESUBTITLE = ""
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
    ("笔记", "/", (
        ("网站", "javascript:;"),
        ("-", ""),
        ("读书", "javascript:;"),)),
    ("创作", "/", (
        ("文章", "javascript:;"),
        ("-", ""),
        ("书单", "javascript:;"),
        ("-", ""),
        ("周报", "javascript:;"),
        ("-", ""),
        ("概念", "javascript:;"),)),
    ("我的", "/", (
        ("书", "javascript:;"),
        ("影", "javascript:;"),
        ("音", "javascript:;"),
        ("-", ""),
        #("店", "javascript:;"),
        #("食", "javascript:;"),
        #("-", ""),
        ("物", "javascript:;"),)),
    ("关于", "/", (
        ("站长", "/pages/about.html"),
        ("-", ""),
        ("联系", "mailto:admin@kaffa.im?subject=Hello%20from%20&body=你好，"),
        ("-", ""),
        ("网站反馈", "mailto:admin@kaffa.im?subject=Hello%20from%20&body=网站反馈："),)),
)
# 添加 20190518
DISPLAY_CATEGORIES_ON_MENU = False

# 添加 20230913
# 修改 20231019
DISPLAY_PAGES_ON_MENU = False

# THEME = "D:/code/github/kaffa/kaffa.github.io/themes/pelican-octopress-theme-cn"
THEME = "D:/code/github/kaffa/kaffa.github.io/themes/pelican-kaffa-theme"

STATIC_PATHS = [
    'js',
    'css',
    'img',
    'file',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon/about.txt': {'path': 'favicon/about.txt'},
    'extra/favicon/android-chrome-192x192.png': {'path': 'favicon/android-chrome-192x192.png'},
    'extra/favicon/android-chrome-512x512.png': {'path': 'favicon/android-chrome-512x512.png'},
    'extra/favicon/apple-touch-icon.png': {'path': 'favicon/apple-touch-icon.png'},
    'extra/favicon/favicon.ico': {'path': 'favicon/favicon.ico'},
    'extra/favicon/favicon-16x16.png': {'path': 'favicon/favicon-16x16.png'},
    'extra/favicon/favicon-32x32.png': {'path': 'favicon/favicon-32x32.png'},
    'extra/favicon/site.webmanifest': {'path': 'favicon/site.webmanifest'},
}

PLUGIN_PATHS = ['D:/code/github/kaffa/kaffa.github.io/plugins']
PLUGINS = [
    'sitemap',
    'featured_image',
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


CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True

AVATAR_URL = 'https://avatars.githubusercontent.com/u/4386281?v=4'
