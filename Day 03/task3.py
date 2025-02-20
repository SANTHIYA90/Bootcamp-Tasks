class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"my dog {self.name} is barking")    

    def sleep(self):
        print(f"my dog {self.name} is sleep ")    
    
class Puppy(dog):
    def play(self):
        print(f"my dog {self.name} is playing")

puppys = Puppy("roy",12)
puppys.bark()
puppys.sleep()
puppys.play()

