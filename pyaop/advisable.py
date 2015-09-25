# coding: utf-8
from aspect import aspect_manager

__author__ = 'marcos'


class MetaAdvisable(type):

    def __new__(mcs, name, bases, attrs):

        if name != "Advisable":

            for name, attr in attrs.iteritems():
                if callable(attr):
                    attrs[name] = aspect_manager.register_join_point(name, attr)

        return super(MetaAdvisable, mcs).__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super(MetaAdvisable, cls).__init__(name, bases, attrs)


class Advisable(object):
    __metaclass__ = MetaAdvisable
