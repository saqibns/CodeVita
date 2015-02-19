class Dog:
	def __init__(self):
		pass
	def walk(self):
		print("I walk on four legs")
	def bark(self):
		print("Woof! Woof!")

class Duck:
	def __init__(self):
		pass
	def walk(self):
		print("I walk on two legs")
	def quack(self):
		print("Quack! Quick!")

def spam(integer):

	a = 2 * integer
	z = str(a)
	l = len(z)
	if is_even(l):
		print("Yes!")
	else:
		print("No!")

def is_even(n):
	return n % 2 == 0

spam(2)
spam('2')
