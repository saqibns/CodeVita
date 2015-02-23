def copy_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    copy = [[0 for i in xrange(cols)] for j in xrange(rows)]
    for i in xrange(rows):
        for j in xrange(cols):
            Type = type(matrix[i][j])
            copy[i][j] = Type(matrix[i][j])
    return copy