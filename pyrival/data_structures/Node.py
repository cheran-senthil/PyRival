class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})" if self else f"{self.__class__.__name__}()"
