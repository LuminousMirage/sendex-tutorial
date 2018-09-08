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
		colordex = colors.index(whatColor)
		theDate = dates[colordex]
		print('The date of',whatColor,'is:',theDate)
##in python 2.7 will use the following instead
##except Exception, e:
##whatever the exception to the variable of e
	except Exception as e:
		print(e)
	print('continuing')