def bitify(x):
    """transform list into BIT"""
    for i in range(len(x)):
        j = i | (i + 1)
        if j < len(x):
            x[j] += x[i]


def bitupdate(bit, idx, x):
    """updates bit[idx] += x"""
    while idx < len(bit):
        bit[idx] += x
        idx |= idx + 1


def bitquery(bit, end):
    """calc sum(bit[:end])"""
    x = 0
    while end:
        x += bit[end - 1]
        end &= end - 1
    return x


def bitkth(bit, k):
    """Find largest idx such that sum(bit[:idx]) <= k"""
    idx = -1
    for d in reversed(range(len(bit).bit_length())):
        right_idx = idx + (1 << d)
        if right_idx < len(bit) and k >= bit[right_idx]:
            idx = right_idx
            k -= bit[idx]
    return idx + 1
