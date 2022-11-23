#Decorators Pattern

def my_dec(func):
    def wrap_dec(*args,**kwargs):
        print("*****")
        func(*args,**kwargs)
        print("*****")

    return wrap_dec

@my_dec
def hello(greet, name="jhaycee"):
    print(greet, name)

hello("hii")