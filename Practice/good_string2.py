string = input() + '#'
gc = 0
lc = 0
i = 0
l = len(string)
flag = False
for i in range(l):
    ch = string[i]
    if ch == 'a' and not flag:
        flag = True
        lc = 1
    elif ch == 'a' and flag:
        lc += 1
    elif ch != 'a' and flag:
        flag = False
        if lc > gc:
            gc = lc

print((gc + 1) * 'a')
