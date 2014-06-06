#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
import os
from py_utilities.compression.tar_utilities import create_tarball
import shutil
import tarfile
import tempfile
import unittest


class TestTarUtilities(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.temp_dir = tempfile.gettempdir()
        self.temp_tar = os.path.join(self.temp_dir, 'test_tar')
        self.test_dir = os.path.join(self.cwd, '..', 'data')

        if not os.path.exists(self.temp_tar):
            os.makedirs(self.temp_tar)

    def tearDown(self):
        if os.path.exists(self.temp_tar):
            shutil.rmtree(self.temp_tar)

    def test_create_tarball_gzip(self):
        create_tarball([self.test_dir], 'foobar', self.temp_tar)
        for file in os.listdir(self.temp_tar):
            if 'foobar' in file:
                filename = os.path.join(self.temp_tar, file)
                ok_(os.stat(filename).st_size > 0)
                tarball = tarfile.open(filename)
                ok_(len(tarball.getmembers()) > 0)

# vim: filetype=python
