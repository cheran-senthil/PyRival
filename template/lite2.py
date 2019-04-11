#!/usr/bin/env python2
from __future__ import division, print_function

import os
import sys
from __builtin__ import xrange as range
from cStringIO import StringIO
from future_builtins import ascii, filter, hex, map, oct, zip
from io import IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    stream = StringIO()
    newlines = 0

    def __init__(self, fd):
        self.fd = fd
        self.flush = lambda: os.write(fd, self.stream.getvalue()) and not self.stream.truncate(0) and self.stream.seek(0)
        self.write = self.stream.write

    def readline(self):
        while self.newlines == 0:
            b, ptr = os.read(self.fd, max(os.fstat(self.fd).st_size, BUFSIZE)), self.stream.tell()
            self.stream.seek(0, 2), self.stream.write(b), self.stream.seek(ptr)
            self.newlines += b.count('\n') + (not b)

        self.newlines -= 1
        return self.stream.readline()


sys.stdin, sys.stdout = FastIO(0), FastIO(1)
input, flush = sys.stdin.readline, sys.stdout.flush


def main():
    pass


if __name__ == '__main__':
    main()
