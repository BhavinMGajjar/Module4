
list1= ['This','is','a','list']
file = open("sample.txt", "w+")

for i in list1:
    file.write('%s\n' %i)

print("Written list successfully")



