from pyrival.TwoSat import *

def test_TwoSat():
    # Test 5000 small satisfiable instances of 2sat

    import random
    for _ in range(5000):
        random.seed(_)

        n = 10
        m = n
        k = 3

        A = [random.randrange(2) for i in range(n)] + [-1] * n
        for i in range(n):
            A[~i] = 1 - A[i]

        fixed = []
        for _ in range(k):
            i = random.randrange(-n, n)
            if A[i]:
                fixed.append(i)

        pairs = []
        for _ in range(m):
            a = random.randrange(-n, n)
            b = random.randrange(-n, n)
            if A[a] or A[b]:
                pairs.append((a,b))

        sat = TwoSat(n)
        for i in fixed:
            sat.set(i)
        for a,b in pairs:
            sat.either(a,b)

        has_solution, solution = sat.solve()
        assert has_solution

        solution += [-1] * n
        for i in range(n):
            solution[~i] = 1 - solution[i]

        for i in fixed:
            assert solution[i]

        for a,b in pairs:
            assert solution[a] or solution[b]
