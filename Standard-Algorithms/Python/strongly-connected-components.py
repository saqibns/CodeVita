time = 0
color = dict()
start = dict()
finish = dict()
parent = dict()
order = list()
reversed_order = list()

def copy_list(listt):
    clone = list()
    for item in listt:
        Type = type(item)
        clone.append(Type(item))
    return clone

def reset_data_structures():
    global color, start, finish, parent, order, reversed_order
    color = dict()
    start = dict()
    finish = dict()
    parent = dict()
    order = list()
    reversed_order = list()

def dfs(graph, enforced_order = None):
    global time
    time = 0
    for vertex in graph:
        color[vertex] = 'W'
        parent[vertex] = None
    if enforced_order == None:
        tmp = graph
    else:
        tmp = enforced_order
    for vertex in tmp:
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
    reversed_order.append(u)
    time += 1
    finish[u] = time

def topological_sort(graph):
    dfs(graph)
    return order

def transpose(graph):
    gt = dict()
    #Intialize the transposed graph
    for vertex in graph:
        gt[vertex] = set()
    for vertex in graph:
        for adj in graph[vertex]:
            gt[adj].add(vertex)
    return gt

def strongly_connected_components(graph):
    topological_sort(graph)
    gt = transpose(graph)
    ord_copy = copy_list(order)
    reset_data_structures()
    dfs(gt, copy_list(ord_copy))
    added = set()
    components = list()

    for vertex in reversed_order:
        forest = set()
        #print 'New Forest:'
        tmp = vertex
        while tmp != None and tmp not in added:
            forest.add(tmp)
            added.add(tmp)
            #print forest
            tmp = parent[tmp]
        if len(forest) > 0:
            components.append(forest)
    return components

g = {
    'a' : set(['b']),
    'b' : set(['e', 'f', 'c']),
    'c' : set(['d', 'g']),
    'd' : set(['c', 'h']),
    'e' : set(['a', 'f']),
    'f' : set(['g']),
    'g' : set(['f']),
    'h' : set(['h'])
    }

print strongly_connected_components(g)


