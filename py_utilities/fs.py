#!/usr/bin/env python
# -*- coding: utf-8 -*-

import errno
import os


def mkdir_p(path):
    """
    Recursive directory creation function. Mimics `mkdir -p`. Doesn't
    raise an error if the leaf exists and is a directory.
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

# vim: filetype=python
