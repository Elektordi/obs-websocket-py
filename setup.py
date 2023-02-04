#!/usr/bin/env python3

from distutils.core import setup
from setuptools.command.sdist import sdist
from obswebsocket import VERSION

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


# Generate classes
class UpdateClasses(sdist):
    def run(self):
        from os.path import dirname
        from sys import path
        path.append(dirname(__file__))
        from generate_classes import generate_classes
        generate_classes()
        sdist.run(self)


setup(
    name='obs-websocket-py',
    packages=['obswebsocket'],
    # cmdclass={'sdist': UpdateClasses},
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
