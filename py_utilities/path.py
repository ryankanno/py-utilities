#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def expanded_abspath(dir):
    expanded = os.path.expanduser(os.path.expandvars(dir))
    return os.path.abspath(expanded)

# vim: filetype=python
