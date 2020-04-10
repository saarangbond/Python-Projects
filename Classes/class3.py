class dog_factory:
	pass
	
dg1 = dog_factory()
dg2 = dog_factory()

dg1.food = "raw meat"
dg1.breed = "greyhound"

dg2.food = "bones"
dg2.breed = "labrador"
dg2.color = "black"

print(dg1.food)
print(dg1.breed)
print()
print(dg2.food)
print(dg2.breed)
print(dg2.color)