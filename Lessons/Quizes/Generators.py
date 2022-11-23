#generators
def fibonocci(num):
    a = 0
    b = 1
    for _ in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

#for x in fibonocci(1000):
#    print(x)


#list
def fibonocci2(num):
    a = 0
    b = 1
    result = []
    for _ in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fibonocci2(100))