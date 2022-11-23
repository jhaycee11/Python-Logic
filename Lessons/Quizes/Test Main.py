from random import randint

def game(answer, guess):
    if 0 < guess < 11:
        if guess == answer:
            print("Genius!!")
            return True
    else:
        print("Hey i said 1-10!")
        return False

if __name__ == "__main__":
    answer = randint(1,10)
    while True:
        try:
            guess = int(input("Guess a number from 1-10: "))
            if game(answer, guess):
                break
        except ValueError:
            print("Input from 1 to 10: ")
            continue
