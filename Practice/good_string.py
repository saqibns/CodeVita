string = input()
idx = 0
l = len(string)
max_count = 0
for i in range(l):
    if string[i] == 'a':
        count = 1
        for j in range(i + 1, l):
            if string[j] != 'a':
                break
            count += 1
        if count > max_count:
            max_count = count

print('a' * (max_count + 1))

