#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput
import hashlib
import os
import shutil
import sys


def concat(filenames, outfile):
    """
    Concatenates filename contents in filename list to outfile
    """
    for line in fileinput.input(filenames):
        outfile.write(line)


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


def print_file_contents(filename, file=sys.stdout):
    """
    Prints contents of filename to a file-like object, `file`
    """
    with open(filename, 'r') as f:
        shutil.copyfileobj(f, file)


def write_file(path, contents):
    """
    Writes contents to file path
    """
    with open(path, 'w') as f:
        f.write(contents)

# vim: filetype=python
