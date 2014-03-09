#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
import os
from py_utilities.fs.path_utilities import expanded_abspath
from py_utilities.fs.path_utilities import filename
import unittest


class TestPath(unittest.TestCase):

    def test_expanded_abspath(self):
        home = os.environ["HOME"]
        ok_(expanded_abspath("~") == home)
        ok_(expanded_abspath("~/foo") == os.path.join(home, 'foo'))
        ok_(expanded_abspath("/foo") == "/foo")
        ok_(expanded_abspath("/foo/bar") == "/foo/bar")

    def test_filename(self):
        paths = ['/foo/bar/', '/foo/bar', 'foo/bar/', 'foo/bar',
                 '\\foo\\bar\\', '\\foo\\bar', 'foo\\bar\\', 'foo\\bar']
        for path in paths:
            ok_(filename(path) == 'bar')

# vim: filetype=python
