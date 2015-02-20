class MinHeap:

    def __init__(self, nodes, distance):
        self.a = nodes                      #Stores the nodes of the graph
        self.d = distance                   #Stores the distance mapping of each node
        self.heap_size = len(nodes)

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
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return minimum


def dijkstra(graph, weight, source):
    distance, parent = initialize_single_source(graph, source)
    s = set()
    q = MinHeap(graph.keys(), distance)
    q.build_min_heap()
    while q.size() > 0:
        u = q.extract_min()
        s.add(u)
        for v in graph[u]:
            relax(u, v, weight, distance, parent)
        q.build_min_heap()
    return distance, parent



def initialize_single_source(graph, source):
    distance = dict()
    parent = dict()
    for vertex in graph:
        distance[vertex] = float('inf')
        parent[vertex] = None
    distance[source] = 0
    return distance, parent

def relax(u, v, weight, distance, parent):
    if distance[v] > distance[u] + weight[(u, v)]:
        distance[v] = distance[u] + weight[(u, v)]
        parent[v] = u


g = {'s' : set(['t', 'y']), 't' : set(['x', 'y']), 'x' : set(['z']), 'z' : set(['x', 's']), 'y' : set(['t', 'x', 'z'])}
gw = {('s', 't') : 10, ('s', 'y') : 5, ('t', 'y') : 2, ('y', 't') : 3, ('t', 'x') : 1, ('y', 'z') : 2, ('x', 'z') : 4, ('z', 'x') : 6, ('y', 'x') : 9, ('z', 's') : 7}

d, p = dijkstra(g, gw, 's')
print d
print p