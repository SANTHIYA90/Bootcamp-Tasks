class Animal:
    def speak(self):
        raise NotImplementedError("subclass is must implement this abstract method")
    
class Dog(Animal):
    def speak(self):
        return "Dog is barking"

class Cat(Animal):
    def speak(self):
        return "Cat is meowing"
    
def animal_speak(animal):
    print(animal.speak())
       
dog = Dog()
cat = Cat()

animal_speak(dog)
animal_speak(cat)





