fstream = open("test1.txt", 'r')
for line in fstream:
	if not line.startswith('From'):
		continue
	else:
		print (line.rstrip())
		#print line