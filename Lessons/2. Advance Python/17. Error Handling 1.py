#Error Handling

while True:
    try:
        age = int(input("What is your age? "))
        10/age
    except ValueError:
        print("Please Input Numbers...")
    except ZeroDivisionError:
        print("Please input higher than 0")
    else:
        print("thank You")
        break

