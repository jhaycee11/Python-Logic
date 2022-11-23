#Error Handling Advance
def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f"oops {err}")

print(sum(2, 0))