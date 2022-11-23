#comprehension set, dict
#list, set, dictionary
""" Set. No Duplicate, not sorted
my_list = {char for char in "hello"}
my_list1 = {x for x in range(100)}
my_list2 = {x ** 2 for x in range(100)}
my_list3 = {x ** 2 for x in range(100) if x % 2 == 0}
print(my_list2)"""

simple_dict = {
    "a" : 1,
    "b" : 2,
}

#my_dict = {k:v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
my_dict = {v:v * 2 for v in [1,2,3]}



print(my_dict)