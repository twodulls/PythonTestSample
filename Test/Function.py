"""
def sum(a,b):
	result = a+b
	return result
a=sum(3,4)
print(a)

def sum(a,b):
	print("%d, %d의 합은 %d입니다." %(a,b,a+b))
a=sum(3,4)
print(a)


def sum_many(*args):
	sum=0
	for i in args:
		sum = sum+i
	return sum

result=sum_many(1,2,3)
print(result)


def say_myself(name, old, man=True):
	print("My name is %s" % name)
	print("My age is %d" % old)
	if man:
		print("Man")
	else:
		print("Woman")

say_myself("Test", 27)


a=1
def vartest(a):
	a=a+1
	return a

a= vartest(a)
print(a)
"""

a=1
def vartest():
	global a
	a=a+1

vartest()
print(a)

vartest()
print(a)