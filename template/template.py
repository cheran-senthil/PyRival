# PYTHON3---------------------------------------------------------------------#
from __future__ import division, print_function
range = xrange

# IMPORTS---------------------------------------------------------------------#
import math
import operator
import random
from atexit import register
from collections import Counter, defaultdict, deque
from fractions import Fraction, gcd
from io import BytesIO
#from decimal import Decimal, getcontext
from itertools import combinations, permutations, product
from Queue import PriorityQueue, Queue
from string import ascii_lowercase, ascii_uppercase
from sys import __stdout__, setrecursionlimit, stdin, stdout

# SETTINGS--------------------------------------------------------------------#
#getcontext().prec = 100
#setrecursionlimit(100000)

# CONSTANTS-------------------------------------------------------------------#
MOD = 10**9 + 7
INF = float('+inf')

# FASTIO----------------------------------------------------------------------#
stdout = BytesIO()
register(lambda: __stdout__.write(stdout.getvalue()))
#stdin = BytesIO(stdin.read())

input = lambda: stdin.readline().rstrip()
print = lambda *args: stdout.write(' '.join(str(x) for x in args) + '\n')
flush = stdout.flush()


# MAIN------------------------------------------------------------------------#
def main():
    # write Python3 code here
    print(input())


if __name__ == '__main__':
    main()
