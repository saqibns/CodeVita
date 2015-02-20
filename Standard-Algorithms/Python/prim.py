class MinHeap:

    def __init__(self, nodes, key):
        self.a = nodes                      #Stores the nodes of the graph
        self.d = key                       #Stores the key mapping of each node
        self.heap_size = len(nodes)
        self.s = set(nodes)

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

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and self.d[self.a[l]] < self.d[self.a[i]]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size and self.d[self.a[r]] < self.d[self.a[smallest]]:
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
        self.s.remove(minimum)
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return minimum

    def exists(self, element):
        return element in self.s

def prim(graph, weight, start):
    key = dict()
    parent = dict()
    for node in graph:
        key[node] = float('inf')
        parent[node] = None
    key[start] = 0
    q = MinHeap(graph.keys(), key)
    q.build_min_heap
    while q.size() > 0:
        u = q.extract_min()
        for v in graph[u]:
            if q.exists(v) and weight[(u, v)] < key[v]:
                parent[v] = u
                key[v] = weight[(u, v)]
        q.build_min_heap()
    return parent

#Tests
g = {
    'a' : set(['b', 'h']),
    'b' : set(['a', 'h', 'c']),
    'h' : set(['a', 'b', 'i', 'g']),
    'i' : set(['h', 'c', 'g']),
    'c' : set(['i', 'd', 'f', 'b']),
    'd' : set(['c', 'f', 'e']),
    'e' : set(['d', 'f']),
    'f' : set(['g', 'c', 'd', 'e']),
    'g' : set(['i', 'h', 'f'])
     }

gw = d = {('b', 'c'): 8, ('e', 'd'): 9, ('h', 'i'): 7, ('d', 'e'): 9, ('i', 'h'): 7, ('b', 'h'): 11, ('c', 'b'): 8, ('a', 'b'): 4, ('c', 'f'): 4, ('h', 'a'): 8, ('g', 'i'): 6, ('d', 'f'): 14, ('f', 'e'): 10, ('a', 'h'): 8, ('i', 'g'): 6, ('d', 'c'): 7, ('g', 'h'): 1, ('i', 'c'): 2, ('b', 'a'): 4, ('c', 'i'): 2, ('h', 'b'): 11, ('e', 'f'): 10, ('c', 'd'): 7, ('h', 'g'): 1, ('f', 'c'): 4, ('g', 'f'): 2, ('f', 'g'): 2, ('f', 'd'): 14}

t = prim(g, gw, 'a')
print t
tw = 0
for node in t:
    if t[node] != None:
        tw += gw[(node, t[node])]

print tw
