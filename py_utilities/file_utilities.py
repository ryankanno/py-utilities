#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


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

# vim: filetype=python
