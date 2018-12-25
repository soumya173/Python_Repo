# Exception Handling
def devide(no1, no2):
	return no1 / no2


try:
	print(devide(4, 0))
except Exception as e:
	print("Exception")
	print(e)

# no1 = int(input("Enter no1: "))
# no2 = int(input("Enter no2: "))
# no1 = 78
# no2 = 5

# print(devide(no1, no2))

arr = [5,6,7,8,5,4,3,3,4]

for x in range(len(arr)):
	print(arr[x])