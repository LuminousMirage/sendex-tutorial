##Python's standard out is buffered (meaning that it collects some of the data "written" to standard out before it writes it to the terminal)
##import the system module, which can use stdin() and stdout(), as well as stderr() and utilize sys.argv()
import sys
##error text, display in red color
sys.stderr.write('This is stderr text\n')
##flush() "flush" the buffer, write everything in the buffer to the terminal
sys.stderr.flush()
##pass messages in blue color
sys.stdout.write('This is stdout text\n')
##sys.argv allow you to pass arguments through to python from the command line
print(sys.argv)

##if more than one argument
if len(sys.argv) > 1:
##print argument one more time
##	print(sys.argv[1])
##print argument float number add 5
	print(float(sys.argv[1]) + 5)
	
##pass the argument into a function
##def main(arg)
##	print(arg)
##print the argument with the function
##	main(sys.argv[1])