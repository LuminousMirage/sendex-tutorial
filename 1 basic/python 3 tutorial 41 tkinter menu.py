from tkinter import *

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("GUI")
		self.pack(fill = BOTH, expand = 1)
##		quitButton = Button(self, text = "Quit", command = self.client_exit)
##		quitButton.place(x = 0, y = 0)
		
##creating a menu instance, menu of the main window
		menu = Menu(self.master)
##define the instance of the menu
		self.master.config(menu = menu)
		
##create the file object
		file = Menu(menu)
##adding command in the menu option, call it exit. Also, the command runs on event is client_exit		
		file.add_command(label = 'Exit', command = self.client_exit)
##adding 'file' to the menu		
		menu.add_cascade(label = 'File', menu = file)
		
##create the edit object
		edit = Menu(menu)
##adding command in the menu option, call it undo.
		edit.add_command(label = 'Undo')
##adding 'edit' to the menu	
		menu.add_cascade(label = 'Edit', menu = edit)
		
	def client_exit(self):
		exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()