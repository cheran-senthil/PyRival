import os
import sys
from io import BytesIO, IOBase

sys.stdout, stream = IOBase(), BytesIO()
sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
sys.stdout.write = stream.write if sys.version_info[0] < 3 else lambda s: stream.write(s.encode())


class FastI():
    """ FastIO for PyPy2 and PyPy3 by Pajenegod """
    stream = BytesIO()
    newlines = 0

    def _read(self):
        s, ptr = os.read(0, (1 << 13) + os.fstat(0).st_size), self.stream.tell()
        self.stream.seek(0, 2)
        self.stream.write(s)
        self.stream.seek(ptr)

        return s

    def read(self):
        while self._read():
            pass
        return self.stream.read() if self.stream.tell() else self.stream.getvalue()

    def readline(self):
        while self.newlines == 0:
            s = self._read()
            self.newlines += s.count(b'\n') + (not s)
        self.newlines -= 1

        return self.stream.readline()

    def readnumbers(self, var=int):
        """ Read numbers till EOF. Use var to change type. """
        numbers, buffer = [], self.read()

        numb, sign = var(0), 1
        for char in buffer:
            if char >= b'0' [0]:
                numb = 10 * numb + ((ord(char) if sys.version_info[0] < 3 else char) - 48)
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
