import hashlib
import datetime
import pandas as pd

data = pd.read_excel("book.xlsx")
book_list = data.to_dict('index')

for i, book in book_list.items():
    date_ = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    book_name = book['name']
    filename = f"20240707-{book_name}.rst"
    slug = hashlib.md5(book['subject_url'].encode('utf-8')).hexdigest()
    rank = int(book['rank'])
    rank_section = """
想读
====================

mark 备读"""

    if rank != -1:
        rank_section = ("""
评分
====================

""" + ('⭐⭐⭐⭐⭐' if rank >= 5 else '⭐' * rank) + '\n' + '⭐' * (rank - 5) + f' {rank} / 10')

    with open('book/' + filename, 'w', encoding="utf-8") as f:
        f.write(f"""{book['name']}
########################################################

:date: {date_}
:author: Kaffa
:category: book
:tags: 
:slug: {slug}
:summary: 
:image: /static/img/2024/hero.png
:subject_url: {book['subject_url']}


{rank_section}


摘录
====================
        
""")
