#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import shutil
import sys


def concat(file_paths, file):
    """
    Concatenates contents in file_paths list to a file-like object, `file`
    """
    for file_path in file_paths:
        copy_file(file_path, file)


def copy_file(file_path, file=sys.stdout):
    """
    Copy contents at file_path to a file-like object, `file`
    """
    with open(file_path, 'r') as f:
        shutil.copyfileobj(f, file)


def file_ext(file_path):
    """
    Returns the file extension at file_path

    >>> file_ext('/foo/bar/what/temp.txt')
    '.txt'

    >>> file_ext('/foo/bar/what/temp.jpg')
    '.jpg'

    >>> file_ext('/foo/bar/what/temp.tar.gz')
    '.gz'

    >>> file_ext('/foo/bar/what/temp')
    ''

    >>> file_ext('')
    ''

    """
    return os.path.splitext(file_path)[-1]


def file_hexdigest(file_path, algo='md5'):
    """
    Returns the hexdigest hash of file_path using algo

    >>> cwd = os.path.dirname(os.path.abspath(__file__))

    >>> file_hexdigest(os.path.join(cwd, '__init__.py'), algo='md5')
    'd41d8cd98f00b204e9800998ecf8427e'

    """
    hash = getattr(hashlib, algo)()

    with open(file_path, 'rb') as f:
        hash.update(f.read())
    return hash.hexdigest()


def write_file(file_path, contents):
    """
    Writes contents to file path
    """
    with open(file_path, 'w') as f:
        f.write(contents)

# vim: filetype=python
