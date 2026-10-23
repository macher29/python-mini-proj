import random

while True:
    user = input("Do you want to roll the dice yes / no: ")

    if user == "yes":
        print(f"Dice: {random.randint(1 , 6)}")

    elif user == "no":
        print("Game ended!")
        print(" ")
        break

    else:
        print("type yes or no")