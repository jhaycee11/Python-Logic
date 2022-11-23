#multiple inheritance
class User:
    def sign_in():
        print("Logged in!")

class Swordie(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Shaman(User):
    def __init__(self, name, talisman):
        self.name = name
        self.talisman = talisman

class Extreme(Swordie, Shaman):
    def __init__(self, name, power, talisman):
        Swordie.__init__(self, name, power)
        Shaman.__init__(self, name, talisman)

    def talisman(self):
        print(f"{self.talisman}") 

extreme = Extreme("JC", 500, 50)
print(extreme.talisman)