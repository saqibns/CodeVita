def main():
    string = raw_input().lower() + ' '
##    words = string.split()
    optional = list()
    n = int(raw_input())
    for i in xrange(n):
        optional.append(raw_input().strip())
    work(string, optional)

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
    print ts, te
    print string[ts + 1 : te]

main()