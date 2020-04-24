import argparse
import asyncio
import shlex
import sys
import pathlib
from asyncio.subprocess import PIPE


async def tee(stream, streams, prefix):
    line = await stream.readline()
    while line.endswith(b'\n'):
        for s, p in zip(streams, prefix):
            s.write(p + line)
            if hasattr(s, 'flush'):
                s.flush()
        line = await stream.readline()

    if line:
        for s, p in zip(streams, prefix):
            s.write(p + line + b" % No new line\n")
            if hasattr(s, 'flush'):
                s.flush()


async def show_exit_code(process, prefix):
    print(prefix, await process.wait(), sep='')


async def async_main(argv=sys.argv):
    parser = argparse.ArgumentParser(pathlib.Path(argv[0]).name)
    parser.add_argument("program1", help="Command to execute first program")
    parser.add_argument("program2", help="Command to execute second program")
    parser.add_argument('--disable-stdout', default=False, action="store_true", help="Do not show stdout")
    parser.add_argument("--program1-stdout-prefix",
                        metavar="PREFIX",
                        default="Program 1 (stdout): ",
                        help="Prefix to add before the first program's stdout")
    parser.add_argument("--program1-stderr-prefix",
                        metavar="PREFIX",
                        default="Program 1 (stderr): ",
                        help="Prefix to add before the first program's stderr")
    parser.add_argument("--program2-stdout-prefix",
                        metavar="PREFIX",
                        default="Program 2 (stdout): ",
                        help="Prefix to add before the second program's stdout")
    parser.add_argument("--program2-stderr-prefix",
                        metavar="PREFIX",
                        default="Program 2 (stderr): ",
                        help="Prefix to add before the second program's stderr")

    args = parser.parse_args(argv[1:])

    process_1 = await asyncio.create_subprocess_exec(*shlex.split(args.program1), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process_2 = await asyncio.create_subprocess_exec(*shlex.split(args.program2), stdin=PIPE, stdout=PIPE, stderr=PIPE)

    program1_stdout_prefix = args.program1_stdout_prefix.encode("utf-8")
    program1_stderr_prefix = args.program1_stderr_prefix.encode("utf-8")
    program2_stdout_prefix = args.program2_stdout_prefix.encode("utf-8")
    program2_stderr_prefix = args.program2_stderr_prefix.encode("utf-8")

    process_1_stdout_tee = [process_2.stdin]
    process_1_stdout_tee_prefixes = [b""]
    process_2_stdout_tee = [process_1.stdin]
    process_2_stdout_tee_prefixes = [b""]

    if not args.disable_stdout:
        process_1_stdout_tee.append(sys.stdout.buffer)
        process_1_stdout_tee_prefixes.append(program1_stdout_prefix)
        process_2_stdout_tee.append(sys.stdout.buffer)
        process_2_stdout_tee_prefixes.append(program2_stdout_prefix)

    await asyncio.gather(
        tee(process_1.stdout, process_1_stdout_tee, process_1_stdout_tee_prefixes),
        tee(process_2.stdout, process_2_stdout_tee, process_2_stdout_tee_prefixes),
        tee(process_1.stderr, [sys.stdout.buffer], [program1_stderr_prefix]),
        tee(process_2.stderr, [sys.stdout.buffer], [program2_stderr_prefix]),
        show_exit_code(process_1, "Program 1 Exited with Code: "),
        show_exit_code(process_2, "Program 2 Exited with Code: "),
    )


def main(argv=sys.argv):
    asyncio.run(async_main(argv))


if __name__ == "__main__":
    main()
