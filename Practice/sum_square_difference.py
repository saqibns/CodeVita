N = 100
s1 = 0
s2 = 0
for i in range(N + 1):
	s1 += i
	s2 += i * i
print(s1 * s1 - s2)
