#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import errno
import os
import shutil


@contextmanager
def cd(path=None):
    prev_cwd = os.getcwd()
    if path is not None:
        os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


def mkdir_p(path):
    """
    Recursive directory creation function. Mimics `mkdir -p`. Doesn't
    raise an error if the leaf exists and is a directory.

    Reference: http://stackoverflow.com/questions/600268/\
    mkdir-p-functionality-in-python/600612#600612
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def rm_if_exists(path):
    """
    Removes a path silently
    """
    try:
        os.remove(path)
    except OSError as exc:
        if exc.errno != errno.ENOENT:
            raise


def rm_rf(path, ignore_errors=True):
    """
    Recursive directory deletion function.
    """
    shutil.rmtree(path, ignore_errors=ignore_errors)


def touch(path, times=None):
    """
    Touches a file. If times is None, then the file’s access and modified
    times are set to the current time.
    """
    with file(path, 'a'):
        os.utime(path, times)

# vim: filetype=python
