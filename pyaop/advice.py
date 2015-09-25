# coding: utf-8

from functools import wraps

from aspect import aspect_manager
from join_point import ProceedingJoinPoint

__author__ = 'marcos'


class Advice(object):

    def __init__(self, point_cut):
        self.point_cut = point_cut
        self._sort_key = 0
        aspect_manager.register_advice(self)

    def __call__(self, fn):
        self._fn = fn

    def __eq__(self, other):
        return self._sort_key == other._sort_key

    def __gt__(self, other):
        return self._sort_key > other._sort_key

    def __lt__(self, other):
        return self._sort_key < other._sort_key

    def advise(self, fn):
        raise NotImplementedError()


class Around(Advice):

    def __init__(self, *args, **kwargs):
        self._sort_key = 4
        super(Around, self).__init__(*args, **kwargs)

    def advise(self, fn):
        this = self

        @wraps(fn)
        def decorated(*args, **kwargs):
            proceeding_join_point = ProceedingJoinPoint(fn)
            proceeding_join_point.set_call_parameters(*args, **kwargs)

            return this._fn(this, proceeding_join_point)

        return decorated


class Before(Advice):

    def __init__(self, *args, **kwargs):
        self._sort_key = 3
        super(Before, self).__init__(*args, **kwargs)

    def advise(self, fn):
        this = self

        @wraps(fn)
        def decorated(*args, **kwargs):
            this._fn(this)
            results = fn(*args, **kwargs)
            return results

        return decorated


class After(Advice):

    def __init__(self, *args, **kwargs):
        self._sort_key = 0
        super(After, self).__init__(*args, **kwargs)

    def advise(self, fn):
        this = self

        @wraps(fn)
        def decorated(*args, **kwargs):

            exception_raised = None
            results = None

            try:
                results = fn(*args, **kwargs)
            except Exception as e:
                exception_raised = e
            finally:
                this._fn(this)
                if exception_raised is not None:
                    raise e

            return results

        return decorated


class AfterReturn(Advice):

    def __init__(self, *args, **kwargs):
        self._sort_key = 1
        super(AfterReturn, self).__init__(*args, **kwargs)

    def advise(self, fn):
        this = self

        @wraps(fn)
        def decorated(*args, **kwargs):
            try:
                results = fn(*args, **kwargs)
            except Exception as e:
                raise e
            else:
                this._fn(this, results)
            return results

        return decorated


class AfterThrowing(Advice):

    def __init__(self, *args, **kwargs):
        self._sort_key = 2
        super(AfterThrowing, self).__init__(*args, **kwargs)

    def advise(self, fn):
        this = self

        @wraps(fn)
        def decorated(*args, **kwargs):
            results = None

            try:
                results = fn(*args, **kwargs)
            except Exception as e:
                this._fn(this, e)

            return results

        return decorated
