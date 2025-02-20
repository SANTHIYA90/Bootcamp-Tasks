class dog:
    def bark(self):
        print(f"dog is barking")

    def sleep(self):
        print(f"dog is sleeping")

class cat:
    def meow(self):
        print(f"cat is meowing")

    def purr(self):
        print(f"cat is purring") 

class hybrid(dog,cat): 
    def show_traits(self):
        print(f"i have both dog and cat") 

dogat = hybrid()
dogat.bark()
dogat.meow()
dogat.sleep()
dogat.purr()                       