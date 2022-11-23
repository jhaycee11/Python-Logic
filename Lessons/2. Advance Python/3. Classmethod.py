#classmethod
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self, name, age):
        #if self.membership:        can use this or below
        if PlayerCharacter.membership:
            self.name = name
            self.age = age


    def shout(self):
        #PlayerCharacter.name cannot be used coz its not an object attr
        print(f"my name is {self.name}!!")

    #parang class object attribute. kahit di
    #instantiate pwede magamit outside the class or func
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    """@staticmethod
    def adding_things2(num1, num2):
        return num1 + num2"""

print(PlayerCharacter.adding_things(2,3))