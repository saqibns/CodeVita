import random
def digit(num, n):
	chunk = num % (10 ** n)
	return chunk // 10 ** (n - 1)

# print(digit(3221, 1))
# print(digit(3221, 2))
# print(digit(3221, 3))
# print(digit(3221, 4))
# print(digit(3221, 5))

bucket = dict()
for i in range(10):
	bucket[i] = list()

a = [10, 3221, 1, 10, 9680, 103, 10, 211]
a = [1, 2, 3, 4, 5, 7, 8, 9]
random.shuffle(a)
print(a)
print()
idx = 1
for i in range(4):
	for j in a:
		dig = digit(j, idx)
		bucket[dig].append(j)
	print(bucket)
	z = 0
	for j in range(10):
		while len(bucket[j]) > 0:
			a[z] = bucket[j].pop()
			z += 1
	print(a)
	print()
	idx += 1
print(a)


