#OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def run(self, kotoba):
        print(kotoba)

player1 = PlayerCharacter("Jhaycee", 29)
player2 = PlayerCharacter("Hoa", 29)
player2.attack = 50
print(player1.name)
print(player2.name)
player1.run
print(player2.attack)