def input_directed_graph_1():
    """
    Input Format:
        4
        1 2 3
        3 1 4
        2 1
        4 1 2 3

        There are four nodes.
        Node 1 is linked to nodes 2 and 3 and so forth
    """
    graph = dict()
    nodes = int(raw_input())
    for i in xrange(nodes):
        line = raw_input().split()              #If nodes are enumerated as strings
        #line = map(int, raw_input.split())      #If nodes are enumerated as integers
        graph[line[0]] = set(line[1:])
    return graph

def input_directed_graph_2():
    """
    Input Format:
        4
        6
        1 2
        3 4
        2 4
        2 3
        4 1
        4 3
        There are four nodes
        Six relationships follow.
    """
    graph = dict()
    nodes = int(raw_input())
    for i in xrange(1, nodes + 1):
        graph[i] = set()
    iterations = int(raw_input())
    for i in xrange(iterations):
        #line = raw_input().split()              #If nodes are enumerated as strings
        line = map(int, raw_input().split())      #If nodes are enumerated as integers
        graph[line[0]].add(line[1])
    return graph

def input_undirected_graph_1():
    """
    Input Format:
        4
        1 2 3
        3 1 4
        2 1
        4 1 2 3

        There are four nodes.
        Node 1 is linked to nodes 2 and 3 and both 2 and 3 are linked to 1 as well
    """
    nodes = int(raw_input())
    graph = dict()
    for i in xrange(1, nodes + 1):
        graph[i] = set()
    for i in xrange(nodes):
        line = map(int, raw_input().split())
        for j in line[1:]:
            graph[line[0]].add(j)
            graph[j].add(line[0])
    return graph

def input_undirected_graph_2():
    """
    Input Format:
        4
        6
        1 2
        3 4
        2 4
        2 3
        4 1
        4 3
        There are four nodes
        Six relationships follow.
    """
    graph = dict()
    nodes = int(raw_input())
    for i in xrange(1, nodes + 1):
        graph[i] = set()
    iterations = int(raw_input())
    for i in xrange(iterations):
        #line = raw_input().split()              #If nodes are enumerated as strings
        line = map(int, raw_input().split())      #If nodes are enumerated as integers
        graph[line[0]].add(line[1])
        graph[line[1]].add(line[0])
    return graph

print input_undirected_graph_2()
