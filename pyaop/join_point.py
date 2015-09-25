# coding: utf-8

__author__ = 'marcos'


class ProceedingJoinPoint(object):

    def __init__(self, fn):
        self._fn = fn
        self._args = []
        self._kwargs = {}

    def set_call_parameters(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def proceed(self):
        return self._fn(*self._args, **self._kwargs)
