
def z_function(S):
    """
    Z Algorithm in O(n)
    :param S: text string to process
    :return: the Z array, where Z[i] = length of the longest common prefix of S[i:] and S
    """

    n = len(S)
    Z = [0] * n
    l = r = 0

    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1

            l, r = i, i + z

        Z[i] = z

    Z[0] = n
    return Z
