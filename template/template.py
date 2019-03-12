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
from io import BytesIO, StringIO

if sys.version_info[0] < 3:
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
else:
    sys.stdin = StringIO(os.read(0, os.fstat(0).st_size).decode())
    sys.stdout = StringIO()
    register(lambda: os.write(1, sys.stdout.getvalue().encode()))

input = lambda: sys.stdin.readline().rstrip('\r\n')


def main():
    pass


if __name__ == '__main__':
    main()
