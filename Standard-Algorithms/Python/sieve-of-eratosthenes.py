import math
def sieve(limit):
    number = [i for i in xrange(limit + 1)]
    marking = [True for i in xrange(limit + 1)]
    upto = int(math.sqrt(limit + 1))
    marking[0] = False
    marking[1] = False
    for i in xrange(2, upto):
        while not marking[i]:
            i += 1
        current = number[i]
        for j in xrange(2 * current, limit + 1, current):
            marking[j] = False
    return number, marking

#Test
n, m = sieve(400)
for i in xrange(len(n)):
    if m[i]:
        print n[i],