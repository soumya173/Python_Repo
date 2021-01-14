from tkinter import *
import parser

class Calculator(object):
	"""docstring for Calculator"""
	def __init__(self, rootone):
		self.position = 0
		self.resEntry = Entry(rootone)
		self.resEntry.grid(row=0, columnspan=6, sticky=W+E)

		Button(rootone, text="1", command=lambda : self.printVariable(1)).grid(row=1, column=0)
		Button(rootone, text="2", command=lambda : self.printVariable(2)).grid(row=1, column=1)
		Button(rootone, text="3", command=lambda : self.printVariable(3)).grid(row=1, column=2)

		Button(rootone, text="4", command=lambda : self.printVariable(4)).grid(row=2, column=0)
		Button(rootone, text="5", command=lambda : self.printVariable(5)).grid(row=2, column=1)
		Button(rootone, text="6", command=lambda : self.printVariable(6)).grid(row=2, column=2)

		Button(rootone, text="7", command=lambda : self.printVariable(7)).grid(row=3, column=0)
		Button(rootone, text="8", command=lambda : self.printVariable(8)).grid(row=3, column=1)
		Button(rootone, text="9", command=lambda : self.printVariable(9)).grid(row=3, column=2)

		Button(rootone, text="AC", command=lambda : self.clearAll()).grid(row=4, column=0)
		Button(rootone, text="0", command=lambda : self.printVariable(0)).grid(row=4, column=1)
		Button(rootone, text="=", command=lambda : self.calculate()).grid(row=4, column=2)

		Button(rootone, text="+", command=lambda : self.printOperator("+")).grid(row=1, column=3)
		Button(rootone, text="-", command=lambda : self.printOperator("-")).grid(row=2, column=3)
		Button(rootone, text="*", command=lambda : self.printOperator("*")).grid(row=3, column=3)
		Button(rootone, text="/", command=lambda : self.printOperator("/")).grid(row=4, column=3)

		Button(rootone, text="pi", command=lambda : self.printOperator("*3.14")).grid(row=1, column=4)
		Button(rootone, text="%", command=lambda : self.printOperator("%")).grid(row=2, column=4)
		Button(rootone, text="(", command=lambda : self.printOperator("(")).grid(row=3, column=4)
		Button(rootone, text="exp", command=lambda : self.printOperator("**")).grid(row=4, column=4)

		Button(rootone, text="<-", command=lambda : self.backSpace()).grid(row=1, column=5)
		Button(rootone, text="x!", command=lambda : self.factorial()).grid(row=2, column=5)
		Button(rootone, text=")", command=lambda : self.printOperator(")")).grid(row=3, column=5)
		Button(rootone, text="^2", command=lambda : self.printOperator("**2")).grid(row=4, column=5)

	def printVariable(self, num):
		self.resEntry.insert(self.position, num)
		self.position += 1

	def clearAll(self):
		self.resEntry.delete(0, END)
		# self.position = 0

	def backSpace(self):
		currentString = self.resEntry.get()
		newString = currentString[:-1]

		self.clearAll()
		self.resEntry.insert(0, newString)
		self.position -= 1

	def printOperator(self, operator):
		opLength = len(operator)
		self.resEntry.insert(self.position, operator)

		self.position += opLength

	def calculate(self):
		expression_string = self.resEntry.get()

		try:
			compiledStr = parser.expr(expression_string).compile()
			result = eval(compiledStr)
			self.clearAll()
			self.resEntry.insert(0, result)
		except Exception as e:
			self.clearAll()
			self.resEntry.insert(0, "ERROR!")

	def factorial(self):
		try:
			num = int(self.resEntry.get())

			if num > 69:
				self.clearAll()
				self.resEntry.insert(0, "Limit Exceeded.")
			else:
				fact = 1
				for i in range(1, num+1):
					fact *= i

				self.clearAll()
				self.resEntry.insert(0, fact)
		except Exception as e:
			self.clearAll()
			self.resEntry.insert(0, "ERROR!")

root = Tk()
root.title("My Calculator")

tmp = Calculator(root)

root.mainloop()