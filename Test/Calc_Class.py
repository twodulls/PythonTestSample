
class Calculator:
	def __init__(self):
		print("__init__(self)")
		self.result = 0

	def adder(self, num):
		print("adder call")
		self.result += num
		return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
