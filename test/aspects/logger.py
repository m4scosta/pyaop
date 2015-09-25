# coding: utf-8
from __future__ import absolute_import, unicode_literals
from pyaop.aspect import Aspect, aspect_manager
from pyaop.advice import After, Before, AfterThrowing, AfterReturn, Around
from pyaop.point_cut import PointCut


class LoggingAspect(Aspect):

    @PointCut(pattern="^init")
    def test(self):
        pass

    @Around(point_cut=test())
    def log_action4(self, proceeding_join_point):
        print "around"
        return proceeding_join_point.proceed()

    @Before(point_cut=test())
    def log_action2(self):
        print("before advice")

    @After(point_cut=test())
    def log_action(self):
        print("after advice")

    @AfterThrowing(point_cut=test())
    def log_action3(self, e):
        print("after throwing advice: " + e.message)

    @AfterReturn(point_cut=test())
    def log_action3(self, return_value):
        print "after returning:", return_value

