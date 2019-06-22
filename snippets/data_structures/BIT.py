def bitify(x):
    for i in range(len(x)):
        j = i | (i + 1)
        if j < len(x):
            x[j] += x[i]


def bitupdate(bit, key, val):
    """updates bit[i] += val"""
    while key < len(bit):
        bit[key] += val
        key |= key + 1


def bitquery(bit, end):
    """calc sum(bit[:r])"""
    val = 0
    while end:
        val += bit[end - 1]
        end &= end - 1
    return val


def bitkth(bit, k):
    """Find largest r such that sum(bit[:r]) <= k"""
    idx = -1
    for d in reversed(range(len(bit).bit_length())):
        right_idx = idx + (1 << d)
        if right_idx < len(bit) and k >= bit[right_idx]:
            idx = right_idx
            k -= bit[idx]
    return idx + 1
