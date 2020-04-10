
total = 0

##variable number of arguments
def sum(*args):
	global total
	for i in args:
		total += i
	print(total)

sum(10, 30, 40, 70, 7)
	