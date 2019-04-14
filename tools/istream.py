import sys

istream = []
i, b = 0, sys.stdin.read()
while True:
    while i < len(b) and b[i].isspace():
        i += 1
    if i == len(b):
        break
    j = i
    while i < len(b) and not b[i].isspace():
        i += 1
    istream.append(int(b[j:i]))

istream.reverse()
getint = istream.pop
