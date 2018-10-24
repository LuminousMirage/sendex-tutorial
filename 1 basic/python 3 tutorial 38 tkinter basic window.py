##import everting from tkinter
from tkinter import *
##create a window and makeing a frame
class Window(Frame):
##this is the parent wiget our main window
	def __init__(self, master = None):
##referencing the initial of the frame class in the library
		Frame.__init__(self, master)
##calling the master widget in main window
		self.master = master
##root window
root = Tk()
##application within that the frame is rooted, create of an instance
app = Window(root)
##initialize and generate the window, #mainloop
root.mainloop()