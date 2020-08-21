"""
Maximizes xor of values in a list (works with big integers)

Example:
>>>> A = [10**20, 3, 6, 4]
>>>> I = max_xor(A)
>>>> xor = 0
>>>> for i in I:
....    xor ^= A[i]
....
>>>> xor
100000000000000000007

"""


def max_xor(A):
    """
    Input:
    List A of non-negative integers
    Output:
    I such that xor(A[i] for i in I) is maximized
    """
    base = []
    how = {}
    reduced_base = {}

    for i in range(len(A)):
        a = A[i]
        tmp = 0
        while a:
            b = a.bit_length() - 1
            if b in reduced_base:
                a ^= reduced_base[b]
                tmp ^= how[b]
            else:
                reduced_base[b] = a
                how[b] = tmp | (1 << len(base))
                base.append(i)
                break
    x = 0
    tmp = 0
    for j in sorted(reduced_base, reverse=True):
        if not x & (1 << j):
            x ^= reduced_base[j]
            tmp ^= how[j]
    I = [base[j] for j in range(len(base)) if tmp & (1 << j)]
    return I
