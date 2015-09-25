# coding: utf-8

__author__ = 'marcos'


def load_module(module):
    return __import__(module)


class AspectLoader(object):

    @staticmethod
    def load_aspects_module(aspects_module):
        load_module(aspects_module)
