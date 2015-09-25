__author__ = 'marcos'

import heapq

class AspectManager(object):

    def __init__(self):
        self.join_points = {}
        self.point_cuts = {}
        self.aspects = []

    def register_join_point(self, name, join_point):
        result = join_point
        for key, value in self.point_cuts.iteritems():
            if value['point_cut'].match(name):
                value['join_points'].append(join_point)

                for advice in value["advices"]:
                    result = advice[1].advise(result)

        return result

    def register_point_cut(self, point_cut):
        key = hash(point_cut)
        self.point_cuts[key] = {
            'point_cut': point_cut,
            'join_points': [],
            'advices': []
        }

    def register_advice(self, advice):
        point_cuts = self.point_cuts
        key = hash(advice.point_cut)
        advices = point_cuts[key]['advices']
        heapq.heappush(advices, (advice._sort_key, advice))

    def register_aspect(self, aspect, **attrs):
        self.aspects.append(aspect)

aspect_manager = AspectManager()


class AspectMeta(type):

    def __new__(mcs, name, bases, attrs):

        aspect = super(AspectMeta, mcs).__new__(mcs, name, bases, attrs)

        aspect_manager.register_aspect(aspect, **attrs)

        return aspect

    def __init__(cls, name, bases, attrs):
        super(AspectMeta, cls).__init__(name, bases, attrs)


class Aspect(object):
    __metaclass__ = AspectMeta
