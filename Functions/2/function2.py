def myfunc(**kwargs):
	for k,v, in kwargs.items():
		print (k, v)
		
myfunc(wish = "birthday", happy = "new-year")