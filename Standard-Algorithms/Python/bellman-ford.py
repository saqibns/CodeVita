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


def bellman_ford(graph, weight, source):
    distance, parent = initialize_single_source(graph, source)
    n = len(graph)
    for i in xrange(n - 1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, weight, distance, parent)
##    print distance
##    print parent
    for u in graph:
        for v in graph[u]:
            if distance[v] > distance[u] + weight[(u, v)]:
##                priznt '(' + u + ', ' + v + ')'
                return False
    return True

#Tests
g1 = {'z' : set(['u', 'x']), 'u' : set(['v', 'x', 'y']), 'v' : set(['u']), 'x' : set(['v', 'y']), 'y' : set(['v', 'z'])}
w1 = {
    ('z', 'u') : 6,
    ('z', 'x') : 7,
    ('u', 'v') : 5,
    ('u', 'x') : 8,
    ('u', 'y') : -4,
    ('v', 'u') : -2,
    ('x', 'v') : -3,
    ('x', 'y') : 9,
    ('y', 'v') : 7,
    ('y', 'z') : 2
    }
print bellman_ford(g1, w1, 'z') #True

g2 = {'z' : set(['u', 'x']), 'u' : set(['v', 'x', 'y']), 'v' : set(['u']), 'x' : set(['v', 'y']), 'y' : set(['v', 'z'])}
w2 = {
    ('z', 'u') : 6,
    ('z', 'x') : 7,
    ('u', 'v') : -5,
    ('u', 'x') : 8,
    ('u', 'y') : -4,
    ('v', 'u') : -2,
    ('x', 'v') : -3,
    ('x', 'y') : 9,
    ('y', 'v') : 7,
    ('y', 'z') : 2
    }
print bellman_ford(g2, w2, 'z') #False
