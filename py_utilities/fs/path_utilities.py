#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntpath
import os


def expanded_abspath(dir):
    expanded = os.path.expanduser(os.path.expandvars(dir))
    return os.path.abspath(expanded)


def filename(path):
    """ Returns filename in path """
    dirs, f = ntpath.split(path)
    return f or ntpath.basename(dirs)

# vim: filetype=python
