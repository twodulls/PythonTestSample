'''
class Service:
	secret="Test is easy"
	def sum(self, a, b):
		result = a+b
		print("%s + %s = %s" %(a,b,result))

pey = Service()
pey.sum(1,1)

Service.sum(pey,1,1)
'''

class Robot:
	def __init__(self, name='dummy'):
		self.nLegs=2
		self.nArms=2
		self.name = name

asimo = Robot()
print(asimo.name)

