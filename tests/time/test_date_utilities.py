#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_utilities.time.date_utilities import EPOCH_AS_STRUCT_TIME
from py_utilities.time.date_utilities import EPOCH_AS_DATETIME
import time
import unittest


class TestDateUtilities(unittest.TestCase):

    def test_epoch_as_struct_time(self):
        ok_(EPOCH_AS_STRUCT_TIME == time.gmtime(0))

    def test_epoch_as_datetime(self):
        ok_(EPOCH_AS_DATETIME.year == 1970)


# vim: filetype=python
