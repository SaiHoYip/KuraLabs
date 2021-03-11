class Mammal:
    def walk (self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def Meoew(self):
        print("meow")


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.Meoew()