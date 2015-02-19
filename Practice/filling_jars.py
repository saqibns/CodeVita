n, m = map(int, raw_input().split())
##print n, m
tot_candies = 0
for i in xrange(m):
    one, two, candies = map(int, raw_input().split())
    total = (two - one + 1) * candies
    tot_candies += total

print tot_candies // n