#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
import os
from py_utilities.klass import get_func_from_file
from py_utilities.klass import get_klass_from_file
import unittest


class Test(object):
    pass


def test_func():
    return 1 + 2


class TestKlass(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))

    def test_get_func_from_file(self):
        func = get_func_from_file(os.path.join(self.cwd, 'test_klass.py'),
                                  'test_func')
        eq_(func(), 3)

        func = get_func_from_file(os.path.join(self.cwd, 'test_klass.pyc'),
                                  'test_func')
        eq_(func(), 3)

    def test_get_klass_from_file(self):
        klass = get_klass_from_file(os.path.join(self.cwd, 'test_klass.py'),
                                    'Test')
        eq_(type(Test), type(klass))

        klass = get_klass_from_file(os.path.join(self.cwd, 'test_klass.pyc'),
                                    'Test')
        eq_(type(Test), type(klass))


# vim: filetype=python
