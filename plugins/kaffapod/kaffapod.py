import json
import logging
import os
from pathlib import Path
from urllib.request import Request, urlopen, urlretrieve
from urllib.parse import urljoin, quote_plus

from pelican import signals
from pelican.contents import Article, Page
from pelican.generators import ArticlesGenerator, PagesGenerator
from pelican import logger

import sqlite3

log = logging.getLogger(__name__)
log.addHandler(logging.FileHandler('d:/app.log', "w", encoding="UTF-8"))


def multi_urljoin(*parts):
    return urljoin(parts[0], "/".join(quote_plus(part.strip("/"), safe="/") for part in parts[1:]))


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


def download_cover(cover_image_url, cover_image_path):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/112.0.0.0 Safari/537.36',
    }

    directory = os.path.dirname(cover_image_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    req = Request(cover_image_url)
    for key, value in headers.items():
        req.add_header(key, value)
    u = urlopen(req)
    resp = u.read()
    with open(cover_image_path, 'wb') as f:
        f.write(resp)


def fetch_subject(instance):
    if type(instance) not in (Article, Page):
        return

    if 'subject_url' not in instance.metadata:
        return



    subject_url = instance.metadata["subject_url"]

    # 兼容网址中未写 /api/
    if 'api' not in subject_url.split('/'):
        subject_url = subject_url.replace('https://neodb.social/', 'https://neodb.social/api/')

    type_, uuid = get_type_uuid(subject_url)

    path = instance.settings.get('PATH')
    kaffapod = instance.settings.get('KAFFAPOD')
    sqlite_path = kaffapod['db_path'] if Path(kaffapod['db_path']).is_absolute() else path + kaffapod['db_path']

    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM subject WHERE type=? and uuid=?', (type_, uuid,))
    row = cursor.fetchone()
    if row:
        subject = row[5]
        subject_obj = json.loads(subject)
    else:
        subject = get_from_subject_url(subject_url)
        subject_obj = json.loads(subject)

        # book 有 orig_title
        # album 没有 orig_title
        subject_title = subject_obj['orig_title'] if 'orig_title' in subject_obj.keys() else subject_obj['title']

        # .replace(':', '') -> unix:-a-history-and-a-memoir
        # .replace('(', '').replace(')', '').replace("'", '-') -> 1989-(taylor's-version)
        subject_obj['slug'] = ((subject_obj['title']
                               .replace(' ', '-')
                               .replace(',', '-')
                               .replace(':', '')
                               .replace('(', '').replace(')', '').replace("'", '-'))
                               .lower().strip())

        cover_image_path = os.path.join(
            kaffapod['img_folder'],
            subject_obj['category'],
            f"{subject_obj['slug']}.{subject_obj['cover_image_url'].split('.')[-1]}")
        download_cover(subject_obj['cover_image_url'], cover_image_path)

        subject_obj['cover_relative_path'] = multi_urljoin(
            kaffapod['img_relative_folder'],
            subject_obj['category'],
            f"{subject_obj['slug']}.{subject_obj['cover_image_url'].split('.')[-1]}")

        # log.debug('cover_relative_path' + cover_relative_path)
        # log.debug(subject_obj)

        subject = json.dumps(subject_obj)

        cursor.execute('''
            INSERT INTO subject(
                type, uuid, name, slug, content, updated_time, comment, cover_relative_path
            ) VALUES (
                ?, ?, ?, ?, ?, DATETIME('now','localtime'), ?, ?
            )''', (type_, uuid, subject_title, subject_obj['slug'], subject, '', subject_obj['cover_relative_path'],))
        conn.commit()

    cursor.close()
    conn.close()

    if 'growth' in instance.metadata:
        if instance.metadata['growth'] not in ('1', '3', '5'):
            return

        instance.metadata['growth'] = {
            '1': 'seedling',
            '3': 'budding',
            '5': 'evergreen'
        }[instance.metadata['growth']]

        '''
        subject_obj['growth'] = {
            1: 'seedling',
            3: 'budding',
            5: 'evergreen'
        }[instance.metadata['growth']]
        '''


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
