#!/usr/bin/env python
# -*- coding: utf-8 -*-


def join(*args):
    """
    Join url paths together
    """
    args_with_no_ws = filter(lambda arg: arg.strip(), args)

    if not len(args_with_no_ws):
        return ""

    if len(args_with_no_ws) == 1:
        return args_with_no_ws[0]

    joined = '/'.join(path.strip('/') for path in args_with_no_ws)

    last_arg = args_with_no_ws[-1]

    if len(last_arg) > 0:
        return joined + '/' if last_arg[-1] == '/' else joined
    else:
        return joined


# vim: filetype=python
