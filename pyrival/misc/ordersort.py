def ordersort_int(order, key=lambda x: x):
    A, B = [[] for _ in range(65536)], [[] for _ in range(65536)]
    for i in order:
        A[key(i) & 65535].append(i)
    for Ai in A:
        for Aij in Ai:
            B[key(Aij) >> 16].append(Aij)

    return [Bij for Bi in B for Bij in Bi]


def ordersort_tuple(order, *keys):
    for key in reversed(keys):
        order = ordersort_int(order, key)
    return order


ordersort_int64 = lambda order, key=lambda x: x: [
    order[i] for i in ordersort_tuple(
        list(range(len(order))),
        [int(key(i) >> 31) for i in order].__getitem__,
        [int(key(i) & 2147483647) for i in order].__getitem__,
    )
]
