class Animal:
    def __init__(self):
        self.num_eyes = 2
     
    def breathe(self):
        print("Hey")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("I breathe through gills")

    
    def swim(self):
        print("I can Swim")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)