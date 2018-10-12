##combine two of the standard library modules previously and use them the parse a website
import urllib.request
import urllib.parse
import re

##establish the connection and request with the target website
url = 'http://pythonprogramming.net'
values = {'q':'basics'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

##lets say I want to parse everything in between the paragraphy tag in the website ex: <p>something here</p>
##.	any character except for a newline
##*	0 or more repetitions
##?	0 or 1 repetitions
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
	print(eachP)