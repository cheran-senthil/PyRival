class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__, )
        return '%s(%r)' % (self.__class__.__name__, self.value)


class LinkedList:
    def __init__(self, iterable=None):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.__len = 0
        if iterable is not None:
            self += iterable

    def get_node(self, index):
        node = sentinel = self.sentinel
        i = 0
        while i <= index:
            node = node.next
            if node == sentinel:
                break
            i += 1
        if node == sentinel:
            node = None
        return node

    def __getitem__(self, index):
        node = self.__get_node(index)
        return node.value

    def __len__(self):
        return self.__len

    def __setitem__(self, index, value):
        node = self.get_node(index)
        node.value = value

    def __delitem__(self, index):
        node = self.get_node(index)
        if node:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.prev = None
            node.next = None
            node.value = None
            self.__len -= 1

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__, )
        list_ = [self.__get_node(i).value for i in range(len(self))]
        return '%s(%r)' % (self.__class__.__name__, list_)

    def append(self, value):
        sentinel = self.sentinel
        node = Node(value)
        self.insert_between(node, sentinel.prev, sentinel)

    def insert(self, index, value):
        sentinel = self.sentinel
        new_node = Node(value)
        len_ = len(self)
        if len_ == 0:
            self.insert_between(new_node, sentinel, sentinel)
        elif index >= 0 and index < len_:
            node = self.get_node(index)
            self.insert_between(new_node, node.prev, node)
        elif index == len_:
            self.insert_between(new_node, sentinel.prev, sentinel)
        else:
            raise IndexError
        self.__len += 1

    def insert_between(self, node, left_node, right_node):
        if node and left_node and right_node:
            node.prev = left_node
            node.next = right_node
            left_node.next = node
            right_node.prev = node
        else:
            raise IndexError
