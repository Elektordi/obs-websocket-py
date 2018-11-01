#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

version = "0.4"

from distutils.core import setup
from setuptools.command.sdist import sdist

# Convert README from Markdown to reStructuredText
description = "Please take a look at README.md"
try:
    description = open('README.md', 'r').read()
    import pypandoc
    description = pypandoc.convert_text(description, 'rst', 'markdown_github')
except:
    pass
# If not possible, leave it in Markdown...

# Generate classes
class updateClasses(sdist):
    def run(self):
        from os.path import dirname
        from sys import path
        path.append(dirname(__file__))
        from generate_classes import generate_classes
        generate_classes()
        sdist.run(self)

setup(
  name = 'obs-websocket-py',
  packages = ['obswebsocket'],
  cmdclass = {'sdist': updateClasses},
  license = 'MIT',
  version = version,
  description = 'Python library to communicate with an obs-websocket server.',
  long_description = description,
  author = 'Guillaume "Elektordi" Genty',
  author_email = 'elektordi@elektordi.net',
  url = 'https://github.com/Elektordi/obs-websocket-py',
  download_url = 'https://github.com/Elektordi/obs-websocket-py/archive/%s.tar.gz'%(version),
  keywords = ['obs', 'obs-studio', 'websocket'],
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',

    'Development Status :: 4 - Beta',

    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
  ],

  install_requires=['websocket-client'],
)
