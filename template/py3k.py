"""Python 3 compatibility tools."""
from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    # from cPickle import dumps
    # from Queue import PriorityQueue, Queue
    pass
else:
    from math import gcd
    # from functools import reduce
    # from pickle import dumps
    # from queue import PriorityQueue, Queue


if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)

        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)

        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)

    def gcd(x, y):
        """greatest common divisor of x and y"""
        while y:
            x, y = y, x % y
        return x

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
