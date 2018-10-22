from tkinter import *

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
##new function added
		self.init_window()
##create function init_window
	def init_window(self)
##set the title of the window to GUI
		self.master.title("GUI")
##filling up the window and adjust the dimension
		self.pack(fill = BOTH, expand = 1)
##creating a button instance
		quitButton = Button(self, text = "Quit")
##position of the button place
		quitButton.place(x = 0, y = 0)

root = Tk()
##specify dimension of the window
root.geometry("400x300")
app = Window(root)
root.mainloop()