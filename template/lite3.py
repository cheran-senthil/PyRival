#!/usr/bin/env python3
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
import os
import sys
from atexit import register
from io import BytesIO

sys.stdout = BytesIO()
_write = sys.stdout.write
sys.stdout.write = lambda s: _write(s.encode())

register(lambda: os.write(1, sys.stdout.getvalue()))
input = BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    pass


if __name__ == '__main__':
    main()
