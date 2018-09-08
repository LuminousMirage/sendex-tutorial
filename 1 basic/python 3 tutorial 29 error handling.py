##tutorial 28 reading csv.py will be using for the example of error handling
import csv

with open('exampleData.csv') as csvfile:

	readCSV = csv.reader(csvfile, delimiter = ',')
	print(readCSV)

	dates = []
	colors = []

	for row in readCSV:
		print('\n', row)
		print(row[0])
		print(row[0],row[1])

		date = row[0]
		color = row[3]

		dates.append(date)
		colors.append(color)

	print('\n', dates)
	print(colors)
##try this block of code, handle the errors
	try:
		whatColor = input('What color do you wish the date for?:')
##adding constraints
		if whatColor in colors:
			colordex = colors.index(whatColor)
			theDate = dates[colordex]
			print('The date of',whatColor,'is:',theDate)
		else:
			print('Color not found or it is not a color, please enter another color!')
##except Exception, e: - used in python 2.7 instead
##except NameError as e: - specify a variable that does not exist
##whatever the exception to the variable of e
	except Exception as e:
		print(e)
	print('continuing')