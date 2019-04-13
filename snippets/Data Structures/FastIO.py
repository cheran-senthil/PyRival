import os
import sys
from builtins import str as __str__
from io import BytesIO

str = lambda x=b'': x if type(x) is bytes else __str__(x).encode()

BUFSIZE = 8192


class FastIO:
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


def print(*args, sep=b' ', end=b'\n', file=sys.stdout, flush=False):
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(end)
    if flush:
        file.flush()
