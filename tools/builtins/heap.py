from heapq import heapify, heappop, heappush, heappushpop, heapreplace


class Heap(list):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        super(Heap, self).__init__(iterable)
        heapify(self)

    def peek(self):
        return self[0]

    def push(self, item):
        heappush(self, item)

    def pop(self):
        return heappop(self)

    def poppush(self, item):
        return heapreplace(self, item)

    replace = poppush

    def pushpop(self, item):
        return heappushpop(self, item)

    def __repr__(self):
        return 'Heap({content})'.format(content=super(Heap, self).__repr__())


class OrderHeap(Heap):
    def __init__(self, iterable=None, key=lambda x: x):
        if iterable is None:
            iterable = []
        self.key = key
        super(OrderHeap, self).__init__((key(item), item) for item in iterable)

    def peek(self):
        return self[0][1]

    def push(self, item):
        super(OrderHeap, self).push((self.key(item), item))

    def pop(self):
        return super(OrderHeap, self).pop()[1]

    def poppush(self, item):
        return heapreplace(self, (self.key(item), item))[1]

    replace = poppush

    def pushpop(self, item):
        return heappushpop(self, (self.key(item), item))[1]

    def __iter__(self):
        return (item_tuple[1] for item_tuple in super(Heap, self).__iter__())

    def __contains__(self, item):
        return item in iter(self)

    def __repr__(self):
        return 'OrderHeap({content}, key={key})'.format(content=list(self), key=self.key)


class RemovalHeap(Heap):
    def __init__(self, iterable=[]):
        _list = list(iterable)
        self._item_set = set(_list)
        if len(_list) != len(self._item_set):
            raise RuntimeError('duplicate items not allowed: {_list}'.format(_list=_list))
        super(RemovalHeap, self).__init__(_list)

    def peek(self):
        return_item = self[0]
        while return_item not in self._item_set:
            heappop(self)
            return_item = self[0]
        return return_item

    def push(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        heappush(self, item)
        self._item_set.add(item)

    def pop(self):
        return_item = heappop(self)
        while return_item not in self._item_set:
            return_item = heappop(self)
        self._item_set.remove(return_item)
        self.sweep()
        return return_item

    def remove(self, item):
        self._item_set.remove(item)
        self.sweep()

    def poppush(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self._item_set.add(item)
        while self[0] not in self._item_set:
            heappop(self)
        return_item = heapreplace(self, item)
        self._item_set.remove(return_item)
        return return_item

    replace = poppush

    def pushpop(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self._item_set.add(item)
        return_item = heappushpop(self, item)
        while return_item not in self._item_set:
            return_item = heappop(self)
        self._item_set.remove(return_item)
        return return_item

    def sweep(self):
        if 2 * len(self._item_set) < super(RemovalHeap, self).__len__():
            self[:] = list(self)
            heapify(self)

    def __iter__(self):
        return iter(self._item_set)

    def __contains__(self, item):
        return item in self._item_set

    def __len__(self):
        return len(self._item_set)

    def __repr__(self):
        return 'RemovalHeap({content})'.format(content=list(self))


# order + removal
class XHeap(Heap):
    def __init__(self, iterable=[], key=lambda x: x):
        self.key = key
        _list = list(iterable)
        self._item_set = set(_list)
        if len(_list) != len(self._item_set):
            raise RuntimeError('duplicate items not allowed: {_list}'.format(_list=_list))
        super(XHeap, self).__init__((key(item), item) for item in _list)

    def peek(self):
        return_item = self[0][1]
        while return_item not in self._item_set:
            heappop(self)
            return_item = self[0][1]
        return return_item

    def push(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        heappush(self, (self.key(item), item))
        self._item_set.add(item)

    def pop(self):
        return_item = heappop(self)[1]
        while return_item not in self._item_set:
            return_item = heappop(self)[1]
        self._item_set.remove(return_item)
        self.sweep()
        return return_item

    def remove(self, item):
        self._item_set.remove(item)
        self.sweep()

    def sweep(self):
        if 2 * len(self._item_set) < super(XHeap, self).__len__():
            self[:] = (item_tuple for item_tuple in super(XHeap, self).__iter__() if item_tuple[1] in self._item_set)
            heapify(self)

    def poppush(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self._item_set.add(item)
        while self[0][1] not in self._item_set:
            heappop(self)
        return_item = heapreplace(self, (self.key(item), item))[1]
        self._item_set.remove(return_item)
        return return_item

    replace = poppush

    def pushpop(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self._item_set.add(item)
        return_item = heappushpop(self, (self.key(item), item))[1]
        while return_item not in self._item_set:
            return_item = heappop(self)[1]
        self._item_set.remove(return_item)
        return return_item

    def __iter__(self):
        return iter(self._item_set)

    def __contains__(self, item):
        return item in self._item_set

    def __len__(self):
        return len(self._item_set)

    def __repr__(self):
        return 'XHeap({content}, key={key})'.format(content=list(self), key=self.key)
