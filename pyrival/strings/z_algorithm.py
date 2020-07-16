
def z_function(text):
    """
    Z Algorithm in O(n)
    :param text: text string to process
    :return: the z_array, where z_array[i] = length of the longest common prefix of text[i:] and text
    """

    n = len(text)
    z_array = [0] * n
    l, r = 0, 0

    for i in range(1, n):
        z = max(0, min(z_array[i - l], r - i))
        while i + z < n and text[z] == text[i + z]:
            z += 1

        if i + z > r:
            l, r = i, i + z

        z_array[i] = z

    z_array[0] = n
    return z_array
