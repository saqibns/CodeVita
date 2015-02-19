l = int(input())
r = int(input())
xor = 0
for i in range(l, r + 1):
    for j in range(l, r + 1):
        new_xor = i ^ j
        if new_xor > xor:
            xor = new_xor
print(xor)