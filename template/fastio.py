import os
import sys
from atexit import register

if sys.version_info[0] < 3:
    from cStringIO import StringIO
else:
    from io import BytesIO as StringIO

sys.stdout = StringIO()
if sys.version_info[0] >= 3:
    _write = sys.stdout.write
    sys.stdout.write = lambda s: _write(s.encode())

register(lambda: os.write(1, sys.stdout.getvalue()))
input = StringIO(os.read(0, os.fstat(0).st_size)).readline