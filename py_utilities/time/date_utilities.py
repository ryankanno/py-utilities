#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar
from datetime import datetime
import random
import time

EPOCH = time.gmtime(0)


def is_leap_year(year):
    """
    Returns true if the year is a leap year, false otherwise

    >>> is_leap_year(2008)
    True
    >>> is_leap_year(2012)
    True
    >>> is_leap_year(2013)
    False
    """
    return calendar.isleap(year)


def is_weekday(date):
    """
    Returns true if date is a weekday, false otherwise

    >>> from datetime import timedelta;
    >>> date = datetime.now()
    >>> last_friday = date - timedelta(days=date.weekday()) \
    + timedelta(days=4, weeks=-1)
    >>> is_weekday(last_friday)
    True
    """
    return date.isoweekday() < 6


def is_weekend(date):
    """
    Returns true if date is a weekend, false otherwise

    >>> from datetime import timedelta;
    >>> date = datetime.now()
    >>> last_friday = date - timedelta(days=date.weekday()) \
    + timedelta(days=4, weeks=-1)
    >>> is_weekend(last_friday)
    False
    """
    return date.isoweekday() > 5


def random_datetime(start_timestamp, end_timestamp, tz=None):
    """
    Returns a random datetime between two timestamps and converts to the tz if
    provided
    """
    interval = end_timestamp - start_timestamp
    random_timestamp = start_timestamp + (random.random() * interval)
    return datetime.fromtimestamp(random_timestamp, tz)

# vim: filetype=python
