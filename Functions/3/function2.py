
def myfunc(name, school, city):
	print(name)
	print(school)
	print(city)
	
myDict = {"name":"Sharon", "school":"St Judes", "city":"LA"}

myfunc(**myDict)