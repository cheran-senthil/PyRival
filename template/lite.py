#!/usr/bin/env python3
import sys
from atexit import register
from io import FileIO, StringIO

input = iter(FileIO(0).read().splitlines()).__next__
sys.stdout = StringIO()
register(lambda: FileIO(1, 'w').write(sys.stdout.getvalue().encode()))


def main():
    pass


if __name__ == '__main__':
    main()
