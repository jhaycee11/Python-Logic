#Apply a function to items of a list with map() in Python

user_names = [
    "LuFFy",
    "Sanji",
    "ZorO",
    "NamI",
    "UsSop",
    "Chopper",
    "Franky",
    "bRook"
]

def make_upper(item):
    return item.upper()
    
print(list(map(make_upper, user_names)))
print(user_names)