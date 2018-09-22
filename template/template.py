"""
Ares hates those who hesitate.

https://github.com/Cheran-Senthil/PyRival
Copyright (c) 2018 Cheran Senthilkumar
"""
# IMPORTS---------------------------------------------------------------------#
from __future__ import division, print_function

import itertools
# import math
# import operator as op
# import random
# from collections import Counter, defaultdict, deque
# from fractions import Fraction, gcd
# from itertools import combinations, permutations, product
# from Queue import PriorityQueue, Queue


# PYTHON3---------------------------------------------------------------------#
class dict(dict):
    def keys(self):
        return dict.iterkeys(self)

    def items(self):
        return dict.iteritems(self)

    def values(self):
        return dict.itervalues(self)


filter = itertools.ifilter
map = itertools.imap
zip = itertools.izip

range = xrange
input = raw_input


# FASTIO----------------------------------------------------------------------#
# from atexit import register
# from io import BytesIO
# from sys import __stdout__, stdin, stdout

# stdout = BytesIO()
# register(lambda: __stdout__.write(stdout.getvalue()))
# stdin = BytesIO(stdin.read())

# input = lambda: stdin.readline().rstrip()
# print = lambda *args: stdout.write(' '.join(str(x) for x in args) + '\n')
# flush = stdout.flush()


# SETTINGS--------------------------------------------------------------------#
# from decimal import Decimal, getcontext
# from sys import setrecursionlimit

# getcontext().prec = 100
# setrecursionlimit(100000)


# CONSTANTS-------------------------------------------------------------------#
MOD = 1000000007
INF = float('+inf')

ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
ASCII_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# MAIN------------------------------------------------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
