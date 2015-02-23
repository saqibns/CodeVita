def transpose(graph):
    gt = dict()
    #Intialize the transposed graph
    for vertex in graph:
        gt[vertex] = set()
    for vertex in graph:
        for adj in graph[vertex]:
            gt[adj].add(vertex)
    return gt

#Tests
g = {
    1 : set([2, 3]),
    2 : set([4]),
    3 : set([]),
    4 : set([1, 3])
    }

print transpose(g)