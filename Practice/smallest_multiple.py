N = 20

def get_factors(n):
	factors = list()
	for i in range(1, n):
		if n % i == 0:
			factors.append(i)
	return factors

def gcd(m, n):
	if n == 0:
		return m
	return gcd(n, m % n)

def lcm(m, n):
	return m * n // gcd(m, n)

l = lcm(1, 2)
for i in range(3, N + 1):
	l = lcm(i, l)
print(l)