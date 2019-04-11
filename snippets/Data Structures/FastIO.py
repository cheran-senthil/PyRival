import os
import sys
from io import BytesIO, IOBase

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


class ostream:
    def __lshift__(self, a):
        if a == endl:
            sys.stdout.write('\n')
            sys.stdout.flush()
        else:
            sys.stdout.write(str(a))
        return self


sys.stdin, sys.stdout = FastIO(0), FastIO(1)
input, flush = sys.stdin.readline, sys.stdout.flush
cout, endl = ostream(), object()
