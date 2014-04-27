#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_utilities.time.date_utilities import EPOCH_AS_STRUCT_TIME
from py_utilities.time.date_utilities import EPOCH_AS_DATETIME
from py_utilities.time.date_utilities import next_day
import time
import unittest


class TestDateUtilities(unittest.TestCase):

    def test_epoch_as_struct_time(self):
        ok_(EPOCH_AS_STRUCT_TIME == time.gmtime(0))

    def test_epoch_as_datetime(self):
        ok_(EPOCH_AS_DATETIME.year == 1970)

    def test_next_day_same_week_where_day_hasnt_passed(self):
        # epoch is Thursday, January 1, 1970
        saturday = next_day(EPOCH_AS_DATETIME, 6)
        ok_(saturday.day == 3)
        ok_(saturday.year == 1970)
        ok_(saturday.month == 1)

    def test_next_day_next_week_where_day_has_passed(self):
        # epoch is Thursday, January 1, 1970
        next_wednesday = next_day(EPOCH_AS_DATETIME, 3)
        ok_(next_wednesday.day == 7)
        ok_(next_wednesday.year == 1970)
        ok_(next_wednesday.month == 1)


# vim: filetype=apython
