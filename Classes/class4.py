class dog_factory:
    def __init__(self, food, breed, color = "black"):
        self.food = food
        self.breed = breed
        self.color = color
        
dg1 = dog_factory("Raw Meat", "Greyhound", "Grey")
dg2 = dog_factory("Bones", "Labrador")

print(dg1.food)
print(dg1.breed)
print(dg1.color)
print()
print(dg2.food)
print(dg2.breed)
print(dg2.color)