def main(tests):
    for dummy in range(tests):
        s = input()
        if invariant(s):
            print('no answer')
        else:    
            work_horse(s)

def work_horse(string):

    chars = list(string)
    # print(chars)

    idx = len(chars) - 2
    last = ord(chars[-1])
    flag = False
    while idx >= 0:
        if ord(chars[idx]) < last:
            #flag = True
            break
        idx -= 1

    #if flag:
    temp = chars[-1]
    chars[-1] = chars[idx]
    chars[idx] = temp

    new_list = chars[idx + 1:]
    s = sorted(new_list)
    start = 0
    while start <= idx:
        print(chars[start], end = '')
        start += 1

    for char in s:
        print(char, end = '')
##    else:
##        print('no answer', end = '')
    print()

def invariant(x):

    i = 0
    while i < len(x) - 1:
        if x[i] < x[i + 1]:
            return False
        i += 1
    return True

tsts = int(input())
main(tsts)
