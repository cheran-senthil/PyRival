import sys
from atexit import register
from io import BytesIO, FileIO, StringIO

INP_FILE = 0
OUT_FILE = 1

if sys.version_info[0] < 3:
    input = iter(FileIO(INP_FILE).read().splitlines()).next

    sys.stdout = BytesIO()
    register(lambda: FileIO(OUT_FILE, 'w').write(sys.stdout.getvalue()))
else:
    input = iter(FileIO(INP_FILE).read().splitlines()).__next__

    sys.stdout = StringIO()
    register(lambda: FileIO(OUT_FILE, 'w').write(sys.stdout.getvalue().encode(
    )))
