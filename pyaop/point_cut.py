# coding: utf-8

import re
from aspect import aspect_manager

__author__ = 'marcos'


class PointCut(object):

    def __init__(self, pattern):
        self.regex = re.compile(pattern)
        aspect_manager.register_point_cut(self)

    def __call__(self, _):
        return lambda: self

    def match(self, value):
        return self.regex.search(value) is not None
