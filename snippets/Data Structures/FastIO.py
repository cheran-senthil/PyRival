import io
import os
import sys

sys.stdout, stream = io.IOBase(), io.BytesIO()
sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
sys.stdout.write = stream.write if sys.version_info[0] < 3 else lambda s: stream.write(s.encode())


class FastI():
    """ FastIO for PyPy3 by Pajenegod """
    stream = io.BytesIO()
    newlines = 0

    def read1(self):
        s, ptr = os.read(0, (1 << 13) + os.fstat(0).st_size), self.stream.tell()
        self.stream.seek(0, 2)
        self.stream.write(s)
        self.stream.seek(ptr)

        return s

    def read(self):
        while self.read1():
            pass
        return self.stream.read() if self.stream.tell() else self.stream.getvalue()

    def readline(self):
        while self.newlines == 0:
            s = self.read1()
            self.newlines += s.count(b'\n') + (not s)
        self.newlines -= 1

        return self.stream.readline()

    def readnumbers(self, var=int):
        """ Read numbers till EOF. Use var to change type. """
        numbers, buffer = [], self.read()

        numb, sign = var(0), 1
        for char in buffer:
            if char >= b'0' [0]:
                numb = 10 * numb + char - 48
            elif char == b'-' [0]:
                sign = -1
            elif char != b'\r' [0]:
                numbers.append(sign * numb)
                numb, sign = var(0), 1

        if buffer and buffer[-1] >= b'0' [0]:
            numbers.append(sign * numb)

        return numbers


sys.stdin = FastI()
input = sys.stdin.readline
