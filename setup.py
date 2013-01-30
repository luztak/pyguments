#!/bin/usr/env python
# -*- coding: utf-8 -*-

import sys
kwargs = {}
major, minor = sys.version_info[:2]
if major >= 3:
    kwargs['use_2to3'] = True

from setuptools import setup, find_packages

import pyguments

setup(
    name = 'pyguments',
    version = pyguments.__version__,
    author = pyguments.__author__,
    author_email = 'luztakmo@gmail.com',
    url = 'https://github.com/luztak/pyguments',
    packages = find_packages();
    description = 'Pyguments is a Python module for parsing command line.',
    long_description = open('README.rst').read(),
    install_requires = [],
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Windows',
        'Operating System :: Mac OS',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
    **kwargs
)
