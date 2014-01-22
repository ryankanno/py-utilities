#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
import os
from py_utilities.text import lines
import unittest


class TestText(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.csv_headers_path = os.path.join(self.cwd, 'data',
                                             'test_csv_to_list_headers.csv')

    def test_lines(self):
        list_of_lines = lines(self.csv_headers_path)
        ok_(len(list_of_lines) == 4)

# vim: filetype=python
