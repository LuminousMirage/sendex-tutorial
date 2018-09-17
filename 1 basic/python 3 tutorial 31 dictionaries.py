##create a dictionary with keys and values and then print it
exDict = {'Jack':[15, 'blonde'], 'Bob':[22, 'brown'], 'Alice':[12, 'black'], 'Kevin':[17, 'red']}
print(exDict)
##print value when the key is Jack
print(exDict['Jack'])
##add Tim and its value
exDict['Tim'] = 14
print(exDict)
##alter Tim's value
exDict['Tim'] = 15
print(exDict)
##remove Tim from dictionary
del exDict['Tim']
print(exDict)
##print Jack favourite color
print(exDict['Jack'][1])