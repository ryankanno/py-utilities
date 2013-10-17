#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imp
import importlib
import os


def get_klass_from_str(cls_as_str):
    """
    Returns a klass from a string

    >>> get_klass_from_str('cStringIO.StringIO')
    <built-in function StringIO>

    >>> get_klass_from_str('cStringIO.StringIO')() #doctest: +ELLIPSIS
    <cStringIO.StringO object at 0x...>

    """
    module_name, class_name = cls_as_str.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def get_klass_from_file(path_to_file, cls_as_str):
    """
    Returns a klass from a file (compiled or not)
    """
    module_name, file_ext = os.path.splitext(os.path.split(path_to_file)[-1])

    if file_ext.lower() == '.py':
        module = imp.load_source(module_name, path_to_file)
    elif file_ext.lower() == '.pyc':
        module = imp.load_compiled(module_name, path_to_file)

    return getattr(module, cls_as_str) if hasattr(module, cls_as_str) else None


get_func_from_str = get_klass_from_str
get_func_from_file = get_klass_from_file

# vim: filetype=python
