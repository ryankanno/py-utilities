#!/usr/bin/env python
# -*- coding: utf-8 -*-

import textwrap


def lines(file_path, strip=True):
    """
    Returns a list of lines from file_path
    """
    with open(file_path, 'r') as f:
        return [strip_if_true(line, strip) for line in f]


def strip_if_true(text, strip):
    """
    Strips text if strip is True
    """
    return text.strip() if strip else text


def wrap(text, width=70, **kwargs):
    r"""
    Returns wrapped text

    >>> test = '12345\n 12345\n 12345\n 12345\n'

    >>> wrap(test, width=3)
    '123\n45\n123\n45\n123\n45\n123\n45'

    """
    return textwrap.fill(text, width, **kwargs)

# vim: filetype=python
