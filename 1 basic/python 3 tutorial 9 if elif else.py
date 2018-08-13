x = 5
y = 10
z = 22

##will not print
if x > y:
	print('x is bigger than y')

##will print x is less than z
elif x < z:
	print('x is less than z')

##this is right statement but it will not print
elif 5 > 2:
	print('5 is bigger than 2')

##will not print
else:
	print('this will print when if and elif(s) not ran')