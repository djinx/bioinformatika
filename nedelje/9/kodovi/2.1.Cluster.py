class Cluster:
	def __init__(self, elements, age):
		self.elements = elements
		self.age = age
		self.left = None
		self.right = None

	def __str__(self):
		return ("%\%%s : %\%%d" %\%% (self.elements, self.age))

	def add_left(self, L):
		self.left = L

	def add_right(self, R):
		self.right = R