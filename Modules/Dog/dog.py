class digFactory:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
        
    def list(self):
        print ("The breed of the dog is", self.breed)
        print ("The color of the dog is", self.color)