def partition(graph):
    color = dict()
    true = set()
    false = set()
    for node in graph:
        color[node] = None
    flag = True
    for node in graph:
        if color[node] == None:
            color[node] = flag
            if flag:
                true.add(node)
            else:
                false.add(node)
            for adj in graph[node]:
                if color[adj] == None:
                    color[adj] = not flag
                    if flag:
                        false.add(adj)
                    else:
                        true.add(adj)
                elif color[adj] == flag:
                    #print (true, false)
                    return None
    return (true, false)

g = {'a' : set('b'), 'b' : set('a')}
print partition(g)

h = {1 : set([4, 5]), 2 : set([4]), 3 : set([5, 6]), 4 : set([1, 2]), 5 : set([1, 3]), 6 : set([3])}
print partition(h)

i = {1 : set([4, 5]), 2 : set([3, 4]), 3 : set([2, 5, 6]), 4 : set([1, 2]), 5 : set([1, 3]), 6 : set([3])}
print partition(i)