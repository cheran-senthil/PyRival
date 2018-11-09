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
        def items(self):
            return dict.iteritems(self)

        def keys(self):
            return dict.iterkeys(self)

        def values(self):
            return dict.itervalues(self)

    def gcd(x, y):
        """gcd(x, y) -> int
        greatest common divisor of x and y
        """
        while y:
            x, y = y, x % y
        return x

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
