def square(no):
	return no**2

newLis = [12, 13, 66, 3]

# Using map
sqLis1 = list(map(square, newLis))

# Using Lambda function
# Lambda function is also known as Annonymus function, since it doesn't have any name
sqLis2 = list(map(lambda x: x**2, newLis))

print(sqLis1)
print(sqLis2)