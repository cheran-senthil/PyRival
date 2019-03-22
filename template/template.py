#!/usr/bin/env python
from __future__ import division, print_function

import atexit
import os
import sys

#region p3k
if sys.version_info[0] < 3:
    from itertools import ifilter, imap, izip

    range = xrange
    filter, map, zip = ifilter, imap, izip

input = lambda: sys.stdin.readline().rstrip('\r\n')

#endregion

#region fastio
if sys.version_info[0] < 3:
    from cStringIO import StringIO
else:
    from io import BytesIO as StringIO

input = StringIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdout = StringIO()
atexit.register(lambda: os.write(1, sys.stdout.getvalue()))

if sys.version_info[0] >= 3:
    _write = sys.stdout.write
    sys.stdout.write = lambda s: _write(s.encode())

#endregion


def main():
    pass


if __name__ == '__main__':
    main()
