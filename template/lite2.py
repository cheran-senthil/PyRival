#!/usr/bin/env python2
from __future__ import division, print_function

import os
import sys
from __builtin__ import xrange as range
from cStringIO import StringIO as BytesIO
from future_builtins import ascii, filter, hex, map, oct, zip
from io import IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._buffer = BytesIO()
        self._fd = file
        self.flush = lambda: os.write(self._fd, self._buffer.getvalue()) and not self._buffer.truncate(0) and self._buffer.seek(0)
        self.write = self._buffer.write

    def readline(self):
        while self.newlines == 0:
            b, ptr = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE)), self._buffer.tell()
            self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr)
            self.newlines += b.count(b'\n') + (not b)
        self.newlines -= 1
        return self._buffer.readline()


sys.stdin, sys.stdout = FastIO(0), FastIO(1)
input = lambda: sys.stdin.readline().rstrip(b'\r\n')


def print(*args, **kwargs):
    sep, file = kwargs.pop('sep', b' '), kwargs.pop('file', sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop('end', b'\n'))
    if kwargs.pop('flush', False):
        file.flush()


def main():
    pass


if __name__ == '__main__':
    main()
