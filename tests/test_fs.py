#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import eq_
from nose.tools import ok_
from nose.tools import raises
import os
from py_utilities.fs import cd
from py_utilities.fs import mkdir_p
from py_utilities.fs import touch
import shutil
import tempfile
import unittest


class TestFs(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.temp_dir = tempfile.gettempdir()

    def tearDown(self):
        tmp_foo = os.path.join(self.temp_dir, 'foo')
        if os.path.exists(tmp_foo):
            shutil.rmtree(tmp_foo)

    def test_cd(self):
        curr = os.getcwd()
        path = os.path.realpath(self.temp_dir)
        with cd(path):
            cwd = os.getcwd()
            ok_(curr != cwd)
            eq_(cwd, path)
        cwd = os.getcwd()
        eq_(curr, cwd)

    def test_mkdir_p(self):
        tmp_foo = os.path.join(self.temp_dir, 'foo')
        tmp_foo_bar = os.path.join(self.temp_dir, 'foo', 'bar')
        tmp_foo_bar_rules = os.path.join(self.temp_dir, 'foo', 'bar', 'rules')
        mkdir_p(tmp_foo_bar_rules)
        ok_(os.path.exists(tmp_foo))
        ok_(os.path.exists(tmp_foo_bar))
        ok_(os.path.exists(tmp_foo_bar_rules))

    @raises(OSError)
    def test_mkdir_p_raise_exception(self):
        tmp_foo_bar_rules = os.path.join(self.temp_dir, 'foo', 'bar', 'rules')
        mkdir_p(tmp_foo_bar_rules)
        tmp_file = os.path.join(tmp_foo_bar_rules, 'file')
        f = open(tmp_file, 'w')
        f.close()
        mkdir_p(tmp_file)

    def test_mkdir_p_should_not_raise_exception(self):
        tmp_foo_bar_rules = os.path.join(self.temp_dir, 'foo', 'bar', 'rules')
        mkdir_p(tmp_foo_bar_rules)
        mkdir_p(tmp_foo_bar_rules)

    def test_touch(self):
        file = os.path.join(self.cwd, 'test_fs.py')
        curr_access_time = os.path.getmtime(file)
        touch(file)
        new_access_time = os.path.getmtime(file)
        ok_(new_access_time > curr_access_time)

# vim: filetype=python
