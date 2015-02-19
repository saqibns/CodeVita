def main():
    #Get the number of strings
    n = int(raw_input())
    for i in xrange(n):
        #Get the string
        string = raw_input()
        #Pass the string to the function and get the result
        print deletion2(string)

def deletion(string):

    #Count the number of A's and B's
    a_count = 0
    b_count = 0
    for i in string:
        if i == 'A':
            a_count += 1
        else:
            b_count += 1

    #Find the minimum
    minim = min(a_count, b_count)

    #Thus, 2 * minim pairs exist
    #All others must be anhilated
    deletions = len(string) - 2 * minim
    return deletions

def deletion2(string):

    #Sentinel
    string += '$'
    #Count the number of clusters one at a time
    char_cnt = 0        #Stores the cluster length
    deletions = 0
    first = string[0]
    for i in string:
        if i == first:
            char_cnt += 1
        else:
            #We've encountered the other character
            #Delete all but one
            deletions += char_cnt

            #Reset the cluster length to zero
            char_cnt = 0
            #Do the same for the other character
            first = i

            #print 'else: ' + str(deletions)

    return deletions - 1 #'-1' for the sentinel

main()