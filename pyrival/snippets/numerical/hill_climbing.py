def hill_climbing(func, x_0, y_0, cmp=min):
    cur = (func(x_0, y_0), (x_0, y_0))
    jmp = 1e9
    while jmp > 1e-20:
        for _ in range(100):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    x = cur[1][0] + dx * jmp
                    y = cur[1][1] + dy * jmp
                    cur = cmp(cur, (func(x, y), (x, y)))
        jmp /= 2
    return cur
