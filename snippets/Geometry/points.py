from itertools import imap
from math import cos, sin
from operator import mul

dist = lambda v1, v2: sum((a - b)*(a - b) for a, b in zip(v1, v2))**0.5

dot = lambda A, B: sum(imap(mul, A, B))

rotate = lambda p, theta, origin=(0, 0): (origin[0] + (p[0] - origin[0]) * cos(theta) - (p[1] - origin[1]) * sin(theta),
                                          origin[1] + (p[0] - origin[0]) * sin(theta) + (p[1] - origin[1]) * cos(theta))
