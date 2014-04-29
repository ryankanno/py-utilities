#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Size(object):
    def __init__(self, size_tuple):
        self._width = float(size_tuple[0])
        self._height = float(size_tuple[1])

    @property
    def aspect_ratio(self):
        return self.width / self.height

    @property
    def height(self):
        return self._height

    @property
    def size(self):
        return (self.width, self.height)

    @property
    def width(self):
        return self._width


# vim: filetype=python
