#Polymorphism
class Pet:
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())
            

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} walk around"

class Cat1(Cat):
    ...

class Cat2(Cat):
    ...

class Cat3(Cat):
    ...


"""
my_cats = [Cat1("Cat1", 50), Cat2("Cat2", 29), Cat3("Cat3", 20)]

my_pets = Pet(my_cats)

my_pets.walk()"""