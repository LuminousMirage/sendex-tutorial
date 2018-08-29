##creation of a class 
class calculator:
##function of addition
	def addition(x,y):
		added = x + y
		return added
##function of subtraction
	def subtraction(x,y):
		sub = x - y
		return(sub)
##function of multiplication
	def multiplication(x,y):
		mult = x * y
		return(mult)
##function of division
	def division(x,y):
		div = x / y
		return(div)
##assign result into var adding
adding = calculator.addition(1,2)
print(adding)
##assign result into var multiply
multiply = calculator.multiplication(3,5)
print(multiply)
##adding the addition and multiplication result
total = adding + multiply
print(total)