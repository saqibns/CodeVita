def multiply(x, y):
    a = [[0 for i in xrange(len(x[0]))] for j in xrange(len(y[0]))]
    for i in xrange(len(x[0])):
        for j in xrange(len(y[0])):
            for k in xrange(len(y[0])):
                a[i][j] += x[i][k] * y[k][j]

    return a

def print_matrix(matrix):
    for i in xrange(len(matrix[0])):
        for j in xrange(len(matrix[0])):
            print matrix[i][j],
        print
x = [[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]]
x1 = [[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
##print_matrix(multiply(multiply(x, x), x))
print_matrix(multiply(multiply(x, x), x))
print
print_matrix(multiply(multiply(x1, x1), x1))