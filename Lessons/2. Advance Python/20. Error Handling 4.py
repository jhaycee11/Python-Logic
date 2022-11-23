#Error Handling

while True:
    try:
        age = int(input("What is your age? "))
        10/age
        raise ValueError("Hey cut it out") #raise your own error

    except ZeroDivisionError:
        print("Please input higher than 0")
        break
    else:
        print("thank You")
        break
    finally:    #for log purpose.
        print("ok, im done!")
        break
    print("can you hear me?")