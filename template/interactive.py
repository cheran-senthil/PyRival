#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import IOBase

input = lambda: sys.stdin.readline().rstrip('\r\n')

#region py3k
if sys.version_info[0] < 3:
    from future_builtins import ascii, filter, hex, map, oct, zip

    range = xrange

#endregion

#region fastio
input = sys.stdin.readline

sys.stdout = IOBase()
sys.stdout.write = lambda x: os.write(1, x) if sys.version_info[0] < 3 else os.write(1, x.encode())

#endregion


def main():
    pass


if __name__ == '__main__':
    main()
