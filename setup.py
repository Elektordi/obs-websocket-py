#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

# Convert README from Markdown to reStructuredText
description = open('README.md', 'r').read()
try:
    import pypandoc
    description = pypandoc.convert_text(description, 'rst', 'markdown_github')
except:
    pass
# If not possible, leave it in Markdown...

setup(
  name = 'obs-websocket-py',
  packages = ['obswebsocket'],
  license = 'MIT',
  version = '0.1',
  description = 'Python library to communicate with an obs-websocket server.',
  long_description = description,
  author = 'Guillaume "Elektordi" Genty',
  author_email = 'elektordi@elektordi.net',
  url = 'https://github.com/Elektordi/obs-websocket-py',
  download_url = 'https://github.com/Elektordi/obs-websocket-py/archive/0.1.tar.gz',
  keywords = ['obs', 'obs-studio', 'websocket'],
  classifiers = [
    'License :: OSI Approved :: MIT License',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    
    'Development Status :: 4 - Beta', # v0.1
    
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7'
  ],
  
  install_requires=['websocket-client'],
)
