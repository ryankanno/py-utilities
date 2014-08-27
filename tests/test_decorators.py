#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
import os
from py_utilities.decorators import apply
from py_utilities.decorators import run_once
from py_utilities.decorators import safe
import unittest


def add_1(iterable):
    return [x+1 for x in iterable]


@apply(add_1)
def foo():
    """ Foo docstring """
    return [1, 2, 3]


@run_once
def foo_once():
    """ Foo_once docstring """
    return [1, 2, 3]


@safe(lambda path: os.stat(path), None)
def fake_foo():
    pass


class TestDecorator(unittest.TestCase):

    def test_apply(self):
        result = foo()
        ok_(result == [2, 3, 4])
        ok_(foo.__name__ == 'foo')
        ok_(foo.__doc__ == ' Foo docstring ')

    def test_run_once(self):
        result = foo_once()
        ok_(result == [1, 2, 3])
        result2 = foo_once()
        ok_(result2 is None)
        ok_(foo_once.__name__ == 'foo_once')
        ok_(foo_once.__doc__ == ' Foo_once docstring ')

    def test_safe(self):
        result = fake_foo('/var/tmp/asdlkfjsadlkfjasdklfjasl')
        ok_(result is None)

# vim: filetype=python
