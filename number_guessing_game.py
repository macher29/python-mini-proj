import random

print("Welcome to number guessing game\n")
print("Type 0 to exit")

while True:
    computer_guess = random.randint(1 , 100)
    user_guess = int(input("Enter a number between 1 to 100: "))

    if computer_guess == user_guess:
        print("Your guess is Right!")
        break

    elif user_guess > computer_guess:
        print("Your guess is high")

    elif user_guess < computer_guess:
        print("Your guess is low")

    elif user_guess == 0:
        break
    else:
        print("Oop's something went wrong")
