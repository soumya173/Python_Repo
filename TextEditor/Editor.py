from tkinter import filedialog, messagebox
from tkinter import *
import tkinter.scrolledtext as ScrolledText
import os
import logging
import datetime

########################################
# Global Configurations
#

# Set LOGGING to True if wana log entries in the log file
LOGGING = True

# Initializing logger object to support logging to file
logger = logging.getLogger("Editor")

class Editor(object):

	############################################
	# parameters: tk root object
	# Description: Initialize parameters and configurations
	#
	def __init__(self, rootone):

		# Setting up log files and configurations
		self.configLogging()

		# Enable zoomed window at startup
		rootone.state("zoomed")
		frame = Frame(rootone)
		frame.pack()

		self.config_menu(rootone)
		self.bind_keyboard_shortcuts(rootone)

		# Text editor with scrollbar
		self.topFrame = Frame(rootone)
		self.topFrame.pack(fill="both", expand="yes")
		self.textBox = ScrolledText.ScrolledText(master=self.topFrame, wrap="word", bg='beige', padx=20, pady=5)

		# On start cursor is placed in the editor
		self.textBox.focus_set()
		self.textBox.pack(fil="both", expand='yes')

	############################################
	# parameters: tk root object
	# Description: Configure menu in the window
	#
	def config_menu(self, rootone):
		logger.debug("Configuring mainMenu")
		self.mainMenu = Menu(rootone)
		rootone.config(menu=self.mainMenu)

		# File Menu
		logger.debug("Configuring fileSubMenu")
		self.fileSubMenu = Menu(self.mainMenu, tearoff=0)
		self.mainMenu.add_cascade(label="File", menu=self.fileSubMenu)

		self.fileSubMenu.add_command(label="New", accelerator="Ctrl+N", command=self.createNewFile)
		self.fileSubMenu.add_command(label="Open", accelerator="Ctrl+O", command=self.openFile)
		self.fileSubMenu.add_command(label="Save As", accelerator="Ctrl+S", command=self.saveAsContents)
		self.fileSubMenu.add_separator()
		self.fileSubMenu.add_command(label="Quit", accelerator="Ctrl+Q", command=self.quitApp)

		# Edit Menu
		logger.debug("Configuring editSubMenu")
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

		logger.debug("Leaving %s:config_menu", self.__class__.__name__)

	############################################
	# parameters: tk root object
	# Description: Binding keyboard shortcuts to action
	#
	def bind_keyboard_shortcuts(self, rootone):
		logger.debug("Binding keyboard shortcuts")

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

		logger.debug("Leaving %s:bind_keyboard_shortcuts", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Selects all text in the editor
	#
	def selectAllOperation(self, event=None):
		logger.debug("Performing select all operation")
		# self.textBox.tag_add('sel', '1.0', 'end')

		numLines = len(self.textBox.get("1.0", "end").split('\n'))
		print(numLines)
		for i in range(1, numLines):
			self.textBox.tag_add('sel', '{}.0'.format(i), '{}.end'.format(i))
			# self.textBox.tag_add('sel', '1.0', '1.end')

		logger.debug("Leaving %s:selectAllOperation", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: deselects all text in the editor
	#
	def deselectAllOperation(self, event=None):
		logger.debug("Performing deselect all operation")
		self.textBox.tag_remove('sel', '1.0', 'end')

		logger.debug("Leaving %s:deselectAllOperation", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Performs undo operation in the editor
	#
	def undoOperation(self, event=None):
		logger.debug("Performing undo operation")
		self.textBox.event_generate("<<Undo>>")

		logger.debug("Leaving %s:undoOperation", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Performs redo operation in the editor
	#
	def redoOperation(self, event=None):
		logger.debug("Performing redo operation")
		self.textBox.event_generate("<<Redo>>")

		logger.debug("Leaving %s:redoOperation", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Performs cut operation in the editor
	#
	def cutOperation(self, event=None):
		logger.debug("Performing cut operation")
		self.textBox.event_generate("<<Cut>>")

		logger.debug("Leaving %s:cutOperation", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Performs copy operation in the editor
	#
	def copyOperation(self, event=None):
		logger.debug("Performing copy operation")
		self.textBox.event_generate("<<Copy>>")

		logger.debug("Leaving %s:copyOperation", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Performs paste operation in the editor
	#
	def pasteOperation(self, event=None):
		logger.debug("Performing paste operation")
		self.textBox.event_generate("<<Paste>>")

		logger.debug("Leaving %s:pasteOperation", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Gets the current contents of the editor and writes to user defined file
	#
	def createNewFile(self, event=None):
		logger.debug("Creating a new file")
		textBoxContents = self.textBox.get("1.0", "end-1c")

		logger.debug("Cheking for existing contents")
		if len(textBoxContents) > 1:
			logger.debug("Unsaved contents found. Asking to save")
			response = messagebox.askyesno("Python","Would you like to save the data?")

			if response == True:
				logger.debug("Saving contents")
				self.saveAsContents()
			else:
				logger.error("Aborted by User")

			logger.debug("Clearing the contents")
			self.textBox.delete("1.0", END)

			logger.debug("Leaving %s:createNewFile", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Read file contents and loads in the editor
	#
	def openFile(self, event=None):
		logger.debug("Opening file")
		file = filedialog.askopenfile(mode="rb", title="Select File", defaultextension=".txt", filetypes=[("All Types", ".*")])

		if file != None:
			logger.debug("Reading file contents")
			fileContents = file.read()
			self.textBox.delete("1.0", END)

			logger.debug("Loding file contents to the editor")
			self.textBox.insert("1.0", fileContents)
			file.close()

			logger.debug("Closing file handler")
		else:
			logger.critical("Failed to open file")

		logger.debug("Leaving %s:openFile", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Gets the current contents and writes to user defined file
	#
	def saveAsContents(self, event=None):
		logger.debug("Reading editor contents")
		textBoxContents = self.textBox.get("1.0", "end-1c")
		file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")

		if file != None:
			logger.debug("Writing editor contents to file")
			file.write(textBoxContents)
			file.close()

			logger.debug("Closing file handler")
		else:
			logger.critical("Failed to save contents")

		logger.debug("Leaving %s:saveAsContents", self.__class__.__name__)

	############################################
	# parameters: keyboard event
	# Description: Highlight words with different colors in the editor
	#
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
				fgcolor = "green"

				logger.debug("Highlighting from %s to %s in %s color", begin_ind, end_ind, fgcolor)
				self.textBox.tag_add(word, begin_ind, end_ind)
				self.textBox.tag_config(word, foreground=fgcolor, background="black")
			else:
				fgcolor = "black"

				logger.debug("Coloring from %s to %s in %s color", begin_ind, end_ind, fgcolor)
				self.textBox.tag_remove(word, begin_ind, end_ind)
				self.textBox.tag_config(word, foreground=color, background="beige")

		logger.debug("Leaving %s:highlightWords", self.__class__.__name__)

	############################################
	# parameters: keyboard event (optional)
	# Description: Quits the app execution
	#
	def quitApp(self, event=None):
		logger.debug("Quiting Application")
		root.destroy()
		os._exit(0)

	############################################
	# Description: Configure log files and directories to support logging
	#
	def configLogging(self):

		# Do not log if logging is disabled by user
		logger.disabled = (not LOGGING)

		logFileName = ""
		if LOGGING:
			dirPath = "logs"

			# Create log directory if it's not already present
			if not os.path.exists(dirPath):
				os.mkdir(dirPath)

			# date and time of log file creation in file name
			curDateTime = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
			logFileName = "{dirname}/{filename}.log".format(dirname=dirPath,filename=curDateTime)

			# Default log level
			logger.setLevel(logging.DEBUG)

			# Configuring the file handle
			fileHandler = logging.FileHandler(logFileName)

			# All type of logs will be logged in the log file
			fileHandler.setLevel(logging.DEBUG)

			# Configuring the console handle
			consoleHandler = logging.StreamHandler()

			# Only CRITICAL logs will be logged in the console
			consoleHandler.setLevel(logging.CRITICAL)

			# Formating log in file (2019-02-22 16:47:36,065 - DEBUG : Configuring mainMenu)
			logFormatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s")
			fileHandler.setFormatter(logFormatter)
			consoleHandler.setFormatter(logFormatter)

			# Adding configured handlers in logger object
			logger.addHandler(fileHandler)
			logger.addHandler(consoleHandler)

		logger.debug("Leaving %s:configLogging", self.__class__.__name__)


# Initializing top frame and starting Application
root = Tk(className="Text Editor")
b = Editor(root)
root.mainloop()