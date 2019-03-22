#!/usr/bin/env python
""" https://github.com/cheran-senthil/PyRival <hello@cheran.io> """

from __future__ import division, print_function

import os
import sys
from atexit import register

if sys.version_info[0] < 3:
    from cStringIO import StringIO
    from itertools import ifilter, imap, izip
else:
    from io import BytesIO as StringIO

sys.stdout = StringIO()
if sys.version_info[0] < 3:
    range = xrange
    filter, map, zip = ifilter, imap, izip
else:
    _write = sys.stdout.write
    sys.stdout.write = lambda s: _write(s.encode())

register(lambda: os.write(1, sys.stdout.getvalue()))
input = StringIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    pass


if __name__ == '__main__':
    main()
