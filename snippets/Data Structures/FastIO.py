import os
import sys
from io import BytesIO, IOBase


class FastI(BytesIO):
    newlines = 0
    read = lambda self: super(FastI, self).read() if self.read1() or self.tell() else self.getvalue()

    def read1(self, getline=False, s=b'\n'):
        while s and not (getline and self.newlines):
            s, ptr = os.read(0, (1 << 13) + os.fstat(0).st_size), self.tell()
            self.newlines += s.count(b'\n')

            self.seek(0, 2)
            self.write(s)
            self.seek(ptr)

    def readline(self):
        self.read1(True)
        self.newlines -= 1
        return super(FastI, self).readline()


class FastO(IOBase):
    stream = BytesIO()
    flush = lambda self: os.write(1, self.stream.getvalue()) + self.stream.truncate(0)
    write = lambda self, s: self.stream.write(s) if sys.version_info[0] < 3 else self.stream.write(s.encode())


sys.stdin, sys.stdout = FastI(), FastO()
input = sys.stdin.readline
