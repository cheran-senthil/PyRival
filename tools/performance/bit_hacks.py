least_bit = lambda x: x & -x


def subset_masks(m):
    x = m
    while x:
        x -= 1
        x &= m
        yield x


def next_mask(x):
    c = least_bit(x)
    r = x + c
    return (((r ^ x) >> 2) // c) | r


def sum_of_subsets(K, D):
    for b in range(K):
        for i in range(1 << K):
            if i & 1 << b:
                D[i] += D[i ^ (1 << b)]
