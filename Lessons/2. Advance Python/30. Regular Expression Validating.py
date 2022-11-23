import re

#Username, Email, Password validation

pattern = re.compile(r"(^[a-zA-z0-9_.+-]+@[a-zA-z0-9_.+-]+\.[[a-zA-z0-9_.]+$)")
string = "jhaycee@gmail.com"
a = pattern.search(string)
#print(a)


# at least 8 char long
# contain any sort letters, numbers $%#@!
pattern2 = re.compile(r"[a-zA-Z&0-9%$#@!]{7,}\d")
password = "boboka@8"
check = pattern2.fullmatch(password)
print(check)