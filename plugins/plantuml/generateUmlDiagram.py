#!/usr/bin/env python
import hashlib
import logging
import os
import sqlite3
import tempfile
from zlib import adler32
from subprocess import Popen, PIPE
from pelican import logger


def generate_uml_image(path, plantuml_code, uml_filename, imgformat, global_plantuml):
    uml_path = os.path.join(path, uml_filename + '.plantuml')
    img_path = os.path.join(path, uml_filename + f'.{imgformat}')

    content = f'@startuml{os.linesep}{plantuml_code}{os.linesep}@enduml'
    with open(uml_path, 'w', encoding='utf-8') as f:
        f.write(content)

    logger.debug("[plantuml] Temporary PlantUML source at " + uml_path)

    if imgformat == 'png':
        imgext = ".png"
        outopt = "-tpng"
    elif imgformat == 'svg':
        imgext = ".svg"
        outopt = "-tsvg"
    else:
        logger.error("Bad uml image format '" + imgformat + "', using png")
        imgext = ".svg"
        outopt = "-tpng"

    conn = sqlite3.connect(r'D:\code\github\kaffa\kaffa.github.io\content\db\0.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM plantuml WHERE name=? and content=?',
                   (uml_filename, content,))
    row = cursor.fetchone()
    md5 = hashlib.md5(content)
    if not row or (row and row[3] != md5):
        cursor.execute("INSERT INTO plantuml(name, content, md5, updated_time) VALUES(?, ?, ?, DATETIME('now','localtime'))",
                       (uml_filename, content, md5))
        conn.commit()

    cursor.close()
    conn.close()


    if os.name == 'posix':
        cmdline = ['plantuml',
                   '-charset', 'UTF-8',
                   '-o', path,
                   outopt, uml_path]
    elif os.name == 'nt':
        cmdline = [global_plantuml['java_path'],
                   '-jar', global_plantuml['plantuml_jar_path'],
                   '-charset', 'UTF-8',
                   '-o', path,
                   outopt, uml_path]

    try:
        logger.debug("[plantuml] About to execute " + " ".join(cmdline))

        p = Popen(cmdline, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
    except Exception as exc:
        raise Exception('Failed to run plantuml: %s' % exc)
    else:
        if p.returncode == 0:
            return os.path.basename(img_path)
        else:
            raise RuntimeError('Error calling plantuml: %s' % err)
