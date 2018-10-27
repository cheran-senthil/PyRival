"""
What I cannot create, I do not understand.

https://github.com/Cheran-Senthil/PyRival
Copyright (c) 2018 Cheran Senthilkumar
"""
# IMPORTS---------------------------------------------------------------------#
from __future__ import division, print_function

import itertools
import sys

# import cmath
# import math
# import operator as op
# import random
# from bisect import bisect_left as bl, bisect_right as br
# from collections import Counter, defaultdict, deque
# from copy import deepcopy
# from decimal import Decimal, getcontext
# from difflib import SequenceMatcher
# from fractions import Fraction, gcd
# from heapq import heappop, heappush
# from Queue import PriorityQueue, Queue
# from string import ascii_lowercase, ascii_uppercase


# PYTHON3---------------------------------------------------------------------#
if sys.version_info[0] < 3:
    # from cPickle import dumps

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
    # from functools import reduce
    # from pickle import dumps
    pass


# SETTINGS--------------------------------------------------------------------#
sys.setrecursionlimit(14800)
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
