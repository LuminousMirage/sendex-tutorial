##pass statement is a null operation, useful in places where your code will eventually go, but has not been written yet
def simple(num1,num2):
	pass

## give num2 a default var of 5
def simple(num1,num2 =5):
	print(num1,num2)

##continue specify things within the parentheses
def basic_window(width,height,font = 'TNR',
				bgc = 'w',scrollbar = True):
	print(width,height,font,bgc)

##change bgc to a, keep others the same
basic_window(500,350,bgc = 'a')
