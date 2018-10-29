def binary_search(a, x):
    """Locate the value exactly equal to x"""
    low, high = 0, len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] > x:
            high = mid - 1
        elif a[mid] < x:
            low = mid + 1
        else:
            return mid

    return -1
