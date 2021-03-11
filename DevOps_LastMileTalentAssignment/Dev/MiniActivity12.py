class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hello my name is {self.name}")
Tom = Person("Tommy G")
print(Tom.name)
Tom.talk()

