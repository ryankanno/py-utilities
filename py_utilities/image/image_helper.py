#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Size(object):
    def __init__(self, size_tuple):
        self.width = float(size_tuple[0])
        self.height = float(size_tuple[1])

    @property
    def aspect_ratio(self):
        return self.width / self.height

    @property
    def size(self):
        return (self.width, self.height)

# vim: filetype=python
