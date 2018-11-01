#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

version = "0.3"

from distutils.core import setup
from setuptools.command.install import install

from generate_classes import generate_classes

# Convert README from Markdown to reStructuredText
description = open('README.md', 'r').read()
try:
    import pypandoc
    description = pypandoc.convert_text(description, 'rst', 'markdown_github')
except:
    pass
# If not possible, leave it in Markdown...

# Generate classes
class CustomInstallCommand(install):
    def run(self):
        generate_classes()
        install.run(self)

setup(
  name = 'obs-websocket-py',
  packages = ['obswebsocket'],
  cmdclass = {'install': CustomInstallCommand},
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
