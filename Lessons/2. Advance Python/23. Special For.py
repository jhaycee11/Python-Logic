def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator, end=" -> ")
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3])