from __future__ import division, print_function

import atexit
import io
import math
import operator
import random
import sys
from collections import Counter, defaultdict, deque
from fractions import Fraction, gcd
#from decimal import Decimal, getcontext
from itertools import combinations, permutations, product
from Queue import PriorityQueue, Queue
from string import ascii_lowercase, ascii_uppercase

#getcontext().prec = 100

MOD = 10**9 + 7
INF = float("+inf")

sys.stdout = io.BytesIO()
atexit.register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
sys.stdin = io.BytesIO(sys.stdin.read()) # comment this line for interactive problems 

input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(" ".join(str(x) for x in args) + "\n")
range = xrange

#---------------------------------------------------------------

def main():
    # write code here
    print(input())

if __name__ == "__main__":
    main()
