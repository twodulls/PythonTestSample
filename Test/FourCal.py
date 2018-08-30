class FourCal:
	def setData(self, first, second):
		self.first = first
		self.second = second
	def sum(self):
		result = self.first + self.second
		return result
	def mul(self):
		result = self.first * self.second
		return result
	def sub(self):
		result = self.first - self.second
		return result
	def div(self):
		result = self.first / self.second
		return result

a = FourCal()
b = FourCal()

a.setData(4,2)
b.setData(3,7)

print(a.sum())

