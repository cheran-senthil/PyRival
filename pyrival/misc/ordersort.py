def bucketsort(order, seq):
    buckets = [0] * (max(seq) + 1)
    for x in seq:
        buckets[x] += 1
    for i in range(len(buckets) - 1):
        buckets[i + 1] += buckets[i]

    new_order = [-1] * len(seq)
    for i in reversed(order):
        x = seq[i]
        idx = buckets[x] = buckets[x] - 1
        new_order[idx] = i

    return new_order


def ordersort(order, seq, reverse=False):
    bit = max(seq).bit_length() >> 1
    mask = (1 << bit) - 1
    order = bucketsort(order, [x & mask for x in seq])
    order = bucketsort(order, [x >> bit for x in seq])
    if reverse:
        order.reverse()
    return order


def long_ordersort(order, seq):
    order = ordersort(order, [int(i & 0x7fffffff) for i in seq])
    return ordersort(order, [int(i >> 31) for i in seq])


def multikey_ordersort(order, *seqs, sort=ordersort):
    for i in reversed(range(len(seqs))):
        order = sort(order, seqs[i])
    return order
