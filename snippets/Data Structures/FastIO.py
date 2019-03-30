import os
import sys
from io import BytesIO


class FastI:
    def __init__(self):
        self.stream = BytesIO()
        self.newlines = 0

    def read(self, b=b'\n'):
        while b:
            b, ptr = os.read(0, (1 << 13) + os.fstat(0).st_size), self.stream.tell()
            self.stream.seek(0, 2), self.stream.write(b), self.stream.seek(ptr)

        return self.stream.read() if self.stream.tell() else self.stream.getvalue()

    def readline(self, b=b'\n'):
        while b and not self.newlines:
            b, ptr = os.read(0, (1 << 13) + os.fstat(0).st_size), self.stream.tell()
            self.stream.seek(0, 2), self.stream.write(b), self.stream.seek(ptr)
            self.newlines += b.count(b'\n')
        self.newlines -= bool(b)

        return self.stream.readline()

    def readnumbers(self, zero=0):
        numbers, b = [], self.read()

        num, sign = zero, True
        for char in b:
            if char >= 48:
                num = num * 10 + char - 48
            elif char == 45:
                sign = False
            elif char != 13:
                numbers.append(num if sign else -num)
                num, sign = zero, True

        if b and b[-1] >= 48:
            numbers.append(num if sign else -num)

        return numbers


class FastO:
    def __init__(self):
        stream = BytesIO()
        self.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
        self.write = lambda s: stream.write(s.encode())


sys.stdin, sys.stdout = FastI(), FastO()
input, flush = sys.stdin.readline, sys.stdout.flush
