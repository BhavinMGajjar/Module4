
list1 = []
file = open("sample.txt", "r")
file1 = file.readlines()

for i in file1:
    list1.append(i.strip())



print(list1)
    

