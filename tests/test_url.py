#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *
from py_utilities.url import join
import unittest


class TestApi(unittest.TestCase):

    def test_join(self):
        eq_(join(), '')
        eq_(join('/foo'), '/foo')
        eq_(join('',''), '')
        eq_(join('','','',''), '')
        eq_(join('http://foo.com/', '/foo'), 'http://foo.com/foo')
        eq_(join('http://foo.com/', '/foo/'), 'http://foo.com/foo/')
        eq_(join('http://foo.com/', '/foo/', 'bar'), 'http://foo.com/foo/bar')

# vim: filetype=python
