#!/usr/bin/env python3
import os
import sys
from io import BytesIO


class FastI(BytesIO):
    newlines = 0

    def __init__(self, fd=0, bufsize=8192):
        self.fd = fd
        self.bufsize = bufsize

    def readline(self):
        while self.newlines == 0:
            b, ptr = os.read(self.fd, max(os.fstat(self.fd).st_size, self.bufsize)), self.tell()
            self.seek(0, 2), self.write(b), self.seek(ptr)
            self.newlines += b.count(b'\n') + (not b)

        self.newlines -= 1
        return super(FastI, self).readline()


class FastO:
    def __init__(self, fd=1):
        stream = BytesIO()
        self.flush = lambda: os.write(fd, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
        self.write = lambda b: stream.write(b.encode())


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
