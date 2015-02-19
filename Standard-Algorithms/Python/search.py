def linear(listt, element, start_from = 0):
    for i in range(start_from, len(listt)):
        if listt[i] == element:
            return i

def binary(listt, element):
    mini = 0
    maxi = len(listt) - 1
    while mini <= maxi:
        mid = (mini + maxi) // 2
        if listt[mid] == element:
            return mid
        elif listt[mid] > element:
            maxi = mid - 1
        else:
            mini = mid + 1

#Tests for Linear Search
print "Linear Search:"
print linear([99, 42, 32, 8, 45, 44, 63, 1, 69, 82, 42, 13, 12, 34, 73], 8)     #3
print linear([99, 42, 32, 8, 45, 44, 63, 1, 69, 82, 42, 13, 12, 34, 73], 73)    #14
print linear([99, 42, 32, 8, 45, 44, 63, 1, 69, 82, 42, 13, 12, 34, 73], 81)    #None
print linear([99, 42, 32, 8, 45, 44, 63, 1, 69, 82, 42, 13, 12, 34, 73], 11)    #None
print linear([99, 42, 32, 8, 45, 44, 63, 1, 69, 82, 42, 13, 12, 34, 73], 99)     #0
print linear([99, 42, 32, 8, 45, 44, 63, 1, 69, 82, 42, 13, 12, 34, 73], 8, 4)  #None

#Tests for Binary Search
print "\nBinary Search"
print binary([4, 5, 9, 13, 18, 19, 26, 29, 33, 36, 40], 4)      #0
print binary([4, 5, 9, 13, 18, 19, 26, 29, 33, 36, 40], 40)     #10
print binary([4, 5, 9, 13, 18, 19, 26, 29, 33, 36, 40], 91)     #None
print binary([4, 5, 9, 13, 18, 19, 26, 29, 33, 36, 40], 12)     #None
print binary([4, 5, 9, 13, 18, 19, 26, 29, 33, 36, 40], 13)     #3