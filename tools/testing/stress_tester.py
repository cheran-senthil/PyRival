import subprocess


def prog2func(args):
    def func(inp):
        proc = subprocess.run(args, input=inp, text=True, capture_output=True)
        return proc.stdout, proc.stderr

    return func


def stress_tester(tests, solution, judge, print_error=True, catch_all=False):
    for inp in tests():
        out, err = solution(inp)
        verdict = judge(inp)[0] == out  # judge(inp, out)

        if not verdict:
            print('input')
            print(inp)

            print('stdout')
            print(out)

            if print_error and err:
                print('stderr')
                print(err)

            print('-' * 80)

            if not catch_all:
                break


def tests():
    for i in range(100):
        yield str(i)


solution = prog2func(["python", "A.py"])
judge = prog2func(["python", "judge.py"])
stress_tester(tests, solution, judge)
