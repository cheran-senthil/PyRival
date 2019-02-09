#!/usr/bin/env python
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

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
# from collections import Counter, defaultdict, deque
# from copy import deepcopy
# from decimal import Decimal
# from difflib import SequenceMatcher
# from functools import reduce
# from heapq import heappop, heappush
from io import BytesIO, FileIO, StringIO

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

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

INP_FILE = 0
OUT_FILE = 1

if sys.version_info[0] < 3:
    sys.stdin = BytesIO(FileIO(INP_FILE).read())
    sys.stdout = BytesIO()
    register(lambda: FileIO(OUT_FILE, 'w').write(sys.stdout.getvalue()))
else:
    sys.stdin = StringIO(FileIO(INP_FILE).read().decode())
    sys.stdout = StringIO()
    register(lambda: FileIO(OUT_FILE, 'w').write(sys.stdout.getvalue().encode(
    )))

input = lambda: sys.stdin.readline().rstrip('\r\n')


def main():
    pass


if __name__ == '__main__':
    main()
