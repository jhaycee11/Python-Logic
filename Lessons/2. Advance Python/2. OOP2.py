#OOP
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self, name, age):
        #if self.membership:        can use this or below
        if PlayerCharacter.membership:
            self.name = name
            self.age = age


    def shout(self, hello):
        #PlayerCharacter.name cannot be used coz its not an object attr
        print(f"my name is {self.name}!!")
        print(f"{hello}")

player1 = PlayerCharacter("Jhaycee", 29)
player2 = PlayerCharacter("Hoa", 29)
player2.attack = 50

player1.shout("Hello")
player2.shout("Hi")