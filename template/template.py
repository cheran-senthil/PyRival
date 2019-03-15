#!/usr/bin/env python
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
from __future__ import division, print_function

import itertools
import os
import sys
from atexit import register

if sys.version_info[0] < 3:
    from cStringIO import StringIO

    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
else:
    from io import BytesIO as StringIO

input = StringIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdout = StringIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

if sys.version_info[0] >= 3:
    _write = sys.stdout.write
    sys.stdout.write = lambda s: _write(s.encode())


def main():
    pass


if __name__ == '__main__':
    main()
