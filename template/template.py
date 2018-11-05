#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Cheran Senthilkumar
#
# This file is part of https://github.com/Cheran-Senthil/PyRival
#
# PyRival is licensed under the MIT License

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

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading


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


def sync_with_stdio(sync=True):
    """
    Sets whether the standard Python streams are allowed to buffer their I/O.

    Parameters
    ----------
    sync : bool, optional
        The new synchronization setting. Default is True.

    """
    global input, flush

    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


def main():
    """Dattebayo!"""
    pass


if __name__ == '__main__':
    # Will only be executed when this module is run directly.
    sync_with_stdio(False)

    if 'PyPy' in sys.version:
        def bootstrap(c):
            callable, arg = c.switch()
            while True:
                to = continulet(lambda _, f, x: f(x), callable, arg)
                callable, arg = c.switch(to=to)

        c = continulet(bootstrap)
        c.switch()

        main()

    else:
        sys.setrecursionlimit(2097152)
        threading.stack_size(134217728)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
