def partition(graph, source):
    """
    The function partitions a graph into two sets if bi-partite partitioning is possible
    otherwise returns 'None'
    """
    visited = dict()
    for node in graph:
        visited[node] = False
    one = set()
    two = set()
    flag = True
    queue1 = list()
    queue2 = list()
    queue1.append(source)
    while len(queue1) > 0 or len(queue2) > 0:
        if flag:
            if len(queue1) != 0:
                current = queue1.pop(0)
                one.add(current)
##                if current not in one:
##                    one.add(current)
##                else:
##                    return None
            else:
                flag = not flag
                continue
        else:
            if len(queue2) != 0:
                current = queue2.pop(0)
                two.add(current)
##                if current not in two:
##                    two.add(current)
##                else:
##                    return None
            else:
                flag = not flag
                continue
        visited[current] = True
        adjacent = graph[current]
        trimmed = [x for x in adjacent if not visited[x]]
        if flag:
            queue2 += trimmed
        else:
            queue1 += trimmed
        flag = not flag

    if len(one & two) == 0:
        return (one, two)
    else:
        return None

g = {'a' : set('b'), 'b' : set('a')}
print partition(g, 'a')

h = {1 : set([4, 5]), 2 : set([4]), 3 : set([5, 6]), 4 : set([1, 2]), 5 : set([1, 3]), 6 : set([3])}
print partition(h, 5)

i = {1 : set([4, 5]), 2 : set([3, 4]), 3 : set([2, 5, 6]), 4 : set([1, 2]), 5 : set([1, 3]), 6 : set([3])}
print partition(i, 1)
