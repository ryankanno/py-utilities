#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_utilities.image.image_helper import Size
import random
import unittest


class TestImageHelper(unittest.TestCase):

    def test_size_obj(self):
        rand_width = random.random()
        rand_height = random.random()
        rand_width_height_tuple = (rand_width, rand_height)
        size_obj = Size(rand_width_height_tuple)
        ok_(size_obj.width == rand_width)
        ok_(size_obj.height == rand_height)
        ok_(size_obj.aspect_ratio == (rand_width / rand_height))
        ok_(size_obj.size == rand_width_height_tuple)

# vim: filetype=python
