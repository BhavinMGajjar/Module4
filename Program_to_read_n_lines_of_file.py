num = int(input("Enter number of lines to read"))

file = open("sample.txt", "r")
print(file.readlines()[0:num])

