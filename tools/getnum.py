import os

zero = 0
numbers = []

num, sign = zero, True
for char in os.read(0, os.fstat(0).st_size):
    if char >= 48:
        num = num * 10 + char - 48
    elif char == 45:
        sign = False
    elif char != 13:
        numbers.append(num if sign else -num)
        num, sign = zero, True

if char >= 48:
    numbers.append(num if sign else -num)

numbers.reverse()
getnum = numbers.pop
