#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from distutils.core import setup
from setuptools.command.install import install

from os.path import dirname
from sys import path
path.append(dirname(__file__))

from generate_classes import generate_classes
from obswebsocket import __version__

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
        print("Generating API classes...")
        generate_classes()
        install.run(self)

setup(
  name = 'obs-websocket-py',
  packages = ['obswebsocket'],
  cmdclass = {'install': CustomInstallCommand},
  license = 'MIT',
  version = __version__,
  description = 'Python library to communicate with an obs-websocket server.',
  long_description = description,
  author = 'Guillaume "Elektordi" Genty',
  author_email = 'elektordi@elektordi.net',
  url = 'https://github.com/Elektordi/obs-websocket-py',
  download_url = 'https://github.com/Elektordi/obs-websocket-py/archive/0.3.tar.gz',
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
  ],

  install_requires=['websocket-client'],
)
