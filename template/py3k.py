""" Python 3 compatibility tools. """
from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    from cPickle import dumps
    from Queue import PriorityQueue, Queue
else:
    from functools import reduce
    from pickle import dumps
    from queue import PriorityQueue, Queue

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip


def gcd(x, y):
    """ greatest common divisor of x and y """
    while y:
        x, y = y, x % y
    return x
