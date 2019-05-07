import sys

istream = []
i, b = 0, sys.stdin.read()
while i < len(b):
    j = i
    while i < len(b) and not b[i].isspace():
        i += 1
    istream.append((b[j:i]))
    while i < len(b) and b[i].isspace():
        i += 1

istream.reverse()
gets = istream.pop
