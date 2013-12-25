#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from nose.tools import raises
import os
from py_utilities.fs import mkdir_p
import shutil
import unittest


class TestFs(unittest.TestCase):

    def tearDown(self):
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


# vim: filetype=python
