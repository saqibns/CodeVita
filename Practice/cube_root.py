# Finding the cube root using Newton's Method

def f(x, k):
	return x ** 3 - k

def f_(x, k):
	return 3 * x ** 2

def cube_root(k):
	xi = 1
	xip1 = xi - f(xi, k) / f_(xi, k)
	while abs(xip1 - xi) > 0.001:
		xi = xip1
		xip1 = xi - f(xi, k) / f_(xi, k)

	return xip1
 