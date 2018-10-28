"""
What I cannot create, I do not understand.

https://github.com/Cheran-Senthil/PyRival
Copyright (c) 2018 Cheran Senthilkumar
"""
# IMPORTS---------------------------------------------------------------------#
from __future__ import division, print_function

import cmath
import itertools
import math
import operator as op
import sys
from bisect import bisect_left, bisect_right
from string import ascii_lowercase, ascii_uppercase

# from collections import Counter, MutableSequence, defaultdict, deque
# from copy import deepcopy
# from decimal import Decimal, getcontext
# from difflib import SequenceMatcher
# from heapq import heappop, heappush

# PYTHON3---------------------------------------------------------------------#
if sys.version_info[0] < 3:
    # import random
    # from cPickle import dumps
    # from fractions import Fraction, gcd
    # from Queue import PriorityQueue, Queue

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

    class dict(dict):
        def items(self):
            return dict.iteritems(self)

        def keys(self):
            return dict.iterkeys(self)

        def values(self):
            return dict.itervalues(self)
else:
    # from fractions import Fraction
    # from functools import reduce
    # from math import gcd
    # from pickle import dumps
    # from queue import PriorityQueue, Queue
    pass


# SETTINGS--------------------------------------------------------------------#
sys.setrecursionlimit(10000)
# getcontext().prec = 100


# IO--------------------------------------------------------------------------#
fastio = False
flush = sys.stdout.flush

if fastio:
    from atexit import register
    from io import BytesIO

    sys.stdout = BytesIO()
    register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
    sys.stdin = BytesIO(sys.stdin.read())

    input = lambda: sys.stdin.readline().rstrip()
    print = lambda *args: sys.stdout.write(' '.join(str(x) for x in args)+'\n')


# MAIN------------------------------------------------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
