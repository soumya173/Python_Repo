from tkinter import filedialog, messagebox
from tkinter import *
import tkinter.scrolledtext as ScrolledText
import os
import logging
import datetime
# from ScrolledText import *

LOGGING = True

class Editor(object):
	"""docstring for MyUi"""
	def __init__(self, rootone):

		curDateTime = datetime.datetime.now().strftime("%d-%B-%Y_%I:%M%p")
		logging.basicConfig(filename='logs/{}.log' % curDateTime, filemode='w', format='%(asctime)s - %(message)s')
		logging.info('Admin logged in')

		rootone.state("zoomed")
		frame = Frame(rootone)
		frame.pack()

		self.config_menu(rootone)
		self.bind_keyboard_shortcuts(rootone)

		self.topFrame = Frame(rootone)
		self.topFrame.pack(fill="both", expand="yes")
		self.textBox = ScrolledText.ScrolledText(master=self.topFrame, wrap="word", bg='beige', padx=20, pady=5)

		self.textBox.focus_set()
		self.textBox.pack(fil="both", expand='yes')

		# self.textBox.bind('<KeyPress>', self.highlightWords)

	def config_menu(self, rootone):
		self.mainMenu = Menu(rootone)
		rootone.config(menu=self.mainMenu)

		# File Menu
		self.fileSubMenu = Menu(self.mainMenu, tearoff=0)
		self.mainMenu.add_cascade(label="File", menu=self.fileSubMenu)

		self.fileSubMenu.add_command(label="New", accelerator="Ctrl+N", command=self.createNewFile)
		self.fileSubMenu.add_command(label="Open", accelerator="Ctrl+O", command=self.openFile)
		self.fileSubMenu.add_command(label="Save As", accelerator="Ctrl+S", command=self.saveAsContents)
		self.fileSubMenu.add_separator()
		self.fileSubMenu.add_command(label="Quit", accelerator="Ctrl+Q", command=self.quitApp)

		# Edit Menu
		self.editSubMenu = Menu(self.mainMenu, tearoff=0)
		self.mainMenu.add_cascade(label="Edit", menu=self.editSubMenu)

		self.editSubMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undoOperation)
		self.editSubMenu.add_command(label="Redo", accelerator="Ctrl+Shift+Z", command=self.redoOperation)
		self.editSubMenu.add_command(label="Select All", accelerator="Ctrl+A", command=self.selectAllOperation)
		self.editSubMenu.add_command(label="Deselect All", accelerator="Ctrl+Shift+A", command=self.deselectAllOperation)
		self.editSubMenu.add_separator()
		self.editSubMenu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cutOperation)
		self.editSubMenu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copyOperation)
		self.editSubMenu.add_command(label="Paste", accelerator="Ctrl+V", command=self.pasteOperation)

	def bind_keyboard_shortcuts(self, rootone):
		# File menu events
		rootone.bind("<Control-n>", self.createNewFile)
		rootone.bind("<Control-N>", self.createNewFile)
		rootone.bind("<Control-o>", self.openFile)
		rootone.bind("<Control-O>", self.openFile)
		rootone.bind("<Control-s>", self.saveAsContents)
		rootone.bind("<Control-S>", self.saveAsContents)
		rootone.bind("<Control-q>", self.quitApp)
		rootone.bind("<Control-Q>", self.quitApp)

		# Edit menu events
		rootone.bind("<Control-z>", self.undoOperation)
		rootone.bind("<Control-Z>", self.undoOperation)
		rootone.bind("<Control-Shift-z>", self.redoOperation)
		rootone.bind("<Control-Shift-Z>", self.redoOperation)
		rootone.bind("<Control-a>", self.selectAllOperation)
		rootone.bind("<Control-A>", self.selectAllOperation)
		rootone.bind("<Control-Shift-KeyPress-a>", self.deselectAllOperation)
		rootone.bind("<Control-Shift-KeyPress-A>", self.deselectAllOperation)


	def selectAllOperation(self, event=None):
		# self.textBox.tag_add('sel', '1.0', 'end')
		numLines = len(self.textBox.get("1.0", "end").split("\n"))
		for i in range(1, numLines):
			# print(i)
			self.textBox.tag_add('sel', '{}.0'.format(i), '{}.end'.format(i))

	def deselectAllOperation(self, event=None):
		self.textBox.tag_remove('sel', '1.0', 'end')

	def undoOperation(self, event=None):
		self.textBox.event_generate("<<Undo>>")

	def redoOperation(self, event=None):
		self.textBox.event_generate("<<Redo>>")

	def cutOperation(self, event=None):
		self.textBox.event_generate("<<Cut>>")

	def copyOperation(self, event=None):
		self.textBox.event_generate("<<Copy>>")

	def pasteOperation(self, event=None):
		self.textBox.event_generate("<<Paste>>")

	def createNewFile(self, event=None):
		textBoxContents = self.textBox.get("1.0", "end-1c")
		if len(textBoxContents) > 1:
			response = messagebox.askyesno("Python","Would you like to save the data?")

			if response == True:
				self.saveAsContents()

			self.textBox.delete("1.0", END)

	def openFile(self, event=None):
		file = filedialog.askopenfile(mode="rb", title="Select File", defaultextension=".txt", filetypes=[("All Types", ".*")])

		if file != None:
			fileContents = file.read()
			self.textBox.delete("1.0", END)
			self.textBox.insert("1.0", fileContents)
			file.close()

	def saveAsContents(self, event=None):
		textBoxContents = self.textBox.get("1.0", "end-1c")
		file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")

		if file != None:
			file.write(textBoxContents)
			file.close()

	def highlightWords(self, event):
		tags = ["Soumya", "Jerry"]
		textBoxContents = self.textBox.get("1.0", "end-1c")
		words = textBoxContents.split(" ")
		# lastWord = textBoxContents.split(" ")

		# print(words[-1])
		for word in words:
			word_len = len(word)
			end_ind = self.textBox.index('end')
			begin_ind = "%s-%sc" % (end_ind, word_len)
			if word in tags:
				self.textBox.tag_add(word, begin_ind, end_ind)
				self.textBox.tag_config(word, foreground="green", background="black")
			else:
				# begin_ind = begin_ind + "-1c"
				self.textBox.tag_remove(word, begin_ind, end_ind)
				self.textBox.tag_config(word, foreground="black", background="beige")

	def quitApp(self, event=None):
		root.destroy()
		os._exit(0)

root = Tk(className="Text Editor")
b = Editor(root)
root.mainloop()