def kmp(string, substring):
    n = len(string)
    substring += chr(128)
    m = len(substring)
    indices = list()
    prefix = compute_prefix_table(substring)
    #print prefix
    i = 0                                   #Number of characters matched
    for j in xrange(n):
        while i > 0 and substring[i] != string[j]:
            i = prefix[i]
        if substring[i] == string[j]:
            i += 1                          #Match next character
        if i == m - 1:                      #Is all of the substring matched
            #print "pattern occurs with shift " + str(j - m + 2)
            indices.append((j - m + 2))
            i = prefix[i]                   #Look for the next match
    return indices

def compute_prefix_table(substring):
    m = len(substring)
    prefix = [0 for i in xrange(m)]
    i = 0
    for j in xrange(1, m):
        while i > 0 and substring[i] != substring[j]:
            i = prefix[i]
        if substring[i] == substring[j]:
            i += 1
        prefix[j] = i
    return prefix

def tester(string, substring):
    indices = kmp(string, substring)
    l = len(substring)
    for i in indices:
        print string[i : i + l]

#Tests
##print compute_prefix_table("atag")
##print compute_prefix_table("acacagt")
##print compute_prefix_table("ababaca")

##print 'atatatacatajatag:'
##print kmp('atatatacatajatag', 'atag')
##print 'tgtaa:'
##print kmp('tgtaa', 'atag')
##print 'ctcatagataggg:'
##print kmp('ctcatagataggg', 'atag')
##print 'ttggcattccc:'
##print kmp('ttggcattccc', 'atag')
##print 'tcaccccaaataggag:'
##print kmp('tcaccccaaataggag', 'atag')
##print 'cggaaggatagaacttcgataca:'
##print kmp('cggaaggatagaacttcgataca', 'atag')
##print 'tttgtgtgaacaatagtgtgtatagtc:'
##print kmp('tttgtgtgaacaatagtgtgtatagtc', 'atag')
##print 'acacagttcaaaacacagtgatcacacagttcacacagtacacagtccg:'
##print kmp('acacagttcaaaacacagtgatcacacagttcacacagtacacagtccg', 'acacagt')
##tester('acacagttcaaaacacagtgatcacacagttcacacagtacacagtccg', 'acacagt')
##print 'agcgacacagtaatcgattgacacagtggg:'
##print kmp('agcgacacagtaatcgattgacacagtggg', 'acacagt')
##tester('agcgacacagtaatcgattgacacagtggg', 'acacagt')
##print 'aatcacacagtttgacacagtcacacagttgagtcagcagactacacagtattg:'
##print kmp('aatcacacagtttgacacagtcacacagttgagtcagcagactacacagtattg', 'acacagt')
##tester('aatcacacagtttgacacagtcacacagttgagtcagcagactacacagtattg', 'acacagt')
##print 'tcagaggggggtacacagtgacacagtgggaacacacagtataacacagtgtc:'
##print kmp('tcagaggggggtacacagtgacacagtgggaacacacagtataacacagtgtc', 'acacagt')
##tester('tcagaggggggtacacagtgacacagtgggaacacacagtataacacagtgtc', 'acacagt')

##print 'ctcatagataggg'
##tester('ctcatagataggg', 'atag')
##print 'cggaaggatagaacttcgataca'
##tester('cggaaggatagaacttcgataca', 'atag')