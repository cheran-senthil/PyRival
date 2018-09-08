from random import randint
from math import gcd

def factor(N):
    if N % 2 == 0:
        return 2
    
    y, c, m = randint(1, N-1), randint(1, N-1), randint(1, N-1)
    g, r, q = 1, 1, 1
    
    while g == 1:             
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while (k < r) and (g == 1):
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r = r * 2
    
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break
        
    return g

print(brent(3367900313 * 5463458053))
print(brent(54673257461630679457))