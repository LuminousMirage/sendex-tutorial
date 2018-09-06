##list of numbers and strings
x = [5,6,2,1,6,7,2,2,6,7,2]
y = ['Janet','Jessy','Kelly','Alice','Joe','Bob']
##adding 2 into the last of the list
x.append(2)
print(x)
##inserting 99 in the index 2 position
x.insert(5,99)
print(x)
##remove number 1 in the list
x.remove(1)
print(x)
##remove index 0
x.remove(x[0])
print(x)
##print element index 0 and 7
print(x[0:7])
##print last element index
print(x[-1])
##search the position of index of the number 99
print('Current list elements: (Search the position of index of the number 99)')
print(x)
print(x.index(99))
##search how many 2 were in the list
print('Current list elements: (Search how many 2 were in the list)')
print(x)
print(x.count(2))
##sort the list in order
x.sort()
print('\nCurrent numbers on the list: ')
print(x)
print('\n')
##sort the name on list in alphabet order
y.sort()
print(y)
##reverse the name on list
y.reverse()
print(y)