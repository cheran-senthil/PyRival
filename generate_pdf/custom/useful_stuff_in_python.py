# --- Fractions ---
from fractions import Fraction

f = Fraction(6, 8)  # Automatically simplifies to 3/4
print(f)  # 3/4
print(f.numerator, f.denominator)  # 3 4


# --- Decimal (High Precision) ---
from decimal import Decimal, getcontext

getcontext().prec = 30  # Set precision
print(Decimal(1) / Decimal(7))  # 0.142857142857142857142857142857
print(Decimal('0.1') + Decimal('0.2'))  # 0.3 (exact)


# --- Output Formatting & Floating Point Decimals ---
val = 5.12399
print(f'{val:.4f}')  # 5.1240 (rounds to 4 decimals)

# Integer zero-padding example
num = 42
print(f'{num:05d}')  # 00042 (zero-pad with <= 5 zeros)


# --- Sys Settings & File / Stream I/O ---
import sys

# Print with flush
# Note that calling input() also flushes
# Warning: flushing can be slow
print('Hello world', flush=True)

# Read input without flushing
input = lambda: sys.stdin.readline().rstrip()

# Reading all tokenized inputs at once.
# Fastest way to read input in Python
# input_data = sys.stdin.read().split()

# Increase recursion depth for deep DFS
# Warning: May not work as expected!
# Consider making use of bootstrap.py instead
sys.setrecursionlimit(200000)  

# Allow huge int-to-string conversions
# Default limit is 4300 digits
sys.set_int_max_str_digits(100000)  

# Print to stderr
print('Debug message', file=sys.stderr)

# Reading from / Writing to files:
# with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
#     content = fin.read()
#     fout.write(content)


# --- Heapq (Min-Heap) ---
import heapq

h = [3, 1, 4, 1, 5, 9]
heapq.heapify(h)  # Transforms list into a min-heap in-place
heapq.heappush(h, 2)  # Push item
print(heapq.heappop(h))  # Pop smallest item
print(h[0])  # Peek at current smallest item


# --- Collections (defaultdict, Counter) ---
from collections import Counter, defaultdict

d = defaultdict(list)
d['key'].append(10)
print(d['key'])  # [10]
print(d['missing_key'])  # [] (automatically created)

c = Counter('abracadabra')
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(c.most_common(2))  # [('a', 5), ('b', 2)]


# --- Random ---
import random

random.seed(42)
print(random.randint(1, 10))  # Random int [a, b] inclusive
print(random.randrange(0, 10, 2))  # Random from range(start, stop, step)
print(random.choice(['apple', 'banana', 'cherry']))  # Random element from sequence
print(random.uniform(1.0, 5.0))  # Random float between a and b inclusive
print(random.getrandbits(8))  # Random integer with k random bits


# --- Itertools ---
import itertools

P = itertools.permutations('ABC', 2)
print(*P)  # ('A', 'B') ('A', 'C') ('B', 'A') ('B', 'C') ('C', 'A') ('C', 'B')

C = itertools.combinations('ABC', 2)
print(*C)  # ('A', 'B') ('A', 'C') ('B', 'C')

CR = itertools.combinations_with_replacement('ABC', 2)
print(*CR)  # ('A', 'A') ('A', 'B') ('A', 'C') ('B', 'B') ('B', 'C') ('C', 'C')


# --- Memoisation ---
from functools import cache

@cache  # Automatically memoises return values
def fib(n):
  return n if n < 2 else fib(n - 1) + fib(n - 2)

print(fib(50))


# --- Bit Operations (bit_length, bit_count) ---
x = 5  # in binary 0b101
print(x.bit_length())  # 3 (number of bits needed to represent x)
print(x.bit_count())  # 2 (number of set bits / popcount, Python 3.10+)


# --- Alphabet & Character Checks ---
import string

print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

vowels = set('aeiouAEIOU')
print('a' in vowels)  # True
print('b'.isalpha())  # True

s = '  hello world  '
print(s.strip())  # 'hello world' (strips both ends)
print(s.lstrip())  # 'hello world  ' (strips left)
print(s.rstrip())  # '  hello world' (strips right)

words = ['apple', 'banana', 'cherry']
print('-'.join(words))  # 'apple-banana-cherry'

print('42'.ljust(5, '0'))  # '42000' (left-justified, padded)
print('42'.rjust(5, '0'))  # '00042' (right-justified, padded)

text = 'apple,banana,cherry'
print(text.split(','))  # ['apple', 'banana', 'cherry'] (with argument)
print('  a   b  c '.split())  # ['a', 'b', 'c'] (without argument, splits by whitespace)

# Substring check & counting
print('ana' in 'banana')  # True (checks if substring exists)
print('bananana'.count('ana'))  # 2 (counts non-overlapping occurrences: b[ana]n[ana])


# --- Bisect (Binary Search) ---
import bisect

arr = [1, 3, 3, 3, 5, 7]
print(bisect.bisect_left(arr, 3))  # 1 (first insertion index)
print(bisect.bisect_right(arr, 3))  # 4 (last insertion index)


# --- Math Module & Division Tricks ---
import math

print(math.pi)  # 3.141592653589793
print(math.gcd(24, 36))  # 12
print(math.lcm(4, 6))  # 12
print(math.comb(5, 2))  # 10 (nCr / binomial coefficient)
print(math.perm(5, 2))  # 20 (nPr)
print(math.isqrt(10))  # 3 (integer square root)
print(math.inf)  # Infinity representation

# Division types:
a, b = 7, 3
print(a // b)  # 2 (floored division)
print(0 -- a // b))  # 3 (ceiled division)


# --- Prime Sieve (Sieve of Eratosthenes) ---
limit = 30
is_prime = [1] * limit
is_prime[0] = is_prime[1] = 0
for i in range(2, int(limit**0.5) + 1):
  if is_prime[i]:
    for j in range(i * i, limit, i):
      is_prime[j] = 0

primes = [i for i, p in enumerate(is_prime) if p]
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
