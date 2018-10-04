##import url library
import urllib.request
##help parse value to our post
import urllib.parse

##get request to the url
##x = urllib.request.urlopen('https://www.google.com')

##reading request, same source code when press ctrl + u on google website
##print(x.read())

'''

##setting a address
url = 'http://pythonprogramming.net'

##dictionaries with getting data from these valuables
values = {'s':'basic','submit':'search'}

##encoding values the data we want to post in
data = urllib.parse.urlencode(values)

##put data in bytes, encode using utf-8
data = data.encode('utf-8')

##first request the url then the data we want to pass
req = urllib.request.Request(url,data)

##get request to the url
resp = urllib.request.urlopen(req)

##reading request
respData = resp.read()

print(respData)

'''

##attempt to visit google search query, read the result. Otherwise, print the exception in string
try:
	x = x = urllib.request.urlopen('https://www.google.com/search?q=test')
	print(x.read())
except Exception as e:
	print(str(e))
	
try:
	url = 'https://www.google.com/search?q=test'
##headers is the data you sent to the website, contains info of you
	headers = {}
##basically changing and announcing ourselves not python
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
##visit this url and changing default headers to headers User-Agent on the upper code
	req = urllib.request.Request(url,headers = headers)
##get request to the url
	resp = urllib.request.urlopen(req)
##reading request
	respData = resp.read()
##open a file
	saveFile = open('withHeaders.txt','w')
##write the string version of response data
	saveFile.write(str(respData))
	saveFile.close()
except Exception as e:
	print(str(e))
	
	
	