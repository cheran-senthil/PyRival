#!/usr/bin/env python3
import os
import sys
from io import BytesIO

BUFSIZE = 8192


class FastIO:
    stream = BytesIO()
    newlines = 0

    def __init__(self, fd):
        self.fd = fd
        self.flush = lambda: os.write(fd, self.stream.getvalue()) and not self.stream.truncate(0) and self.stream.seek(0)
        self.write = lambda b: self.stream.write(b.encode())

    def readline(self):
        while self.newlines == 0:
            b, ptr = os.read(self.fd, max(os.fstat(self.fd).st_size, BUFSIZE)), self.stream.tell()
            self.stream.seek(0, 2), self.stream.write(b), self.stream.seek(ptr)
            self.newlines += b.count(b'\n') + (not b)

        self.newlines -= 1
        return self.stream.readline()


sys.stdin, sys.stdout = FastIO(0), FastIO(1)
input = sys.stdin.readline


def main():
    pass


if __name__ == '__main__':
    main()
