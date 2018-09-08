import csv
##open the file and load data from exampleData.csv
with open('exampleData.csv') as csvfile:
##assign the data into readCSV with delimiter seperate with ,
	readCSV = csv.reader(csvfile, delimiter = ',')
	print(readCSV)
##declare empty string for dates and colors
	dates = []
	colors = []
##loop every row
	for row in readCSV:
		print('\n', row)
		print(row[0])
		print(row[0],row[1])
##assign color and date
		date = row[0]
		color = row[3]
##adding the data into the empty string
		dates.append(date)
		colors.append(color)

	print('\n', dates)
	print(colors)
##let user to find out what date is it when they type in color
	whatColor = input('What color do you wish the date for?:')
	colordex = colors.index(whatColor)
##load the corresponding date with the search of the color
	theDate = dates[colordex]
	print('The date of',whatColor,'is:',theDate)