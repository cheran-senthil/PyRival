def least_rotation(s):
    s += s
    i, ans = 0, 0

    while 2 * i < len(s):
        ans = i
        j, k = i + 1, i

        while (2 * j < len(s)) and (s[k] <= s[j]):
            if s[k] < s[j]:
                k = i
            else:
                k += 1
            j += 1

        while i <= k:
            i += j - k

    return s[ans:ans + (len(s) // 2)]
