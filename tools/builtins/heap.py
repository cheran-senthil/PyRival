from importlib import import_module


def _heappop_max(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup_max(heap, 0)
        return returnitem
    return lastelt


def _heappush_max(heap, item):
    heap.append(item)
    _siftdown_max(heap, 0, len(heap) - 1)


def _heappushpop_max(heap, item):
    if heap and heap[0] > item:
        item, heap[0] = heap[0], item
        _siftup_max(heap, 0)
    return item


def _heapreplace_max(heap, item):
    returnitem = heap[0]
    heap[0] = item
    _siftup_max(heap, 0)
    return returnitem

_heapops = ['heapify', 'heappush', 'heappop', 'heappushpop', 'heapreplace', '_siftup', '_siftdown'] + \
           ['_heapify_max', '_heappush_max', '_heappop_max', '_heappushpop_max', '_heapreplace_max', '_siftup_max', '_siftdown_max']
# If available, use C implementation
for module in ['heapq', '_heapq']:
    try:
        m = import_module(module)
        for f in _heapops:
            try:
                globals().update({f: getattr(m, f)})
            except:
                pass
    except:
        pass


class Heap(object):
    def __init__(self, iterable=None, reverse=False):
        if reverse:
            self.heapify, self.heappush, self.heappop = _heapify_max, _heappush_max, _heappop_max
            self.heappushpop, self.heapreplace = _heappushpop_max, _heapreplace_max
        else:
            self.heapify, self.heappush, self.heappop = heapify, heappush, heappop
            self.heappushpop, self.heapreplace = heappushpop, heapreplace

        if iterable is None:
            iterable = []
        self.heap = list(iterable)
        self.heapify(self.heap)

    def peek(self):
        return self.heap[0]

    def push(self, item):
        self.heappush(self.heap, item)

    def pop(self):
        return self.heappop(self.heap)

    def poppush(self, item):
        return self.heapreplace(self.heap, item)

    replace = poppush

    def pushpop(self, item):
        return self.heappushpop(self.heap, item)

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return iter(self.heap)

    def __contains__(self, item):
        return item in iter(self)

    def __repr__(self):
        return 'Heap({content})'.format(content=heap)


class OrderHeap(Heap):
    def __init__(self, iterable=None, key=lambda x: x, reverse=False):
        if iterable is None:
            iterable = []
        self.key = key
        super(OrderHeap, self).__init__(((key(item), item) for item in iterable), reverse=reverse)

    def peek(self):
        return self.heap[0][1]

    def push(self, item):
        self.heappush(self.heap, (self.key(item), item))

    def pop(self):
        return self.heappop(self.heap)[1]

    def poppush(self, item):
        return self.heapreplace(self.heap, (self.key(item), item))[1]

    replace = poppush

    def pushpop(self, item):
        return self.heappushpop(self.heap, (self.key(item), item))[1]

    def __iter__(self):
        return (item_tuple[1] for item_tuple in super(OrderHeap, self).__iter__())

    def __repr__(self):
        return 'OrderHeap({content}, key={key})'.format(content=self.heap, key=self.key)


class RemovalHeap(Heap):
    def __init__(self, iterable=None, reverse=False):
        if iterable is None:
            iterable = []
        _list = list(iterable)
        self._item_set = set(_list)
        if len(_list) != len(self._item_set):
            raise RuntimeError('duplicate items not allowed: {_list}'.format(_list=_list))
        super(RemovalHeap, self).__init__(_list, reverse=reverse)

    def peek(self):
        return_item = self.heap[0]
        while return_item not in self._item_set:
            self.heappop(self.heap)
            return_item = self.heap[0]
        return return_item

    def push(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self.heappush(self.heap, item)
        self._item_set.add(item)

    def pop(self):
        return_item = self.heappop(self.heap)
        while return_item not in self._item_set:
            return_item = self.heappop(self.heap)
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
        while self.heap[0] not in self._item_set:
            self.heappop(self.heap)
        return_item = self.heapreplace(self.heap, item)
        self._item_set.remove(return_item)
        return return_item

    replace = poppush

    def pushpop(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self._item_set.add(item)
        return_item = self.heappushpop(self.heap, item)
        while return_item not in self._item_set:
            return_item = self.heappop(self.heap)
        self._item_set.remove(return_item)
        return return_item

    def sweep(self):
        if 2 * len(self._item_set) < super(RemovalHeap, self).__len__():
            self.heap[:] = list(self)
            self.heapify(self.heap)

    def __iter__(self):
        return (item for item in super(RemovalHeap, self).__iter__() if item in self._item_set)

    def __contains__(self, item):
        return item in self._item_set

    def __len__(self):
        return len(self._item_set)

    def __repr__(self):
        return 'RemovalHeap({content})'.format(content=list(self))


# order + removal
class XHeap(Heap):
    def __init__(self, iterable=None, key=lambda x: x, reverse=False):
        if iterable is None:
            iterable = []
        self.key = key
        _list = list(iterable)
        self._item_set = set(_list)
        if len(_list) != len(self._item_set):
            raise RuntimeError('duplicate items not allowed: {_list}'.format(_list=_list))
        super(XHeap, self).__init__(((key(item), item) for item in _list), reverse=reverse)

    def peek(self):
        return_item = self.heap[0][1]
        while return_item not in self._item_set:
            self.heappop(self.heap)
            return_item = self.heap[0][1]
        return return_item

    def push(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self.heappush(self.heap, (self.key(item), item))
        self._item_set.add(item)

    def pop(self):
        return_item = self.heappop(self.heap)[1]
        while return_item not in self._item_set:
            return_item = self.heappop(self.heap)[1]
        self._item_set.remove(return_item)
        self.sweep()
        return return_item

    def remove(self, item):
        self._item_set.remove(item)
        self.sweep()

    def sweep(self):
        if 2 * len(self._item_set) < super(XHeap, self).__len__():
            self.heap[:] = (item_tuple for item_tuple in super(XHeap, self).__iter__()
                            if item_tuple[1] in self._item_set)
            self.heapify(self.heap)

    def poppush(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self._item_set.add(item)
        while self.heap[0][1] not in self._item_set:
            self.heappop(self.heap)
        return_item = self.heapreplace(self.heap, (self.key(item), item))[1]
        self._item_set.remove(return_item)
        return return_item

    replace = poppush

    def pushpop(self, item):
        if item in self._item_set:
            raise RuntimeError('duplicate item not allowed: {item}'.format(item=item))
        self._item_set.add(item)
        return_item = self.heappushpop(self.heap, (self.key(item), item))[1]
        while return_item not in self._item_set:
            return_item = self.heappop(self.heap)[1]
        self._item_set.remove(return_item)
        return return_item

    def __iter__(self):
        return (item_tuple[1] for item_tuple in super(XHeap, self).__iter__() if item_tuple[1] in self._item_set)

    def __contains__(self, item):
        return item in self._item_set

    def __len__(self):
        return len(self._item_set)

    def __repr__(self):
        return 'XHeap({content}, key={key})'.format(content=list(self), key=self.key)
