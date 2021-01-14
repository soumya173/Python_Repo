# Open a file in "w" mode
file = open("sample.txt", "w")
# file = open("sample.txt", "r")

line = "This is a sample line"
file.write(line)

# content = file.read()
# print(content)

# Close the file
file.close()