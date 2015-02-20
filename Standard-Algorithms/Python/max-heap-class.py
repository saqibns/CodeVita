class MaxHeap:

    def __init__(self, a):
        self.a = a
        self.heap_size = len(a)

    def __str__(self):
        return str(self.a)

    def size(self):
        return self.heap_size

    def parent(self, i):
        return i / 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.a[l] > self.a[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.a[r] > self.a[largest]:
            largest = r
        if largest != i:
            tmp = self.a[i]
            self.a[i] = self.a[largest]
            self.a[largest] = tmp
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in xrange((self.heap_size - 1) / 2, -1, -1):
            self.max_heapify(i)

    def maximum(self):
        return self.a[0]

    def extract_max(self):
        if self.heap_size < 0:
            raise Exception("Underflow")
        maximum = self.a[0]
        self.a[0] = self.a[self.heap_size - 1]
        self.a.pop()
        self.heap_size = self.heap_size - 1
        self.max_heapify(0)
        return maximum

    def increase_key(self, i, key):
        if key < self.a[i]:
            raise Exception("New key is smaller than current key")
        self.a[i] = key
        while i > 0 and self.a[self.parent(i)] < self.a[i]:
            tmp = self.a[i]
            self.a[i] = self.a[self.parent(i)]
            self.a[self.parent(i)] = tmp
            i = self.parent(i)

    def max_heap_insert(self, key):
        self.heap_size = self.heap_size + 1
        self.a.append(float('-inf'))
        self.increase_key(self.heap_size - 1, key)

#Tests
heap = MaxHeap([1, 2, 3, 4, 5, 6, 7])
heap.build_max_heap()
print heap
z = heap.extract_max()
print z
print heap
heap.increase_key(4, 10)
print heap
heap.max_heap_insert(8)
print heap