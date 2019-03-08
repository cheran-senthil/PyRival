#!/usr/bin/env python2
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
from __future__ import division, print_function

import itertools
import os
import sys
from atexit import register
from io import BytesIO


class dict(dict):
    """ dict() -> new empty dictionary """

    def items(self):
        """ D.items() -> a set-like object providing a view on D's items """
        return dict.iteritems(self)

    def keys(self):
        """ D.keys() -> a set-like object providing a view on D's keys """
        return dict.iterkeys(self)

    def values(self):
        """ D.values() -> an object providing a view on D's values """
        return dict.itervalues(self)


def gcd(x, y):
    """ greatest common divisor of x and y """
    while y:
        x, y = y, x % y
    return x


range = xrange

filter = itertools.ifilter
map = itertools.imap
zip = itertools.izip

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')


def main():
    pass


if __name__ == '__main__':
    main()
