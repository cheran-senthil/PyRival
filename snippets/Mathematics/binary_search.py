def binary_search(l, value):
    low, high = 0, len(l) - 1

    while low <= high:
        mid = (low + high) // 2
        if l[mid] > value:
            high = mid - 1
        elif l[mid] < value:
            low = mid + 1
        else:
            return mid

    return -1
