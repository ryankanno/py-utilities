#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_weekday(date):
    """
    Returns true if date is a weekday, false otherwise
    """
    return date.isoweekday() < 6


def is_weekend(date):
    """
    Returns true if date is a weekend, false otherwise
    """
    return date.isoweekday() > 5


# vim: filetype=python
