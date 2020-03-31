def ordersort(order, key=lambda x: x, reverse=False):
    new_order, keymap = order[:], [key(idx) for idx in order]

    n = len(order)
    for i in range(0, n - 1, 2):
        if keymap[order[i]] > keymap[order[i ^ 1]]:
            order[i], order[i ^ 1] = order[i ^ 1], order[i]

    width = 2
    while width < n:
        for i in range(0, n, 2 * width):
            left, right = min(i + width, n), min(i + 2 * width, n)
            j, k = left, i
            while i < left and j < right:
                if keymap[order[i]] > keymap[order[j]]:
                    new_order[k] = order[j]
                    j += 1
                else:
                    new_order[k] = order[i]
                    i += 1
                k += 1
            while i < left:
                new_order[k] = order[i]
                k += 1
                i += 1
            while k < right:
                new_order[k] = order[k]
                k += 1
        order, new_order = new_order, order
        width *= 2

    if reverse:
        order.reverse()
    return order
