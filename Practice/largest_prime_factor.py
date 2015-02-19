def sieve(n):
	prime = list(range(2, n))
	is_prime = [True for i in range(2, n)]
	for i in range(len(prime)):
		factor = prime[i]
		if not is_prime[i]:
			continue
		for j in range(i + 1, len(prime)):
			if prime[j] % factor == 0:
				is_prime[j] = False

	i = len(prime) - 1
	while True:
		if is_prime[i]:
			return prime[i]
		i -= 1

def is_prime(n):
	for i in range(2, int(n ** 0.5)  + 1):
		if n % i == 0:
			return False
	return True

def work(n):
	for i in range(int(n ** 0.5), 1, -1):
		if n % i == 0:
			if is_prime(i):
				print(i)
				break

print(work(600851475143))


