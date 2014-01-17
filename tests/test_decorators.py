#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from py_utilities.decorators import apply
import unittest


def add_1(iterable):
    return [x+1 for x in iterable]


@apply(add_1)
def foo():
    return [1, 2, 3]


class TestDecorator(unittest.TestCase):

    def test_apply(self):
        result = foo()
        ok_(result == [2, 3, 4])

# vim: filetype=python
