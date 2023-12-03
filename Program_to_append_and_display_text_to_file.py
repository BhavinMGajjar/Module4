file = open("sample.txt", "a")
file.write("This is an appended text to this file")
file.close


file = open("sample.txt", "r")
print(file.read())

