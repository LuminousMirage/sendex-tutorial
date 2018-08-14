x = 6
y = 6

def example1():
##this will result in error since it is not a global var yet
##	x += 5
##declare global var x
	global x
	
	print(x)
	x += 5
	print(x)
	
def example2():
##other ways of not declare global var
	globx = y
	
	print(globx)
	globx += 5
	print(globx)
	
	return globx

example1()

##print example 2 result
y = example2()
print(y)