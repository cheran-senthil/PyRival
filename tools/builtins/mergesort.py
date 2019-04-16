def mergesort(A):
    B, n = A[:], len(A)
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            right, end = min(i + width, n), min(i + 2 * width, n)
            j = right
            for k in range(i, end):
                if i < right and (j >= end or A[i] <= A[j]):
                    B[k] = A[i]
                    i += 1
                else:
                    B[k] = A[j]
                    j += 1
        A = B[:]
        width *= 2
    return A
