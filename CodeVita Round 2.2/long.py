def main():
    try:
        string = raw_input().lower().strip()
        if len(string.split()) < 2:
##            print 'Invalid Input'
            exit(0)
        string += ' '
    ##    words = string.split()
    ##    print string
        optional = list()
        n = int(raw_input())
        for i in xrange(n):
            optional.append(raw_input().lower().strip())
        work(string, optional)
    except:
        print 'Invalid Input'

def work(string, optional):
    length = len(string)
    markers = list([0])
    for op in optional:
        found = string.find(op + ' ', 0)
        while found != -1:
            markers.append(found)
            found = string.find(op + ' ', found + 1)
    markers.sort()
    markers.append(length)
##    print markers
    one = markers[0]
    two = markers[1]
    maxi = two - one
    ts = one
    te = two
    two = 2
    while two < len(markers):
        diff = markers[two] - markers[two - 1]
        if diff > maxi:
            maxi = diff
            ts = markers[two - 1]
            te = markers[two]
        two += 1
    while string[ts] != ' ':
        ts += 1
##    print ts, te
##    string = string.strip()
    print string[ts + 1 : te]

main()