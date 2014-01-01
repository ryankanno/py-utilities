#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
import os
from py_utilities.path import expanded_abspath
import unittest


class TestPath(unittest.TestCase):

    def test_expanded_abspath(self):
        home = os.environ["HOME"]
        ok_(expanded_abspath("~") == home)
        ok_(expanded_abspath("~/foo") == os.path.join(home, 'foo'))
        ok_(expanded_abspath("/foo") == "/foo")
        ok_(expanded_abspath("/foo/bar") == "/foo/bar")

# vim: filetype=python
