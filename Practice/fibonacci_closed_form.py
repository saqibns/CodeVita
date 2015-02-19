##import math
##
##ALPHA = 1 / math.sqrt(5)
##ROOT_1 = (1 + math.sqrt(5)) / 2
##ROOT_2 = (1 - math.sqrt(5)) / 2
##
##def fibonacci(nth):
##    first = ALPHA * ROOT_1 ** nth
##    second = -ALPHA * ROOT_2 ** nth
##    return first + second
##
####idx = 0
####f = fibonacci(idx)
####limit = 10 ** 10
####while f < limit:
####    idx += 1
####    f = fibonacci(idx)
####
####print idx

a = 0
b = 0
c = 1
count = 0
lst = list()
while count <= 50:
    count += 1
    a = b
    b = c
    c = a + b
    lst.append(a)
print lst