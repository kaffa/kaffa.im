import logging
import os.path
from xml.dom.minidom import parse
from pelican import signals

log = logging.getLogger(__name__)
log.addHandler(logging.FileHandler('d:/app.log', "w", encoding="UTF-8"))


def add_atom_description(context, feed):
    file_path = os.path.join(context['OUTPUT_PATH'], context['FEED_ALL_ATOM'])
    try:
        dom = parse(file_path)
        feed_element = dom.getElementsByTagName('feed')[0]
        new_description = dom.createElement('description')
        new_description_text = dom.createTextNode('feedId:41342818708527123+userId:41447029693323264')
        new_description.appendChild(new_description_text)
        feed_element.appendChild(new_description)
        with open(file_path, 'w', encoding='utf-8') as f:
            dom.writexml(f)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")

def add_rss_description(context, feed):
    file_path = os.path.join(context['OUTPUT_PATH'], context['FEED_ALL_RSS'])
    try:
        dom = parse(file_path)
        rss = dom.getElementsByTagName('rss')[0]
        channel = rss.getElementsByTagName('channel')[0]
        descriptions = channel.getElementsByTagName('description')
        if descriptions[0].hasChildNodes():
            descriptions[0].childNodes[0].data = 'feedId:55805414897308672+userId:41447029693323264'
        else:
            descriptions[0].appendChild(dom.createTextNode('feedId:55805414897308672+userId:41447029693323264'))
        with open(file_path, 'w', encoding='utf-8') as f:
            dom.writexml(f)
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")


def add_claim(context, feed):
    add_atom_description(context, feed)
    add_rss_description(context, feed)


def register():
    signals.feed_generated.connect(add_claim)


if __name__ == '__main__':
    add_atom_description({
        'OUTPUT_PATH': 'D:/code/github/kaffa/kaffa.github.io/docs',
        'FEED_ALL_ATOM': 'feeds/all.atom.xml'
    }, None)
