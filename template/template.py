"""
What I cannot create, I do not understand.

https://github.com/Cheran-Senthil/PyRival
Copyright (c) 2018 Cheran Senthilkumar
"""
from __future__ import division, print_function

import cmath
import itertools
import math
import operator as op
import sys
from bisect import bisect_left, bisect_right
from string import ascii_lowercase, ascii_uppercase

# import random
# from collections import Counter, MutableSequence, defaultdict, deque
# from copy import deepcopy
# from decimal import Decimal
# from difflib import SequenceMatcher
# from heapq import heappop, heappush


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


def sync_with_stdio(sync=True):
    """
    Sets whether the standard Python streams are allowed to buffer their I/O.

    Parameters
    ----------
    sync : bool
        the new synchronization setting

    """
    global input, flush

    if sync:
        flush = sys.stdout.flush
    else:
        from atexit import register

        if sys.version_info[0] < 3:
            from io import BytesIO

            input = iter(sys.stdin.read().splitlines()).next
            sys.stdout = BytesIO()
        else:
            from io import StringIO

            input = iter(sys.stdin.read().splitlines()).__next__
            sys.stdout = StringIO()

        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


def main():
    pass


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    sync_with_stdio()
    main()
