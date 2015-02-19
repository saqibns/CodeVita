def main():
    n = int(raw_input())
    for i in xrange(n):
        string = raw_input()
        print reduce(string)

def reduce(string):

    #Start from both the beginning and the end
    idx = 0                 #Beginning index
    jdx = len(string) - 1   #End Index

    trans = 0               #Counts the number of transformations required
    while idx <= jdx:
        trans += abs(ord(string[idx]) - ord(string[jdx]))
        idx += 1
        jdx -= 1
    return trans

##print reduce("cba")
main()