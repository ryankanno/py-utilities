#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_utilities.time.date_utilities import EPOCH
import time
import unittest


class TestDateUtilities(unittest.TestCase):

    def test_epoch(self):
        ok_(EPOCH == time.gmtime(0))

# vim: filetype=python
