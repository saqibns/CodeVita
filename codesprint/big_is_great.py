def main(tests):
    for dummy in range(tests):
        s = input()
        if invariant(s):
            print('no answer')
        else:    
            work_horse(s)

def invariant(x):

    i = 0
    while i < len(x) - 1:
        if x[i] < x[i + 1]:
            return False
        i += 1
    return True

def work_horse(string):

    leng = len(string)
    l = leng - 2
    while l >= 0:
        if string[l] < string[l + 1]:
            break
        l -= 1

    i = l
    prev = '{'
    at = 0
    while l < leng:
        if string[l] < prev and string[l] > string[i]:
            prev = string[l]
            at = l
        l += 1
    #print(string[i], string[at])

    lst = list(string)
    tmp = lst[i]
    lst[i] = lst[at]
    lst[at] = tmp

    for char in lst[ : i + 1]:
        print(char, end = '')
    for char in sorted(lst[i + 1 :]):
        print(char, end = '')
    print()


tsts = int(input())
main(tsts)

