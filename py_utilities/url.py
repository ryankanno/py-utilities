#!/usr/bin/env python
# -*- coding: utf-8 -*-


def join(*args):
    """
    Join url paths together
    """
    if not len(args):
        return ""

    if len(args) == 1:
        return args[0]

    joined = '/'.join(path.strip('/') for path in args)

    is_empty = dict.fromkeys(" /")

    if all(c in is_empty for c in joined):
        return ""

    last_arg = args[-1]

    if len(last_arg) > 0:
        return joined + '/' if last_arg[-1] == '/' else joined
    else:
        return joined


# vim: filetype=python
