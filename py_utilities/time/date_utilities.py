#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_weekday(date):
    """
    Returns true if date is a weekday, false otherwise

    >>> import datetime; from datetime import timedelta;
    >>> date = datetime.datetime.now()
    >>> last_friday = date - timedelta(days=date.weekday()) \
    + timedelta(days=4, weeks=-1)
    >>> is_weekday(last_friday)
    True
    """
    return date.isoweekday() < 6


def is_weekend(date):
    """
    Returns true if date is a weekend, false otherwise

    >>> import datetime; from datetime import timedelta;
    >>> date = datetime.datetime.now()
    >>> last_friday = date - timedelta(days=date.weekday()) \
    + timedelta(days=4, weeks=-1)
    >>> is_weekend(last_friday)
    False
    """
    return date.isoweekday() > 5


# vim: filetype=python
