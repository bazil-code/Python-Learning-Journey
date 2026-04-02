# Polymorphism means "Many Forms". 

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof Woof!"
    
class Tiger:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Roar Roar!"
    
for pet in [Dog("Oreo"), Tiger("Sheru")]:
    print(pet.speak())