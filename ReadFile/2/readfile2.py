
try:
	fstream = open("test1.txt", 'r')
except:
    print("file not found")

myList = list()

for line in fstream:
    if not line.startswith('From'):
        continue
    else:
        myList.append(line.rstrip())
        
print(myList)

for item in myList:
    print(item)