class Cat:
    ...
"""   
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Hoa", 24)
cat2 = Cat("Xoai", 100)
cat3 = Cat("Chom", 30)

def get_oldest_cat(*args):
    return max(args)"""

# Output
print(f"The oldest cat is {...} years old.")