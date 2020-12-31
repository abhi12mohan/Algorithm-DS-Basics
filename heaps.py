class MamaBearDB:
    def __init__(self, k):
        "Initialize database"
        self.k = k
        self.k_array = []
        self.max_heap = []
        self.min_heap = []

    def record_bowl(self, s):
        "Add bowl with size s"
        if len(self.k_array) == 0:
            self.k_array.append(s)

        elif len(self.k_array) < self.k:
            for i in range(len(self.k_array)):
                if self.k_array[i] > s:
                    self.k_array[i:i] = [s]
                    break
                elif i == len(self.k_array)-1:
                    self.k_array.append(s)
                    break

        elif s <= self.k_array[0]:
            if len(self.min_heap) - len(self.max_heap) > 0:
                self.max_heap.append(s)
                max_heapify_up(self.max_heap, len(self.max_heap), len(self.max_heap) - 1)
            else:
                self.max_heap.append(s)
                max_heapify_up(self.max_heap, len(self.max_heap), len(self.max_heap) - 1)

                self.shift_right()
                self.k_array[0:0] = [self.max_heap.pop(0)]
                self.max_heap[0:0] = [self.max_heap.pop(len(self.max_heap) - 1)]
                max_heapify_down(self.max_heap, len(self.max_heap), 0)

        elif s >= self.k_array[self.k - 1]:
            if len(self.min_heap) - len(self.max_heap) > 0:
                self.min_heap.append(s)
                min_heapify_up(self.min_heap, len(self.min_heap), len(self.min_heap) - 1)

                self.shift_left()
                self.k_array.append(self.min_heap.pop(0))
                self.min_heap[0:0] = [self.min_heap.pop(len(self.min_heap) - 1)]
                min_heapify_down(self.min_heap, len(self.min_heap), 0)
            else:
                self.min_heap.append(s)
                min_heapify_up(self.min_heap, len(self.min_heap), 0)

        elif s > self.k_array[0] and s < self.k_array[self.k - 1]:
            if len(self.min_heap) - len(self.max_heap) > 0:
                for i in range(len(self.k_array)):
                    if self.k_array[i] > s:
                        self.k_array[i:i] = [s]
                        self.shift_left()
                        break
                    elif i == len(self.k_array)-1:
                        self.k_array.append(s)
                        self.shift_left()
                        break
            else:
                for i in range(len(self.k_array)):
                    if self.k_array[i] > s:
                        self.k_array[i:i] = [s]
                        self.min_heap.append(self.k_array.pop(self.k))
                        min_heapify_up(self.min_heap, len(self.min_heap), len(self.min_heap) - 1)
                        break
                    elif i == len(self.k_array)-1:
                        self.k_array.append(s)
                        self.min_heap.append(self.k_array.pop(self.k))
                        min_heapify_up(self.min_heap, len(self.min_heap), len(self.min_heap) - 1)
                        break

    def best_bowls(self):
        "Return tuple of best bowls in sorted order"
        return tuple(self.k_array)

    def shift_right(self):
        self.min_heap.append(self.k_array.pop(len(self.k_array) - 1))
        min_heapify_up(self.min_heap, len(self.min_heap), len(self.min_heap) - 1)

    def shift_left(self):
        self.max_heap.append(self.k_array.pop(0))
        max_heapify_up(self.max_heap, len(self.max_heap), len(self.max_heap) - 1)

###########################

def parent(i):
    p = (i - 1) // 2
    return p if i > 0 else i

def left(i, n):
    l = 2 * i + 1
    return l if l < n else i

def right(i, n):
    r = 2 * i + 2
    return r if r < n else i

def max_heapify_up(A, n, c):
    p = parent(c)

    if A[p] < A[c]:
        A[c], A[p] = A[p], A[c]
        max_heapify_up(A, n, p)

def min_heapify_up(A, n, c):
    p = parent(c)

    if A[p] > A[c]:
        A[c], A[p] = A[p], A[c]
        min_heapify_up(A, n, p)

def max_heapify_down(A, n, p):
    l, r = left(p, n), right(p, n)
    c = l if A[r] < A[l] else r

    if A[p] < A[c]:
        A[c], A[p] = A[p], A[c]
        max_heapify_down(A, n, c)

def min_heapify_down(A, n, p):
    l, r = left(p, n), right(p, n)
    c = l if A[r] > A[l] else r

    if A[p] > A[c]:
        A[c], A[p] = A[p], A[c]
        min_heapify_down(A, n, c)


if __name__ == '__main__':
    first = MamaBearDB(1)
    (57, 48, 65, 67, 53, 63,)
    first.record_bowl(100)
    first.record_bowl(1)


    print(first.max_heap)
    print(tuple(first.k_array))
    print(first.min_heap)
