import pyrival.SortedList
from bisect import bisect_left as lower_bound, bisect_right as upper_bound 

def test_SortedList():
    pyrival.SortedList.block_size = 30

    L = pyrival.SortedList.SortedList()
    A = []
    
    a = 1
    for _ in range(1000):
        a = (5 * a + 1) % 101
        
        assert str(A) == str(L)
        assert A.count(a) == L.count(a)
        assert A == list(L)
        assert len(A) == len(L)
        assert (a in L) == (a in A)
        assert lower_bound(A, a) == L.lower_bound(a)
        assert upper_bound(A, a) == L.upper_bound(a)

        L.insert(a)
        A.insert(lower_bound(A,a), a)
        
        i = lower_bound(A,a)
        assert str(A) == str(L)
        assert A.count(a) == L.count(a)
        assert A == list(L)
        assert A[i] == L[i] == a
        assert len(A) == len(L)
        assert (a in L) == (a in A)
        assert lower_bound(A, a) == L.lower_bound(a)
        assert upper_bound(A, a) == L.upper_bound(a)

    i = 1
    while A:
        i = (5 * i + 1) % len(A)
        a = A[i]

        assert str(A) == str(L)
        assert A.count(a) == L.count(a)
        assert A == list(L)
        assert len(A) == len(L)
        assert A[i] == L[i]
        assert (a in L) == (a in A)
        assert lower_bound(A, a) == L.lower_bound(a)
        assert upper_bound(A, a) == L.upper_bound(a)
        
        assert A.pop(i) == L.pop(i) == a 
        
        assert str(A) == str(L)
        assert A.count(a) == L.count(a)
        assert A == list(L)
        assert len(A) == len(L)
        assert (a in L) == (a in A)
        assert lower_bound(A, a) == L.lower_bound(a)
        assert upper_bound(A, a) == L.upper_bound(a)


    a = 1
    for _ in range(1000):
        a = (5 * a + 1) % 101
        
        assert str(A) == str(L)
        assert A.count(a) == L.count(a)
        assert A == list(L)
        assert len(A) == len(L)
        assert (a in L) == (a in A)
        assert lower_bound(A, a) == L.lower_bound(a)
        assert upper_bound(A, a) == L.upper_bound(a)

        L.insert(a)
        A.insert(lower_bound(A,a), a)
        
        i = lower_bound(A,a)
        assert str(A) == str(L)
        assert A.count(a) == L.count(a)
        assert A == list(L)
        assert A[i] == L[i] == a
        assert len(A) == len(L)
        assert (a in L) == (a in A)
        assert lower_bound(A, a) == L.lower_bound(a)
        assert upper_bound(A, a) == L.upper_bound(a)
