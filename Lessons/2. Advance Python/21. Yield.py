#Yield vs Return

def generator_function(num):
    for i in range(num):
        yield i*2

def print_gen():
    for i in generator_function(10000):
        print(i)

#for item in generator_function(1000):
#    print(item)


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)

    return result



print(make_list(100))

print_gen()