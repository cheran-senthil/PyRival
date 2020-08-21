import argparse
import asyncio
import io
import pathlib
import shlex
import sys
from asyncio.subprocess import PIPE


class PrefixedStream(io.IOBase):
    def __init__(self, stream, prefix):
        self.stream = stream
        self.prefix = prefix
        self.flush = stream.flush

    def close(self):
        pass

    def write(self, b):
        return self.stream.write(self.prefix + b)


async def tee(in_stream, out_streams):
    line = await in_stream.readline()
    while line.endswith(b"\n"):
        for out_stream in out_streams:
            out_stream.write(line)
            if hasattr(out_stream, "flush"):
                out_stream.flush()
        line = await in_stream.readline()

    if line:
        for out_stream in out_streams:
            out_stream.write(line)
            if hasattr(out_stream, "flush"):
                out_stream.flush()

    for out_stream in out_streams:
        out_stream.close()


async def show_exit_code(process, prefix):
    print(prefix, await process.wait(), sep="")


async def async_main(argv=None):
    argv = sys.argv if argv is None else argv

    parser = argparse.ArgumentParser(pathlib.Path(argv[0]).name, description="A interactive runner")
    parser.add_argument("command_1", type=str, help="command to execute first program")
    parser.add_argument("command_2", type=str, help="Command to execute second program")
    parser.add_argument(
        "--command1-stdout-prefix",
        metavar="PREFIX",
        default="Command 1 (stdout): ",
        help="Prefix to add before the first command's stdout",
    )
    parser.add_argument(
        "--command1-stderr-prefix",
        metavar="PREFIX",
        default="Command 1 (stderr): ",
        help="Prefix to add before the first command's stderr",
    )
    parser.add_argument(
        "--command2-stdout-prefix",
        metavar="PREFIX",
        default="Command 2 (stdout): ",
        help="Prefix to add before the second command's stdout",
    )
    parser.add_argument(
        "--command2-stderr-prefix",
        metavar="PREFIX",
        default="Command 2 (stderr): ",
        help="Prefix to add before the second command's stderr",
    )

    args = parser.parse_args(argv[1:])

    proc_1 = await asyncio.create_subprocess_exec(*shlex.split(args.command_1), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    proc_2 = await asyncio.create_subprocess_exec(*shlex.split(args.command_2), stdin=PIPE, stdout=PIPE, stderr=PIPE)

    proc_1_stdout = PrefixedStream(sys.stdout.buffer, args.command1_stdout_prefix.encode("utf-8"))
    proc_2_stdout = PrefixedStream(sys.stdout.buffer, args.command2_stdout_prefix.encode("utf-8"))
    proc_1_stderr = PrefixedStream(sys.stderr.buffer, args.command1_stderr_prefix.encode("utf-8"))
    proc_2_stderr = PrefixedStream(sys.stderr.buffer, args.command2_stderr_prefix.encode("utf-8"))

    await asyncio.gather(
        tee(proc_1.stdout, [proc_2.stdin, proc_1_stdout]),
        tee(proc_2.stdout, [proc_1.stdin, proc_2_stdout]),
        tee(proc_1.stderr, [proc_1_stderr]),
        tee(proc_2.stderr, [proc_2_stderr]),
        show_exit_code(proc_1, "Program 1 Exited with Code: "),
        show_exit_code(proc_2, "Program 2 Exited with Code: "),
    )


def main(argv=None):
    argv = sys.argv if argv is None else argv
    asyncio.run(async_main(argv))


if __name__ == "__main__":
    main()
