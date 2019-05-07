from types import GeneratorType


def recursion(func_call):
    call_stack, get_stack = [func_call], []
    while call_stack:
        func_call = next(func_call) if func_call else call_stack[-1].send(get_stack.pop())
        if isinstance(func_call, GeneratorType):
            call_stack.append(func_call)
        else:
            call_stack.pop()
            get_stack.append(func_call)
            func_call = None
    return get_stack.pop()
