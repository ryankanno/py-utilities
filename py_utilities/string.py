#!/usr/bin/env python
# -*- coding: utf-8 -*-


def truncate(str, length, trailing_chars='...'):
    """
    Returns a truncated str of length with a trailing '...'

    >>> truncate('foobar', 3)
    'foo...'

    >>> truncate('foobar', 1)
    'f...'

    >>> truncate('', 1)
    ''

    >>> truncate('hello', 100)
    'hello'

    """
    return (str[:length] + trailing_chars) if len(str) > length else str

# vim: filetype=python
