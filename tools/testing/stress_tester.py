import subprocess


def stress_tester(tests, solution, checker):
    for inp in tests():
        out, err = solution(inp)
        verdict, _ = checker(inp)
        # verdict = checker(inp, out)

        if not verdict:
            print('input')
            print(inp)

            print('stdout')
            print(out)

            if err:
                print('stderr')
                print(err)

            print('-' * 80)


def prog2func(args):
    def func(inp):
        proc = subprocess.run(args, input=inp, text=True, capture_output=True)
        return proc.stdout, proc.stderr

    return func


def tests():
    for i in range(100):
        yield str(i)


solution = prog2func("python A.py")
checker = prog2func("python checker.py")
stress_tester(tests, solution, checker)
