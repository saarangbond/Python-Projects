fstream = open("test.txt", 'r')
data = fstream.read()
print(data, end = '')

print()
print("Data length", len(data))