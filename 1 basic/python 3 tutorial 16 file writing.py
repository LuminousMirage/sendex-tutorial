text = 'Sample text to Save\nNew line"
##open a file, if it doesn't exist, create one instead. w stands for write to a file, everything in the file will be clear
##save to a path two directory infront - '../../exampleFile.txt'
##save to c - 'c:/exampleFile.txt'
saveFile = open('exampleFile.txt','w')
##save the content into the file
saveFile.write(text)
##closing the file
saveFile.close()