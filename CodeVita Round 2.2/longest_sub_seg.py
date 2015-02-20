def main():
    try:
        string = raw_input().lower()
        words = string.split()
        optional = list()
        n = int(raw_input())
        for i in xrange(n):
            optional.append(raw_input().strip())
        work(words, optional)
    except:
        print strin.strip()

def work(words, optional):
    length = len(words)
##    markers = [True for x in xrange(length)]
    mark = list()
    for op in optional:
        idx = 0
        while idx < length:
            if words[idx] == op:
##                markers[idx] = False
                mark.append(idx)
            idx += 1
    mark.sort()
    mark.append(length)
    maxi = 0
    start = 0
    ts = 0
    te = 0
    for elem in mark:
        diff = elem - start
        if diff > maxi:
            maxi = diff
            ts = start
            te = elem - 1
        start = elem + 1
##    print markers
    print mark
    print maxi, ts, te
    for i in xrange(ts, te):
        print words[i],
    print words[te]


main()