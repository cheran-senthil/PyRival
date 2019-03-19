""" Python 3 compatibility tools. """
from __future__ import division, print_function

import sys

if sys.version_info[0] < 3:
    from cStringIO import StringIO
    from itertools import ifilter, imap, izip
    from Queue import Queue
else:
    from functools import reduce
    from io import BytesIO as StringIO
    from queue import Queue

if sys.version_info[0] < 3:
    input, range = raw_input, xrange
    filter, map, zip = ifilter, imap, izip


def gcd(x, y):
    """ greatest common divisor of x and y """
    while y:
        x, y = y, x % y
    return x
