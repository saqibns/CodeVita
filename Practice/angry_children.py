##TEST_1 = [10, 100, 300, 200, 1000, 20, 30]
##TEST_2 = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
##TEST_3 = [10, 20, 30, 100, 101, 102]
##TEST_4 = [6327, 571, 6599, 479, 7897, 9322, 4518, 571, 6677, 7432, 815, 6920, 4329, 4104, 7775, 5708, 7991, 5802, 8619, 6053, 7539, 7454, 9000, 3267, 6343, 7165, 4095, 439, 5621, 4095, 153, 1948, 1018, 6752, 8779, 5267, 2426, 9649, 2190, 9103, 7081, 3006, 2376, 7762, 3462, 151, 3471, 1453, 2305, 8442]
def main():
    #Get 'n'
    n = int(raw_input())
    #Get 'k'
    k = int(raw_input())

    #Get 'n' numbers
    sequence = list()
    for i in xrange(n):
        sequence.append(int(raw_input()))

    #Get the answer
    print minimize(sequence, n, k)

def minimize(sequence, n, k):
    #Get the sorted sequence
    srted = sorted(sequence)
##    print srted

    i = 0
    j = k - 1

    #Save the minimum difference
    min_diff = float('inf')

    #See 'k' steps ahead
    while j < n:
        diff = srted[j] - srted[i]
##        print 'diff: ' + str(diff)
        if diff < min_diff:
            min_diff = diff
##            idxl = i
##            idxu = j
        i += 1
        j += 1
##    print srted[idxl : idxu + 1]
    return min_diff

##print minimize(TEST_1, 7, 3)
##print minimize(TEST_2, 10, 4)
##print minimize(TEST_3, 6, 3)
##print minimize(TEST_4, 50, 8)
main()