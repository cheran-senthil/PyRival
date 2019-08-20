class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        if not self:
            return "{}()".format(self.__class__.__name__)
        return "{}({})".format(self.__class__.__name__, self.value)
