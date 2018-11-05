import sys

if 'PyPy' in sys.version:
    from _continuation import continulet
else:
    import threading


def main():
    pass


if __name__ == '__main__':
    if 'PyPy' in sys.version:
        def bootstrap(c):
            callable, arg = c.switch()
            while True:
                to = continulet(lambda _, f, x: f(x), callable, arg)
                callable, arg = c.switch(to=to)

        c = continulet(bootstrap)
        c.switch()

        main()

    else:
        sys.setrecursionlimit(2097152)
        threading.stack_size(134217728)

        main_thread = threading.Thread(target=main)
        main_thread.start()
        main_thread.join()
