def radix_sort(numbers, max_len):
    buckets = [list() for i in xrange(10)]
    for i in xrange(max_len):
        #print 'Pass : ' + str(i)
        mod = 10 ** (i + 1)
        div = 10 ** i
        for number in numbers:
            index = (number % mod) / div
            buckets[index].append(number)
        numbers = list()
        #print buckets
        #print numbers
        for j in xrange(10):
            for number in buckets[j]:
                numbers.append(number)
            buckets[j] = list()
        #print numbers
    return numbers

#Tests
print radix_sort([489, 143, 78, 20, 9, 333, 221, 892, 700, 10, 85], 3)
print radix_sort([5121, 1186, 912, 5963, 3140, 6874, 4386, 5419, 8043, 8389, 6794, 17, 42,  1184, 4648, 7719, 9874, 4593, 2175, 36, 1825, 7320, 9685, 7832], 4)