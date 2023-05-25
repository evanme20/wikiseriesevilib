#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: _version.py
#
# Copyright 2023 Evi Vanmechelen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
Manages the version of the package.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""

import os

__author__ = '''Evi Vanmechelen <evi_github@gmail.com>'''
__docformat__ = '''google'''
__date__ = '''25-05-2023'''
__copyright__ = '''Copyright 2023, Evi Vanmechelen'''
__license__ = '''MIT'''
__maintainer__ = '''Evi Vanmechelen'''
__email__ = '''<evi_github@gmail.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".

VERSION_FILE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
        '.VERSION'
    )
)

LOCAL_VERSION_FILE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '.VERSION'
    )
)

try:
    with open(VERSION_FILE_PATH, encoding='utf8') as f:
        __version__ = f.read()
except IOError:
    try:
        with open(LOCAL_VERSION_FILE_PATH, encoding='utf8') as f:
            __version__ = f.read()
    except IOError:
        __version__ = 'unknown'
