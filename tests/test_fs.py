#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from nose.tools import raises
import os
from py_utilities.fs import mkdir_p
from py_utilities.fs import touch
import shutil
import unittest


class TestFs(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))

    def tearDown(self):
        if os.path.exists('/tmp/foo'):
            shutil.rmtree('/tmp/foo')

    def test_mkdir_p(self):
        mkdir_p('/tmp/foo/bar/rules')
        ok_(os.path.exists('/tmp/foo'))
        ok_(os.path.exists('/tmp/foo/bar'))
        ok_(os.path.exists('/tmp/foo/bar/rules'))

    @raises(OSError)
    def test_mkdir_p_raise_exception(self):
        mkdir_p('/tmp/foo/bar/rules')
        f = open('/tmp/foo/bar/rules/file', 'w')
        f.close()
        mkdir_p('/tmp/foo/bar/rules/file')

    def test_mkdir_p_should_not_raise_exception(self):
        mkdir_p('/tmp/foo/bar/rules')
        mkdir_p('/tmp/foo/bar/rules')

    def test_touch(self):
        file = os.path.join(self.cwd, 'test_fs.py')
        curr_access_time = os.path.getmtime(file)
        touch(file)
        new_access_time = os.path.getmtime(file)
        ok_(new_access_time > curr_access_time)

# vim: filetype=python
