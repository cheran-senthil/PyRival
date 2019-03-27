import io
import os
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n')

#region fastio
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

sys.stdout, stream = io.IOBase(), io.BytesIO()
sys.stdout.flush = lambda: os.write(1, stream.getvalue()) and not stream.truncate(0) and stream.seek(0)
sys.stdout.write = lambda s: stream.write(s.encode())

#endregion


def main():
    pass


if __name__ == '__main__':
    main()
