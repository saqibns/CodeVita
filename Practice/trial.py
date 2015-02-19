x = raw_input()
y = raw_input()

f = dict()
for i in xrange(97, 123):
    f[chr(i)] = 0

for char in x:
    f[char] += 1

for char in y:
    f[char] -= 1

total = 0
for key in f.keys():
    total += abs(f[key])

print total