

file1 = open("sample.txt", "r")
file2 = open("copied.txt","a")

for i in file1:
    file2.write(i)

print("Copied Successfully")

file1.close()
file2.close()




