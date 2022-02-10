# Exercise #1: Write a program that generates the following pattern.
def topOrBottom():
    print("#####")
def top2():
    print("#   #")
def top3():
    print(" # # ")
def bottom():
    print("  #  ")

topOrBottom()
top2()
top3()
bottom()
top3()
top2()
topOrBottom()


# Exercise #2: Program to convert a number from feet to inches and to convert from feet to metres.

def feetoinches(feet):
    inches = feet * 12
    return inches

def feetometres(feet):
    metres = feet * 0.3048
    metres = format(metres,".4f")
    return metres

for i in range(10):
    print(i,"ft:")
    print("...",feetoinches(i), "inches")
    print("...",feetometres(i), "meters")

# Exercise #3: Write a function that rolls two dice.
# Your function should be designed to accept a single argument (an integer)
# and generate two die rolls between 1 and the number supplied.
# Your function should then return the two rolls in ascending order.

from random import randint

def two_die_rolls(side):
    num1 = randint(1,side)
    num2 = randint(1,side)

    if num1 < num2:
        return num1, num2
    else:
        return num2, num1

for i in range(6, 11):
    num1, num2 = two_die_rolls(i)
    print(i, "Slided dice roll: ", num1, "&", num2)

#Exercise #4 : Guess the number and limit the guess to 6 guesses for the user.

from random import randint
secretNumber = randint(1, 20)
print("I am thinking of a number between 1 and 20.")
# Ask the player to guess the number 6 times.
nofguesses = 0
guess = 0
while nofguesses < 7:
    guess = int(input("Guess a number: "))
    nofguesses += 1
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    elif guess == secretNumber:
        break
if guess == secretNumber:
    print("You guessed the number in " + str(nofguesses) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))





