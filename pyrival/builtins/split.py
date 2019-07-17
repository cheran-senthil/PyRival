def split(b):
    words, i = [], 0
    while i < len(b):
        j = i
        while i < len(b) and not b[i].isspace():
            i += 1
        words.append(b[j:i])
        while i < len(b) and b[i].isspace():
            i += 1
    return words
