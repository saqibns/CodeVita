time = 0
color = dict()
start = dict()
finish = dict()
parent = dict()
order = list()

def dfs(graph):
    global time
    time = 0
    for vertex in graph:
        color[vertex] = 'W'
        parent[vertex] = None
    for vertex in graph:
        if color[vertex] == 'W':
            dfs_visit(graph, vertex)

def dfs_visit(graph, u):
    global time
    time += 1
    start[u] = time
    color[u] = 'G'
    for v in graph[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs_visit(graph, v)
    color[u] = 'B'
    order.insert(0, u)
    time += 1
    finish[u] = time

def topological_sort(graph):
    dfs(graph)
    return order

#Tests
g = {'undershorts' : set(['pants', 'shoes']), 'socks' : set(['shoes']), 'pants' : set(['shoes', 'belt']), 'shirt' : set(['belt', 'tie']), 'tie' : set(['jacket']), 'belt' : set(['jacket']), 'watch' : set([]), 'jacket' : set([]), 'shoes' : set([])}
op = topological_sort(g)
print op
print [finish[key] for key in op]

