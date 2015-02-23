time = 0
color = dict()
start = dict()
finish = dict()
parent = dict()

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
    time += 1
    finish[u] = time

#Tests
g = {'u' : set(['v', 'x']), 'v' : set(['y']), 'x' : set(['v']), 'y' : set(['x']), 'w' : set(['y', 'z']), 'z' : set('z')}

dfs(g)
print start
print finish
print parent
