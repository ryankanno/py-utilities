#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


def apply(func_to_apply):
    def decorator(func):
        @functools.wraps(func)
        def f(*args, **kwargs):
            return func_to_apply(func(*args, **kwargs))
        return f
    return decorator
# vim: filetype=python
