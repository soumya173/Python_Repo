from tkinter import *
import tkinter.messagebox

# def printSomething():
# 	print("You clicked me.")

# def saveSomthing():
# 	print("You Saved Me.")

def showInfo():
	tkinter.messagebox.showinfo("INFO Title", "This is the body of the INFO")

def showError():
	tkinter.messagebox.showerror("ERROR Title", "This is the body of the ERROR")

def askQuestion():
	response = tkinter.messagebox.askquestion("Question Title", "Can you ask a question?")

	if response == 'yes':
		print("Your response is Yes")
	else:
		print("Your response is No")

# button1 = Button(root, text="Click Me", command=printSomething)
# button1.pack()

# class MyUi(object):
# 	"""docstring for MyUi"""
# 	def __init__(self, rootone):
# 		frame = Frame(rootone)
# 		frame.pack()

# 		self.printButton = Button(frame, text="Click Me", command=self.printSomeOtherText)
# 		self.printButton.pack()

# 		self.quitButton = Button(frame, text="Quit", command=frame.quit)
# 		self.quitButton.pack(side=LEFT)

# 	def printSomeOtherText(self):
# 		print("You Clicked Me!")

# root = Tk()

# b = MyUi(root)

root = Tk()

# myMenu = Menu(root)
# root.config(menu=myMenu)

# subMenu = Menu(myMenu)
# myMenu.add_cascade(label="File", menu=subMenu)

# subMenu.add_command(label="Project", command=printSomething)
# subMenu.add_command(label="Save", command=saveSomthing)

# subMenu.add_separator()

# subMenu.add_command(label="Exit", command=root.quit)

# newSubMenu = Menu(myMenu)
# myMenu.add_cascade(label="Edit", menu=newSubMenu)

# newSubMenu.add_command(label="Undo", command=printSomething)

# toolbar = Frame(root, bg="Red")
# insertButton = Button(toolbar, text="Insert File", command=printSomething)
# insertButton.pack(side=LEFT, padx=2, pady=3)

# printButton = Button(toolbar, text="Print Something", command=printSomething)
# printButton.pack(side=LEFT, padx=2, pady=3)

# toolbar.pack(side=TOP, fill=X)

infoButton = Button(root, text="INFO", command=showInfo)
errorButton = Button(root, text="ERROR", command=showError)
askButton = Button(root, text="QUESTION", command=askQuestion)

infoButton.pack()
errorButton.pack()
askButton.pack()

# status = Label(root, text="This is the status bar", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)

root.mainloop()








