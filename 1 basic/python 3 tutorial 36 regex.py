'''
Identifiers

\d	any number
\D	anything but a number
\s	space
\S	anything but a space
\w	any character
\W	anything but a character
.	any character, except for a newline
\b	the whitespace around words
\.	a period

Modifiers

{1,3}	for digits, you expect 1-3 counts of digits, or "places"
+		match 1 or more
?		match 0 or 1 repetitions
*		match 0 or MORE repetitions
$		match the end of a string
^		match the start of a string
|		matches either/or ex: x|y = will match either x or y
[]		range or "variance" ex: [1-5a-zA-Z]
{x}		expecting "x" amount
{x,y}	expect to see this x-y amounts of the precedng code

White space characters

\n		new line
\s		space
\t		tab
\e		escape
\f		form feed
\r		return

Don't forget

. + * ? [ ] $ ^ ( ) {} | \

'''

##import regular expression
import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old. Edward is 97, and his grandfather, Oscar is 102
'''

##find all digits that is length 1 to 3
ages = re.findall(r'\d{1,3}',exampleString)
##find words that start with at least 1 capital letter then 0 or more letter and stop when it reach a space, coma, etc 
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

##put them in dictionary correspondingly
ageDict = {}
x = 0
##assign the names relate to age
for eachName in names:
	ageDict[eachName] = ages[x]
	x += 1

print(ageDict)

