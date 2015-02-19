def hoare_partition(a, p, r):
	x = a[p]
	i = p - 1
	j = r + 1
	while True:
		j = j - 1
		while a[j] <= x:
			j = j - 1
		while a[i] >= x:
			i = i + 1

		if i < j:
			a[i], a[j] = a[j], a[i]
		else:
			return j
a = [13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21]

def quicksort(a, p, r):
	if p < r:
		q = hoare_partition(a, p, r)
		quicksort(a, p, q - 1)
		quicksort(a, q + 1, r)

quicksort(a, 0, len(a) - 1)
print(a)
