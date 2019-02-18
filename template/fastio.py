import os
import sys
from atexit import register
from io import BytesIO, StringIO

if sys.version_info[0] < 3:
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
else:
    sys.stdin = StringIO(os.read(0, os.fstat(0).st_size).decode())
    sys.stdout = StringIO()
    register(lambda: os.write(1, sys.stdout.getvalue()).encode())

input = lambda: sys.stdin.readline().rstrip('\r\n')
