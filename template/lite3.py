#!/usr/bin/env python3
import os
import sys
from atexit import register
from io import StringIO

sys.stdin = StringIO(os.read(0, os.fstat(0).st_size).decode())
sys.stdout = StringIO()
register(lambda: os.write(1, sys.stdout.getvalue().encode()))

input = lambda: sys.stdin.readline().rstrip('\r\n')


def main():
    pass


if __name__ == '__main__':
    main()
