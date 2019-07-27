def partial(S):
    P = [0] * len(S)
    g = 0
    for i in range(1, len(S)):
        while g and (S[g] != S[i]):
            g = P[g - 1]
        P[i] = g = g + (S[g] == S[i])
 
    return P
 
def match(S, pattern):
    P = partial(pattern)
    g = 0
    ret = []
    
    for i in range(len(S)):
        while g and pattern[g] != S[i]:
            g = P[g - 1]
        g += pattern[g] == S[i]
        if g == len(P): 
            ret.append(i + 1 - g)
            g = P[g - 1]
    
    return ret
