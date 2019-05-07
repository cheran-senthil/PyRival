from types import GeneratorType


def bootstrap(call):
    stack = []
    while True:
        if type(call) is GeneratorType:
            stack.append(call)
            call = next(call)
        else:
            stack.pop()
            if not stack:
                break
            call = stack[-1].send(call)
    return call
