#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
import os
from py_utilities.file_utilities import print_file_contents
import StringIO
import unittest


class TestFileUtilities(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.test_file = os.path.join(self.cwd, 'data',
                                      'test_csv_to_list_headers.csv')

    def test_print_file_contents(self):
        output = StringIO.StringIO()
        print_file_contents(self.test_file, output)
        eq_(output.getvalue(), 'Name,Age\nRyan,21\nBob,22\nJoe,23\n')

# vim: filetype=python
