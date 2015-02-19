def fast_targeted_order(ugraph):

    n = len(ugraph)
    degree_sets = [set() for __ in xrange(n)]
    for node in ugraph:
        degree_sets[len(ugraph[node])].add(node)
##    print degree_sets
    l = list()
    for k in range(n - 1, -1 , -1):
        while len(degree_sets[k]) != 0:
            u = degree_sets[k].pop()
            for neighbour in ugraph[u]:
                d = len(ugraph[neighbour])
                degree_sets[d].remove(neighbour)
                degree_sets[d - 1].add(neighbour)
                ugraph[neighbour].remove(u)
            #print ugraph
            l.append(u)
            del u

    return l


g = {1 : set([2, 3, 4]), 2 : set([1, 6]), 3 : set([1, 5]), 4 : set([1, 5]), 5 : set([3, 4]), 6 : set([2]), 7 : set([]), 8 : set([9]), 9 : set([8])}
print fast_targeted_order(g)