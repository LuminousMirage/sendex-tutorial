from tkinter import *

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("GUI")
		self.pack(fill = BOTH, expand = 1)
##adding event handling in this button
		quitButton = Button(self, text = "Quit", command = self.client_exit)
		quitButton.place(x = 0, y = 0)
		
##function for exit purpose
	def client_exit(self):
		exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()