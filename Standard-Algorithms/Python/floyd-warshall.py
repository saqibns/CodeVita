def copy_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    copy = [[0 for i in xrange(cols)] for j in xrange(rows)]
    for i in xrange(rows):
        for j in xrange(cols):
            Type = type(matrix[i][j])
            copy[i][j] = Type(matrix[i][j])
    return copy

def floyd_warshall(graph_matrix):
    n = len(graph_matrix)
    d0 = copy_matrix(graph_matrix)
    d1 = [[0 for i in xrange(n)] for j in xrange(n)]
    d = [d0, d1]
    t = 1
    for k in xrange(n):
        for j in xrange(n):
            for i in xrange(n):
                d[t][i][j] = min(d[1 - t][i][j], (d[1 - t][i][k] + d[1 - t][k][j]))
##        print "Pass : " + str(k)
##        print d[t]
        t = 1 - t
    return d[1 - t]

#Test
m = [[0, 3, 8, float('inf'), -4], [float('inf'), 0, float('inf'), 1, 7], [float('inf'), 4, 0, float('inf'), float('inf')], [2, float('inf'), -5, 0, float('inf')], [float('inf'), float('inf'), float('inf'), 6, 0]]

print floyd_warshall(m)