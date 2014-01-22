#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lines(file_path):
    """
    Returns a list of lines from file_path
    """
    with open(file_path, 'r') as f:
        return [line for line in f]

# vim: filetype=python
