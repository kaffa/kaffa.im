import codecs
import json
import logging
import re
import sys
from pelican import signals
from pelican.contents import Article, Page
from pelican.generators import ArticlesGenerator, PagesGenerator
from urllib.request import Request, urlopen

import sqlite3

log = logging.getLogger(__name__)
log.addHandler(logging.FileHandler('d:/app.log', "w", encoding="UTF-8"))


def get_from_subject_url(subject_url):
    req = Request(subject_url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/112.0.0.0 Safari/537.36',
    }
    for key, value in headers.items():
        req.add_header(key, value)
    u = urlopen(req)
    return u.read().decode('utf8')


def get_type_uuid(subject_url):
    arr = subject_url.split('/')
    return arr[-2], arr[-1]


def fetch_subject(instance):
    if type(instance) not in (Article, Page):
        return

    if "subject_url" in instance.metadata:
        subject_url = instance.metadata["subject_url"]

        if 'api' not in subject_url.split('/'):
            subject_url = subject_url.replace('https://neodb.social/', 'https://neodb.social/api/')

        type_, uuid = get_type_uuid(subject_url)

        conn = sqlite3.connect(r'D:\code\github\kaffa\kaffa.github.io\content\db\0.db')
        cursor = conn.cursor()

        cursor.execute('select * from subject where type=? and uuid=?', (type_, uuid,))
        row = cursor.fetchone()
        if row:
            subject = row[5]
            subject_obj = json.loads(subject)
        else:
            subject = get_from_subject_url(subject_url)
            subject_obj = json.loads(subject)

            # book 有 orig_title
            # album 没有 orig_title
            subject_title = subject_obj['orig_title'] if 'orig_title' in subject_obj else subject_obj['title']
            # .replace(':', '') unix:-a-history-and-a-memoir
            # .replace('(', '').replace(')', '').replace("'", '-') 1989-(taylor's-version)
            subject_slug = (subject_obj['title']
                            .replace(' ', '-')
                            .replace(':', '')
                            .replace('(', '').replace(')', '').replace("'", '-')).lower().strip()

            cursor.execute('''INSERT INTO subject(type, uuid, name, slug, content, updated_time, comment)
                VALUES(?, ?, ?, ?, ?, DATETIME('now','localtime'), ?)''',
                (type_, uuid, subject_title, subject_slug, subject, '',))
            conn.commit()

        cursor.close()
        conn.close()

        instance.subject = subject_obj


def pod_start(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            for article in generator.articles:
                fetch_subject(article)
                for translation in article.translations:
                    fetch_subject(translation)
        elif isinstance(generator, PagesGenerator):
            for page in generator.pages:
                fetch_subject(page)
                for translation in page.translations:
                    fetch_subject(translation)


def register():
    signals.all_generators_finalized.connect(pod_start)
