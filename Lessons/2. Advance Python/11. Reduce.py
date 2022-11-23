#reduce
from functools import reduce

my_nums = [1, 2, 3]

def multiply_by2(item):
    return item.upper()

def check_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item



print(reduce(accumulator, my_nums,0))