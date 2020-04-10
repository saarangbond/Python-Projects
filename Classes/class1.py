class test:
	my_sum = 200 ##class variable
	
	def __init__(self):         ##self is like a pointer
		self.my_sum += 100      ##__init__ is a constructor, my_sum referenced as a local variable
		
	def get_sum(self):
		print (self.my_sum)
		
obj1 = test()     ##Obj1 is an instance variable
obj1.get_sum()