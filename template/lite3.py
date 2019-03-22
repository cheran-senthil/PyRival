import os
import sys
from atexit import register
from io import BytesIO

input = lambda: sys.stdin.readline().rstrip('\r\n')

#region fastio
input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

_write = sys.stdout.write
sys.stdout.write = lambda s: _write(s.encode())

#endregion


def main():
    pass


if __name__ == '__main__':
    main()
