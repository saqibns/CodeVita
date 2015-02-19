# Breadth First Search

def bfs(graph, start):
    color = dict()
    distance = dict()
    parent= dict()
    for key in graph.keys():
        color[key] = 'W'
        distance[key] = 0
        parent[key] = None

    color[start] = 'G'
    queue = list()
    queue.append(start)
    while len(queue) > 0:
        u = queue.pop(0)
        for v in graph[u]:
            if color[v] == 'W':
                color[v] = 'G'
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
        color[u] = 'B'
    return distance, parent

# Depth Breadth Search

def dfs(graph, start):
    color = dict()
    parent = dict()
    distance = dict()
    for key in graph.keys():
        color[key] = 'W'
        parent[key] = None
        distance[key] = 0
    color[start] = 'G'
    stack = list()
    stack.append(start)
    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if color[v] == 'W':
                color[v] = 'G'
                distance[v] = distance[u] + 1
                parent[v] = u
                stack.append(v)
        color[u] = 'B'
    return distance, parent

# Path tracer

def trace(distance, parents, start, end):
    if distance[end] == 0:
        return []
    path = list()
    path.append(end)
    current = end
    while current != start:
        current = parents[current]
        path.append(current)
    return path
    
g = {'r' : set(['s', 'v']), 's' : set(['r', 'w']), 't' : set(['u', 'w', 'x']), 'u' : set(['x', 'y']), 'v' : set(['r']), 'w' : set(['s', 't', 'x']), 'x' : set(['w', 't', 'u', 'y']), 'y' : set(['u', 'x'])}
h = {1 : set([2, 3]), 2 : set([4]), 3 : set([5]), 4 : set([]), 5 : set([])}
print "Breadth First Search:"
a, b  = bfs(g, 's')
print a
print b
print

a, b = bfs(h, 1)
print a
print b
print list(reversed(trace(a, b, 1, 4)))
print

print "Depth First Search:"
x, y = dfs(g, 's')
print x
print y
print
