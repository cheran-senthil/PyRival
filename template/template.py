#!/usr/bin/env python
"""
This file is part of https://github.com/Cheran-Senthil/PyRival.

Copyright 2018 Cheran Senthilkumar all rights reserved,
Cheran Senthilkumar <hello@cheran.io>
Permission to use, modify, and distribute this software is given under the
terms of the MIT License.

"""
from __future__ import division, print_function

import cmath
import itertools
import math
import operator as op
# import random
import sys
from atexit import register
from bisect import bisect_left, bisect_right
# from collections import Counter, MutableSequence, defaultdict, deque
# from copy import deepcopy
# from decimal import Decimal
# from difflib import SequenceMatcher
# from fractions import Fraction
# from heapq import heappop, heappush

if sys.version_info[0] < 3:
    # from cPickle import dumps
    from io import BytesIO as stream
    # from Queue import PriorityQueue, Queue
else:
    # from functools import reduce
    from io import StringIO as stream
    from math import gcd
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


def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.

    Args:
        sync (bool, optional): The new synchronization setting.

    """
    global input, flush

    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


def read_ints():
    numb, sign = 0, 1
    res = []

    s = sys.stdin.read()
    for i in range(len(s)):
        if s[i] >= '0':
            numb = 10 * numb + ord(s[i]) - 48
        else:
            if s[i] == '-':
                sign = -1
            else:
                res.append(sign * numb)
                numb, sign = 0, 1

    if s[-1] >= '0':
        res.append(sign * numb)

    return res


def main():
    pass


if __name__ == '__main__':
    sync_with_stdio(False)

    if 'PyPy' in sys.version:
        main()
    else:
        import threading

        sys.setrecursionlimit(2097152)
        threading.stack_size(134217728)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
