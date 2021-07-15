import ast
import inspect
import sys
from types import GeneratorType


class Bootstrap(ast.NodeTransformer):
    def __init__(self):
        self.active = [False]
        self.bootstrap = set()

    @staticmethod
    def resolve(to):
        stack = []
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    def __call__(self, func):
        self.bootstrap.add(func.__name__)

    def visit_Call(self, node):
        self.generic_visit(node)
        if getattr(node.func, "id", None) in self.bootstrap:
            if self.active[-1]:
                return ast.Yield(node)
            else:
                return ast.Call(
                   ast.Attribute(ast.Name("Bootstrap", ast.Load()), "resolve",
                                 ast.Load()), [node], [])
        return node

    def visit_Return(self, node):
        self.generic_visit(node)
        return ast.Expr(ast.Yield(node.value)) if self.active[-1] else node

    def visit_FunctionDef(self, node):
        new_decorator_list = [
            decorator for decorator in node.decorator_list
            if getattr(decorator, "id", None) != "bootstrap"
        ]
        self.active.append(len(new_decorator_list) != len(node.decorator_list))
        node.decorator_list = new_decorator_list
        self.generic_visit(node)
        self.active.pop()
        return node


bootstrap = Bootstrap()


def main():
    pass


if __name__ == "__main__":
    source = inspect.getsource(sys.modules[__name__])
    tree = bootstrap.visit(ast.parse(source))
    ast.fix_missing_locations(tree)
    # print(ast.unparse(tree)) # for debugging
    exec(compile(tree, __file__, "exec"), {})
elif __name__ == "builtins":
    main()
