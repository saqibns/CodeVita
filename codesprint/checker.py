import itertools
import random


def perms(string):

    lst = list(string)
    p = itertools.permutations(lst)
    strings = list()
    for perm in p:
        tmp = ''
        for char in perm:
            tmp += char
        strings.append(tmp)
    return strings

def nextt(string):

    s = list(sorted(set(perms(string))))
    i = 0
    while s[i] != string:
        i += 1
    return s[i + 1]   

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
    new = ''
    while start <= idx:
        #print(chars[start], end = '')
        new += chars[start]
        start += 1

    for char in s:
        #print(char, end = '')
        new += char
##    else:
##        print('no answer', end = '')
    return new

def invariant(x):

    i = 0
    while i < len(x) - 1:
        if x[i] < x[i + 1]:
            return False
        i += 1
    return True

def generate():

    r = ''
    length = random.randrange(10)
    for i in range(length):
        r += chr(random.randrange(97, 122))
    return r

def check(string):

    n = nextt(string)
    if string != n:
        return n
    else:
        return 'no answer'

def check2(string):
    if invariant(string):
            return 'no answer'
    else:
        return work_horse(string)
            
def main():
    for i in range(20):
        s = generate()

        ans1 = check(s)
        ans2 = check2(s)
        if ans1 != ans2:
            print(s, ans1, ans2)
            break 

print(nextt('nizam'))
print(nextt('shamsi'))
print(nextt('prahlad'))

