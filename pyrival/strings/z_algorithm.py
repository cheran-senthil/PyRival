
def z_function(text):
    """
    Z Algorithm in O(n)
    :param text: text string to process
    :return: the z_array, where z_array[i] = length of the longest common prefix of text[i:] and text
    """

    n = len(text)
    z_array = [0 for _ in range(n)]
    l = r = 0

    for i in range(1, n):
        z = z_array[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and text[z] == text[i + z]:
                z += 1

            l, r = i, i + z

        z_array[i] = z

    z_array[0] = n
    return z_array

