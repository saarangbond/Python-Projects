class dog_factory:
    def __init__(self, food, breed, color = "black"):
        self.food = food
        self.breed = breed
        self.color = color
        
    def display(self):
        print(self.food)
        print(self.breed)
        print(self.color)
        print("--------")
        
dg1 = dog_factory("Raw Meat", "Greyhound", "Grey")
dg2 = dog_factory("Bones", "Labrador")

dg1.display()
dg2.display()
