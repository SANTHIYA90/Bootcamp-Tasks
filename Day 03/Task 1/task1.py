class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
            print(f"{self.name} is barking")
            
    def sleep(self):
                print(f"{self.name}is sleeping")
dog1 = dog("jacky",5)
dog1.bark()
dog1.sleep()