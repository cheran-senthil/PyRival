"""Python 3 compatibility tools."""
from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    # from fractions import Fraction
    # from fractions import gcd
    # from cPickle import dumps
    # from Queue import PriorityQueue, Queue
    pass
else:
    # from functools import reduce
    # from fractions import Fraction
    # from math import gcd
    # from pickle import dumps
    # from queue import PriorityQueue, Queue
    pass


if sys.version_info[0] < 3:
    class dict(dict):
        def items(self):
            return dict.iteritems(self)

        def keys(self):
            return dict.iterkeys(self)

        def values(self):
            return dict.itervalues(self)

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
