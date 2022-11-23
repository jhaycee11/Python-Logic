#Lambda expressions
from functools import reduce

my_nums = [1, 2, 3]

"""lamba and function

in function:[ def multipy_two(item): ]
in lambda:[ lambda item: ]
in function:[ return item * 2 ]
in lambda:[ item * 2 ]

"""

print(list(map(lambda item: item * 2, my_nums)))
print(list(filter(lambda item: item % 2 != 0, my_nums)))
print(reduce(lambda acc, item: acc + item, my_nums))