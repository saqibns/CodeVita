class MinHeap:

    def __init__(self, a):
        self.a = a
        self.heap_size = len(a)

    def __str__(self):
        return str(self.a)

    def parent(self, i):
        return i / 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.a[l] < self.a[i]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.a[r] < self.a[smallest]:
            smallest = r
        if smallest != i:
            tmp = self.a[i]
            self.a[i] = self.a[smallest]
            self.a[smallest] = tmp
            self.min_heapify(smallest)

    def build_min_heap(self):
        for i in xrange((self.heap_size - 1) / 2, -1, -1):
            self.min_heapify(i)

    def minimum(self):
        return self.a[0]

    def extract_min(self):
        if self.heap_size < 0:
            raise Exception("Underflow")
        minimum = self.a[0]
        self.a[0] = self.a[self.heap_size - 1]
        self.a.pop()
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return minimum

    def decrease_key(self, i, key):
        if key > self.a[i]:
            raise Exception("New key is larger than current key")
        self.a[i] = key
        while i > 0 and self.a[self.parent(i)] > self.a[i]:
            tmp = self.a[i]
            self.a[i] = self.a[self.parent(i)]
            self.a[self.parent(i)] = tmp
            i = self.parent(i)

    def min_heap_insert(self, key):
        self.heap_size = self.heap_size + 1
        self.a.append(float('inf'))
        self.decrease_key(self.heap_size - 1, key)

#Tests
heap = MinHeap([7, 6, 5, 4, 3, 2, 1])
heap.build_min_heap()
print heap
z = heap.extract_min()
print z
print heap
heap.decrease_key(4, 0)
print heap
heap.min_heap_insert(1)
print heap