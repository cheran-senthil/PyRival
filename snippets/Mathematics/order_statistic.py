def order_statistic(a, k):
    left, right = 0, len(a) - 1

    while True:
        if right <= left + 1:
            if (right == left + 1) and (a[right] < a[left]):
                a[left], a[right] = a[right], a[left]

            return a[k - 1]

        mid = (left + right) // 2
        a[mid], a[left + 1] = a[left + 1], a[mid]

        if a[left] > a[right]:
            a[left], a[right] = a[right], a[left]

        if a[left + 1] > a[right]:
            a[right], a[left + 1] = a[left + 1], a[right]

        if a[left] > a[left + 1]:
            a[left], a[left + 1] = a[left + 1], a[left]

        i, j = left + 1, right
        cur = a[left + 1]

        while True:
            i += 1
            while a[i] < cur:
                i += 1

            j -= 1
            while a[j] > cur:
                j -= 1

            if i > j:
                break

            a[i], a[j] = a[j], a[i]

        a[left + 1] = a[j]
        a[j] = cur

        if j >= k - 1:
            right = j - 1

        if j <= k - 1:
            left = i
