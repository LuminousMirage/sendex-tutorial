##tuples, value can not be change, called "immutable". It is iterate faster than python list
##x = 5,6,2,6
##x = (5,6,2,6)

def exampleFunc():
	return 15,6

x,y = exampleFunc()
print(x,y)

##lists, more commonly use
y = [5,6,2,6]
##print the whole list
print(y)
##print its index value
print(y[0],y[1])