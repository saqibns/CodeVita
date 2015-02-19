height = [1]
table = {0 : 1}
for i in range(1, 61):
    prev = table[i - 1]
    if i % 2 == 0:
        ht = prev + 1
    else:
        ht = prev * 2
    table[i] = ht

print(table)

