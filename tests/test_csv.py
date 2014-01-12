#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
import os
from py_utilities.csv_utilities import csv_to_headers
from py_utilities.csv_utilities import csv_to_list
import unittest


class TestCsv(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.csv_headers_path = os.path.join(self.cwd, 'data',
                                             'test_csv_to_list_headers.csv')
        self.csv_no_headers_path = os.path.join(
            self.cwd, 'data', 'test_csv_to_list_no_headers.csv')

    def test_csv_to_list(self):
        data = csv_to_list(self.csv_headers_path)
        ok_(len(data) == 3)
        data = csv_to_list(self.csv_no_headers_path, has_headers=False)
        ok_(len(data) == 4)

    def test_csv_to_headers(self):
        data = csv_to_headers(self.csv_headers_path)
        ok_(len(data) == 2)
        data = csv_to_headers(self.csv_no_headers_path, has_headers=False)
        ok_(len(data) == 0)

# vim: filetype=python
