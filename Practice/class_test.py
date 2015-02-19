class Animal:
	def __init__(self, height = 1.0 , weight = 10.0, name = 'Animal'):
		self._height = height
		self._weight = weight
		self._name = name

	def get_name(self):
		return self._name

	def get_height(self):
		return self._height

	def get_weight(self):
		return self._weight


a = Animal(97.4, 300.0, 'Volley')
b = Animal()

print(a.get_weight())
print(b.get_weight())
print(b.get_name())
