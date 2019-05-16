import pathlib
import subprocess


def dir2tests(directory, recursive=False):
    glob = pathlib.Path(directory).glob('**/*' if recursive else '*')
    return [path.open().read() for path in glob if path.is_file()]


def cmd2func(args):
    def func(inp):
        proc = subprocess.run(args, input=inp, text=True, capture_output=True)
        return proc.stdout, proc.stderr

    return func


def sol2judge(sol):
    def func(inp, out):
        ans, _ = sol(inp)
        return ans == out, ans

    return func


def stress_tester(tests, solution, judge=None, catch_all=False):
    if judge is None:
        verdict, answer = False, ''
        catch_all = True

    for inp in tests:
        out, err = solution(inp)

        if judge:
            verdict, answer = judge(inp, out)

        if not verdict:
            print('Input')
            print(inp)

            print('Output')
            print(out)

            if err:
                print('Error')
                print(err)

            if answer:
                print('Answer')
                print(answer)

            print('-' * 80)

            if not catch_all:
                break


def tests():
    for i in range(100):
        yield str(i)


solution = cmd2func(["python", "A.py"])
judge = sol2judge(cmd2func(["python", "judge.py"]))

stress_tester(tests(), solution, judge)
#stress_tester(dir2tests('test'), solution, judge)
