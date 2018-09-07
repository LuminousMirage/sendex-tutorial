##lists within lists
x = [[5,6],[6,7],[7,2],[2,5]]
y = [
	[[5,7],[6,6]],
	[[6,6],[7,8]],
	[7,2],
	[2,5]
	]
##print all index
print(x)
##print index 0
print(x[0])
##print index 0 from second element
print(x[1][1])
##print index 0 from second group within first elements
print(y[1][0][1])