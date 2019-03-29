#!/usr/bin/env python2
from __future__ import division, print_function

import os
import sys
from __builtin__ import xrange as range
from cStringIO import StringIO
from future_builtins import ascii, filter, hex, map, oct, zip
from io import IOBase

sys.stdout, stream = IOBase(), StringIO()
sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
sys.stdout.write = stream.write

input, flush = sys.stdin.readline, sys.stdout.flush
input = StringIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    pass


if __name__ == '__main__':
    main()
