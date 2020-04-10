class dog_factory:
    skinTexture = "smooth"

    def __init__(self, food, breed, color = "black"):
        self.food = food
        self.breed = breed
        self.color = color
        
    def display(self):
        print(self.food)
        print(self.breed)
        print(self.color)
        print("--------")
        
    def getSkinTexture(self):
        return self.skinTexture
        
dg1 = dog_factory("Raw Meat", "Greyhound", "Grey")
dg2 = dog_factory("Bones", "Labrador")

dog_factory.display(dg1)
dog_factory.display(dg2)

print(dg1.getSkinTexture())
print(dg2.getSkinTexture())
print(dg1.__dict__)

dg2.skinTexture = "rough"
print(dg1.getSkinTexture())
print(dg2.getSkinTexture())
print(dg1.__dict__)