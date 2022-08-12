class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.__class__.__name__ + ("({})".format(self.value) if self else "()")
