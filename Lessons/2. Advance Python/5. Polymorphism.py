#pholymorphism
import random


class User:
    def login():
        print("Logged in!")

class Swordie(User):
    def __init__(self, name, dammage):
        self.name = name
        self.dammage = dammage

    def attack(self):
        self.dammage = random.randint(self.dammage - 10, self.dammage)
        print(f"Attack and gives {self.dammage}")

class Archer(User):
    def __init__(self, name, dammage, arrow):
        self.name = name
        self.dammage = dammage
        self.arrow = arrow

    def attack(self):
        get_dammage = random.randint(self.dammage - 10, self.dammage)
        self.arrow -= 1
        print(f"Attack and gives {get_dammage}, arrow remaining: {self.arrow}")


swordie = Swordie("Melodias", 50)
arch = Archer("Hoa", 50, 500)

def char_attack(char):
    char.attack()

char_attack(swordie)