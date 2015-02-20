import math
tests = int(input())

for i in range(tests):
    number = int(input())
    root1 = int(math.sqrt(number))
    root2 = math.sqrt(number - (root1 * root1))

    if root2 == math.ceil(root2):
        print('Yes')
    else:
        print('No')


    
