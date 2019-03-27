from __future__ import division, print_function

import os
import sys
import io
from cStringIO import StringIO
from future_builtins import ascii, filter, hex, map, oct, zip

input = lambda: sys.stdin.readline().rstrip('\r\n')
range = xrange

#region fastio
input = StringIO(os.read(0, os.fstat(0).st_size)).readline

sys.stdout, stream = io.IOBase(), StringIO()
sys.stdout.flush = lambda: os.write(1, stream.getvalue())
sys.stdout.write = stream.write

#endregion


def main():
    pass


if __name__ == '__main__':
    main()
