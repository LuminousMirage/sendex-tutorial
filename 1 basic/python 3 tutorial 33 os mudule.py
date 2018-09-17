##operation system library can be use for changing path, move directory, etc
import os
import time
##shpw the current working directory
curDir = os.getcwd()
print(curDir)
##create a file called newDir
os.mkdir('newDir')

##add 4 second delay
time.sleep(4)
##rename newDir file name
os.rename('newDir','newDir renamed')

time.sleep(4)
##remove newDir renamed file
os.rmdir('newDir renamed')