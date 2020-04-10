##exception handling
try:
	fstream = open("tes21.txt", 'r')
except:
	print("file not found")
	exit()

for line in fstream:
	if not line.startswith("From"):
		continue
	else:
		print(line.rstrip())