#!/usr/bin/env python3
import os, re
from distutils.core import setup

def read_version():
    version_file = os.path.join(os.path.dirname(__file__), "obswebsocket", "__init__.py")
    with open(version_file, "r") as f:
        content = f.read()
    match = re.search(r'^VERSION\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if match:
        return match.group(1)

VERSION=read_version()

# Convert README from Markdown to reStructuredText
description = "Please take a look at README.md"
try:
    description = open('README.md', 'rt').read()
    import pypandoc
    description = pypandoc.convert_text(description, 'rst', 'gfm')
except ImportError:
    # If not possible, leave it in Markdown...
    print("Cannot find pypandoc, not generating README!")

requirements = open('requirements.txt', 'rt').readlines()
requirements = [x.strip() for x in requirements if x]

setup(
    name='obs-websocket-py',
    packages=['obswebsocket'],
    license='MIT',
    version=VERSION,
    description='Python library to communicate with an obs-websocket server.',
    long_description=description,
    author='Guillaume "Elektordi" Genty',
    author_email='elektordi@elektordi.net',
    url='https://github.com/Elektordi/obs-websocket-py',
    keywords=['obs', 'obs-studio', 'websocket'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=requirements,
)
