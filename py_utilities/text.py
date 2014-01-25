#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

# vim: filetype=python
