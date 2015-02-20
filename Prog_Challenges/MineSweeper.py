import sys
def input_handler():
    rows, cols = map(int, raw_input().split())
    count = 0
    while rows > 0 and cols > 0:
        count += 1
        field = [[0 for i in xrange(cols)] for j in xrange(rows)]
        #print_field(field, rows, cols)
        for i in xrange(rows):
            line = raw_input()
            j = 0
            for char in line:
                if char == "*":
                    field[i][j] = -1
                j += 1
        #print_field(field, rows, cols)
        fill_field(field, rows, cols)
        print 'Field #' + str(count) + ':'
        print_field(field, rows, cols)
        print
        rows, cols = map(int, raw_input().split())

def get_neighbours(rows, cols, x, y):
    neighbours = list()
    x_inc = (0, 0, 1, 1, 1, -1, -1, -1)
    y_inc = (-1, 1, 0, -1, 1, 0, -1, 1)
    for i in xrange(8):
        new_x = x + x_inc[i]
        new_y = y + y_inc[i]
        if (0 <= new_x < rows) and (0 <= new_y < cols):
            neighbours.append((new_x, new_y))
    return neighbours

def fill_field(field, rows, cols):
    for i in xrange(rows):
        for j in xrange(cols):
            if field[i][j] == -1:
                neighbours = get_neighbours(rows, cols, i, j)
                for row, col in neighbours:
                    if field[row][col] != -1:
                        field[row][col] += 1

def print_field(field, rows, cols):
    for i in xrange(rows):
        for j in xrange(cols):
            if field[i][j] == -1:
                sys.stdout.write('*')
            else:
                sys.stdout.write(str(field[i][j]))
        print

##print get_neighbours(3, 3, 1, 1)
##print get_neighbours(3, 3, 0, 0)
##print get_neighbours(3, 3, 2, 2)
##print get_neighbours(3, 3, 2, 1)
input_handler()