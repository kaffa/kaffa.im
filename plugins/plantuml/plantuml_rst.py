#!/usr/bin/env python
"""Custom reST_ directive for plantuml_ integration.
   Adapted from ditaa_rst plugin.

.. _reST: http://docutils.sourceforge.net/rst.html
.. _plantuml: http://plantuml.sourceforge.net/
"""

import os

from docutils.nodes import image, literal_block
from docutils.parsers.rst import Directive, directives
from pelican import signals, logger

from .generateUmlDiagram import generate_uml_image


global_siteurl = "" # URL of the site, filled on plugin initialization
global_output_path = ""
global_plantuml = None


class PlantUML_rst(Directive):
    """ reST directive for PlantUML """
    required_arguments = 0
    optional_arguments = 0
    has_content = True

    global global_siteurl
    global global_output_path
    global global_plantuml

    option_spec = {
        'class' : directives.class_option,
        'alt'   : directives.unchanged,
        'format': directives.unchanged,
        'filename': directives.unchanged,
    }

    def run(self):
        folder_list = global_plantuml['uml_image_folder'].strip('/').split('/')
        folder_list.insert(0, global_output_path)
        path = os.path.abspath(os.path.join(*folder_list))

        if not os.path.exists(path):
            os.makedirs(path)

        nodes = []
        body = '\n'.join(self.content)

        try:
            uml_format = self.options.get('format', 'svg')
            uml_filename = self.options.get('filename', '')
            url = (global_siteurl + '/' +
                   global_plantuml['uml_image_folder'].strip('/') + '/' +
                   generate_uml_image(path, body, uml_filename, uml_format, global_plantuml))

        except Exception as exc:
            error = self.state_machine.reporter.error(
                'Failed to run plantuml: %s' % exc,
                literal_block(self.block_text, self.block_text),
                line=self.lineno)
            nodes.append(error)
        else:
            alt = self.options.get('alt', 'uml diagram')
            classes = self.options.pop('class', ['uml'])
            imgnode = image(uri=url, classes=classes, alt=alt)
            nodes.append(imgnode)

        return nodes

def pelican_init(pelicanobj):

    global global_siteurl
    global global_output_path
    global global_plantuml

    global_siteurl = pelicanobj.settings['SITEURL']
    global_output_path = pelicanobj.settings['OUTPUT_PATH'] if 'OUTPUT_PATH' in pelicanobj.settings else 'output'

    if 'PLANTUML' in pelicanobj.settings:
        global_plantuml = pelicanobj.settings['PLANTUML']
    else:
        global_plantuml = {}

        if os.name == 'nt':
            if 'JAVA_HOME' not in os.environ:
                logger.debug("[plantuml] requires Java SDK, install Java and config the environment variable JAVA_HOME")
                return
            global_plantuml['java_path'] = os.environ['JAVA_HOME'].rstrip('\\') + "\\bin\\java.exe"

            if 'PLANTUML_PATH' not in os.environ:
                logger.debug("[plantuml] requires the environment variable PLANTUML_PATH, the default is 'c:\\plantuml\\plantuml.jar'")
                return
            global_plantuml['java_path'] = 'c:\\plantuml\\plantuml.jar'

            global_plantuml['uml_image_folder'] = '/images/'

    """ Prepare configurations for the MD plugin """
    try:
        import markdown
        from .plantuml_md import PlantUMLMarkdownExtension
    except:
        # Markdown not available
        logger.debug("[plantuml] Markdown support not available")
        return

    # Register the Markdown plugin
    config = {
        'siteurl': pelicanobj.settings['SITEURL']
    }

    try:
        if 'MD_EXTENSIONS' in pelicanobj.settings.keys(): # pre pelican 3.7.0
            pelicanobj.settings['MD_EXTENSIONS'].append(PlantUMLMarkdownExtension(config))
        elif 'MARKDOWN' in pelicanobj.settings.keys() and \
             not ('extension_configs' in pelicanobj.settings['MARKDOWN']['extension_configs']):  # from pelican 3.7.0
            pelicanobj.settings['MARKDOWN']['extension_configs']['plantuml.plantuml_md'] = config
    except:
        logger.error("[plantuml] Unable to configure plantuml markdown extension")


def register():
    """Plugin registration."""
    signals.initialized.connect(pelican_init)
    directives.register_directive('uml', PlantUML_rst)
