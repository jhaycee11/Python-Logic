import sys
from random import randint

""" this is a normal coding
answer = randint(1,10)

while True:
    try:
        guess = int(input("Guess a number 1-10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("Youre a genius")
                break
        else:
            print("I said 1-10 : ")
    except ValueError:
        print("please enter a number: ")
        continue"""


#This is an argv version
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input("Guess a number 1-10: "))
        if 0 < guess < int(sys.argv[2]):
            if guess == answer:
                print("Youre a genius")
                break
        else:
            print("I said 1-10 : ")
    except ValueError:
        print("please enter a number: ")
        continue