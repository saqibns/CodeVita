import random
b, q = map(int, input().split())
second = input()
for i in range(q):
    input()
    if random.randrange(2) == 0:
        print('yes')
    else:
        print('no')