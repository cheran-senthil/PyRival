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

    def gcd(a, b):
        """
        Calculate the Greatest Common Divisor of a and b.

        Parameters
        ----------
        a, b : int

        Returns
        -------
        int
            The greatest common divisor of the integers a and b.

        """
        while b:
            a, b = b, a % b
        return a

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
