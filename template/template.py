#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
from io import IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from cStringIO import StringIO
    from future_builtins import ascii, filter, hex, map, oct, zip
else:
    from io import BytesIO as StringIO


class FastI:
    stream = StringIO()
    newlines = 0

    def readline(self):
        while self.newlines == 0:
            b, ptr = os.read(0, (1 << 13) + os.fstat(0).st_size), self.stream.tell()
            self.stream.seek(0, 2), self.stream.write(b), self.stream.seek(ptr)
            self.newlines += b.count(b'\n') + (not b)

        self.newlines -= 1
        return self.stream.readline()


class FastO(IOBase):
    def __init__(self):
        stream = StringIO()
        self.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
        self.write = stream.write if sys.version_info[0] < 3 else lambda b: stream.write(b.encode())


class ostream:
    def __lshift__(self, a):
        if a == endl:
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            sys.stdout.write(str(a))
        return self


sys.stdin, sys.stdout = FastI(), FastO()
input, flush = sys.stdin.readline, sys.stdout.flush
cout, endl = ostream(), object()


def main():
    pass


if __name__ == '__main__':
    main()
