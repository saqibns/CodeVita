def copy_graph(graph):
    """
    Copies a graph if it is implemented as a dictionary
    """
    copy = dict()
    for key in graph:
        #Find the type of object associated with the key
        Type = type(graph[key])

        #Add the key-value pair to the new graph
        copy[key] = Type(graph[key])

    return copy

#Tests
g = {1: set([2, 4]), 2: set([1, 3, 4]), 3: set([1, 2]), 4: set([2])}
h = copy_graph(g)

#Making a change to one of the graphs should not change the other
g[1].add(3)
h[4].add(1)

print g
print h
print g == h
print g is h

