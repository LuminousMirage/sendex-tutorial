import time, math
##absolute value function
exNun1 = -5
exNun2 = 5
print(abs(exNun1))
##compare if they are same after absolute value method
if abs(exNun1) == exNun2:
	print('The value is same now')

##rounding, minimum and maximum function
exList = [5,2,6,7,8,0]
x = 3.14159
intx = '88'
stringx = 77

##rounding function
print('Nearest rounding:', round(x))
##maximum function
print('maximum value:', max(exList))
##minimum function
print('minimum value:', min(exList))

##round up and down with floor and ceil function
print('Rounding down:', math.floor(x))
print('Rounding up:', math.ceil(x))

##convert into int
print('convert string into int number:', int(intx))
##convert into float
print('convert string into float number:', float(intx))

##convert into string
print('convert int into string:', str(stringx))

##help function - function like a search bar, can use urllib to show info, (type ctrl c to break out)
help()
##can use to show specific part of info, an example to show all info about time
##import time first
##help(time)

