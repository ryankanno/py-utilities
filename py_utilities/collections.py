#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator


def has_dupes(iterable):
    """
    Returns true if iterable contains dupes.
    All values in the iterable need to be hashable

    >>> has_dupes(['1', '2', '3', '3'])
    True

    >>> has_dupes(['1', '2', '3', '4'])
    False

    >>> has_dupes(('1', '1', '3', '4'))
    True

    >>> has_dupes((1, 2, 3, 4))
    False

    >>> has_dupes([])
    False
    """
    curr_size = len(iterable)
    return False if curr_size == 0 else curr_size != len(set(iterable))


def index_min(seq):
    """
    Returns the index of the first occurrence minima in a sequence

    >>> index_min([1,2,3,4,5,6,1,2,1])
    0

    >>> index_min([2,2,3,4,5,6,1,2,1])
    6

    >>> index_min([])
    Traceback (most recent call last):
        ...
    ValueError: min() arg is an empty sequence

    """
    return min(enumerate(seq), key=operator.itemgetter(1))[0]


def index_max(seq):
    """
    Returns the index of the first occurrence maxima in a sequence

    >>> index_max([1,2,3,4,5,6,1,2,1])
    5

    >>> index_max([9,2,3,4,5,6,1,2,1])
    0

    >>> index_max([])
    Traceback (most recent call last):
        ...
    ValueError: max() arg is an empty sequence

    """
    return max(enumerate(seq), key=operator.itemgetter(1))[0]


def value_min(seq):
    """
    Returns the value of the first occurrence minima in a sequence

    >>> value_min([1,2,3,4,5,6,1,2,1])
    1

    >>> value_min([2,2,3,4,5,6,8,2,9])
    2

    >>> value_min([])
    Traceback (most recent call last):
        ...
    ValueError: min() arg is an empty sequence

    """
    return min(enumerate(seq), key=operator.itemgetter(1))[1]


def value_max(seq):
    """
    Returns the value of the first occurrence maxima in a sequence

    >>> value_max([1,2,3,4,5,6,1,2,1])
    6

    >>> value_max([2,2,3,4,5,6,8,2,9])
    9

    >>> value_max([])
    Traceback (most recent call last):
        ...
    ValueError: max() arg is an empty sequence

    """
    return max(enumerate(seq), key=operator.itemgetter(1))[1]

# vim: filetype=python
