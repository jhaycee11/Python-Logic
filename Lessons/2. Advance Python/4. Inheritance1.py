#Iheritance

class User:
    def sign_in(self):
        print("Logged in")

class Swordie(User):
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def attack(self):
        print(f"attacking with {self.skill}")

class Archer(User):
    def __init__(self, name, skill, arrow):
        self.name = name
        self.skill = skill
        self.arrow = arrow

    def attack(self):
        print(f"attacking with {self.skill} arrow left: {self.arrow}")

swordie = Swordie("Meliodas", "darkness")
archer = Archer("Hoa", "Starfall", 500)


swordie.sign_in()
swordie.attack()
archer.attack()