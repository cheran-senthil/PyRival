def stress(tests, solution, checker):
    for inp in tests():
        out, err = solution(inp)
        verdict = checker(inp, out)

        if not verdict:
            print('input')
            print(inp)

            print('stdout')
            print(out)

            if err:
                print('stderr')
                print(err)

            print('-' * 80)
