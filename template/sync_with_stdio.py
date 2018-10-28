import sys


def sync_with_stdio(sync=True):
    """
    Sets whether the standard Python streams are allowed to buffer their I/O.

    Parameters
    ----------
    sync : bool
        the new synchronization setting

    """
    global input, flush

    if sync:
        flush = sys.stdout.flush
    else:
        from atexit import register

        if sys.version_info[0] < 3:
            from io import BytesIO

            input = iter(sys.stdin.read().splitlines()).next
            sys.stdout = BytesIO()
        else:
            from io import StringIO

            input = iter(sys.stdin.read().splitlines()).__next__
            sys.stdout = StringIO()

        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
