def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, len(heap) - 1)


def heappop(heap):
    lastelt = heap.pop()
    if not heap:
        return lastelt

    returnitem, heap[0] = heap[0], lastelt
    _siftup(heap)
    return returnitem


# Does a pop and then a push
def heapreplace(heap, item):
    returnitem, heap[0] = heap[0], item
    _siftup(heap)
    return returnitem


# Does a push and then a pop
def heappushpop(heap, item):
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _siftup(heap)
    return item


def heapify(x):
    for i in reversed(range(len(x) // 2)):
        _siftup(x, i)


def _siftdown(heap, pos):
    newitem = heap[pos]
    ppos = (pos - 1) >> 1
    while pos and newitem < heap[ppos]:
        heap[pos] = heap[ppos]
        pos = ppos
        ppos = (pos - 1) >> 1
    heap[pos] = newitem


def _siftup(heap, pos=0):
    # Move the item at pos to a leaf
    # by switching place with smallest child (bias to right)
    newitem = heap[pos]

    leftchild = 2 * pos + 1
    rightchild = leftchild + 1
    while rightchild < len(heap):
        if heap[leftchild] < heap[rightchild]:
            heap[pos] = heap[leftchild]
            pos = leftchild
        else:
            heap[pos] = heap[rightchild]
            pos = rightchild
        leftchild = 2 * pos + 1
        rightchild = leftchild + 1
    if leftchild < len(heap):  # Special case of only one child
        heap[pos] = heap[leftchild]
        pos = leftchild
    # Now newitem has been moved to an leaf
    heap[pos] = newitem
    _siftdown(heap, pos)
