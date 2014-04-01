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


def get_first_dir_path(dir_paths):
    """
    Returns the first valid dir path in dir_paths
    """
    dir_paths = [path for path in dir_paths if os.path.isdir(path)]
    return dir_paths[0] if len(dir_paths) > 0 else None


# vim: filetype=python
