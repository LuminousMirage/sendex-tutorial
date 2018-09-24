##import url library
import urllib.request
##get request to the url
x = urllib.request.urlopen('https://www.google.com')
##reading request, same source code when press ctrl + u on google website
print(x.read())