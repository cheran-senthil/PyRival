#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
    from cStringIO import StringIO as BytesIO
else:
    from io import BytesIO

BUFSIZE = 8192


class FastIO(IOBase):
    stream = BytesIO()
    newlines = 0

    def __init__(self, fd):
        self.fd = fd
        self.flush = lambda: os.write(fd, self.stream.getvalue()) and not self.stream.truncate(0) and self.stream.seek(0)
        self.write = self.stream.write if sys.version_info[0] < 3 else lambda b: self.stream.write(b.encode())

    def readline(self):
        while self.newlines == 0:
            b, ptr = os.read(self.fd, max(os.fstat(self.fd).st_size, BUFSIZE)), self.stream.tell()
            self.stream.seek(0, 2), self.stream.write(b), self.stream.seek(ptr)
            self.newlines += b.count(b'\n') + (not b)

        self.newlines -= 1
        return self.stream.readline()


sys.stdin, sys.stdout = FastIO(0), FastIO(1)
input, flush = sys.stdin.readline, sys.stdout.flush


def main():
    pass


if __name__ == '__main__':
    main()
