def cycle_finding(f, x0):
    # main phase: search successive powers of two
    power = lam = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        if power == lam:  # time to start a new power of two?
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    # Find the position of the first repetition of length lam
    mu = 0
    tortoise = hare = x0
    for _ in range(lam):
        hare = f(hare)
    # The distance between the hare and tortoise is now lam.

    # Next, the hare and tortoise move at same speed until they agree
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return lam, mu
