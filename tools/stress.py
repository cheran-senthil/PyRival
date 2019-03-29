import argparse
import shlex
import subprocess
import sys


def main(argv):
    parser = argparse.ArgumentParser(description='Tool to stress test a solution')
    parser.add_argument('testcase_generator', help='A command to generate testcases')
    parser.add_argument('solution', help='A command to run the solution to stress test')
    parser.add_argument('checker', help='A command to check if a solution is correct')
    parser.add_argument('-t', '--timeout', type=int, help='Timeout')
    parser.add_argument('-n', '--ntestcases', type=int, help='Number of testcases to run solution on')

    args = parser.parse_args(argv[1:])

    testcase_generator = shlex.split(args.testcase_generator)
    solution = shlex.split(args.solution)
    checker = shlex.split(args.checker)
    timeout = args.timeout
    ntestcases = args.ntestcases

    for _ in range(ntestcases):
        testcase = subprocess.run(testcase_generator, capture_output=True).stdout
        output = subprocess.run(solution, input=testcase, capture_output=True).stdout

        verdict = subprocess.run(checker, input=testcase+output, capture_output=True).stdout

        if verdict == b'WA\n':
            print(testcase.decode())


if __name__ == "__main__":
    main(sys.argv)
