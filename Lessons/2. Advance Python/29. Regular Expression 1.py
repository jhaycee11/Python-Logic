import re

"""1st
string = "search inside of this text please"

a = re.search("thiS", string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())"""

pattern = re.compile("this")



#2nd
"""#fullmatch sample *didnt return value when not exact match
pattern = re.compile("search this inside of this text please")"""
"""#match sample
pattern = re.compile("search this inside of this text")"""


string = "search this inside of this text please"

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(b)
