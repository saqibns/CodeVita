def quicksort(a):

	l = len(a)
	if l <= 1:
		return a
	else:
		p = a[l - 1]
		less = list()
		great = list()
		i = 0
		while i < l - 1:
			if a[i] <= p:
				less.append(a[i])
			else:
				great.append(a[i])
			i += 1

		return quicksort(less) + [p] + quicksort(great)

print(quicksort([3, 4, 7, 1, 0, 8, 8, 3, 6, 12, 1]))